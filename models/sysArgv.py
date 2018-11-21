class SysArgv(object):
    def __init__(self, argv):
        self._argv = argv

    def get_dir(self):
        i = len(self._argv) - 1
        return self._argv[i]

    def get_options(self):
        for arg in self._argv:
            if arg.startswith('-'):
                return arg[1:]
        return None
