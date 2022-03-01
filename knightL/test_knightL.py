import knightL


def test_normal():
    """Test minimum case."""
    assert knightL.knightlOnAChessboard(5) == """4 4 2 8
4 2 4 4
2 4 -1 -1
8 4 -1 1"""
