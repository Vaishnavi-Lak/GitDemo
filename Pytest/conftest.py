import pytest


@pytest.fixture(scope="class")
def setup():
    print("First execution")
    yield  # is executed after test execution is completed
    print("Last execution")


@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["John", "Seal", "johns@gmail.com"]


@pytest.fixture(params=["Chrome", "Firefox", "IE"])
def crossBrowser(request):
    return request.param


@pytest.fixture(params=[("Chrome","John","Doe"), ("Firefox","John"),("IE","Serve")])
def crossBrowser(request):
    return request.param

# to align each value separately for a browser wrap the data together
# Eg: (params=[("Chrome","John","Doe"), ("Firefox","John")
