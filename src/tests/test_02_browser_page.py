"""
Exercise 02: Browser & Page Fundementals

See Exercises/Module02_BrowserPageFundementals.md for full instructions.
Run: pytest src/tests/test_02_browser_page.py -v --headed
"""

from playwright.sync_api import expect, sync_playwright


target_url = "https://the-internet.herokuapp.com/add_remove_elements/"
expected_title = "The Internet"
expected_heading = "Add/Remove Elements"


def test_add_and_remove_elements() -> None:
    """Complete the browser, context, page, interaction, and assertion steps."""

    # TODO 1: Start Playwright in synchronous mode and store it as p.
    with __________________________ as p:

        # TODO 2: Launch Chromium in headed mode with slow_mo=1000.
        browser = p.________.launch(
            headless=____,
            slow_mo=____,
        )

        # These variables are initialized so cleanup can be performed safely.
        context = None

        try:
            # TODO 3: Create a new isolated browser context.
            
            # TODO 4: Create a new page inside the context.
            
            # TODO 5: Navigate to TARGET_URL.
            
            # TODO 6: Locate the Add Element button by role and accessible name.
            
            # TODO 7: Assert that the Add Element button is visible.
            expect(__________).to_be_________()

            # TODO 8: Click the Add Element button exactly twice using a loop.
            for _ in range(____):
                add_button.________()

            # TODO 9: Locate every Delete button by role and accessible name.
            delete_buttons = page.____________(
                "button",
                name=________,
            )

            # TODO 10: Count the Delete buttons.
            delete_button_count = delete_buttons._______()
            print("Delete buttons found:", ___________________)

            # TODO 11: Assert that the page title is EXPECTED_TITLE.
            assert page.________() == ______________, (
                f"Expected title {EXPECTED_TITLE!r}, received {page.title()!r}."
            )

            # TODO 12: Assert that the current URL is TARGET_URL.
            assert page.____ == __________, (
                f"Expected URL {TARGET_URL!r}, received {page.url!r}."
            )

            # TODO 13: Assert that the first Delete button is visible.
            expect(delete_buttons._______).to_be_________()

        finally:
            # TODO 14: Close the context if it was successfully created.
            if context is not None:
                context.________()

            # TODO 15: Close the browser.
            browser.________()