"""
Exercise 04: Waits & Synchronization
See Exercises/Module04_Waits.md for full instructions.
Run: pytest src/tests/test_04_waits.py -v --headed

Complete a dynamic loading workflow using:
1. A page load wait
2. A visibility wait
3. A hidden-state wait
4. A retrying text assertion
"""

from playwright.sync_api import expect, sync_playwright


target_url = "https://the-internet.herokuapp.com/dynamic_loading/1"
expected_message = "Hello World!"


def test_dynamic_loading_with_waits() -> None:
    """Complete the dynamic loading flow and required synchronization."""

    # TODO 1: Start Playwright in synchronous mode.
    with sync_playwright() as p:

        # TODO 2: Launch Chromium in headed mode.
        browser = p.chromium.launch(headless=False, slow_mo=2000)

        try:
            # TODO 3: Create a new page.
            page = browser.new_page()

            # TODO 4: Navigate to target_url.
            page.goto(target_url)

            # TODO 5: Wait until the page DOM is ready.
            page.wait_for_load_state("domcontentloaded")

            # TODO 6: Locate the Start button by ARIA role and name.
            start_button = page.get_by_role("button", name="Start")

            # TODO 7: Wait until the Start button is visible.
            start_button.wait_for(state="visible")

            # TODO 8: Click the Start button.
            start_button.click()

            # TODO 9: Locate the loading indicator using #loading.
            loading_indicator = page.locator("#loading")

            # TODO 10: Locate the final message using #finish h4.
            message = page.locator("#finish h4")

            # TODO 11: Wait until the loading indicator is hidden.
            loading_indicator.wait_for(state="hidden")

            # TODO 12: Wait until the final message is visible.
            message.wait_for(state= "visible")

            # TODO 13: Assert that the message has the expected text.
            expect(message).to_have_text(expected_message)

            # TODO 14: Retrieve the final message text.
            final_message = message.inner_text()

            # TODO 15: Print: Final message: Hello World!
            print("Final message:", final_message)

        finally:
            # TODO 16: Close the browser.
            browser.close()