import sys

if sys.version_info[0] == 2:
    from .unicorn_py2 import *
else:
    from .unicorn_py3 import *