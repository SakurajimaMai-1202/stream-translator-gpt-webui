import os
import sys
import subprocess
import time
from flask import Flask, render_template, request, jsonify, url_for
import re
import yt_dlp
import threading
import webbrowser
from flask_socketio import SocketIO
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import redis
from dotenv import load_dotenv
import requests

# Load environment variables
load_dotenv()

if getattr(sys, 'frozen', False):
    template_folder = os.path.join(sys._MEIPASS, 'templates')
    static_folder = os.path.join(sys._MEIPASS, 'static')
    app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
else:
    app = Flask(__name__)

socketio = SocketIO(app)

def start_redis():
    if os.name == 'nt':  # Windows
        redis_paths = [
            "C:\\Program Files\\Redis\\redis-server.exe",
            "C:\\Redis\\redis-server.exe",
            "redis-server.exe"  # 如果 Redis 在系統 PATH 中
        ]
        for path in redis_paths:
            if os.path.exists(path):
                subprocess.Popen([path])
                print(f"正在使用路徑啟動 Redis: {path}")
                time.sleep(2)  # 給 Redis 一些啟動時間
                return True
        print("警告: 無法找到 Redis 執行文件。Redis 相關功能將被禁用。")
        return False
    else:  # macOS 和 Linux
        try:
            subprocess.Popen(["redis-server"])
            print("正在啟動 Redis 伺服器...")
            time.sleep(2)  # 給 Redis 一些啟動時間
            return True
        except FileNotFoundError:
            print("警告: 無法找到 Redis。Redis 相關功能將被禁用。")
            return False

def check_redis(max_retries=5, delay=1):
    redis_url = os.getenv('REDIS_URL', 'redis://localhost:6379')
    for _ in range(max_retries):
        try:
            client = redis.Redis.from_url(redis_url, decode_responses=True)
            client.ping()
            print("成功連接到 Redis!")
            return client
        except (redis.exceptions.ConnectionError, redis.exceptions.ResponseError) as e:
            print(f"無法連接到 Redis: {e}，{delay} 秒後重試...")
            time.sleep(delay)
    print(f"在 {max_retries} 次嘗試後仍無法連接到 Redis。")
    return None

translation_process = None
should_restart = True

def run_translation(url, model, language, output_mode, translation_model):
    global translation_process, should_restart
    while should_restart:
        hide_transcribe = "--hide_transcribe_result" if output_mode == "translation-only" else ""
        if translation_model == "local_llm":
            command = f"stream-translator-gpt {url} --model {model} --language {language} --use_faster_whisper --gpt_base_url {os.getenv('GPT_BASE_URL')} --gpt_translation_prompt \"Translate from Japanese to Traditional Chinese\" --openai_api_key {os.getenv('GPT_BASE_URL_API_KEY')} {hide_transcribe} --output_timestamps --max_audio_length 15 --output_file_path ./result.srt"
        elif translation_model == "gpt":
            command = f"stream-translator-gpt {url} --model {model} --language {language} --use_faster_whisper --gpt_translation_prompt \"Translate from Japanese to Chinese\" --openai_api_key {os.getenv('OPENAI_API_KEY')} {hide_transcribe} --output_timestamps --max_audio_length 15 --output_file_path ./result.srt"
        elif translation_model == "gemini":
            command = f"stream-translator-gpt {url} --model {model} --language {language} --use_faster_whisper --gpt_translation_prompt \"Translate from Japanese to Chinese\" --google_api_key {os.getenv('GOOGLE_API_KEY')} {hide_transcribe} --output_timestamps --max_audio_length 15 --output_file_path ./result.srt"
        else:
            print("未知的翻譯模型")
            return

        translation_process = subprocess.Popen(command, shell=True)
        translation_process.wait()
        time.sleep(5)

    if os.path.exists('./result.srt'):
        os.remove('./result.srt')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stream_info', methods=['POST'])
