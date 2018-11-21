from models.log import Logger
from models.files import FileHandler
from subprocess import Popen, PIPE


class Ffmpeg(object):
    def __init__(self, directory):
        self._dir = directory
        self._log = Logger(self._dir)

    def test(self, file, options):
        opt = '' if options is None else options
        self._log.note(file)
        file_lbl = self._dir + file

        args = ["ffmpeg", "-v", "error", "-i", file_lbl, "-f", "null", '-']
        process = Popen(args, stderr=PIPE)
        while True:
            line = process.stderr.readline()
            if line != '':
                if not self._ignore_error(line):
                    self._log.error(line.rstrip())
                    if not 'w' in opt:
                        process.kill()
                        break
            else:
                break

    def _ignore_error(self, error_output):
        allowed_errors = ["Application provided invalid, non monotonically increasing dts to muxer in stream",
                            "place holder ZZZZZZ"]
        for error in allowed_errors:
            if error in error_output:
                return True
        return False
