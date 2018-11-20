"""Main script"""
import os
import sys
from models.files import FileHandler
from models.log import Logger

args = sys.argv
dir = args[1]
log = Logger(dir)

log.header()
file_handeler = FileHandler(dir)
file_list = file_handeler.get_clean_list()

for file in file_list:
    log.note(file)

    file_lbl = file_handeler.make_py_compatable(dir + file)

    args = file_lbl, log.file_name
    os.system("ffmpeg -v error -i {} -f null - 2>>{}".format(*args))

log.end()
