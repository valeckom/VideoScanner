import os
import sys
import re
import subprocess
import time
from datetime import datetime
from models.files import FileHandeler
# from models.files import FileHandeler

version = "0.1"
log_file = "video_scanner.log"
args = sys.argv
dir = args[1]
file_handeler = FileHandeler(dir)

# files = []
# raw_files = os.listdir(dir)
# for file in raw_files:
#     if ".mp4" in file:
#         files.append(file)

log_file = dir + log_file
timestamp = '{:%Y-%m-%d %H:%M}'.format(datetime.now())

print("Video Scanner v{}".format(version))
print(timestamp)

with open(log_file, 'a') as f:
    f.write('{}\n'.format(timestamp))

for file in file_handeler.get_clean_list():
    with open(log_file, 'a') as f:
        f.write('{}\n'.format(file))
    print(file)

    temp_file = file_handeler.make_py_compatable(file)
    os.system("ffmpeg -v error -i {} -f null - 2>>{}".format(dir+temp_file, log_file))

with open(log_file, 'a') as f:
    f.write("\n\n")
