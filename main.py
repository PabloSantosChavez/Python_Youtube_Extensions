from pytubefix import YouTube
from pytubefix.cli import on_progress
import os

url = ""

yt = YouTube(url, on_progress_callback=on_progress)
print("Title:", yt.title)

# Get the highest resolution video stream
video_stream = yt.streams.filter(file_extension='mp4', only_video=True).order_by('resolution').desc().first()
print(f"Downloading video: {video_stream.resolution}")

# Get the audio stream
audio_stream = yt.streams.filter(only_audio=True).first()
print("Downloading audio")

# Download video and audio
video_stream.download(filename='video.mp4')
audio_stream.download(filename='audio.mp4')

# Combine video and audio using ffmpeg
os.system("ffmpeg -i video.mp4 -i audio.mp4 -c:v copy -c:a aac output.mp4")

print("Download and combination complete!")
