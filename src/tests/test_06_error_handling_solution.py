"""
Exercise 06: Error Handling
See Exercises/Module06_ErrorHandling.md for full instructions.
Run: pytest src/tests/test_06_error_handling.py -v --headed -s

Diagnose and correct five common Playwright failures:
1. Timeout caused by an incorrect locator
2. Interaction with content that is not visible yet
3. Action interrupted by navigation
4. Invalid selector
5. Assertion mismatch
"""

from playwright.sync_api import (
    TimeoutError as PlaywrightTimeoutError,
    expect,
    sync_playwright,
)
import re

login_url = "https://the-internet.herokuapp.com/login"
dynamic_loading_url = "https://the-internet.herokuapp.com/dynamic_loading/1"
redirect_url = "https://the-internet.herokuapp.com/redirector"
expected_status_url = "https://the-internet.herokuapp.com/status_codes"
expected_heading = "Login Page"
expected_dynamic_text = "Hello World!"


def test_error_handling_exercises() -> None:
    """Complete each diagnosis and prove the corrected behaviour."""

    # TODO 1: Start Playwright in synchronous mode.
    with sync_playwright() as p:

        # TODO 2: Launch Chromium in headed mode.
        browser = p.chromium.launch(headless=False,slow_mo=2000)

        try:
            # TODO 3: Create a new page.
            page = browser.new_page()

            # ----------------------------------------------------------
            # Exercise A: Timeout caused by an incorrect locator
            # ----------------------------------------------------------
            page.goto(login_url)

            try:
                # This locator is intentionally incorrect.
                page.click("#login", timeout=1000)
            except PlaywrightTimeoutError as error:
                print("Timeout error caught:", type(error).__name__)
                print("Cause: the locator #login does not match the button.")
            
            # TODO 4: Locate the real Login button.
            login_button = page.get_by_role("button",name="Login")

            # TODO 5: Prove that the corrected locator is visible.
            expect(login_button).to_be_visible()
            
            # ----------------------------------------------------------
            # Exercise B: Element is not visible yet
            # ----------------------------------------------------------
            page.goto(dynamic_loading_url)
            hidden_message = page.locator("#finish h4")

            try:
                # The message is hidden before Start is clicked.
                hidden_message.click(timeout=1000)
            except PlaywrightTimeoutError as error:
                print("Visibility-related timeout caught:", type(error).__name__)

            # TODO 6: Click the Start button.
            page.get_by_role("button",name="Start").click()

            # TODO 7: Wait until hidden_message becomes visible.
            hidden_message.wait_for(state="visible",timeout=0)

            # TODO 8: Assert that it has expected_dynamic_text.
            expect(hidden_message).to_have_text(expected_dynamic_text)
            
            # ----------------------------------------------------------
            # Exercise C: Navigation handling
            # ----------------------------------------------------------
            page.goto(redirect_url)
        
            # TODO 9: Wait for navigation while clicking a#redirect.
            with page.expect_navigation(url= re.compile(r".*/status_codes$")):
                page.locator("a#redirect").click()

            # TODO 10: Assert that the destination URL is correct.
            expect(page).to_have_url(re.compile(r".*/status_codes$"))

            # ----------------------------------------------------------
            # Exercise D: Invalid selector
            # ----------------------------------------------------------
            page.goto(login_url)

            try:
                # This selector is intentionally misspelled.
                page.fill("#usernme", "tomsmith", timeout=1000)
            except PlaywrightTimeoutError as error:
                print("Invalid-locator timeout caught:", type(error).__name__)
                print("Cause: #usernme contains a spelling mistake.")

            # TODO 11: Correct the selector and fill the username field.
            page.fill("#username", "tomsmith")

            # TODO 12: Verify that the field contains tomsmith.
            expect(page.locator("#username")).to_have_value("tomsmith")
            
            # ----------------------------------------------------------
            # Exercise E: Assertion mismatch
            # ----------------------------------------------------------
            heading = page.locator("h2")

            try:
                # This expected value is intentionally incorrect.
                expect(heading).to_have_text("Wrong Title", timeout=1000)
            except AssertionError as error:
                print("Assertion error caught:", type(error).__name__)
                print("Cause: the expected heading does not match the page.")

            # TODO 13: Add the corrected heading assertion.
            expect(heading).to_have_text(expected_heading)
            """
            # ----------------------------------------------------------
            # Exercise F: Create your own error and correction
            # ----------------------------------------------------------
            # TODO 14: Add one intentional failure in a try block.
            try:
                ____________________________________________
            except __________________________ as error:
                print("Custom error caught:", type(error).__name__)

            # TODO 15: Add a corrected action or assertion that proves
            # your custom diagnosis.
            ________________________________________________
            """
        finally:
            # TODO 16: Close the browser.
            browser.close()
