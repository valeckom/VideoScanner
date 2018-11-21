import config
from subprocess import Popen, PIPE


class Ffmpeg(object):
    def __init__(self):
        self._process = None

    def test_file(self, file):
        config.log.note(file)
        file_lbl = config.dir + file

        args = ["ffmpeg", "-v", "error", "-i", file_lbl, "-f", "null", '-']
        self._process = Popen(args, stderr=PIPE)
        self._read_error_output()

    def _read_error_output(self):
        while True:
            if self._end_of_errors():
                config.number_of_files_scanned + 1
                break

    def _end_of_errors(self):
        line = self._process.stderr.readline()
        if line == '':
            return True
        if not self._valid_error(line) or self._scan_whole_file_after_error():
            return False
        return True

    def _scan_whole_file_after_error(self):
        if not 'w' in config.command_options:
            self._process.kill()
            return False
        return True

    def _valid_error(self, error_output):
        allowed_errors = ["Application provided invalid, non monotonically increasing dts to muxer in stream",
                            "place holder ZZZZZZZ"]
        for error in allowed_errors:
            if error in error_output:
                return False
        config.log.error(error_output.rstrip())
        return True
