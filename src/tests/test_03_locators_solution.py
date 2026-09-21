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
    with sync_playwright() as p:

        # TODO 2: Launch Chromium in headed mode.
        browser = p.chromium.launch(
            headless= False,
            slow_mo=2000
        )

        try:
            # TODO 3: Create a new page.
            context = browser.new_context()
            page = context.new_page()

            # TODO 4: Navigate to TARGET_URL.
            page.goto(target_url)

            # TODO 5: Create a CSS ID locator for the username field.
            username_button = page.locator("#username")

            # TODO 6: Fill the username field with VALID_USERNAME.
            username_button.fill(valid_username)

            # TODO 7: Create an XPath locator for the password field.
            password_field = page.locator('//*[@id="password"]')

            # TODO 8: Fill the password field with VALID_PASSWORD.
            password_field.fill(valid_password)                      

            # TODO 9: Locate the Login button by ARIA role and accessible name.
            login_button = page.get_by_role("button",name="Login")

            # TODO 10: Click the Login button.
            login_button.click()

            # TODO 11: Implement the URL assertion.
            # The URL after login must contain "/secure".
            expect(page.url).to_have_url(target_url)

            # TODO 12: Locate the success message.
            success_message = page.locator('//*[@id="flash"]')

            # TODO 13: Implement the success-message assertion.
            expect(success_message).to_contain_text(expected_success_text)

            # TODO 14: Use one additional locator strategy.
            # Choose CSS attribute, label, text, or another suitable strategy.
            alternative_locator = __________________________

            # TODO 15: Use your alternative locator in a meaningful check or
            # interaction. Write the complete statement yourself.
            ________________________________________________

        finally:
            # TODO 16: Close the browser.
            browser.close()
