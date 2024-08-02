from app import app
import threading
import webbrowser
import time

def open_browser():
    """
    等待 3 秒後打開瀏覽器，以確保 Flask 服務器已經啟動
    """
    time.sleep(3)
    webbrowser.open_new('http://127.0.0.1:5000/')

if __name__ == '__main__':
    # 在新線程中運行打開瀏覽器的函數
    threading.Thread(target=open_browser).start()

    # 運行 Flask 應用
    app.run(debug=False)