from __future__ import absolute_import, division, print_function

import sys
import os
import subprocess
import numpy as np
from glob import glob

import setuptools
from setuptools import setup, find_packages
from build_ext_steps import Extension, CustomBuildStep, SharedExtension
from build_ext_steps import BuildExtCmd




import config
from config import EXTRA_COMPILE_ARGS, EXTRA_LINK_ARGS
from config import ROOT_DIR, SRC_DIR, PACKAGE_DIR, DEV_DIR
from config import REAL_SRC_DIR
from config import C_DIR, DOC_DIR,  PXD_DIR

####################################################################
# Delete files
####################################################################

# The following intermediate files must be deleted are after 
# building the extension
intermediate_delete = [
     os.path.join(C_DIR, "*.o"),
     os.path.join(PXD_DIR, "*.o"),
]

def delete_intermediate_files():
    for file_pattern in intermediate_delete:
        #print(file_pattern)
        for file in glob(file_pattern):
            try:
                #print(file)
                os.remove(file)
            except:
                pass



# The following files are deleted before building the extension
# if the command line option -f or --force has been set
ext_delete = [
    os.path.join(PACKAGE_DIR, "*.dll"), 
    os.path.join(PACKAGE_DIR, "*.pyd"),
]


def force_delete():
    """Delete some files before command 'build_ext'"""
    if not "-f" in sys.argv and not  "--force" in sys.argv:
        return
    for file_pattern in ext_delete:
        print(file_pattern)
        for file in glob(file_pattern):
            try:
                print(file)
                os.remove(file)
            except:
                pass
   


####################################################################
# create directories
####################################################################

def make_dir(*args):
    """Create subdirectory if it does not exist

    The path is given by the arguments
    """
    directory = os.path.realpath(os.path.join(*args))
    if not os.path.exists(directory):
        os.makedirs(directory)
    fname = os.path.join(directory, "readme.txt")
    with open(fname, "wt") as f:
        f.write(
"""The files in this directory have been created automatically
or copied from some other place.
So it is safe to delete all files in this directory.
"""
        )   

####################################################################
# extend path
####################################################################

def extend_path():
    sys.path.append(REAL_SRC_DIR)

####################################################################
# Desription of the list 'custom_presteps'.
#
# This is a list of programs to be run before executing the 'build_ext' 
# command. Each entry of list 'custom_presteps' is a list which we call 
# a program lists. A program list ia a list of strings corresponding to 
# a program to be executed with:
#     subprocess.call(program_list) . 
# The first entry of a program list is the name of the program to be 
# executed; here sys.executable means the current python version. 
# Subsequents entries correspond to command line arguments.
#
# If the first entry in that list is not a string then it is 
# interpreted as a function to be called with the arguments
# given by the subsequent entries of that list.
####################################################################


if os.name == "nt":
    shared_libs_stage1 = ["libdouble_code"]
    shared_libs_stage2 = shared_libs_stage1 + [
                "libtriple_code"]
else:
    raise DistutilsPlatformError(
        "I don't know how to link to the shared libraries "
        "(just built) in the '%s' operating system" % os.name
    )


stage1_presteps = CustomBuildStep(
  "prepare_stage1",
  [make_dir, "src", "miniproject", "dev", "c_files"],
  [make_dir, "src", "miniproject", "dev", "c_doc"],
  [make_dir, "src", "miniproject", "dev", "pxd_files"],
  [force_delete],
  [extend_path],
  [sys.executable,  "codegen_stage1.py"],
)


stage1_shared = SharedExtension(
   "miniproject.double_code",
    sources = [
        os.path.join(C_DIR,  "double_function.c"),
    ],
    include_dirs = [ C_DIR ],
    library_dirs = [ C_DIR  ],
    extra_compile_args = EXTRA_COMPILE_ARGS, 
    extra_link_args = EXTRA_LINK_ARGS,
    implib_dir = C_DIR,
    define_macros = [ ("DOUBLE_FUNCTION_DLL_EXPORTS", None)],
)


