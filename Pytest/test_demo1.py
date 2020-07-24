import pytest


@pytest.mark.smoke
def test_firstProgram(setup):
    print("Hello")


# every method is treated as a test case

@pytest.mark.skip
def test_secondProgram(setup):
    print("Good Morning")
