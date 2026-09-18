### Exercise 02 — API Assertions & Response Body

#### 🎯 Goal

Learn how to validate a Playwright API response with Python assertions and extract values from a JSON response body.

In this exercise, you will:

- Send a GET request for pets with status `sold`
- Validate the HTTP response status
- Provide a useful assertion error message
- Convert the response body from JSON to Python data
- Verify the response structure
- Verify that every returned pet has status `sold`
- Extract and print all returned pet IDs
- Dispose of the API request context safely

Before writing code, review the Pet Store Swagger documentation:

- Find `GET /pet/findByStatus`
- Execute the endpoint with the parameter `status=sold`
- Inspect the response status code
- Inspect the JSON response body
- Identify the `id` and `status` properties of each pet

#### 📖 Background

##### Python assert statements

A Python `assert` statement verifies that an expression is true.

```python
assert response.status == expected_status
```

Add an error message to make failures easier to understand.

```python
error_message = (
    f"Expected response status: {expected_status}; "
    f"actual response status: {response.status}"
)
assert response.status == expected_status, error_message
```

##### Reading JSON response data

Use `response.json()` to convert JSON into Python lists and dictionaries.

```python
response_body = response.json()
```

The response from `GET /pet/findByStatus` is expected to be a list of pet dictionaries.

```python
first_pet_id = response_body[0]["id"]
```

A nested value can be accessed through multiple dictionary keys.

```python
pet_category = pet["category"]["name"]
```

Only access optional nested values after checking that the keys exist.

##### Testing all returned items

Use `all()` to verify a condition for every item in a list.

```python
assert all(pet.get("status") == "sold" for pet in pets)
```

##### Extracting IDs

Use a list comprehension to collect all pet IDs.

```python
pet_ids = [pet["id"] for pet in pets]
```

The shared Pet Store data can change, so the exercise does not assert a fixed number of returned pets.

#### 🏗️ File to work in

| File | What to build |
|---|---|
| `src/tests/test_02_api_assertions.py` | Complete the GET request, assertions, response processing, and ID extraction |

#### ✅ Task 1 — Prepare headers and parameters

Create:

- An `Accept: application/json` header
- A query parameter requesting pets with status `sold`

#### ✅ Task 2 — Create the API request context

Start synchronous Playwright and create an `APIRequestContext`.

A browser is not required for this API test.

#### ✅ Task 3 — Send the GET request

Call `GET /pet/findByStatus` with the headers and parameters.

#### ✅ Task 4 — Assert the response status

Assert that the response status equals `200`.

Build and use an error message that includes both the expected and actual status.

#### ✅ Task 5 — Read and validate the response body

Convert the response body to Python data and assert that it is a list.

#### ✅ Task 6 — Validate the returned statuses

Assert that every returned item's `status` is `sold`.

The assertion should fail with a clear message if another status appears.

#### ✅ Task 7 — Print all sold-pet IDs

Create a list of all returned IDs and print:

```text
Sold pet IDs: [<id>, <id>, ...]
```

#### ✅ Task 8 — Inspect one returned pet

If at least one pet is returned:

- Print the first pet's ID
- Print its name when available
- Print its category name when the nested category data is available

Do not fail only because the list is empty or optional fields are absent.

#### ✅ Task 9 — Clean up

Dispose of the request context in `finally`.

#### 🏃 Run the exercise

```bash
pytest src/tests/test_02_api_assertions.py -v -s
```

#### 💡 Tips

- `response.status` contains the HTTP status code.
- `response.json()` returns Python data.
- Use `isinstance(response_body, list)` to verify the top-level structure.
- Use `.get()` for optional dictionary values.
- Use `all()` to validate every returned pet.
- Do not assert a fixed pet count in a shared API.
- Dispose of the request context in `finally`.

#### 📌 Reference

- [Playwright API testing](https://playwright.dev/python/docs/api-testing)
- [Playwright APIResponse](https://playwright.dev/python/docs/api/class-apiresponse)
- [Python assert statement](https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement)
- [Pet Store Swagger documentation](https://petstore.swagger.io/)
