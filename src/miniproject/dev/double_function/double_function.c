
#include <stdint.h>
#include "uint_std_t.h"
#include "double_function.h"



#ifdef __cplusplus
extern "C" {
#endif


DOUBLE_FUNCTION_API
uint_std_t double_function(uint_std_t k)
// This is a rather trivial function that returning 2 * k .
// Its purpose is to demonstrate how to put this function into
// a shared library (or into a DLL in Windows) and to write a
// Python wrapper for that function with Cython.
{
    return 2 * k;
}
   

     
#ifdef __cplusplus
}
#endif


