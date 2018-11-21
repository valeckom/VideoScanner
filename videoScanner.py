"""Main script"""
import sys
from models.files import FileHandler
from models.log import Logger
from models.ffmpeg import Ffmpeg
from models.sysArgv import SysArgv

args = SysArgv(sys.argv)
dir = args.get_dir()
opt = args.get_options()
log = Logger(opt, dir)
ffmpeg = Ffmpeg(dir)

log.header()
file_handeler = FileHandler(dir)
file_list = file_handeler.get_clean_list()

for file in file_list:
    ffmpeg.test_file(file, opt)

log.end()
