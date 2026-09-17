"""
Exercise 05: Assertions
See Exercises/Module05_Assertions.md for full instructions.
Run: pytest src/tests/test_05_assertions.py -v --headed

Complete a successful login flow and validate:
1. Page title and URL
2. Success-message visibility and text
3. Logout-link visibility and href
4. Basic page visibility
"""

import re

from playwright.sync_api import expect, sync_playwright


target_url = "https://the-internet.herokuapp.com/login"
valid_username = "tomsmith"
valid_password = "SuperSecretPassword!"
expected_title_text = "Internet"
expected_url_path = "/secure"
expected_success_text = "You logged into a secure area!"
expected_logout_href = "/logout"


def test_successful_login_assertions() -> None:
    """Complete the login flow and all required assertions."""

    # TODO 1: Start Playwright in synchronous mode.
    with __________________________ as p:

        # TODO 2: Launch Chromium in headed mode.
        browser = __________________________________________

        try:
            # TODO 3: Create a new page.
            page = __________________________

            # TODO 4: Navigate to target_url.
            ________________________________________________

            # TODO 5: Locate and fill the username field.
            ________________________________________________

            # TODO 6: Locate and fill the password field.
            ________________________________________________

            # TODO 7: Locate and click the Login button.
            ________________________________________________

            # TODO 8: Assert that the page title contains
            # expected_title_text. Use re.compile().
            expect(________).to_have_title(__________________)

            # TODO 9: Assert that the URL contains expected_url_path.
            # Use re.compile().
            expect(________).to_have_url(____________________)

            # TODO 10: Locate the success message using #flash.
            success_message = ______________________________

            # TODO 11: Assert that the success message is visible.
            ________________________________________________

            # TODO 12: Assert that it contains expected_success_text.
            expect(_______________).to_contain_text(_____________________)

            # TODO 13: Locate the Logout link by role and accessible name.
            logout_link = __________________________________

            # TODO 14: Assert that the Logout link is visible.
            ________________________________________________

            # TODO 15: Assert that its href equals expected_logout_href.
            expect(___________).to_have_attribute(_______, _______________)

            # TODO 16: Locate the body element.
            page_body = ____________________________________

            # TODO 17: Assert that the body is visible.
            ________________________________________________

            # TODO 18: Print: All assertions passed!
            ________________________________________________

        finally:
            # TODO 19: Close the browser.
            ________________________________________________