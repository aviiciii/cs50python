from plates import is_valid

def test_length():
    assert is_valid('a') == False
    assert is_valid('ipho123') == False
    assert is_valid('van123') == True

def test_startLetters():
    assert is_valid('ab') == True
    assert is_valid('a123') == False
    assert is_valid('z2') == False

def test_numbersLast():
    assert is_valid('ama2on') == False
    assert is_valid('g00gle') == False
    assert is_valid('ll001') == False
    assert is_valid('ll100') == True

def test_invalidChar():
    assert is_valid('ir0.1') == False
    assert is_valid('gt!') == False
    assert is_valid('wall e') == False

