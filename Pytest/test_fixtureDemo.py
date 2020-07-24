import pytest


@pytest.mark.usefixtures("setup")
class TestFixtures:

    def test_fixDemo1(self):
        print("Under fixDemo1")

    def test_fixDemo2(self):
        print("Under fixDemo2")

    def test_fixDemo3(self):
        print("Under fixDemo3")

    def test_fixDemo4(self):
        print("Under fixDemo4")


