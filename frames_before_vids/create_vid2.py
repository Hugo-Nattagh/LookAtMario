import os

os.system("ffmpeg -r 30 -i img%01d.png -vcodec mpeg4 -y movie.mp4")
