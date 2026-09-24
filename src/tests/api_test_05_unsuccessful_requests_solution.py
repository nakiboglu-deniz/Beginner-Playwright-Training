"""
Exercise 05: Unsuccessful API Requests
See Exercises/Module05_API_Unsuccessful_Requests.md for full instructions.
Run: pytest src/tests/test_05_unsuccessful_requests.py -v -s
"""

import time
from playwright.sync_api import sync_playwright

base_url = "https://petstore.swagger.io/v2/"
expected_not_found = 404
non_existing_pet_id = int(time.time() * 1000) + 999999999
non_existing_status = "not-a-real-status"


def test_unsuccessful_requests() -> None:
    headers = {"Accept": "application/json","api_key": "special-key"}

    with sync_playwright() as playwright:  # TODO 1
        request_context = None
        try:
            # TODO 2: Create the API request context with base_url.
            request_context = playwright.request.new_context(base_url=base_url)

            # Scenario A: non-existing pet ID
            # TODO 3: Send GET /pet/{non_existing_pet_id}.
            missing_pet_response = request_context.get("/pet/{non_existing_pet_id}")

            # TODO 4: Build and use an assertion error message.
            error_message = f"Expected {expected_not_found}, received {missing_pet_response.status}"
            assert missing_pet_response.status == expected_not_found, error_message

            # TODO 5: Print content type and raw/text body.
            print("Missing-pet content type:", missing_pet_response.headers.get("content-type"))
            print("Missing-pet response body:", missing_pet_response.body())

            # Scenario B: non-existing status
            # TODO 6: Send GET pet/findByStatus with the invalid status.
            invalid_status_response = request_context.get("/pet/{findByStatus}")
            print("Invalid-status response:", invalid_status_response.status)
            print("Invalid-status body:", invalid_status_response.body)

            # TODO 7: Add the assertion supported by the documented
            # expectation after comparing it with the observed response.
            # assert _______________________________________________in__

            # Scenario C: PUT with a non-existing pet ID
            body = {
                "id": non_existing_pet_id,
                "name": "unknown_pet",
                "photoUrls": ["string"],
                "status": "available",
            }
            put_headers = {
                "Content-Type": "application/json",
                "Accept": "application/json",
            }

            # TODO 8: Send the PUT request.
            put_response = request_context.put("/pet",headers=put_headers,data=body)
            print("PUT non-existing ID status:", put_response.status)
            print("PUT non-existing ID body:", put_response.body())

            # TODO 9: Document the expected status from Swagger and compare
            # it with the actual response without hiding a discrepancy.
            documented_expected_status = put_response.status
            print("Documented expected status:", non_existing_status)
            print("Actual status:", documented_expected_status)
        finally:
            # TODO 10: Dispose of the request context.
            if request_context is not None:
                request_context.dispose()
