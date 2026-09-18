"""
Exercise 01: Pet Store API GET Request
See Exercises/Module01_API_GET_Request.md for full instructions.
Run: pytest src/tests/api_test_01_get_request.py -v --headed

Complete two GET requests using Playwright APIRequestContext:
1. Retrieve pets with status sold
2. Retrieve pet ID 1 and determine whether it is sold
"""

from playwright.sync_api import sync_playwright


find_by_status_url = "https://petstore.swagger.io/v2/pet/findByStatus"
pet_by_id_base_url = "https://petstore.swagger.io/v2/pet/"
pet_id = 1
sold_status = "sold"
expected_success_status = 200


def test_find_sold_pets_and_check_pet_one() -> None:
    """Complete the GET requests and process their JSON responses."""

    # TODO 1: Create query parameters for pets with status sold.
    parameters = {
        ________: ________,
    }

    # TODO 2: Create a header that accepts application/json.
    headers = {
        ________: __________________,
    }

    # TODO 3: Start Playwright in synchronous mode.
    with __________________________ as playwright:
        request_context = None

        try:
            # TODO 4: Create an APIRequestContext.
            request_context = ______________________________________

            # TODO 5: Send the GET request with headers and parameters.
            sold_response = request_context.____(
                __________________,
                headers=________,
                params=__________,
            )

            # TODO 6: Print the sold-pets response status.
            print("Sold-pets response status:", __________________)

            # TODO 7: Assert that the response status is 200.
            assert ________________ == ______________________, (
                f"Expected status {expected_success_status}, "
                f"received {sold_response.status}."
            )

            # TODO 8: Read the response body as JSON.
            sold_pets = ______________________________

            # TODO 9: Assert that sold_pets is a list.
            assert isinstance(_________, ______), (
                f"Expected a list, received {type(sold_pets).__name__}."
            )

            # TODO 10: Count the returned pets.
            sold_pet_count = __________________________
            print("Number of sold pets:", ________________)

            # TODO 11: Create a list containing every returned pet ID.
            sold_pet_ids = [________________ for pet in __________]
            print("Sold pet IDs:", ______________)

            # TODO 12: Assert that every returned pet has status sold.
            assert all(
                __________________________________________
                for pet in sold_pets
            ), "The response contains a pet whose status is not sold."

            # TODO 13: Construct the URL for pet ID 1.
            pet_by_id_url = ______________________________________

            # TODO 14: Send a GET request for pet ID 1.
            pet_response = ______________________________________

            print("Pet ID 1 response status:", pet_response.status)

            # TODO 15: If the request succeeds, read the pet and determine
            # whether its status equals sold_status. Otherwise, print the
            # unsuccessful response status. Complete the full conditional.
            if __________________________________________:
                pet = ____________________________________
                is_pet_sold = ____________________________
                print(f"Is pet ID {pet_id} sold?", ____________)
            else:
                print(
                    f"Pet ID {pet_id} could not be retrieved. "
                    f"Response status: {__________________}"
                )

        finally:
            # TODO 16: Dispose of the request context if it was created.
            if request_context is not None:
                ____________________________________________