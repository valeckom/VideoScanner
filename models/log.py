"""Handle all log file related functions"""
from datetime import datetime


class Logger(object):
    def __init__(self, directory, file_name):
        self.dir = directory
        self.file = self.dir + file_name
        self.version = "0.1"

    @staticmethod
    def _time_stamp():
        return '{:%Y-%m-%d %H:%M}'.format(datetime.now())

    @staticmethod
    def _short_time_stamp():
        return '{:%H:%M}'.format(datetime.now())

    def _write(self, content):
        print(content)
        with open(self.file, 'a') as f:
            f.write('{}\n'.format(content))

    def time_date_stamp(self):
        self.write(self._time_stamp())

    def header(self):
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
