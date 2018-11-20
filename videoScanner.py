"""Main script"""
import os
import sys
from models.files import FileHandeler
from models.log import Logger

args = sys.argv
dir = args[1]
log = Logger(dir)

log.header()
file_handeler = FileHandeler(dir)

for file in file_handeler.get_clean_list():
    log.note(file)

    temp_file = file_handeler.make_py_compatable(dir + file)

    args = temp_file, log.file_name
    os.system("ffmpeg -v error -i {} -f null - 2>>{}".format(*args))

log.end()
