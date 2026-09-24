"""
Exercise 07: Refactor API Tests with a Base URL
See Exercises/Module07_API_Refactoring.md for full instructions.
Run: pytest src/tests/test_07_get_refactored.py -v -s     --html=report_ex7.html --self-contained-html
"""

from playwright.sync_api import sync_playwright
from pages.constants import BASE_URL


def test_find_sold_pets_with_base_url() -> None:
    headers = {"Accept": "application/json"}
    parameters = {"status": "sold"}

    with __________________________ as playwright:  # TODO 1
        request_context = None
        try:
            # TODO 2: Create the context with BASE_URL.
            request_context = ______________________________________

            # TODO 3: Use the relative findByStatus path.
            response = request_context.____(
                ______________________,
                headers=________,
                params=__________,
            )

            # TODO 4: Assert success and validate the response list.
            assert _________________________________________________
            pets = _________________________________________________
            assert isinstance(____, ______)
            assert all(________________________________ for pet in pets)
        finally:
            # TODO 5: Dispose of the request context.
            if request_context is not None:
                ____________________________________________


def test_missing_pet_with_base_url() -> None:
    missing_pet_id = 999999999999999999

    with __________________________ as playwright:  # TODO 6
        request_context = None
        try:
            # TODO 7: Create the context with BASE_URL.
            request_context = ______________________________________

            # TODO 8: Use a relative path containing missing_pet_id.
            response = _____________________________________________

            # TODO 9: Print and assert the expected missing-pet status.
            print("Missing-pet status:", ___________________________)
            assert _________________________________________________
        finally:
            # TODO 10: Dispose of the request context.
            if request_context is not None:
                ____________________________________________
