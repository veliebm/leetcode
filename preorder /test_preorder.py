import sys

def test_prompt(capsys, monkeypatch):
    t = "6"
    arr = "1 2 5 3 6 4"
    stdout = "1 2 5 3 4 6 "

    def yield_input():
        def get():
            temp = yield_input.__dict__.get('previous', t)
            yield_input.__dict__['previous'] = arr
            return temp
        return get()

    with monkeypatch.context() as m:
        m.setattr("builtins.input", yield_input)
        import preorder
        del sys.modules["preorder"]
        captured = capsys.readouterr()
        assert captured.out == stdout
