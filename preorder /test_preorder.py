import subprocess


def test_normal():
    """Test a regular case."""
    generate_test(input=b'6\n1 2 5 3 6 4\n\n', output=b'1 2 5 3 6 4 ')


def generate_test(input, output):
    result = subprocess.run("python ./preorder.py".split(), input=input, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    assert result.returncode == 0
    assert result.stdout == output
    assert result.stderr == b''
