from miniproject.mini_double import uint_double

from miniproject.mini_triple import uint_triple


def wrap_double(k):
    """Python wrapper of a C function that doubles an integer ``k``."""
    return uint_double(k)



def wrap_triple(k):
    """Python wrapper of a C function that triples an integer ``k``.

    The function returns  3 * ``k``.

    For small values ``k`` the function reads the result from a
    table which has been generated by a python script. For large 
    values ``k`` it uses a function from a shared library.

    Both, the table and the shared library have been created in
    a prior step of the build process.
    """
    return uint_triple(k)



