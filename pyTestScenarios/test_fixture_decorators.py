import pytest
@pytest.fixture # A fixture is a function that runs before and sometime after you test to provide setup data and environment for your tests. It is used to create a consistent and repeatable testing environment, allowing you to set up necessary conditions for your tests to run successfully.
def sample_data():
    data = {"name": "Shubham", "age": 25}
    return data

# This fixture will be executed once per module, and the returned value will be shared among all tests in the module that use this fixture.
@pytest.fixture(scope='module')
def sample_data2():
    print("Setup executed")
    return 100

# Yield fixture (Setup and Teardown)
@pytest.fixture
def browser():
    print("Launching browser")
    yield 'Browser instance'
    print("Closing browser")

'''
    - Code before yield is the setup code, which is executed before the test function runs.
    - Code after yield is the teardown code, which is executed after the test function completes.
    
    Very useful in 'Playwright' for :
            - Opening a browser
            - Closing browser
            - Cleaning Test Data
'''


def test_sample_data(sample_data):
    assert sample_data["name"] == "Shubham"
    assert sample_data["age"] == 25




