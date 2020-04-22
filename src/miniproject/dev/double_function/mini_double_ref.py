

def uint_double(k):
    """Substitute for corresponding C function in the mini_double package


    The cython extension 'mini_double' is used for code generation.
    Depending on the details of the build process, it may not yet be
    available when the code is generated. So we take this function as
    a substitute for the corresponding function in the ``mini_double``
    package.
    """
    return 2*k


