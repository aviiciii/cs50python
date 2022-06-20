from jar import Jar
import pytest


def test_init():
    with pytest.raises(ValueError):
         jar = Jar(-1)


def test_init_correct():
    jar = Jar(10)
    assert str(jar) == ''


def test_str():
    jar = Jar()
    assert str(jar) == ''

    jar.deposit(1)
    assert str(jar) == '🍪'

    jar.deposit(11)
    assert str(jar) == '🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪'


def test_deposit():
    jar = Jar(10)

    jar.deposit(10)
    assert str(jar) == '🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪'

    with pytest.raises(ValueError):
         jar.deposit(1)


def test_withdraw():
    jar = Jar(10)

    jar.deposit(8)
    jar.withdraw(2)
    assert str(jar) == '🍪🍪🍪🍪🍪🍪'

    with pytest.raises(ValueError):
         jar.deposit(8)