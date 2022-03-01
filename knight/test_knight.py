import knight


def test_normal():
    """Test normal, standard case."""
    assert knight.moves(4, 0, 0, 1, 1, 1, 0) == 4
    assert knight.moves(7, 0, 0, 4, 3, 3, 4) == 5


def test_unreachable():
    """Test case in which knight cannot reach goal."""
    assert knight.moves(5, 0, 0, 4, 3, 3, 0) == -1


def test_trivial():
    """Test case in which knight spawns on goal."""
    assert knight.moves(15, 12, 12, 12, 12, 10, 9) == 0
    assert knight.moves(20, 12, 12, 12, 12, 11, 11) == 0
