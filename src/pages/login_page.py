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
        self.page = __________________________

        # TODO 2: Define the username-field locator.
        self.username = ______________________

        # TODO 3: Define the password-field locator.
        self.password = ______________________

        # TODO 4: Define the Login-button locator.
        self.login_button = __________________

        # TODO 5: Define the flash-message locator.
        self.message = _______________________

    def navigate(self) -> None:
        """Open the login page."""
        # TODO 6: Navigate to login_url.
        ______________________________________

    def login(self, user: str, password: str) -> None:
        """Enter credentials and submit the login form."""
        # TODO 7: Fill the username field with user.
        ______________________________________

        # TODO 8: Fill the password field with password.
        ______________________________________

        # TODO 9: Click the Login button.
        ______________________________________

    def assert_login_success(self) -> None:
        """Validate the successful-login state."""
        # TODO 10: Assert that the flash message is visible.
        ______________________________________

        # TODO 11: Assert that it contains success_text.
        expect(____________).to_contain_text(________________)

        # TODO 12: Assert that the URL contains /secure.
        expect(_________).to_have_url(________________________)

    def assert_login_failed(self) -> None:
        """Validate the invalid-password state."""
        # TODO 13: Assert that the flash message is visible.
        ______________________________________

        # TODO 14: Assert that it contains invalid_password_text.
        expect(____________).to_contain_text(________________________)

        # TODO 15: Assert that the URL still contains /login.
        expect(_________).to_have_url(________________________)