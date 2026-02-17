import pytest

@pytest.fixture(scope='function')
def setup():
    print("Setup process")
    yield
    print("Close browser")

# @pytest.fixture(scope='function')
# def tear_down():
#     print("")

@pytest.mark.usefixtures('setup')
def test_login():
    print("Execution Completed")