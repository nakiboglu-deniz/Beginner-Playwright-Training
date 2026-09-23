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
        "status": 'sold',
    }

    # TODO 2: Create the Accept: application/json header.
    headers = {
        'Accept': "application/json",
    }

    # TODO 3: Start Playwright in synchronous mode.
    with sync_playwright() as playwright:
        request_context = None

        try:
            # TODO 4: Create an APIRequestContext.
            request_context = playwright.request.new_context()

            # TODO 5: Send the GET request.
            response = request_context.get(
                find_by_status_url,
                headers=headers,
                params=parameters,
            )

            # TODO 6: Build an error message containing expected and actual status.
            error_message = (
                f"Expected response status: {expected_status_code}; "
                f"actual response status: {response.status}"
            )

            # TODO 7: Assert that the response status is 200.
            assert response.status == expected_status_code, error_message

            # TODO 8: Convert the response body to Python data.
            response_body = response.json()
            print(response_body)

            # TODO 9: Assert that the response body is a list.
            assert isinstance(response_body, list), (
                f"Expected a list, received {type(response_body).__name__}."
            )

            # TODO 10: Assert that every returned pet has status sold.
            assert all(
                pet["status"] == "sold"
                for pet in response_body
            ), "The response contains a pet whose status is not sold."

            # TODO 11: Create a list containing all returned pet IDs.
            sold_pet_ids = [pet["id"] for pet in response_body]

            # TODO 12: Print the list of sold-pet IDs.
            print("Sold pet IDs:", sold_pet_ids)
            
            # TODO 13: If at least one pet exists, print selected values.
            if not sold_pet_ids:
                first_pet = response_body[0]
                print("First pet ID:", first_pet["id"])
                print("First pet name:", first_pet["name"])

                category = first_pet["category"]
                if isinstance(category, dict):
                    print("First pet category:", category.get("name"))
            
        finally:
            # TODO 14: Dispose of the request context if it was created.
            if request_context is not None:
                request_context.dispose()