import os
import sys
from shutil import copyfile

from config import SRC_DIR, DEV_DIR,  C_DIR, DOC_DIR, PXD_DIR
from config import REAL_SRC_DIR 
from config import INT_BITS 
sys.path.append(REAL_SRC_DIR)


FILE_DIR = os.path.join(DEV_DIR, "triple_function")

try:
    # Try importing the fast C function
    from miniproject.mini_double import uint_double 
except (ImportError, ModuleNotFoundError):
    # Use the slow python function if the C function is not available
    from miniproject.dev.double_function.mini_double_ref import uint_double 



from codegen_stage1 import write_std_int_header


def write_triple_table():
    fname = os.path.join(C_DIR , "triple_table.c")
    f = open(fname, "wt")
    table = [i + uint_double(i) for i in range(3)]
    f.write("""// This file has been generated automatically. Do not change!")

#include <stdint.h>

uint8_t TRIPLE_TABLE[] = {%d, %d, %d};

""" % tuple(table))
    f.close()

def make_c_functions():
    write_std_int_header()
    for file_name in ["triple_function.c",  "triple_function.h"]:
        copyfile(os.path.join(FILE_DIR, file_name),
                   os.path.join(C_DIR ,file_name)
        )
    for file_name in ["mini_triple.pyx"]:
        copyfile(os.path.join(FILE_DIR, file_name),
            os.path.join(PXD_DIR, file_name)
        )

if __name__ == "__main__":
    write_triple_table()
    make_c_functions()



    