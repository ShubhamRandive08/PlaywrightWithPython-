import pytest

#before & after --> before this fucntion execute that & also
@pytest.mark.order(1)
def test_loginApp():
    print("This is loginApp test")

@pytest.mark.order(before="test_searchApp")
def test_LogoutApp():
    print("This is LogoutApp test")

@pytest.mark.order(after="test_LogoutApp")
def test_searchApp():
    print("This is searchApp test")



