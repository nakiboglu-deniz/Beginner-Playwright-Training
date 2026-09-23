"""
Exercise 03: Create a Pet with a POST Request
See Exercises/Module03_API_POST_Request.md for full instructions.
Run: pytest src/tests/test_03_api_post_request.py -s --headed

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
        "Content-type": "application/json",
        "Accept": "application/json",
    }

    # TODO 2: Complete the new-pet request body.
    body = {
        "id": 1010,
        "category": {
            "id": 1010,
            "name": "purring_pets",
        },
        "name": "my_pet",
        "photoUrls": ["string"],
        "tags": [
            {
                "id": 1010,
                "name": "string",
            }
        ],
        "status": "available",
    }

    # TODO 3: Start Playwright in synchronous mode.
    with sync_playwright() as playwright:
        request_context = None

        try:
            # TODO 4: Create an APIRequestContext.
            request_context = playwright.request.new_context()

            # TODO 5: Send POST /pet with headers and body.
            post_response = request_context.post(
                pet_url,
                headers=headers,
                data=body,
            )

            print("POST response status:", post_response.status)

            # TODO 6: Assert that the POST status is 200.
            assert post_response.status == expected_success_status

            # TODO 7: Read and validate the content-type header.
            content_type = post_response.headers.get("content-type","")
            assert "application/json" in content_type

            # TODO 8: Read the created pet as JSON.
            created_pet = post_response.json()

            # TODO 9: Assert that created_pet is a dictionary.
            assert isinstance(created_pet, dict)

            # TODO 10: Extract and print the created pet ID.
            created_pet_id = created_pet["id"]
            print("Created pet ID:", created_pet_id)

            # TODO 11: Construct the GET URL for the created pet.
            get_pet_url = f"{pet_url}/{created_pet_id}"

            # TODO 12: Retrieve the created pet.
            get_response = request_context.get(
                get_pet_url,
                headers={"Accept": "application/json"},
            )

            # TODO 13: Assert that the GET request succeeded.
            assert get_response.status == expected_success_status

            # TODO 14: Read the GET response body.
            retrieved_pet = get_response.json()

            # TODO 15: Compare ID, name, and status with submitted data.
            assert retrieved_pet["id"] == created_pet_id
            assert retrieved_pet["name"] == created_pet["name"]
            assert retrieved_pet["status"] == created_pet["status"]
            
            # TODO 16: Send a second POST request with an empty body.
            empty_body_response = request_context.post(
                pet_url,
                headers=headers,
                data=[],
            )

            # TODO 17: Print its status, content type, and response text.
            print("Empty-body status:", empty_body_response.status)
            print("Empty-body content type:", empty_body_response.headers.get("content-type"))
            print("Empty-body response:", empty_body_response.json())
        
        finally:
            # TODO 18: Dispose of the request context if it was created.
            if request_context is not None:
                request_context.dispose()
