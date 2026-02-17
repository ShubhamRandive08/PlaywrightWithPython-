# To know the concept of the Markers
import pytest

@pytest.fixture
def page():
    print("Open Browser")
    yield
    print("Close Browser")

@pytest.mark.sanity
def test_sanity(page):
    print("Sanity Testing with browser")

@pytest.mark.smoke
def test_smoke(page):
    print("Smoke Testing with Browser")

@pytest.mark.skip
def test_skip():
    print("Skip Test")