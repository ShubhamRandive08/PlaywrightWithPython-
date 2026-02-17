import pytest

def get_data():
    return [
        ("shubham@gmail.com", "1234"),
        ("shubham1@gmail.com", "1234")
    ]

@pytest.mark.parameter("username, password", get_data())
def test_loginflow(username,password):
    print(username, "------",password)