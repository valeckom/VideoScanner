import os
import sys
from models.files import FileHandeler
from models.log import Logger

log_file = "video_scanner.log"
args = sys.argv
dir = args[1]
file_handeler = FileHandeler(dir)
log = Logger(dir, log_file)

log.header()

for file in file_handeler.get_clean_list():
    log.note(file)

    temp_file = file_handeler.make_py_compatable(file)
    os.system("ffmpeg -v error -i {} -f null - 2>>{}".format(dir+temp_file, log_file))

log.end()
