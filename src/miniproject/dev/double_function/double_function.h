
#ifndef DOUBLE_FUNCTION_H
#define DOUBLE_FUNCTION_H


#define DOUBLE_FUNCTION_DLL  // We want a DLL!!


// Generic helper definitions for shared library support
#if defined _WIN32 || defined __CYGWIN__
  #define DOUBLE_FUNCTION_HELPER_DLL_IMPORT __declspec(dllimport)
  #define DOUBLE_FUNCTION_HELPER_DLL_EXPORT __declspec(dllexport)
  #define DOUBLE_FUNCTION_HELPER_DLL_LOCAL
#else
  #if __GNUC__ >= 4
    #define DOUBLE_FUNCTION_HELPER_DLL_IMPORT __attribute__ ((visibility ("default")))
    #define DOUBLE_FUNCTION_HELPER_DLL_EXPORT __attribute__ ((visibility ("default")))
    #define DOUBLE_FUNCTION_HELPER_DLL_LOCAL  __attribute__ ((visibility ("hidden")))
  #else
    #define DOUBLE_FUNCTION_HELPER_DLL_IMPORT
    #define DOUBLE_FUNCTION_HELPER_DLL_EXPORT
    #define DOUBLE_FUNCTION_HELPER_DLL_LOCAL
  #endif
#endif


// Now we use the generic helper definitions above to define DOUBLE_FUNCTION_API 
// and DOUBLE_FUNCTION_LOCAL.
// DOUBLE_FUNCTION_API is used for the public API symbols. It either DLL imports 
// or DLL exports (or does nothing for static build). 
// DOUBLE_FUNCTION_LOCAL is used for non-api symbols.

#ifdef DOUBLE_FUNCTION_DLL // defined if DOUBLE_FUNCTION is compiled as a DLL
  #ifdef DOUBLE_FUNCTION_DLL_EXPORTS // defined if we are building the DOUBLE_FUNCTION DLL 
                           // (instead of using it)
    #define DOUBLE_FUNCTION_API DOUBLE_FUNCTION_HELPER_DLL_EXPORT
  #else
    #define DOUBLE_FUNCTION_API DOUBLE_FUNCTION_HELPER_DLL_IMPORT
  #endif // DOUBLE_FUNCTION_DLL_EXPORTS
  #define DOUBLE_FUNCTION_LOCAL DOUBLE_FUNCTION_HELPER_DLL_LOCAL
#else // DOUBLE_FUNCTION_DLL is not defined: this means DOUBLE_FUNCTION is a static lib.
  #define DOUBLE_FUNCTION_API
  #define DOUBLE_FUNCTION_LOCAL
#endif // DOUBLE_FUNCTION_DLL


#include "uint_std_t.h"


#ifdef __cplusplus
extern "C" {
#endif


DOUBLE_FUNCTION_API
uint_std_t double_function(uint_std_t k);



#ifdef __cplusplus
}
#endif

#endif // #ifndef DOUBLE_FUNCTION_H

