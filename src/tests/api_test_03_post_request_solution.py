"""
Exercise 03: Create a Pet with a POST Request
See Exercises/Module03_API_POST_Request.md for full instructions.
Run: pytest src/tests/test_03_api_post_request.py -v --headed

Complete this workflow:
1. Create a pet with POST /pet
2. Store the returned pet ID
3. Retrieve the pet with GET /pet/{petId}
4. Observe the response to an empty POST body
"""

import time

from playwright.sync_api import sync_playwright


pet_url = "https://petstore.swagger.io/v2/pet"
generated_pet_id = int(time.time() * 1000)
expected_success_status = 200


def test_create_and_retrieve_pet() -> None:
    """Complete the POST request and verify the created pet with GET."""

    # TODO 1: Complete the request headers.
    headers = {
        ______________: __________________,
        ________: __________________,
    }

    # TODO 2: Complete the new-pet request body.
    body = {
        "id": __________________,
        "category": {
            "id": ______,
            "name": __________________,
        },
        "name": __________________,
        "photoUrls": [__________________],
        "tags": [
            {
                "id": ______,
                "name": ______________,
            }
        ],
        "status": __________________,
    }

    # TODO 3: Start Playwright in synchronous mode.
    with __________________________ as playwright:
        request_context = None

        try:
            # TODO 4: Create an APIRequestContext.
            request_context = ______________________________________

            # TODO 5: Send POST /pet with headers and body.
            post_response = request_context.____(
                __________,
                headers=________,
                data=____,
            )

            print("POST response status:", post_response.status)

            # TODO 6: Assert that the POST status is 200.
            assert __________________________________________

            # TODO 7: Read and validate the content-type header.
            content_type = _________________________________________
            assert "application/json" in __________________________

            # TODO 8: Read the created pet as JSON.
            created_pet = __________________________________________

            # TODO 9: Assert that created_pet is a dictionary.
            assert isinstance(____________, ______)

            # TODO 10: Extract and print the created pet ID.
            created_pet_id = _______________________________________
            print("Created pet ID:", __________________)

            # TODO 11: Construct the GET URL for the created pet.
            get_pet_url = __________________________________________

            # TODO 12: Retrieve the created pet.
            get_response = request_context.____(
                _____________,
                headers={"Accept": "application/json"},
            )

            # TODO 13: Assert that the GET request succeeded.
            assert _________________________________________________

            # TODO 14: Read the GET response body.
            retrieved_pet = ________________________________________

            # TODO 15: Compare ID, name, and status with submitted data.
            assert _________________________________________________
            assert _________________________________________________
            assert _________________________________________________

            # TODO 16: Send a second POST request with an empty body.
            empty_body_response = request_context.____(
                __________,
                headers=________,
                data=____,
            )

            # TODO 17: Print its status, content type, and response text.
            print("Empty-body status:", ____________________________)
            print("Empty-body content type:", ______________________)
            print("Empty-body response:", __________________________)

        finally:
            # TODO 18: Dispose of the request context if it was created.
            if request_context is not None:
                ____________________________________________
