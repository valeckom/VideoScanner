"""Main script"""
from models.ffmpeg import Ffmpeg
import config

log = config.log
ffmpeg = Ffmpeg()

total_videos = len(config.file_list)
n_videos = 0

for i, file in enumerate(config.file_list):
    config.log.progress(i, config.file_list, file)
    ffmpeg.test_file(file)
    n_videos += 1

log.end(n_videos)
