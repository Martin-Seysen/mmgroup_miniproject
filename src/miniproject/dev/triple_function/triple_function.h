
#ifndef TRIPLE_FUNCTION_H
#define TRIPLE_FUNCTION_H


#define TRIPLE_FUNCTION_DLL  // We want a DLL!!


// Generic helper definitions for shared library support
#if defined _WIN32 || defined __CYGWIN__
  #define TRIPLE_FUNCTION_HELPER_DLL_IMPORT __declspec(dllimport)
  #define TRIPLE_FUNCTION_HELPER_DLL_EXPORT __declspec(dllexport)
  #define TRIPLE_FUNCTION_HELPER_DLL_LOCAL
#else
  #if __GNUC__ >= 4
    #define TRIPLE_FUNCTION_HELPER_DLL_IMPORT __attribute__ ((visibility ("default")))
    #define TRIPLE_FUNCTION_HELPER_DLL_EXPORT __attribute__ ((visibility ("default")))
    #define TRIPLE_FUNCTION_HELPER_DLL_LOCAL  __attribute__ ((visibility ("hidden")))
  #else
    #define TRIPLE_FUNCTION_HELPER_DLL_IMPORT
    #define TRIPLE_FUNCTION_HELPER_DLL_EXPORT
    #define TRIPLE_FUNCTION_HELPER_DLL_LOCAL
  #endif
#endif


// Now we use the generic helper definitions above to define TRIPLE_FUNCTION_API 
// and TRIPLE_FUNCTION_LOCAL.
// TRIPLE_FUNCTION_API is used for the public API symbols. It either DLL imports 
// or DLL exports (or does nothing for static build). 
// TRIPLE_FUNCTION_LOCAL is used for non-api symbols.

#ifdef TRIPLE_FUNCTION_DLL // defined if TRIPLE_FUNCTION is compiled as a DLL
  #ifdef TRIPLE_FUNCTION_DLL_EXPORTS // defined if we are building the TRIPLE_FUNCTION DLL 
                           // (instead of using it)
    #define TRIPLE_FUNCTION_API TRIPLE_FUNCTION_HELPER_DLL_EXPORT
  #else
    #define TRIPLE_FUNCTION_API TRIPLE_FUNCTION_HELPER_DLL_IMPORT
  #endif // TRIPLE_FUNCTION_DLL_EXPORTS
  #define TRIPLE_FUNCTION_LOCAL TRIPLE_FUNCTION_HELPER_DLL_LOCAL
#else // TRIPLE_FUNCTION_DLL is not defined: this means TRIPLE_FUNCTION is a static lib.
  #define TRIPLE_FUNCTION_API
  #define TRIPLE_FUNCTION_LOCAL
#endif // TRIPLE_FUNCTION_DLL


#include "uint_std_t.h"


#ifdef __cplusplus
extern "C" {
#endif


TRIPLE_FUNCTION_API
uint_std_t triple_function(uint_std_t k);



#ifdef __cplusplus
}
#endif

#endif // #ifndef TRIPLE_FUNCTION_H

