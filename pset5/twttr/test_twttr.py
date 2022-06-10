from twttr import shorten

def test_nonAlpha():
    assert shorten('$twenty-five') == '$twnty-fv'
    assert shorten('25 dollars') == '25 dllrs'
    assert shorten('$25.00') == '$25.00'

def test_consonants():
    assert shorten('tstst') == 'tstst'
    assert shorten('lgbtq') == 'lgbtq'

def test_vowels():
    assert shorten('aie') == ''
    assert shorten('ou') == ''

def test_capital():
    assert  shorten('APPLE') == 'PPL'

