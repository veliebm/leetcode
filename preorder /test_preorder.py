import sys
from unittest.mock import Mock


def test_cases(capsys, monkeypatch):
    cases = [
        ("6", "1 2 5 3 6 4", "1 2 5 3 4 6 ")
    ]

    for case in cases:
        run_test(*case, capsys, monkeypatch)


def run_test(t, arr, stdout, capsys, monkeypatch):
    yield_input = Mock(side_effect=[t, arr])

    with monkeypatch.context() as m:
        m.setattr("builtins.input", yield_input)
        import preorder
        captured = capsys.readouterr()
        assert captured.out == stdout
        del sys.modules["preorder"]
