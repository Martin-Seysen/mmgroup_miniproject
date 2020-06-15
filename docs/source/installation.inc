
The current version of the ``miniproject`` package is a source distribution 
that has been tested on a 64-bit Windows platform only. It runs with 
python 3.6 or higher. The distribution contains a number of extensions 
written in ``C`` which have to be built before use. At present there is no 
binary distribution for Windows.

Before you can use this package or build its extensions you should install 
the following python packages:

.. table:: External Python packages required
  :widths: 30 70


  ======================== =========================================================
  Package                  Purpose 
  ======================== =========================================================
  ``cython``               Development: integrating ``C`` programs into the 
                           ``mminiproject`` package
  ``numpy``,  ``scipy``    Recommendation: These packages are not really needed here,
                           but they should be installed, since they are required for
                           the ``mmgroup`` package.
  ``pytest``               Testing: basic package used for testing
  ``setuptools``           Development: basic package used for setup and building
                           extensions
  ``sphinx``               Documentation: basic package used for documentation
  ``sphinxcontrib-bibtex`` Documentation: bibliography in BibTeX style
  ======================== =========================================================
    

Packages used for the purpose of documentation are required only if you want to 
rebuild the documentation. If you want to rebuild the documentation you should
also install the following programs:


.. table:: External programs required
  :widths: 20 30 50


  ========= ============== ===========================================================
  Program   Purpose        Location 
  ========= ============== ===========================================================
  miktex    Documentation  https://miktex.org/
  Perl      Documentation  https://www.perl.org/get.html
  ========= ============== ===========================================================



Building the extension
----------------------

To build the required extension, go to root directory of the distribution.
The is the directory containing the files ``setup.py`` and ``README.rst``.
From there run the following two commands::

    python setup.py build_ext 
    pytest src/miniproject/ -v







Installing a C compiler for cython in Windows 
---------------------------------------------

The bad news for Windows developers is that there is no pre-installed 
``C`` compiler on a standard Windows system. However, the ``Cython`` 
package requires a ``C`` compiler. Here in principle, the user has the 
choice between the following two compilers:

   *  ``MSVC``

   *  ``MinGW-w64``

The user has to install a ``C`` compiler so that it cooperates with 
``cython``. 
That installation process is out of the scope of this document.

For installing ``MinGW``, one might start looking at
https://cython.readthedocs.io/en/latest/src/tutorial/appendix.html.

For installing ``MSVC``, one might start looking at 
https://wiki.python.org/moin/WindowsCompilers

The current ``setup.py`` supports ``MinGW`` and ``MSVC`` for 64-bit 
Windows. According to the last URL the ``MinGW`` compiler works with 
all Python versions up to 3.4. 

The author has installed the ``MSVC`` compiler with the Microsoft
*Build Tools for Visual Studio* from:

https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=BuildTools&rel=16 ,

following the instructions in

https://www.scivision.dev/python-windows-visual-c-14-required/  .

Before typing ``python setup.py bdist_wheel`` in a Windows command 
line the author had to type::


  "C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\VC\Auxiliary\Build\vcvars64.bat"

Here the path my be different on the user's Windows system.


