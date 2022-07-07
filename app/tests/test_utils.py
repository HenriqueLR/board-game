from utils.square import cast_square


def test_cast_square():
    assert type(cast_square()) == int
    assert cast_square() <= 6
