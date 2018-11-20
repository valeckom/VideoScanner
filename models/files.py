"""Handle the files in a directory"""
import os
from models.log import Logger


class FileHandler(object):
    def __init__(self, directory):
        self.dir = directory
        self._check_valid_dir()
        self.files = []
        self.log = Logger(self.dir)
        self.extrack_list_of_video_files()

    def get_clean_list(self):
        return self.files

    def make_py_compatable(self, file_name):
        new_name = file_name
        spec_char = [' ', '(', ')', '\'']
        for c in spec_char:
            new_name = new_name.replace(c, "\\{}".format(c))
        return new_name

    def extrack_list_of_video_files(self):
        raw_files = os.listdir(self.dir)
        for file in raw_files:
            if self._file_has_known_extension(file):
                self.files.append(file)
            else:
                self.log.note("SKIPPED (unknown extension) - {}".format(file))

    def _check_valid_dir(self):
        if self.dir.endswith('/'):
            return
        print("Error: Unexpected argument. A directory should end with a forward slash ('/')")
        exit(1)

    def _file_has_known_extension(self, file):
        file_types = [".mp4", ".mov", ".vob", ".mkv"]
        for file_type in file_types:
            if file.endswith(file_type):
                return True
        return False
