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

    with sync_playwright() as playwright:  # TODO 1
        request_context = None
        try:
            # TODO 2: Create the context with BASE_URL.
            request_context = playwright.request.new_context(base_url=BASE_URL)

            # TODO 3: Use the relative findByStatus path.
            response = request_context.get(
                "pet/findByStatus",
                headers=headers,
                params=parameters,
            )

            # TODO 4: Assert success and validate the response list.
            assert response.status == 200
            pets = response.json()
            assert isinstance(pets, list)
            assert all(pet["status"]== "sold" for pet in pets)
        finally:
            # TODO 5: Dispose of the request context.
            if request_context is not None:
                request_context.dispose()


def test_missing_pet_with_base_url() -> None:
    missing_pet_id = 999999999999999999
    headers = {"Accept": "application/json"}

    with sync_playwright() as playwright:  # TODO 6
        request_context = None
        try:
            # TODO 7: Create the context with BASE_URL.
            request_context = playwright.request.new_context(base_url=BASE_URL)

            # TODO 8: Use a relative path containing missing_pet_id.
            response = request_context.get(f"pet/{missing_pet_id}", headers=headers)

            # TODO 9: Print and assert the expected missing-pet status.
            print("Missing-pet status:", response.status)
            assert response.status == 404
        finally:
            # TODO 10: Dispose of the request context.
            if request_context is not None:
                request_context.dispose()
