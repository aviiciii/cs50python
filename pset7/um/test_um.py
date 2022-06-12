from um import count


def test_input():
    assert count('yummy') == 0
    assert count('mum ') == 0

def test_nospace():
    assert count('um') == 1
    assert count('um, can i... um... help?') == 2

def test_space():
    assert count(' um ') == 1

def test_case():
    assert count('Um, how you doin') == 1
    assert count('umm.. UM.. whats um up?') == 2
if __name__ == "__main__":
    main()