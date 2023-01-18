from moviepy import editor
from os import walk
import datetime


def audio_record():
    video_files_name = []
    video_file_path = "video/"
    for (dirpath, dirnames, filenames) in walk(video_file_path):
        video_files_name.extend(filenames)
        break
    start_time = datetime.datetime.now()
    print("---------------Start record audio from video!--------------")
    for file in video_files_name:
        video = editor.VideoFileClip(f"{video_file_path}{file}")
        audio = video.audio
        audio.write_audiofile(f"audio/from_{file[:-4]}_{datetime.datetime.now()}.mp3".replace(' ', '_'))
    end_record = datetime.datetime.now() - start_time
    print(f"---------End record audio from video with total time: {end_record} ----------")


if __name__ == "__main__":
    audio_record()
