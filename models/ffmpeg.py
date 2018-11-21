import os
from models.log import Logger
from models.files import FileHandler


class Ffmpeg(object):
    def __init__(self, directory):
        self._dir = directory
        self._log = Logger(self._dir)
        self._file_handeler = FileHandler(self._dir)

    def test(self, file):
        self._log.note(file)

        file_lbl = self._file_handeler.make_py_compatable(self._dir + file)

        args = file_lbl, self._file_handeler.make_py_compatable(self._log.file)
        os.system("ffmpeg -v error -i {} -f null - 2>>{}".format(*args))
