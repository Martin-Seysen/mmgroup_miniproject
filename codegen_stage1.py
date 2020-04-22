import os
import sys
from shutil import copyfile



from config import SRC_DIR, DEV_DIR,  C_DIR, DOC_DIR, PXD_DIR
from config import REAL_SRC_DIR 
from config import INT_BITS 
sys.path.append(REAL_SRC_DIR)


FILE_DIR = os.path.join(DEV_DIR, "double_function")




def write_std_int_header():
    fname = os.path.join(C_DIR , "uint_std_t.h")
    f = open(fname, "wt")
    f.write("""// This file has been generated automatically. Do not change!")

#ifndef UINT_STD_T_H
#define UINT_STD_T_H
typedef uint%d_t uint_std_t;
#endif

""" % INT_BITS)
    f.close()

def make_c_functions():
    write_std_int_header()
    for file_name in ["double_function.c",  "double_function.h"]:
        copyfile(os.path.join(FILE_DIR, file_name),
                   os.path.join(C_DIR ,file_name)
        )
    for file_name in ["mini_double.pyx"]:
        copyfile(os.path.join(FILE_DIR, file_name),
            os.path.join(PXD_DIR, file_name)
        )

if __name__ == "__main__":
    make_c_functions()



    