import sys
from unittest.mock import Mock
import pytest


testdata = [
    ("6\n1 2 5 3 6 4", "1 2 5 3 4 6 "),
    ("15\n1 14 3 7 4 5 15 6 13 10 11 2 12 8 9", "1 14 3 2 7 4 5 6 13 10 8 9 11 12 15 "),
]


@pytest.mark.parametrize("stdin, stdout", testdata)
def test_case(stdin, stdout, capsys, monkeypatch):
    """Test a case."""
    yield_input = Mock(side_effect=stdin.splitlines())

    with monkeypatch.context() as m:
        m.setattr("builtins.input", yield_input)
        import preorder
        captured = capsys.readouterr()
        assert captured.out == stdout
        del sys.modules["preorder"]
