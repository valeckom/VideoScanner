"""Handle all log file related functions"""
from datetime import datetime


class Logger(object):
    def __init__(self, directory):
        self.file_name = "video_scanner.log"
        self.dir = directory
        self.file = self.dir + self.file_name
        self.version = "0.1"

    @staticmethod
    def _time_stamp():
        return '{:%Y-%m-%d %H:%M}'.format(datetime.now())

    @staticmethod
    def _short_time_stamp():
        return '{:%H:%M}'.format(datetime.now())

    def _write(self, content):
        print(content)
        with open(self.file, "at") as f:
            f.write('{}\n'.format(content))

    def time_date_stamp(self):
        self.write(self._time_stamp())

    def header(self):
        self._setup_log()
        msg = "Video Scanner v{}\n(c) Mark Valecko 2018".format(self.version)
        self._write(msg)
        self._write("{}\n".format(self._time_stamp()))

    def note(self, msg):
        msg = "({}) {}".format(self._short_time_stamp(), msg)
        self._write(msg)

    def end(self):
        msg = "\nProcess completed at {}".format(self._short_time_stamp())
        self._write(msg)
        self._write('')

    def _setup_log(self):
        try:
            self._erase_log()
        except IOError:
            self._create_log()

    def _erase_log(self):
        with open(self.file, 'r+') as f:
            f.truncate(0) # need '0' when using r+

    def _create_log(self):
        with open(self.file, 'w') as f:
            pass
        print("created log file")
