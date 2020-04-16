"""Configutation for development"""

import sys
import os
from collections import defaultdict

# Bit length of an integer used in the representation of the monster 
# This should be 32 for a 32-bit and 64 for a 64-bit system.
INT_BITS = 64

# Extra compile arguments for .c files to be used in setup.py
EXTRA_COMPILE_ARGS = defaultdict(list)

# Update the EXTRA_COMPILE_ARGS dictionary with entries
#     compiler : <list of options> .
# Here 'compiler' is a string. For a list of available compilers, run:
#     python setup.py build_ext --help-compiler
EXTRA_COMPILE_ARGS.update({
    'mingw32':  [
        "-m64", "-Ofast", "-flto", "-march=native", "-funroll-loops"
    ],
})

# Extra link arguments for .c files to be used in setup.py
EXTRA_LINK_ARGS = defaultdict(list)
# Similiar to updating EXTRA_COMPILE_ARGS, we may update 
# the EXTRA_LINK_ARGS dictionary with a list of pairs
#     compiler : <list of options> .


ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
SRC_DIR = os.path.join(ROOT_DIR, "src")
PACKAGE_DIR = os.path.join(SRC_DIR, "miniproject")
DEV_DIR = os.path.join(PACKAGE_DIR, "dev")

C_DIR = os.path.join(DEV_DIR, "c_files")
DOC_DIR = os.path.join(DEV_DIR, "c_doc")
PXD_DIR = os.path.join(DEV_DIR, "pxd_files")











