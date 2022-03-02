import sys
from unittest.mock import Mock
import pytest


testdata = [
    ("ABACA", "ABACA"),
    ("Rumpelstiltskin", "Rumpelstiltskin"),
    ("howmuchwoodwouldawoodchuckchuckifawoodchuckcouldchuckwood?", "howmuchwoodwouldawoodchuckchuckifawoodchuckcouldchuckwood?"),
]


@pytest.mark.parametrize("stdin, stdout", testdata)
def test_case(stdin, stdout, capsys, monkeypatch):
    """
    Test a case.
    """
    yield_input = Mock(side_effect=stdin.splitlines())

    with monkeypatch.context() as m:
        m.setattr("builtins.input", yield_input)
        import huffman
        captured = capsys.readouterr()
        assert captured.out == stdout
        del sys.modules["huffman"]
