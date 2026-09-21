"""
Exercise 01: Open Website

See Exercises/Module01_OpenWebsite.md for full instructions.
Run: pytest src/tests/test_01_openwebiste.py -v --headed
"""

from playwright.sync_api import sync_playwright


target_url = "https://the-internet.herokuapp.com"
expected_title = "The Internet"
expected_header = "Welcome to the-internet"
expected_viewport = {"width": 1920, "height": 1080}


def test_open_website() -> None:
    """Complete the Playwright test by replacing each TODO placeholder."""

    # TODO 1: Start Playwright in synchronous mode and store it as p.
    with sync_playwright() as p:

        # TODO 2: Launch Chromium.
        # Requirements:
        # - Run in headed mode
        # - Start the browser maximized
        # - Use a slow_mo delay of 1000 milliseconds
        browser = p.chromium.launch(
            headless=False,
            args=["--start-maximized"],
            slow_mo=1000,
        )

        try:
            # TODO 3: Create a new page with a 1920 x 1080 viewport.
            page = browser.new_page(
                viewport={
                    "width": expected_viewport["width"],
                    "height": expected_viewport["height"],
                }
            )

            # TODO 4: Navigate to TARGET_URL.
            page.goto(target_url)

            # TODO 5: Retrieve the page title.
            page_title = page.title()


            # TODO 6: Retrieve the text content of the first h1 element.
            main_header = page.text_content("h1")

            # TODO 7: Print the extracted title and header.
            print("Title:", page_title)
            print("Header:", main_header)

            # TODO 8: Assert that the page title equals EXPECTED_TITLE.
            assert page_title == expected_title, (
                f"Expected title {EXPECTED_TITLE!r}, received {page_title!r}."
            )

            # TODO 9: Assert that the main header equals EXPECTED_HEADER.
            assert main_header == expected_header, (
                f"Expected header {EXPECTED_HEADER!r}, received {main_header!r}."
            )

            # TODO 10: Add one additional assertion of your own.
            # Examples: verify that the title is not empty, that the header is
            # a string, or that the URL uses HTTPS.
            # assert ______________________________________

        finally:
            # TODO 11: Close the browser even when an assertion fails.
            browser.close()
