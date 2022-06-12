from working import convert
import pytest

def test_format():
    with pytest.raises(ValueError):
         convert('09:00 AM - 7:00 PM')
    with pytest.raises(ValueError):
         convert('9:00AM to 7:00PM')

def test_convert():
    assert convert('09:00 AM to 3:00 PM') == '09:00 to 15:00'
    assert convert('03:11 AM to 8:59 AM') == '03:11 to 08:59'

def test_range():
    with pytest.raises(ValueError):
         convert('09:00 AM to 17:00 PM')
    with pytest.raises(ValueError):
         convert('09:60 AM to 07:00 PM')

if __name__ == '__main__':
    main()