import os
import sys
import re
import subprocess
from subprocess import Popen, PIPE, STDOUT
import time
from datetime import datetime

version = "0.1"
log_file = "video_scanner.log"
args = sys.argv
dir = args[1]

files = []
raw_files = os.listdir(dir)
for file in raw_files:
    if ".mp4" in file:
        files.append(file)

log_file = dir + log_file
timestamp = '{:%Y-%m-%d %H:%M}'.format(datetime.now())

print("Video Scanner v{}".format(version))
print(timestamp)

with open(log_file, 'a') as f:
    f.write('{}\n'.format(timestamp))

for file in files:
    with open(log_file, 'a') as f:
        f.write('{}\n'.format(file))
    print(file)
    temp_file = file.replace(' ', "\ ")
    # os.system("ffmpeg -v error -i {} -f null - 2>>{}".format(dir+temp_file, log_file))
    os.system("ffmpeg -v error -i {} -f null - 2>>{}".format(dir+temp_file, log_file))

with open(log_file, 'a') as f:
    f.write("\n\n")
