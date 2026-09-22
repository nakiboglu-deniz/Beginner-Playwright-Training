"""
Exercise 07: Login Flow with Page Object Model
See Exercises/Module07_LoginFlowPOM.md for full instructions.
Run: pytest src/tests/test_07_login_pom.py -v --headed

Complete two scenarios using LoginPage:
1. Successful login
2. Invalid-password login

Do not place CSS or XPath selectors in this test file.
"""

from playwright.sync_api import sync_playwright

from pages.login_page import LoginPage


valid_username = "tomsmith"
valid_password = "SuperSecretPassword!"
invalid_password = "wrongpassword"


def test_successful_login_with_pom() -> None:
    """Complete the valid-login scenario using only LoginPage methods."""

    # TODO 1: Start Playwright in synchronous mode.
    with sync_playwright() as p:

        # TODO 2: Launch Chromium in headed mode.
        browser = p.chromium.launch(headless=False, slow_mo=2000)

        try:
            # TODO 3: Create a new page.
            page = browser.new_page()

            # TODO 4: Create the LoginPage object.
            login_page = LoginPage(page)

            # TODO 5: Navigate with the page object.
            login_page.navigate()

            # TODO 6: Log in with the valid credentials.
            login_page.login(valid_username,valid_password)

            # TODO 7: Validate the successful login.
            login_page.assert_login_success()

        finally:
            # TODO 8: Close the browser.
            browser.close()


def test_invalid_password_with_pom() -> None:
    """Complete the invalid-password scenario using only LoginPage methods."""

    # TODO 9: Start Playwright in synchronous mode.
    with sync_playwright() as p:

        # TODO 10: Launch Chromium in headed mode.
        browser = p.chromium.launch()

        try:
            # TODO 11: Create a new page.
            page = browser.new_page()

            # TODO 12: Create the LoginPage object.
            login_page = LoginPage(page)

            # TODO 13: Navigate with the page object.
            login_page.navigate()

            # TODO 14: Log in with valid_username and invalid_password.
            login_page.login(valid_username,invalid_password)

            # TODO 15: Validate the failed login.
            login_page.assert_login_failed()

        finally:
            # TODO 16: Close the browser.
            browser.close()