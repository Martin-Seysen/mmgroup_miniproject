This project demonstrates the build process for the ``mmgroup`` project.

The build process for the ``mmgroup`` python  project is quite involved. 
It proceeds in several stages. Python extensions generated in an early 
stage of the build process are used to generate (rather large) tables
which are used in automatically generated C programs. These C programs
are used as building building blocks for more python extensions in a
later stage of the building process. 

When porting the ``mmgroup`` project to another operating system we  
highly recommend to port this ``miniproject`` first.


Project Documentation see

https://mmgroup-miniproject.readthedocs.io/en/latest/

License
-------

Copyright Martin Seysen, 2020.

Distributed under the terms of the `MIT`_ license, the miniproject is free and 
open source software.

.. _`MIT`: https://github.com/Martin-Seysen/test_repository/blob/master/LICENSE

