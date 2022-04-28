# Testing code


## What's automated testing ?

> *testing* is the practice of evaluating software
> by checking runtime behaviour VS intented behaviour.

> *manual testing* consists in checking "by hand" (or by eye) that the
> application works.

> *automated testing* consists in making the run+check part automatic.

Manual testing is easy, but doesn't scale, and tommorow you'll have to start from scratch.

Automated tested is *scalable* and *can* be easy (if you know your tools).

## Why bother ?

Here's a non-exhaustive list of ways tests can be useful

1) tests help demonstrate softare works as intented *and continues to in the future*
2) tests help catching bugs before broken code is pushed to prod
3) tests enable refactoring
4) tests document intented usage

## What's *a* test ?

Essentially, a test is a small piece of user code that can be thought of as a 4 steps process:
1) set the stage (*setup*)
2) do something
3) make assertions about the result
4) cleanup (*teardown*)

steps 1 and 4 are optional, and sometimes even step 2.

https://docs.pytest.org/en/7.1.x/explanation/anatomy.html#test-anatomy


# Testing in Python

There are a handlful ways to write tests in Python.
We will briefly see what the standard library offers before we switch to `pytest`.

This directory contains a dummy Python package under `src` which contains
code to be tested, and a `tests` directory with example test code.


### demonstrate unittest
Invoke
```shell
$ python -m unittest tests/test_unittest.py
```

What we learned:
- `unittest` is part of the standard library (available anywhere !)
- writing tests requires creating whole classes (subclassing `unittest.TestCase`)
- we can test within a context (`setUp` + `tearDown`) to handle side effects

> *side effects* encompass every observable state change caused by calling function,
>other than its return value.
>
> Side effects are not intrinsically undesirable (e.g. `os.makedirs` is *mostly* about side effects).

### demonstrate pytest
Invoke
```shell
$ pytest tests/test_pytest.py
```

What we learned:
- pytest enables writing tests as functions instead of class methods
- no need to use special comparision methods like `assertEqual`, `assertIsNotNone`...
- pytest is compatible with unittest !

## Diving into pytest

### possible test outcomes

Let's review all possible outcomes of a test
1) *PASS* -> everything went well, hurray !
2) *FAIL* -> the test failed ! the code under test is probably broken (or maybe the test itself...)
3) *ERROR* -> something wen wrong during test *collection*, some tests could not be run
4) *SKIPPED* -> the test was intentionally not run
5) *XFAIL* -> the test was eXpected to fail, and did
6) *XPASS* -> the test was eXpected to fail, but passed !
7) *XPASS* into *FAIL* -> the test was eXpected to fail, but passed, *and* we're considering this as a FAIL

### pytest's core concept: fixtures
> *fixture* is a word with a lot of different meanings in the programming world.
> pytest calls "fixtures" functions that run before and sometimes after a test.
> They can be used and combined to create a *context* (setup/teardown) or handle test data.

Their syntax is a little unique to pytest. For instance you will often see
fixture passed as arguments to a test function
```python
import pytest

@pytest.fixture()
def hello_goodbye():
    print("Hi !")
    yield
    print("Goodbye !")

def test_stuff(hello_goodbye):
    assert 1 == 1

```

Alternatively, when the return value of the fixture isn't used within a test, it
is good practice to declare it with a decorator instead
```python
@pytest.mark.usefixtures("hello_goodbye")
def test_stuff_2():
    assert 1 == 1
```

TODO:
- build our own fixture `tmp_file`
- 'disassemble' setup/teardown (`--setup-show`)
- review a couple builtin fixtures (`tmp_path`, `capsys`...)
- build a reusable test dataset as a fixture (scope="session")

### testing for failures: `pytest.raises` and `pytest.warns`
It is good practice to check what happens when your code *can't* work.
Testing for ill cases helps making sure error messages are clear.

```python
import pytest

def foo():
   raise ValueError("don't call this function")

def test_error():
    with pytest.raises(
        ValueError,
        match="don't call this function",
    ):
        foo()
```

### scaling tests cases with `pytest.mark.parametrize`
Show live examples ?
https://github.com/neutrinoceros/inifix/blob/e03a75172869534e6539040dc45a74513eb7cf3a/tests/test_io.py#L44


### pytest CLI cheatsheet
Most useful command line flags include:

- `-s` don't capture stdout (free `print`)
- `-v` (also `-vv` and `-vvv`) increase output verbosity
- `-x` stop after one failure
- `--pdb` invoke the Python debugger on failures
- `--lf` (or `--last-failed`) only run tests which failed last time
- `--sw` (or `--step-wise`) run all tests and stop at the first failing one. Next invoke will start on that test.

### Exercises
#### 1. Write test code for existing library code

#### 2. Use an existing test to discover (and fix) a bug
> *TDD* or "Test Driven Development" is the practice of writing tests first, and
> library code later. The idea is to envision *how* code should be used and *what*
> it should do before it even exists, so there's less of a chance we will unwillingly
> displace goals.
#### 3. Free time: test your own stuff !
