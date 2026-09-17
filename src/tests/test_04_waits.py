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
    with __________________________ as p:

        # TODO 2: Launch Chromium in headed mode.
        browser = __________________________________________

        try:
            # TODO 3: Create a new page.
            page = __________________________

            # TODO 4: Navigate to target_url.
            ________________________________________________

            # TODO 5: Wait until the page DOM is ready.
            ________________________________________________

            # TODO 6: Locate the Start button by ARIA role and name.
            start_button = _________________________________

            # TODO 7: Wait until the Start button is visible.
            ________________________________________________

            # TODO 8: Click the Start button.
            ________________________________________________

            # TODO 9: Locate the loading indicator using #loading.
            loading_indicator = ____________________________

            # TODO 10: Locate the final message using #finish h4.
            message = ______________________________________

            # TODO 11: Wait until the loading indicator is hidden.
            ________________________________________________

            # TODO 12: Wait until the final message is visible.
            ________________________________________________

            # TODO 13: Assert that the message has the expected text.
            expect(________).to_have_text(________________)

            # TODO 14: Retrieve the final message text.
            final_message = ________________________________

            # TODO 15: Print: Final message: Hello World!
            print("Final message:", ________________________)

        finally:
            # TODO 16: Close the browser.
            ________________________________________________