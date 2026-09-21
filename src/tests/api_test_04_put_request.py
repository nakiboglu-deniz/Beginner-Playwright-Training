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
    headers = {______________: __________________, ________: __________________}

    # TODO 2: Complete the original pet body.
    original_body = {
        "id": __________________,
        "category": {"id": 1010, "name": "purring_pets"},
        "name": __________________,
        "photoUrls": ["string"],
        "tags": [{"id": 1010, "name": "purring"}],
        "status": __________________,
    }

    with __________________________ as playwright:  # TODO 3
        request_context = None
        try:
            # TODO 4: Create a context with the v2 base URL.
            request_context = playwright.request.new_context(
                base_url=____________________________________
            )

            # TODO 5: Create the original pet with POST.
            create_response = ______________________________________
            assert _________________________________________________
            created_pet_id = _______________________________________

            # TODO 6: Build an updated body with the same ID.
            updated_body = {
                **original_body,
                "id": __________________,
                "name": __________________,
                "status": __________________,
            }

            # TODO 7: Update the pet with PUT.
            update_response = ______________________________________
            assert _________________________________________________

            # TODO 8: Read and validate the PUT response body.
            updated_pet = __________________________________________
            assert _________________________________________________
            assert _________________________________________________
            assert _________________________________________________

            # TODO 9: Retrieve the updated pet by ID.
            get_response = _________________________________________
            assert _________________________________________________
            retrieved_pet = ________________________________________

            # TODO 10: Verify the persisted name and status.
            assert _________________________________________________
            assert _________________________________________________

            print("Updated pet:", retrieved_pet)
        finally:
            # TODO 11: Dispose of the request context.
            if request_context is not None:
                ____________________________________________
