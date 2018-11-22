import sys
from models.log import Logger
from models.sysArgv import SysArgv
from models.files import FileHandler

args = SysArgv(sys.argv)
dir = args.get_dir()
command_options = args.get_options()
log = Logger(dir)
number_of_files_scanned = 0

log.header()
file_handeler = FileHandler(dir)
file_list = file_handeler.get_clean_list()
