# Exercise 2:  Use an existing test to discover (and fix) a bug
import pytest
from src.main import repeated_greetings


def test_neg_repeat():
    with pytest.raises(
        ValueError, match="Expected a strictly positive value for *repetition*, got -1"
    ):
        repeated_greetings("Clément", repetitions=-1)


def test_capitalization(capsys):
    # capitalize=True should force 'name' to be written as 'Name'
    repeated_greetings("clément", 1, captitalize=True)
    out, err = capsys.readouterr()
    assert out == "Hello Clément !"
