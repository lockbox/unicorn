# Unicorn Python bindings, by Nguyen Anh Quynnh <aquynh@gmail.com>
import sys
from . import arm_const, arm64_const, mips_const, sparc_const, m68k_const, x86_const, riscv_const, s390x_const, tricore_const
from .unicorn_const import *

if sys.version_info[0] == 2:
    from .unicorn_py2 import Uc, uc_version, uc_arch_supported, version_bind, debug, UcError, __version__
else:
    from .unicorn_py3 import Uc, uc_version, uc_arch_supported, version_bind, debug, UcError, __version__
