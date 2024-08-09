# **stream-translator-gpt-webui**
stream-translator-gpt-webui
English | 繁體中文
本專案基於 [stream-translator-gpt](https://github.com/ionic-bond/stream-translator-gpt)，旨在提供一個觀眾能夠在觀看 YouTube 直播時，實時轉譯字幕並透過大型語言模型進行翻譯。

將直播、聊天室和字幕轉譯三項功能結合於一個頁面，為不懂其他語言的觀眾提供更好的直播觀看體驗 (目前支援日英中互相翻譯)
![](https://cdn.discordapp.com/attachments/1102904709532098610/1268862352925921384/Clip_2024-08-02_17-24-40.png?ex=66adf7a7&is=66aca627&hm=a7b139f731f73aa51307dc2af91bbd1e9a2b6976e5f33be6c0b4203b734d3dff&)
(此圖片的翻譯模型為gemma2-27b)

準備工作(windows)

1.安裝[Python 3.10(](https://www.python.org/downloads/release/python-3100/)推薦)

2.安裝[CUDA12.1](https://developer.nvidia.com/cuda-12-1-0-download-archive) (推薦)

3.安裝[CUDNN](https://developer.nvidia.com/rdp/cudnn-archive)

4.安裝[Pytorch](https://pytorch.org/get-started/locally/)(要匹配CUDA版本)

5.安裝[ffmpeg](https://ffmpeg.org/download.html)

6.安裝[yt-dlp](https://github.com/yt-dlp/yt-dlp) 建議使用PIP拉取

7.安裝[stream-translator-gpt](https://github.com/ionic-bond/stream-translator-gpt/blob/main/README_CN.md)

8.安裝[redis](https://github.com/tporadowski/redis/releases)(建議到github上下載)

9.安裝依賴項 PIP

    pip install flask flask-socketio flask-limiter  python-dotenv requests yt-dlp ffmpeg  gevent

10.  如果你想用  **Gemini API**  進行翻譯，需要[**創建一個Google API密鑰**](https://aistudio.google.com/app/apikey)。 （每分鐘免費15次請求）

11.  如果你想用    **GPT API**  進行翻譯，需要[**創建一個OpenAI API密鑰**](https://platform.openai.com/api-keys)

12. 如果你想用 **Local LLM **進行翻譯 你需要自行架設或是用兼容openai api的方式 主要需要填入自架的大模型網址&api key (目前測試過 sakura 14b /gemma 27b/ llama 3.1 8b)
  
13. [申請YouTube Data API key](https://gg90052.github.io/blog/yt_api_key/)

14. 將此專案下載為ZIP檔案
 

*備註
ffmpeg,redis,cuda,cudnn 需要寫入系統的環境變數path內
並且需要在關閉網頁後 手動將後台的CMD視窗給關閉

若遇到torch相關錯誤 可以嘗試使用這個 

    pip3 install torch==2.2.2 torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

環境變數path內需要有以下這幾個 若你裝在其他地方 就依照這個格式下去改 看你安裝在哪邊
```
     C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.1\bin
     C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.1\libnvvp
     C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.1\include
     C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.1\lib
     C:\Users\User\AppData\Local\Programs\Python\Python310\
     C:\Users\User\AppData\Local\Programs\Python\Python310\Scripts\
     C:\Program Files\Redis
     C:\ffmpeg\bin
```


如何執行 

1.解壓縮zip檔

2.請用記事本打開.env 輸入翻譯的api key 與YouTube Data API key 

3.在資料夾內右鍵以終端開啟

4. 直接輸入 python app.py做執行，



目前疑似問題:shorts類的直式直播 網址需要從底下的分享複製網址才會正常 否則會將whisper鎖在small並且 無法執行翻譯指令


