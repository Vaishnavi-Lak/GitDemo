import pytest


def test_demo2prog(setup):
    msg = "Hello"
    print(msg)
    assert msg == "Hello", "Match failed and text is different"


@pytest.mark.smoke
def test_demo2Second(setup):
    a = 3
    b = 6
    assert a + b == 9, "Addition did not match"
    print("Sum is", a + b)



