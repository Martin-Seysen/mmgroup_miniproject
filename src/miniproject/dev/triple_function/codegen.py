import os
import sys
from shutil import copyfile

FILE_DIR = os.path.dirname(os.path.realpath(__file__))
DEV_DIR = os.path.dirname(FILE_DIR)
PACKAGE_DIR = os.path.dirname(DEV_DIR)
SRC_DIR = os.path.dirname(PACKAGE_DIR)

sys.path.append(SRC_DIR)
from miniproject.dev.config import INT_BITS, C_DIR, PXD_DIR
assert sys.path.pop() == SRC_DIR


from miniproject.mini_double import uint_double
from miniproject.dev.double_function.codegen import write_std_int_header


os.chdir(FILE_DIR)



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



    