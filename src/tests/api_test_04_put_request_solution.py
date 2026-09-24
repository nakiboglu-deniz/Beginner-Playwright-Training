"""
Exercise 04: Update a Pet with a PUT Request
See Exercises/Module04_API_PUT_Request.md for full instructions.
Run: pytest src/tests/test_04_api_put_request.py -v -s
"""

import time
from playwright.sync_api import sync_playwright

pet_path = "pet"
expected_success_status = 200
generated_pet_id = int(time.time() * 1000)


def test_create_update_and_get_pet() -> None:
    # TODO 1: Complete the JSON headers.
    headers = {"Content-type": "application/json", "Accept": "application/json"}

    # TODO 2: Complete the original pet body.
    original_body = {
        "id": 1010,
        "category": {"id": 1010, "name": "purring_pets"},
        "name": "my_pet",
        "photoUrls": ["string"],
        "tags": [{"id": 1010, "name": "purring"}],
        "status": "sold",
    }

    with sync_playwright() as playwright:  # TODO 3
        request_context = None
        try:
            # TODO 4: Create a context with the v2 base URL.
            request_context = playwright.request.new_context(
                base_url= 'https://petstore.swagger.io/v2/'
            )

            # TODO 5: Create the original pet with POST.
            create_response = request_context.post(pet_path, data=original_body)
            assert create_response.status == expected_success_status
            created_pet_id = create_response.json()["id"]
            

            # TODO 6: Build an updated body with the same ID.
            updated_body = {
                **original_body,
                "id": created_pet_id,
                "name": "my new cat",
                "status": "vaccinated",
            }

            # TODO 7: Update the pet with PUT.
            update_response = request_context.put(pet_path,data=updated_body)
            assert update_response.status == expected_success_status

            # TODO 8: Read and validate the PUT response body.
            updated_pet = update_response.json()
            assert updated_pet["id"] == created_pet_id
            assert updated_pet["name"] == updated_body["name"]
            assert updated_pet["status"] == updated_body["status"]

            # TODO 9: Retrieve the updated pet by ID.
            get_response = request_context.get(f"{pet_path}/{created_pet_id}")
            assert get_response.status == expected_success_status
            retrieved_pet = get_response.json()

            # TODO 10: Verify the persisted name and status.
            assert retrieved_pet["name"] == updated_pet["name"]
            assert retrieved_pet["status"] == updated_pet["status"]

            print("Updated pet:", retrieved_pet)
        finally:
            # TODO 11: Dispose of the request context.
            if request_context is not None:
                request_context.dispose()
