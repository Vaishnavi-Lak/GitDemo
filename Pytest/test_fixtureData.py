import pytest

from Pytest.BaseClass import Baseclass


@pytest.mark.usefixtures("dataLoad")
class TestExample(Baseclass):
    def test_editProfile(self, dataLoad):
        log = self.logDemo()
        print(dataLoad)
        print(dataLoad[0])
        log.info("This is for data load 0")
        print(dataLoad[1])
        log.warning(dataLoad[1])


def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])