stage2_presteps = CustomBuildStep(
  "prepare_stage2",
  [sys.executable, "codegen_stage2.py"],
)


stage2_shared = SharedExtension(
    "miniproject.triple_code",
    sources = [
        os.path.join(C_DIR,  "triple_function.c"),
        os.path.join(C_DIR,  "triple_table.c"),
    ],
    libraries = shared_libs_stage1, 
    include_dirs = [ C_DIR ],
    library_dirs = [ C_DIR],
    extra_compile_args = EXTRA_COMPILE_ARGS, 
    extra_link_args = EXTRA_LINK_ARGS,
    implib_dir = C_DIR,
    define_macros = [ ("TRIPLE_FUNCTION_DLL_EXPORTS", None)],
)



import_step = CustomBuildStep(
    "import python extensions",
    [sys.executable,  "import_all.py"],
    [delete_intermediate_files],
    ["pytest", "src/miniproject/", "-v"],
)


ext_modules=[
    stage1_presteps,
    stage1_shared, 
    Extension("miniproject.mini_double",
        sources=[
            os.path.join(PACKAGE_DIR, "dev", 
               "pxd_files", "mini_double.pyx"),
        ],
        #libraries=["m"] # Unix-like specific
        include_dirs = [ C_DIR ],
        library_dirs = [C_DIR , PACKAGE_DIR] ,
        libraries = shared_libs_stage1, 
        #runtime_library_dirs = ["."],
        extra_compile_args = EXTRA_COMPILE_ARGS, 
        extra_link_args = EXTRA_LINK_ARGS, 
    ),
    stage2_presteps,
    stage2_shared, 
    Extension("miniproject.mini_triple",
        sources=[
            os.path.join(PACKAGE_DIR, "dev", 
               "pxd_files", "mini_triple.pyx"),
        ],
        #libraries=["m"] # Unix-like specific
        include_dirs = [ C_DIR ],
        library_dirs = [C_DIR , PACKAGE_DIR] ,
        libraries = shared_libs_stage2, 
        #runtime_library_dirs = ["."],
        extra_compile_args = EXTRA_COMPILE_ARGS, 
        extra_link_args = EXTRA_LINK_ARGS, 
    ),
    import_step,
]


long_description = """The *miniproject* package is a tiny package that demonstrates the
build process for the *mmgroup* package. The *mmgroup* package is a 
python implementation of Conway's construction of the monster group, 
which is the largest sporadic finite simple group. 

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
"""



setup(
    name = 'miniproject',    
    version = '0.0.1',    
    license='BSD-2-Clause',
    description='This models the build process of the mmgroup project',
    long_description=long_description,
    author='Martin Seysen',
    author_email='m.seysen@gmx.de',
    url='https://github.com/Martin-Seysen/mmgroup_miniproject.git',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        #'Operating System :: Unix',
        #'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        #Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        # uncomment if you test on these interpreters:
        # 'Programming Language :: Python :: Implementation :: IronPython',
        # 'Programming Language :: Python :: Implementation :: Jython',
        # 'Programming Language :: Python :: Implementation :: Stackless',
        'Topic :: Scientific/Engineering :: Mathematics',
    ],
    project_urls={
       # 'Changelog': 'yet unknown',
       # 'Issue Tracker': 'yet unknown',
    },
    keywords=[
        
    ],
    python_requires='>=3.6',
    install_requires=[
         'numpy', 'scipy', 
    ],
    extras_require={
        # eg:
        #   'rst': ['docutils>=0.11'],
        #   ':python_version=="2.6"': ['argparse'],
    },
    setup_requires=[
        'numpy', 'scipy', 'pytest-runner', 'Cython',
        # 'sphinx',  'sphinxcontrib-bibtex',
    ],
    tests_require=[
        'pytest',
    ],
    cmdclass={
        'build_ext': BuildExtCmd,
    },
    ext_modules = ext_modules,
    include_dirs=[np.get_include()],  # This gets all the required Numpy core files
)



