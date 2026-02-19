import re, pytest
from playwright.sync_api import sync_playwright # 1. sync_api : Synchronous version of the playwright. 2. sync_playwright : Main entry point to start playwright
with sync_playwright() as p: # sync_playwright() : Start the playwright engine
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://udemy.com")
    print(page.title())
    browser.close()

def test_new():
    print("Hell")