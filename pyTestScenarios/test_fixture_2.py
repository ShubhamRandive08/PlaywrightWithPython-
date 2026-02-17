import pytest

@pytest.fixture(scope='module')
def setup():
    print("DB connection started")
    yield
    print("DB connection ended")

@pytest.fixture(scope='function')
def before_each_function():
    print("Establish connection with iOS driver")

    yield
    print("Connection terminated")

# def test_demo(setup,before_each_function):
#     print("Demo test")

@pytest.mark.usefixtures("setup")
def test_demo():
    print("Demo Test")