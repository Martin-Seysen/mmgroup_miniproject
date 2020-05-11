

================================
Description of the *miniproject*
================================


Introduction
============

The *miniproject* package is a tiny stupid package that demonstrates the
build process for the *mmgroup* package. The *mmgroup* package is 
a python implementation of Conway's construction :cite:`Con85` of the 
monster group :math:`\mathbb{M}`, which is the largest sporadic 
finite simple group. 

That package contains C programs that have been generated automatically 
by a progam code generator. Here automatically generated low-level 
functions written in C are used to compute rather large tables, which
will be use by high-level C programs. This means that the build
process has to take place in several stages. Also, there are C 
subroutines which are used by both, low-level and high-level functions.
So it makes sense to place these subroutines into a shared library.

When porting the *mmgroup* package to another operating system, several
aspects specific to the operating system have to be considered. This 
*miniproject* package can be considered as a model for the 
*mmgroup* package focussing on the os-specific aspects.


Installation
============

.. include:: installation.inc

Application interface
=====================

.. autofunction:: miniproject.wrapper.wrap_double

.. autofunction:: miniproject.wrapper.wrap_triple


The modified build process
==========================

The necessary classes for modifying the build process given by the
``setuptools/distutils`` package is code in the ``build_ext_steps.py``
script.


.. automodule:: build_ext_steps


The build process for the *miniproject* package
===============================================

The *miniproject* package
contains a function ``double_function`` written in C and stored in
a shared library. That function doubles an integer value. There is a 
python wrapper (written in Cython) which makes that function available
in python. The ``pytest`` package is used to test that function.

The *miniproject* package also contains a function ``triple_function`` 
witten in C  and stored in another shared library. Again, there is a 
python wrapper (written in Cython) for that function so that it can also 
be tested with ``pytest``.

Function ``triple_function`` calls function ``double_function``, which
is in a different shared library. For small values it uses a 
precomputed table ``triple_table.c`` for tripling a number. That table 
is precomputed by the python script ``codegen.py``. Of course, the
C program ``triple_table.c`` must be integrated into the process that
builds the python wrapper for function ``triple_function``.
 
So the functionality provided by this package is trivial, but the 
building process for this package is extremely involved. That build 
process is based on the standard  ``setuptools/distutils`` package. As 
usual, there is a standard script ``setup.py`` in the root directory of 
the package controls the build process. 

In the current version the necessary modifications of the 
``setuptools/distutils`` package required for a multi-step build
process are contain in the ``build_ext_steps.py`` script in the
root directory.

Porting  the *miniproject* and the *mmgroup* package
====================================================

The current versions of the *miniproject* and *mmgroup* packages 
support the 64-bit Windows operating system with the *mingw32* 
complier only.

The author is aware of the fact that porting a package as complex as
the *mmgroup* package to a different operating system, or even 
adjusting it to a different compiler, may be a highly frustrating job.
Here the  *miniproject* can be used as a model for the *mmgroup*
package.

It is highly recommended to port the *miniproject* to any operating 
system before porting the *mmgroup* package.

After porting the *miniproject* the file ``build_ext_steps.py``
(and all new files created for the porting process)
should be copied from the root directory of the *miniproject*
to the corresponding directory of the *mmgroup* package. 


.. only:: html

   .. rubric:: **References**

.. bibliography:: references.bib



