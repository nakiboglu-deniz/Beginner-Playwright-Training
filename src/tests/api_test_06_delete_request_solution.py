"""
Exercise 06: Delete a Pet
See Exercises/Module06_API_DELETE_Request.md for full instructions.
Run: pytest src/tests/test_06_api_delete_request.py -v -s
"""

import time
from playwright.sync_api import sync_playwright

base_url = "https://petstore.swagger.io/v2/"
pet_id = int(time.time() * 1000)


def test_create_delete_and_verify_pet() -> None:
    # TODO 1: Complete the JSON headers used to create the pet.
    create_headers = {"Accept": "application/json", "Content-type": "application/json"}

    # TODO 2: Complete the DELETE headers, including api_key=special-key.
    delete_headers = {
        "Accept": "application/json",
        "api_key": "special-key"
    }

    body = {
        "id": pet_id,
        "name": "pet_for_deletion",
        "photoUrls": ["string"],
        "status": "available",
    }

    with sync_playwright() as playwright:  # TODO 3
        request_context = None
        try:
            # TODO 4: Create the request context with base_url.
            request_context = playwright.request.new_context(base_url=base_url)

            # TODO 5: Create the pet and assert success.
            create_response = request_context.post("pet",headers=create_headers,data=body)
            assert create_response.status == 200
            created_pet_id = create_response.json()["id"]

            # TODO 6: Delete the created pet.
            delete_response = request_context.delete(f"pet/{created_pet_id}",headers=delete_headers)
            print("DELETE status:", delete_response.status)

            # TODO 7: Assert that DELETE succeeded.
            assert delete_response.status == 200

            # TODO 8: Request the deleted pet with GET.
            get_response = request_context.get(f"pet/{created_pet_id}")
            print("GET after DELETE status:", get_response.status)

            # TODO 9: Assert that the pet is not found anymore.
            assert get_response.status == 404
        finally:
            # TODO 10: Dispose of the request context.
            if request_context is not None:
                request_context.dispose()
