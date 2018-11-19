"""Handle the files in a directory"""
import os

class FileHandeler(object):
    def __init__(self, directory):
        self.dir = directory
        self.files = []
        self.extrack_list_of_video_files()

    def extrack_list_of_video_files(self):
        raw_files = os.listdir(self.dir)
        for file in raw_files:
            if ".mp4" in file:
                self.files.append(file)

    def get_clean_list(self):
        return self.files

    def make_py_compatable(self, file_name):
        return file_name.replace(' ', "\ ")
