from fuel import convert, gauge
import pytest

def test_input():
    assert convert('1/2') == 50
    assert convert('1/1') == 100
    assert convert('0/10') == 0

def test_errors():
    with pytest.raises(ZeroDivisionError):
         convert('2/0')
    with pytest.raises(ValueError):
         convert('3/2')

def test_output():
    assert gauge(1) == 'E'
    assert gauge(100) == 'F'
    assert gauge(50) == '50%'