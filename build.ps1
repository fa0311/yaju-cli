yt-dlp https://www.youtube.com/watch?v=DQFxW-v0WSQ -o assets/video.webm
ffmpeg -i assets/video.webm -vf fps=10 assets/frame/%04d.png
python main.py
