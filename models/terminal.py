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

    def write(self, msg, ignore_verbose_lvl=False):
        if ignore_verbose_lvl or self._verbose_is_active():
            print msg
