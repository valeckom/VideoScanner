import config


class Terminal(object):
    def __init__(self):
        # self._verbose = self._verbose_is_active(option)
        pass

    @staticmethod
    def _verbose_is_active():
        if 'v' in config.command_options:
            return True
        return False

    @staticmethod
    def _progress_is_active():
        if 'p' in config.command_options:
            return True
        return False

    def write(self, msg, ignore_verbose_lvl=False, progress=False):
        if ignore_verbose_lvl:
            print msg
            return
        if self._verbose_is_active():
            print msg
            return
        if self._progress_is_active() and progress:
            print msg
            return
