
#include <stdint.h>
#include "uint_std_t.h"
#include "double_function.h"
#include "triple_function.h"



#ifdef __cplusplus
extern "C" {
#endif


extern uint8_t TRIPLE_TABLE[3];

TRIPLE_FUNCTION_API
uint_std_t triple_function(uint_std_t k)
// Return 3 * k 
// The function uses the table TRIPLE_TABLE[] for tripling a
// number k < 3. For tripling larger values k it uses function
// double_function() in the shared library 'double_code'.
{
    if (k < 3) return TRIPLE_TABLE[(uint8_t)(k)];
    return k + double_function(k);
}
   

     
#ifdef __cplusplus
}
#endif


