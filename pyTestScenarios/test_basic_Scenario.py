import pytest

def setup_function():
    print("This is the setup function")

def teardown_function():
    print("This is the teardown function")

def test_login():
    print("This is the login test")

def test_logout():
    print("This is the logout test")