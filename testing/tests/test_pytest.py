import pytest
from src.algebra import add
from src.greetings import greet


def test_simple_additon():
    assert add(1, 1) == 2


@pytest.mark.xfail
def test_broken(self):
    assert add(1, 1) == 3


def test_greet_to_file(tmp_path):
    # tmp_path is a temporary directory
    outfile = tmp_path / "greetings.txt"
    greet("Heisenberg", str(outfile))
    content = outfile.read_text()
    assert content == "Hello Heisenberg !"
