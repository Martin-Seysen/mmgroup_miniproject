from __future__ import absolute_import, division, print_function
from __future__ import  unicode_literals


import pytest

from random import randint

from miniproject.mini_triple import uint_triple



#####################################################################
# Test basis of Golay code and cocode against its reference
#####################################################################

@pytest.mark.user
def test_double():
    for i in range(24):
        assert uint_triple(i) == 3 * i



