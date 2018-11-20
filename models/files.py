"""Handle the files in a directory"""
import os
from models.log import Logger


class FileHandeler(object):
    def __init__(self, directory):
        self.dir = directory
        self.files = []
        self.file_types = [".mp4", ".mov", ".vob", ".mkv"]
        self.log = Logger(self.dir)
        self.extrack_list_of_video_files()

    def extrack_list_of_video_files(self):
        raw_files = os.listdir(self.dir)
        for file in raw_files:
            if self._file_has_known_extension(file):
                self.files.append(file)
            else:
                self.log.note("SKIPPED (unknown extension) - {}".format(file))

    def _file_has_known_extension(self, file):
        for file_type in self.file_types:
            if file_type in file:
                return True
        return False

    def get_clean_list(self):
        return self.files

    def make_py_compatable(self, file_name):
        new_name = file_name
        spec_char = [' ', '(', ')']
        for c in spec_char:
            new_name = new_name.replace(c, "\\{}".format(c))
        return new_name
