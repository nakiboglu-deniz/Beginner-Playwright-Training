"""
Exercise 07: LoginPage Page Object
See Exercises/Module07_LoginFlowPOM.md for full instructions.

Complete this class before running:
pytest src/tests/test_07_login_pom.py -v --headed

Keep all login-page locators, actions, and page-specific assertions here.
"""

import re

from playwright.sync_api import Page, expect


class LoginPage:
    """Page object for The Internet login page."""

    login_url = "https://the-internet.herokuapp.com/login"
    success_text = "You logged into a secure area!"
    invalid_password_text = "Your password is invalid!"

    def __init__(self, page: Page) -> None:
        # TODO 1: Store the supplied Playwright Page.
        self.page = page

        # TODO 2: Define the username-field locator.
        self.username = "#username"

        # TODO 3: Define the password-field locator.
        self.password = "#password"

        # TODO 4: Define the Login-button locator.
        self.login_button = page.get_by_role("button", name="Login")

        # TODO 5: Define the flash-message locator.
        self.message = "#flash"

    def navigate(self) -> None:
        """Open the login page."""
        # TODO 6: Navigate to login_url.
        self.page.goto(self.login_url)

    def login(self, user: str, password: str) -> None:
        """Enter credentials and submit the login form."""
        # TODO 7: Fill the username field with user.
        self.page.fill(self.username,user)

        # TODO 8: Fill the password field with password.
        self.page.fill(self.password, password)

        # TODO 9: Click the Login button.
        self.login_button.click()

    def assert_login_success(self) -> None:
        """Validate the successful-login state."""
        # TODO 10: Assert that the flash message is visible.
        expect(self.page.locator(self.message)).to_be_visible()

        # TODO 11: Assert that it contains success_text.
        expect(self.page.locator(self.message)).to_contain_text(self.success_text)

        # TODO 12: Assert that the URL contains /secure.
        expect(self.page).to_have_url(re.compile(re.compile(r".*/status_codes$")))

    def assert_login_failed(self) -> None:
        """Validate the invalid-password state."""
        # TODO 13: Assert that the flash message is visible.
        expect(self.page.locator(self.message)).to_be_visible()

        # TODO 14: Assert that it contains invalid_password_text.
        expect(self.page.locator(self.message)).to_contain_text(self.invalid_password_text)

        # TODO 15: Assert that the URL still contains /login.
        #expect(_________).to_have_url(________________________)