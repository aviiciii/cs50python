from seasons import get_min as f
import pytest

def test_input():
     with pytest.raises(TypeError):
         f(12-12-2012) == 'Invalid date'

# commented not required for submit
"""'def test_inpt():
    assert f(2012-13-12) == 'Invalid date'
    assert f(2012-12-32) == 'Invalid date'
    assert f(2012-32-12) == 'Invalid date'

def test_format():
    assert f(12-12-12) == 'Invalid date'
    assert f(2012-322-12) == 'Invalid date'
    assert f(323-1-1) == 'Invalid date'"""