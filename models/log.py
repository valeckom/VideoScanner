"""Handle all log file related functions"""
from datetime import datetime


class Logger(object):
    def __init__(self, directory):
        self.file_name = "video_scanner.log"
        self.file = directory + self.file_name
        self.version = "0.3"
        self.terminal = Terminal()

    def time_date_stamp(self):
        self.write(self._time_stamp())

    def header(self):
        self._setup_log()
        msg = "Video Scanner v{}\r\n(c) Mark Valecko 2018".format(self.version)
        self._write(msg)
        self._write("{}\r\n".format(self._time_stamp()))

    def note(self, msg):
        self._write(msg)

    def error(self, msg):
        self._write("ERROR "+ msg)

    def end(self, number_of_videos_scanned):
        msg = "\r\n{} videos scanned at {}".format(number_of_videos_scanned, self._short_time_stamp())
        self._write(msg)
        self._write('')

    @staticmethod
    def _time_stamp():
        return '{:%Y-%m-%d %H:%M}'.format(datetime.now())

    @staticmethod
    def _short_time_stamp():
        return '{:%H:%M}'.format(datetime.now())

    def _write(self, content):
        self.terminal.write(content)
        with open(self.file, "a") as f:
            f.write('{}\r\n'.format(content))

    def _setup_log(self):
        try:
            self._erase_log()
        except IOError:
            self._create_log()

    def _erase_log(self):
        with open(self.file, 'r+') as f:
            f.truncate(0) # need '0' when using r+
        self.terminal.write("log file erased")

    def _create_log(self):
        with open(self.file, 'w') as f:
            pass
        self.terminal.write("created log file")


class Terminal(object):
    def __init__(self):
        # self._verbose = self._verbose_is_active(option)
        pass

    # def _verbose_is_active(self, option):
    #     if 'v' in option:
    #         return True
    #     return False

    def write(self, msg):
        print msg