def stream_info():
    url = request.json.get('url')
    if not url:
        return jsonify({"success": False, "error": "未提供URL"}), 400

    try:
        ydl_opts = {'quiet': True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            video_id = info['id']
            title = info['title']
            channel_id = info['channel_id']
            channel_name = info['channel']

            # 使用 YouTube Data API 獲取頻道詳細信息
            api_key = os.getenv('YOUTUBE_API_KEY')
            channel_response = requests.get(f'https://www.googleapis.com/youtube/v3/channels?part=snippet&id={channel_id}&key={api_key}')
            channel_data = channel_response.json()

            if 'items' in channel_data and len(channel_data['items']) > 0:
                channel_avatar = channel_data['items'][0]['snippet']['thumbnails']['default']['url']
            else:
                channel_avatar = ''

            return jsonify({
                "success": True,
                "title": title,
                "channel": channel_name,
                "videoId": video_id,
                "channelAvatar": channel_avatar,
                "chatId": video_id  # 添加聊天室ID
            })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/translate', methods=['POST'])
def translate():
    global translation_process, should_restart
    data = request.json
    url = data.get('url')
    model = data.get('model')
    language = data.get('language')
    output_mode = data.get('outputMode')
    translation_model = data.get('api')

    if not all([url, model, language, output_mode, translation_model]):
        return jsonify({"success": False, "error": "缺少必要參數"}), 400

    if translation_process:
        should_restart = False
        translation_process.terminate()
        translation_process.wait()

    if os.path.exists('./result.srt'):
        os.remove('./result.srt')

    should_restart = True
    threading.Thread(target=run_translation, args=(url, model, language, output_mode, translation_model)).start()
    return jsonify({"success": True})

@socketio.on('request_subtitles')
def handle_subtitles_request():
    subtitles = []
    if os.path.exists('./result.srt'):
        with open('./result.srt', 'r', encoding='utf-8') as file:
            content = file.read()
            pattern = re.compile(r'(\d+:\d+:\d+,\d+ --> \d+:\d+:\d+,\d+)\n([\s\S]*?)(?=\n\n|\Z)')
            matches = pattern.findall(content)
            for time, text in matches:
                lines = text.strip().split('\n')
                if len(lines) == 2:
                    subtitles.append({"time": time, "original": lines[0], "translation": lines[1]})
                else:
                    subtitles.append({"time": time, "original": "", "translation": lines[0]})
    socketio.emit('subtitles_update', {"subtitles": subtitles})

@app.route('/stop_translation', methods=['POST'])
def stop_translation():
    global translation_process, should_restart
    if translation_process:
        should_restart = False
        translation_process.terminate()
        translation_process.wait()
    return jsonify({"success": True})

@app.errorhandler(429)
def ratelimit_handler(e):
    return jsonify(error="請求過於頻繁，請稍後再試。"), 429

if __name__ == '__main__':
    try:
        redis_started = start_redis()
        redis_client = check_redis() if redis_started else None

        if redis_client:
            limiter = Limiter(
                key_func=get_remote_address,
                app=app,
                storage_uri=os.getenv('REDIS_URL', 'redis://localhost:6379'),
                storage_options={"connection_pool": redis_client.connection_pool}
            )
            print("成功初始化 Redis 速率限制。")
        else:
            print("警告：無法連接到 Redis。將使用內存存儲進行速率限制。")
            limiter = Limiter(key_func=get_remote_address, app=app)

        # 為需要速率限制的路由添加裝飾器
        app.view_functions['stream_info'] = limiter.limit("10 per minute")(app.view_functions['stream_info'])
        app.view_functions['translate'] = limiter.limit("5 per minute")(app.view_functions['translate'])

        def open_browser():
            webbrowser.open_new('http://localhost:8000')

        threading.Timer(3, open_browser).start()

        print("啟動服務器...")
        socketio.run(app, host='0.0.0.0', port=8000, use_reloader=False)
    except Exception as e:
        print(f"程序啟動時發生錯誤：{e}")
        import traceback
        traceback.print_exc()
