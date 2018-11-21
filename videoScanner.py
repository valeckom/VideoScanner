"""Main script"""
import sys
from models.files import FileHandler
from models.log import Logger
from models.ffmpeg import Ffmpeg

args = sys.argv
dir = args[1]
log = Logger(dir)
ffmpeg = Ffmpeg(dir)

log.header()
file_handeler = FileHandler(dir)
file_list = file_handeler.get_clean_list()

for file in file_list:
    ffmpeg.test(file)

log.end()
