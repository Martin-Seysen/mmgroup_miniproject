# cython: language_level=3

from __future__ import absolute_import, division, print_function
from __future__ import  unicode_literals

from libc.stdint cimport uint32_t, uint16_t, uint8_t

from libc.stdint cimport uint64_t as uint_std_t



cdef extern from "double_function.h":
    uint_std_t double_function(uint_std_t k)


def uint_double(uint_std_t k):
    """Python wrapper of a C function that doubles an integer ``k``."""
    cdef uint_std_t k1 = k
    return int(double_function(k1))


