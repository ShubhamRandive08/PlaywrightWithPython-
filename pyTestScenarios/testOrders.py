import pytest


@pytest.mark.order(1)
def test_login():
    print("Login")

@pytest.mark.order(5)
def test_logout():
    print("Logout")

@pytest.mark.order(2)
def test_search():
    print("Search App")

@pytest.mark.order(3)
def test_edit():
    print("Edit User")

@pytest.mark.order(4)
def test_delete():
    print("Delete user")


