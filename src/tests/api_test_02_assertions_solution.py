"""
Exercise 02: API Assertions & Response Body
See Exercises/Module02_API_Assertions_ResponseBody.md for full instructions.
Run: pytest src/tests/test_02_api_assertions.py -v -s

Complete a GET request and validate:
1. Response status
2. Response-body structure
3. Status of every returned pet
4. Extracted pet IDs
"""

from playwright.sync_api import sync_playwright


find_by_status_url = "https://petstore.swagger.io/v2/pet/findByStatus"
expected_status_code = 200
sold_status = "sold"


def test_sold_pets_assertions_and_response_body() -> None:
    """Complete the assertions and inspect the sold-pets response body."""

    # TODO 1: Create the request parameters for status sold.
    parameters = {
        ________: ________,
    }

    # TODO 2: Create the Accept: application/json header.
    headers = {
        ________: __________________,
    }

    # TODO 3: Start Playwright in synchronous mode.
    with __________________________ as playwright:
        request_context = None

        try:
            # TODO 4: Create an APIRequestContext.
            request_context = ______________________________________

            # TODO 5: Send the GET request.
            response = request_context.____(
                __________________,
                headers=________,
                params=__________,
            )

            # TODO 6: Build an error message containing expected and actual status.
            error_message = (
                f"Expected response status: {____________________}; "
                f"actual response status: {________________}"
            )

            # TODO 7: Assert that the response status is 200.
            assert __________________________________, _____________

            # TODO 8: Convert the response body to Python data.
            response_body = ______________________________

            # TODO 9: Assert that the response body is a list.
            assert isinstance(_____________, ______), (
                f"Expected a list, received {type(response_body).__name__}."
            )

            # TODO 10: Assert that every returned pet has status sold.
            assert all(
                __________________________________________
                for pet in response_body
            ), "The response contains a pet whose status is not sold."

            # TODO 11: Create a list containing all returned pet IDs.
            sold_pet_ids = [________________ for pet in _____________]

            # TODO 12: Print the list of sold-pet IDs.
            print("Sold pet IDs:", ______________)

            # TODO 13: If at least one pet exists, print selected values.
            if ________________________________:
                first_pet = ___________________
                print("First pet ID:", ____________________)
                print("First pet name:", __________________)

                category = ________________________________
                if isinstance(category, dict):
                    print("First pet category:", __________________)

        finally:
            # TODO 14: Dispose of the request context if it was created.
            if request_context is not None:
                ____________________________________________