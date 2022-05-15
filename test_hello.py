from hello import add, mult


def test_add():
    assert 2 == add(1, 1)


def test_mult():
    assert 6 == mult(3, 2)
    assert 21 == mult(7, 3)
