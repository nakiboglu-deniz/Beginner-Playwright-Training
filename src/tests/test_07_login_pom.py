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
    with __________________________ as p:

        # TODO 2: Launch Chromium in headed mode.
        browser = __________________________________________

        try:
            # TODO 3: Create a new page.
            page = __________________________

            # TODO 4: Create the LoginPage object.
            login_page = _________________________________

            # TODO 5: Navigate with the page object.
            ________________________________________________

            # TODO 6: Log in with the valid credentials.
            ________________________________________________

            # TODO 7: Validate the successful login.
            ________________________________________________

        finally:
            # TODO 8: Close the browser.
            ________________________________________________


def test_invalid_password_with_pom() -> None:
    """Complete the invalid-password scenario using only LoginPage methods."""

    # TODO 9: Start Playwright in synchronous mode.
    with __________________________ as p:

        # TODO 10: Launch Chromium in headed mode.
        browser = __________________________________________

        try:
            # TODO 11: Create a new page.
            page = __________________________

            # TODO 12: Create the LoginPage object.
            login_page = _________________________________

            # TODO 13: Navigate with the page object.
            ________________________________________________

            # TODO 14: Log in with valid_username and invalid_password.
            ________________________________________________

            # TODO 15: Validate the failed login.
            ________________________________________________

        finally:
            # TODO 16: Close the browser.
            ________________________________________________