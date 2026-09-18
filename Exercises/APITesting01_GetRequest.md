### Exercise 01 — Pet Store API GET Request

#### 🎯 Goal

Learn how to use Playwright's `APIRequestContext` to send GET requests to the Pet Store REST API, provide request headers and query parameters, read JSON response data, and answer questions about pets stored by status.

In this exercise, you will:

- Explore the Pet Store API documentation
- Identify an API method, path, parameters, headers, and response
- Start Playwright without launching a browser
- Create an `APIRequestContext`
- Send a GET request with headers and query parameters
- Convert the response body to Python data
- Determine how many pets have the status `sold`
- Print the IDs of sold pets
- Request the pet whose ID is `1`
- Determine whether pet `1` is sold
- Dispose of the request context safely

Before writing code, explore the API manually:

- Open the Pet Store Swagger documentation
- Find `GET /pet/findByStatus`
- Review its request parameter
- Execute it with the status `sold`
- Find the endpoint that retrieves one pet by ID
- Review the possible successful and unsuccessful responses

#### 📖 Background

##### REST API requests

A REST API allows a client to access and manipulate data through HTTP requests. A request includes:

- An HTTP method, such as GET
- A URL containing the request path
- Optional query parameters
- Optional request headers

The API returns a response containing:

- A status code
- Response headers
- A response body

##### GET requests

GET requests retrieve data from the server without creating or updating a resource.

The endpoint introduced in this module is:

```text
GET /pet/findByStatus
```

It accepts a `status` query parameter. The exercise uses the status `sold` to retrieve pets that have already been sold.

##### Playwright APIRequestContext

Playwright provides `APIRequestContext` for making HTTP requests without opening a browser.

```python
with sync_playwright() as playwright:
    request_context = playwright.request.new_context()
```

The request context provides methods such as `get()`, `post()`, `put()`, and `delete()`.

##### Headers and query parameters

Headers describe the expected request or response format. Query parameters filter or modify the request.

```python
headers = {
    "Accept": "application/json",
}

parameters = {
    "status": "sold",
}
```

Pass them to the GET request with `headers=` and `params=`.

```python
response = request_context.get(
    find_by_status_url,
    headers=headers,
    params=parameters,
)
```

##### Reading the response

The response status is available through `response.status`.

```python
print(response.status)
```

Use `response.json()` to convert a JSON response body into Python data.

```python
response_body = response.json()
```

For `GET /pet/findByStatus`, the successful response body is a list of pet objects. Each item can contain values such as `id`, `name`, and `status`.

##### Retrieving one pet by ID

Use the pet ID as part of the URL path when requesting one specific pet.

```text
GET /pet/{petId}
```

For pet `1`, construct the URL from the provided base path and ID instead of hardcoding the complete URL in multiple places.

##### Cleaning up

Dispose of the request context after the test completes.

```python
request_context.dispose()
```

Use `finally` so cleanup also occurs when a request or assertion fails.

#### 🏗️ File to work in

| File | What to build |
|---|---|
| `src/tests/test_01_api_get_request.py` | Complete the GET requests, response processing, and required checks |

#### ✅ Task 1 — Prepare the request data

Use the constants provided in the starter script and create:

- A parameter dictionary containing `status: sold`
- A header dictionary accepting JSON responses

The dictionary names and values are intentionally incomplete.

#### ✅ Task 2 — Start Playwright

Start Playwright in synchronous mode and create an `APIRequestContext`.

Do not launch Chromium. API testing uses the request context directly.

#### ✅ Task 3 — Request sold pets

Send a GET request to `find_by_status_url` using:

- The JSON request headers
- The `sold` query parameter

Print the returned status code.

#### ✅ Task 4 — Read the JSON response

Convert the response body to Python data with `response.json()`.

Confirm that you understand whether the returned top-level structure is a list or a dictionary.

#### ✅ Task 5 — Determine how many pets are sold

Calculate the number of pets returned by the sold-status request and print:

```text
Number of sold pets: <count>
```

Do not enter a fixed expected count. The Pet Store is a shared API and its data can change.

#### ✅ Task 6 — Print all sold-pet IDs

Create a list containing the `id` value of every returned pet and print:

```text
Sold pet IDs: [<id>, <id>, ...]
```

Use a loop or list comprehension.

#### ✅ Task 7 — Request pet ID 1

Construct the pet-by-ID URL using `pet_by_id_base_url` and `pet_id`.

Send a second GET request using the same JSON header.

#### ✅ Task 8 — Determine whether pet ID 1 is sold

The Pet Store is a shared environment, so the request may return a pet or an unsuccessful response.

Implement this logic:

- If the status code is `200`, read the JSON body and compare its `status` value with `sold`
- Print whether pet ID `1` is sold
- Otherwise, print that the pet could not be retrieved together with the returned status code

#### ✅ Task 9 — Add essential checks

Implement only these checks:

- The sold-pets request returns status code `200`
- The sold-pets response body is a list
- Every item returned by the sold-status query has status `sold`

Leave the checks incomplete in the Python exercise and implement them yourself.

Do not assert that pet ID `1` exists, because the data in this public shared API may change.

#### ✅ Task 10 — Clean up

Dispose of the `APIRequestContext` in `finally`.

#### 🏃 Run the exercise

```bash
pytest src/tests/test_01_api_get_request.py -v -s
```

The `-s` option displays the status codes, sold-pet count, ID list, and pet ID `1` result.

#### 💡 Tips

- Use `playwright.request.new_context()` instead of opening a browser.
- Pass query parameters through `params=`.
- Pass the Accept header through `headers=`.
- `response.status` is a property, not a function.
- `response.json()` converts JSON into Python lists and dictionaries.
- Use `len()` to count the returned pets.
- Avoid hardcoding a sold-pet count because shared API data can change.
- Dispose of the request context in `finally`.

#### 📌 Reference

- [Playwright API testing](https://playwright.dev/python/docs/api-testing)
- [Playwright APIRequestContext](https://playwright.dev/python/docs/api/class-apirequestcontext)
- [Pet Store Swagger documentation](https://petstore.swagger.io/)