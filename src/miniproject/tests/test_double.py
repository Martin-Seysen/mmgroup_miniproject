from __future__ import absolute_import, division, print_function
from __future__ import  unicode_literals


import pytest

from random import randint

from miniproject.mini_double import uint_double



#####################################################################
# Test basis of Golay code and cocode against its reference
#####################################################################

@pytest.mark.user
def test_double():
    for i in range(24):
        x = randint(0, 1000)
        assert uint_double(x) == 2 * x



