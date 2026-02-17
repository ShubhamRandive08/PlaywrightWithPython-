import pytest

@pytest.mark.order(1)
def test_loginApp():
    print("This is loginApp test")

@pytest.mark.order(5)
def test_LogoutApp():
    print("This is LogoutApp test")

@pytest.mark.order(2)
def test_searchApp():
    print("This is searchApp test")

@pytest.mark.order(3)
def test_createUser():
    print("This is createUser test")

@pytest.mark.order(6)
def test_editUser():
    print("This is editUser test")

@pytest.mark.order(4)
def test_deleteUser():
    print("This is deleteUser test")

