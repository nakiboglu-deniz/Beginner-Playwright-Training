"""
Exercise 08: Test Report & Screenshot
See Exercises/Module08_TestReportScreenshot.md for full instructions.
Run:
pytest src/tests/test_08_report_screenshot.py -v --headed -s \
    --html=report.html --self-contained-html

Complete an intentionally failing login test that captures:
1. The initial page state
2. The UI state when the assertion fails
3. A self-contained pytest HTML report
"""

import os

from playwright.sync_api import expect, sync_playwright


target_url = "https://the-internet.herokuapp.com/login"
valid_username = "tomsmith"
invalid_password = "wrongpassword"
expected_success_text = "You logged into a secure area!"
screenshot_directory = "screenshots"
before_screenshot = "screenshots/before_login.png"
failure_screenshot = "screenshots/failure.png"


def test_capture_failed_login_and_report() -> None:
    """Complete the failed-login flow and capture diagnostic screenshots."""

    # TODO 1: Create screenshot_directory if it does not exist.
    ________________________________________________

    # TODO 2: Start Playwright in synchronous mode.
    with __________________________ as p:

        # TODO 3: Launch Chromium in headed mode.
        browser = __________________________________________

        try:
            # TODO 4: Create a new page.
            page = __________________________

            # TODO 5: Navigate to target_url.
            ________________________________________________

            # TODO 6: Capture the initial state at before_screenshot.
            ________________________________________________

            # TODO 7: Fill the username with valid_username.
            ________________________________________________

            # TODO 8: Fill the password with invalid_password.
            ________________________________________________

            # TODO 9: Click the Login button.
            ________________________________________________

            # TODO 10: Locate the flash message with #flash.
            flash_message = ________________________________

            try:
                # TODO 11: Intentionally assert that the message contains
                # expected_success_text. This assertion should fail.
                expect(_______________).to_contain_text(_____________________)

            except AssertionError as error:
                # TODO 12: Capture a full-page failure screenshot.
                page.screenshot(
                    path=____________________,
                    full_page=____,
                )

                # TODO 13: Print the assertion error.
                print("Assertion failed:", __________)

                # Keep this statement so pytest records the failure.
                raise

        finally:
            # TODO 14: Close the browser.
            ________________________________________________