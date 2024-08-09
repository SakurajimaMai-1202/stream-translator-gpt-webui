# **stream-translator-gpt-webui**
stream-translator-gpt-webui 

English | [繁體中文](https://github.com/SakurajimaMai-1202/stream-translator-gpt-webui/blob/main/README_zh_tw.md) 

stream-translator-gpt-webui
This project is based on stream-translator-gpt, aiming to provide viewers with real-time subtitle translation using large language models while watching YouTube live streams.

It combines live streaming, chat room, and subtitle translation features on a single page, offering a better live streaming experience for viewers who don't understand other languages. Currently supports mutual translation between Japanese, English, and Chinese.

![](https://cdn.discordapp.com/attachments/1102904709532098610/1268862352925921384/Clip_2024-08-02_17-24-40.png?ex=66adf7a7&is=66aca627&hm=a7b139f731f73aa51307dc2af91bbd1e9a2b6976e5f33be6c0b4203b734d3dff&)

(The translation model in this image is gemma2-27b)

Preparation (Windows)

1.Install [Python 3.10(](https://www.python.org/downloads/release/python-3100/) (recommended)

2.Install [CUDA12.1](https://developer.nvidia.com/cuda-12-1-0-download-archive) (recommended)

3.Install [CUDNN](https://developer.nvidia.com/rdp/cudnn-archive)

4.Install [Pytorch](https://pytorch.org/get-started/locally/) (must match CUDA version)

5.Install [ffmpeg](https://ffmpeg.org/download.html)

6.Install [yt-dlp](https://github.com/yt-dlp/yt-dlp)(recommended to use PIP)

7.Install [stream-translator-gpt](https://github.com/ionic-bond/stream-translator-gpt)

8.Install [redis](https://github.com/tporadowski/redis/releases) (recommended to download from GitHub)

9.Install  dependencies:

    pip install flask flask-socketio flask-limiter  python-dotenv requests yt-dlp ffmpeg  gevent

10.If you want to use Gemini API for translation, [you need to create a Google API key.](https://aistudio.google.com/app/apikey) (15 free requests per minute)

11.If you want to use GPT API for translation, [you need to create an OpenAI API key](https://platform.openai.com/api-keys)

12.If you want to use Local LLM for translation, you need to set up your own or use a method compatible with the OpenAI API. You mainly need to fill in the URL and API key of your self-hosted large model. (Currently tested with sakura 14b / gemma 27b / llama 3.1 8b)

[Apply for a YouTube Data API key](https://gg90052.github.io/blog/yt_api_key/)

13.Download this project as a ZIP file

*Note
ffmpeg, redis, cuda, cudnn need to be written into the system's environment variable path.
After closing the webpage, you need to manually close the CMD window in the background.
If you encounter torch-related errors, you can try using this:

Copy
    pip3 install torch==2.2.2 torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

The environment variable PATH needs to include the following. If you've installed them in other locations, modify the paths accordingly based on where you've installed them:
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
**How to run**

1.Unzip the ZIP file.

2.Open the .env file with Notepad and enter your translation API key and YouTube Data API key.

3.Right-click inside the folder and select "Open in Terminal" or "Open command window here".

4.Run the program by typing python app.py in the terminal.

5.If you want a one-click solution, go to the releases section and download the pre-packaged EXE file. Place it in the folder, and you can use it directly.
