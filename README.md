# **stream-translator-gpt-webui**
stream-translator-gpt-webui 

English | [繁體中文](https://github.com/SakurajimaMai-1202/stream-translator-gpt-webui/blob/main/README_zh_tw.md) 

stream-translator-gpt-webui
This project is based on stream-translator-gpt, aiming to provide viewers with real-time subtitle translation using large language models while watching YouTube live streams.

It combines live streaming, chat room, and subtitle translation features on a single page, offering a better live streaming experience for viewers who don't understand other languages. (Currently available for Japanese to Chinese and English to Chinese translation)
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

9.Install other dependencies:

    pip install flask flask-socketio flask-limiter  python-dotenv requests

10.If you want to use Gemini API for translation, [you need to create a Google API key.](https://aistudio.google.com/app/apikey) (15 free requests per minute)

11.If you want to use GPT API for translation, [you need to create an OpenAI API key](https://platform.openai.com/api-keys)

12.If you want to use Local LLM for translation, you need to set up your own or use a method compatible with the OpenAI API. You mainly need to fill in the URL and API key of your self-hosted large model. (Currently tested with sakura 14b / gemma 27b / llama 3.1 8b)

[Apply for a YouTube Data API key](https://gg90052.github.io/blog/yt_api_key/)

13.Download this project as a ZIP file

*Note
ffmpeg, redis, cuda, cudnn need to be written into the system's environment variable path.
After closing the webpage, you need to manually close the CMD window in the background.
How to run

Unzip the ZIP file
Open the .env file with Notepad and enter the translation API key and YouTube Data API key
Right-click in the folder and open terminal

To package as an exe, enter pyinstaller youtube_translator.spec in the terminal. It will automatically package as an exe. The exe file will be in the dist folder in your folder. You can directly run the exe file in the future.

If you don't want to package it, you can directly enter python app.py to run it.
