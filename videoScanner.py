"""Main script"""
import sys
from models.files import FileHandler
from models.log import Logger
from models.ffmpeg import Ffmpeg
from models.sysArgv import SysArgv
import config

args = SysArgv(sys.argv)
dir = args.get_dir()
opt = args.get_options()
log = config.log
ffmpeg = Ffmpeg(dir)

# file_handeler = FileHandler(dir)
# file_list = file_handeler.get_clean_list()
# log.set_number_of_files(len(file_list))

n_videos = 0

for file in config.file_list:
    ffmpeg.test_file(file, opt)
    n_videos += 1

log.end(n_videos)
