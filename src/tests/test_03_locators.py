"""
Exercise 03: Locators & Element Interaction

See Exercises/Module03_Locators.md for full instructions.
Run: pytest src/tests/test_03_locators.py -v --headed

Use three different locator strategies in the login flow:
1. CSS ID for the username
2. XPath for the password
3. ARIA role for the Login button
"""

from playwright.sync_api import expect, sync_playwright


target_url = "https://the-internet.herokuapp.com/login"
valid_username = "tomsmith"
valid_password = "SuperSecretPassword!"
expected_success_text = "You logged into a secure area!"


def test_login_with_different_locators() -> None:
    """Complete the login flow and the two required validations."""

    # TODO 1: Start Playwright in synchronous mode.
    with __________________________ as p:

        # TODO 2: Launch Chromium in headed mode.
        browser = __________________________________________

        try:
            # TODO 3: Create a new page.
            page = __________________________

            # TODO 4: Navigate to TARGET_URL.
            ________________________________________________

            # TODO 5: Create a CSS ID locator for the username field.
            username_field = _______________________________

            # TODO 6: Fill the username field with VALID_USERNAME.
            ________________________________________________

            # TODO 7: Create an XPath locator for the password field.
            password_field = _______________________________

            # TODO 8: Fill the password field with VALID_PASSWORD.
            ________________________________________________

            # TODO 9: Locate the Login button by ARIA role and accessible name.
            login_button = _________________________________

            # TODO 10: Click the Login button.
            ________________________________________________

            # TODO 11: Implement the URL assertion.
            # The URL after login must contain "/secure".
            expect(________).to_have_url(____________________)

            # TODO 12: Locate the success message.
            success_message = ______________________________

            # TODO 13: Implement the success-message assertion.
            expect(_______________).to_contain_text(_____________________)

            # TODO 14: Use one additional locator strategy.
            # Choose CSS attribute, label, text, or another suitable strategy.
            alternative_locator = __________________________

            # TODO 15: Use your alternative locator in a meaningful check or
            # interaction. Write the complete statement yourself.
            ________________________________________________

        finally:
            # TODO 16: Close the browser.
            ________________________________________________
