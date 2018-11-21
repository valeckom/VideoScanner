"""Main script"""
from models.ffmpeg import Ffmpeg
import config

log = config.log
ffmpeg = Ffmpeg()

total_videos = len(config.file_list)
n_videos = 0

for i, file in enumerate(config.file_list):
    config.log.note("({}/{})".format(len(config.file_list) - i, len(config.file_list)))
    ffmpeg.test_file(file)
    n_videos += 1

log.end(n_videos)
