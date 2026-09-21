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
    create_headers = {______________: __________________, ________: __________________}

    # TODO 2: Complete the DELETE headers, including api_key=special-key.
    delete_headers = {
        ________: __________________,
        ________: __________________,
    }

    body = {
        "id": pet_id,
        "name": "pet_for_deletion",
        "photoUrls": ["string"],
        "status": "available",
    }

    with __________________________ as playwright:  # TODO 3
        request_context = None
        try:
            # TODO 4: Create the request context with base_url.
            request_context = ______________________________________

            # TODO 5: Create the pet and assert success.
            create_response = ______________________________________
            assert _________________________________________________
            created_pet_id = _______________________________________

            # TODO 6: Delete the created pet.
            delete_response = ______________________________________
            print("DELETE status:", ________________________________)

            # TODO 7: Assert that DELETE succeeded.
            assert _________________________________________________

            # TODO 8: Request the deleted pet with GET.
            get_response = _________________________________________
            print("GET after DELETE status:", ______________________)

            # TODO 9: Assert that the pet is not found anymore.
            assert _________________________________________________
        finally:
            # TODO 10: Dispose of the request context.
            if request_context is not None:
                ____________________________________________
