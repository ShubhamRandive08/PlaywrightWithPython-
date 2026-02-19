from playwright.sync_api import Page, expect
import re

def test_has_title(page : Page):
    page.goto("https://playwright.com")
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page : Page):
    page.goto('https://playwright.com')
    page.get_by_role("link", name="Get started").click()
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()
    page.wait_for_timeout(5000)