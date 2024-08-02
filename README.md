# **stream-translator-gpt-webui**
stream-translator-gpt-webui
這是一個基於[stream-translator-gpt](https://github.com/ionic-bond/stream-translator-gpt)的專案

主要是用於 youtube 直播轉譯字幕並且透過LLM做翻譯呈現在網頁上
![](https://cdn.discordapp.com/attachments/1102904709532098610/1268862352925921384/Clip_2024-08-02_17-24-40.png?ex=66adf7a7&is=66aca627&hm=a7b139f731f73aa51307dc2af91bbd1e9a2b6976e5f33be6c0b4203b734d3dff&)

準備工作(windows)

1.安裝[Python 3.10(](https://www.python.org/downloads/release/python-3100/)推薦)

2.安裝[CUDA12.1](https://cangmang.xyz/articles/1682852371010) (推薦)

3.安裝[CUDNN](https://cangmang.xyz/articles/1682852371010%29)

4.安裝[Pytorch](https://pytorch.org/get-started/locally/)(要匹配CUDA版本)

5.安裝[ffmpeg](https://ffmpeg.org/download.html)

6.安裝[yt-dlp](https://github.com/yt-dlp/yt-dlp) 建議使用PIP拉取

7.安裝[stream-translator-gpt](https://github.com/ionic-bond/stream-translator-gpt/blob/main/README_CN.md)

8.安裝[redis](https://github.com/tporadowski/redis/releases)(建議到github上下載)

9.安裝其他依賴項

    pip install flask flask-socketio flask-limiter  python-dotenv requests

10.  如果你想用  **Gemini API**  進行翻譯，需要[**創建一個Google API密鑰**](https://aistudio.google.com/app/apikey)。 （每分鐘免費15次請求）
11.  如果你想用    **GPT API**  進行翻譯，需要[**創建一個OpenAI API密鑰**](https://platform.openai.com/api-keys)
12. [申請YouTube Data API key](https://gg90052.github.io/blog/yt_api_key/)
13. 將此專案下載為ZIP檔案
*備註
ffmpeg,redis,cuda,cudnn 需要寫入系統的環境變數path內
並且需要在關閉網頁後 手動將後台的CMD視窗給關閉


如何執行 

1.解壓縮zip檔

2.請用記事本打開.env 輸入翻譯的api key 與YouTube Data API key 

3.在資料夾內右鍵以終端開啟

4.打包為exe 在終端內輸入pyinstaller youtube_translator.spec 會自動打包為exe exe檔會在你的資料夾內的dist資料夾內 以後直接執行exe即可

5.若不想打包 可以直接輸入 python app.py做執行，



