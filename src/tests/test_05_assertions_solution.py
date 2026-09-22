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
    with sync_playwright() as p:

        # TODO 2: Launch Chromium in headed mode.
        browser = p.chromium.launch()

        try:
            # TODO 3: Create a new page.
            page = browser.new_page()

            # TODO 4: Navigate to target_url.
            page.goto(target_url)

            # TODO 5: Locate and fill the username field.
            page.fill("#username",valid_username)

            # TODO 6: Locate and fill the password field.
            page.fill("#password",valid_password)

            # TODO 7: Locate and click the Login button.
            page.get_by_role("button",name="Login").click()

            # TODO 8: Assert that the page title contains
            # expected_title_text. Use re.compile().
            expect(page).to_have_title(re.compile(expected_title_text))

            # TODO 9: Assert that the URL contains expected_url_path.
            # Use re.compile().
            expect(page).to_have_url(re.compile(expected_url_path))

            # TODO 10: Locate the success message using #flash.
            success_message = page.locator("#flash")

            # TODO 11: Assert that the success message is visible.
            expect(success_message).to_be_visible()

            # TODO 12: Assert that it contains expected_success_text.
            expect(success_message).to_contain_text(expected_success_text)

            # TODO 13: Locate the Logout link by role and accessible name.
            logout_link = page.get_by_role("link", name ="Logout")

            # TODO 14: Assert that the Logout link is visible.
            expect(logout_link).to_be_visible()

            # TODO 15: Assert that its href equals expected_logout_href.
            expect(logout_link).to_have_attribute("href", expected_logout_href) 

            # TODO 16: Locate the body element.
            page_body = page.locator("body")

            # TODO 17: Assert that the body is visible.
            expect(page_body).to_be_visible()

            # TODO 18: Print: All assertions passed!
            print("All assertions passed!")
            
        finally:
            # TODO 19: Close the browser.
            browser.close()