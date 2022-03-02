import sys
from unittest.mock import Mock

def test_prompt(capsys, monkeypatch):
    t = "6"
    arr = "1 2 5 3 6 4"
    stdout = "1 2 5 3 4 6 "
    yield_input = Mock(side_effect=[t, arr])

    with monkeypatch.context() as m:
        m.setattr("builtins.input", yield_input)
        import preorder
        del sys.modules["preorder"]
        captured = capsys.readouterr()
        assert captured.out == stdout
