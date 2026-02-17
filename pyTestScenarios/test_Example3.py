import pytest

#before & after --> before this fucntion execute that & also
@pytest.mark.order("last")
def test_loginApp():
    print("This is loginApp test")

@pytest.mark.order()
def test_LogoutApp():
    print("This is LogoutApp test")

@pytest.mark.order("first")
def test_searchApp():
    print("This is searchApp test")



