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
    with sync_playwright() as p:

        # TODO 2: Launch Chromium in headed mode with slow_mo=1000.
        browser = p.chromium.launch(
            headless=False,
            slow_mo=2000,
        )

        # These variables are initialized so cleanup can be performed safely.
        context = None

        try:
            # TODO 3: Create a new isolated browser context.
            context = browser.new_context()
            
            # TODO 4: Create a new page inside the context.
            page = context.new_page()
            
            # TODO 5: Navigate to TARGET_URL.
            page.goto(target_url)
            
            # TODO 6: Locate the Add Element button by role and accessible name.
            add_button = page.get_by_role('button',name="Add Element")
            
            # TODO 7: Assert that the Add Element button is visible.
            expect(add_button).to_be_visible()

            # TODO 8: Click the Add Element button exactly twice using a loop.
            for i in range(2):
                add_button.click()

            # TODO 9: Locate every Delete button by role and accessible name.
            delete_buttons = page.get_by_role(
                "button",
                name="Delete",
            )

            # TODO 10: Count the Delete buttons.
            delete_button_count = delete_buttons.count()
            print("Delete buttons found:", delete_button_count)

            # TODO 11: Assert that the page title is EXPECTED_TITLE.
            assert page.title() == expected_title, (
                f"Expected title {EXPECTED_TITLE!r}, received {page.title()!r}."
            )

            # TODO 12: Assert that the current URL is TARGET_URL.
            assert page.url == target_url, (
                f"Expected URL {TARGET_URL!r}, received {page.url!r}."
            )

            # TODO 13: Assert that the first Delete button is visible.
            expect(delete_buttons.first).to_be_visible()

        finally:
            # TODO 14: Close the context if it was successfully created.
            if context is not None:
                context.close()

            # TODO 15: Close the browser.
            browser.close()