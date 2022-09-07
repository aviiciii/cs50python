from project import select_movie, question, get_result


def test_select_movie():
    assert select_movie(['Avatar (2009)']) == ('Avatar', '2009')
    assert select_movie(['Avatar (200)']) == None
    assert select_movie(['Avatar 2009']) == None
    assert select_movie(['Avatar(2009)']) == None


def test_question():
    assert question('Avatar') == ['_','_','_','_','_','_']
    assert question('avatar') == ['_','_','_','_','_','_']
    assert question('Avatar 2') == ['_','_','_','_','_','_', ' ', '_']
    assert question('Avatar: 2') == ['_','_','_','_','_','_', ':', ' ', '_']


def test_get_result():
    assert get_result(True) == 'Correct!'
    assert get_result(False) == 'Incorrect, try again!'