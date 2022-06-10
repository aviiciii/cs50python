from bank import value

def test_hello():
    assert value('hello') == 0
    assert value('hello, world') == 0


def test_h():
    assert value('hey') == 20
    assert value('how ya doin') == 20
    assert value('hola habibi') == 20
    assert value('hel, lo') == 20

def test_noH():
    assert value('whats up, buddy') == 100
    assert value('what the he!@') == 100

def test_capital():
    assert value('HELLO') == 0
    assert value('Hey') == 20