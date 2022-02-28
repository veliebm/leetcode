import knight


def test_normal():
    assert knight.moves(4, 0, 0, 1, 1, 1, 0) == 4


def test_unreachable():
    assert knight.moves(5, 0, 0, 4, 3, 3, 0) == -1


def test_trivial():
    assert knight.moves(15, 12, 12, 12, 12, 10, 9) == 0
    assert knight.moves(20, 12, 12, 12, 12, 11, 11) == 0
