### Exercise 03 — Create a Pet with a POST Request

#### 🎯 Goal

Learn how to create a new Pet Store resource with Playwright's `APIRequestContext`, send a JSON request body, read the created pet's ID, and retrieve the pet with a follow-up GET request.

In this exercise, you will:

- Explore `POST /pet` in Swagger
- Build a Python dictionary representing a pet
- Create JSON request headers
- Send a POST request
- Validate the response status and content type
- Read the created pet's ID from the JSON response
- Retrieve the created pet with `GET /pet/{petId}`
- Compare selected response values
- Investigate what happens when the POST body is empty
- Dispose of the request context safely

Before writing code:

- Open the Pet Store Swagger documentation
- Find `POST /pet`
- Review the request body model
- Submit a sample pet manually
- Inspect the response status, headers, and JSON body
- Find `GET /pet/{petId}` for retrieving the created pet

#### 📖 Background

##### POST requests

POST requests create new resources on a server.

The endpoint used in this exercise is:

```text
POST /pet
```

##### JSON request bodies

Create the request body as a Python dictionary. Playwright converts the dictionary into JSON when it is passed through `data=`.

```python
body = {
    "id": pet_id,
    "category": {
        "id": 1010,
        "name": "purring_pets",
    },
    "name": "my_pet",
    "photoUrls": ["string"],
    "tags": [
        {
            "id": 1010,
            "name": "purring",
        }
    ],
    "status": "available",
}
```

##### Request headers

The `Content-Type` header describes the request-body format. The `Accept` header describes the desired response format.

```python
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
}
```

##### Sending the POST request

```python
response = request_context.post(
    pet_url,
    headers=headers,
    data=body,
)
```

##### Reading the created pet

The successful response contains the created pet data in JSON format.

```python
created_pet = response.json()
created_pet_id = created_pet["id"]
```

Store the returned ID and use it in a GET request.

```python
get_response = request_context.get(
    f"{pet_url}/{created_pet_id}",
    headers={"Accept": "application/json"},
)
```

##### Shared API data

The Pet Store is a shared public environment. Use a generated ID to reduce collisions with other learners. The starter script provides a helper value based on the current time.

#### 🏗️ File to work in

| File | What to build |
|---|---|
| `src/tests/test_03_api_post_request.py` | Complete pet creation, response validation, GET verification, and empty-body exploration |

#### ✅ Task 1 — Build the request body

Complete the pet dictionary using the provided generated ID.

Include:

- `id`
- `category`
- `name`
- `photoUrls`
- `tags`
- `status`

#### ✅ Task 2 — Create the headers

Add both:

- `Content-Type: application/json`
- `Accept: application/json`

#### ✅ Task 3 — Create the API request context

Start synchronous Playwright and create an `APIRequestContext`.

#### ✅ Task 4 — Send the POST request

Send the pet dictionary to `POST /pet` through the `data=` argument.

#### ✅ Task 5 — Validate the POST response

Implement these essential checks:

- The response status is `200`
- The response `content-type` contains `application/json`
- The returned body is a dictionary

#### ✅ Task 6 — Store the created pet ID

Read the JSON response, extract its `id`, and store it in `created_pet_id`.

Print:

```text
Created pet ID: <id>
```

#### ✅ Task 7 — Retrieve the created pet

Construct the GET URL using `created_pet_id`, send the request, and assert that the GET response status is `200`.

#### ✅ Task 8 — Compare the returned data

Read the GET response body and verify:

- Its ID equals `created_pet_id`
- Its name equals the submitted name
- Its status equals the submitted status

#### ✅ Task 9 — Explore an empty POST body

Send a second POST request to the same endpoint using an empty dictionary.

Print:

- The returned status code
- The returned content type
- The response body as text

This step is observational. Do not assert a specific response because the shared API implementation may behave differently from the documented expectation.

#### ✅ Task 10 — Clean up

Dispose of the request context in `finally`.

#### 🏃 Run the exercise

```bash
pytest src/tests/test_03_api_post_request.py -v --headed
```

#### 💡 Tips

- Pass a Python dictionary through `data=`.
- Use both `Content-Type` and `Accept` headers.
- Header names in `response.headers` are typically lowercase.
- Store the ID returned by the API instead of assuming it matches the submitted value.
- Use the stored ID in the follow-up GET request.
- Treat the empty-body request as an observation, not a fixed assertion.
- Dispose of the request context in `finally`.

#### 📌 Reference

- [Playwright API testing](https://playwright.dev/python/docs/api-testing)
- [Playwright APIRequestContext post](https://playwright.dev/python/docs/api/class-apirequestcontext#api-request-context-post)
- [Playwright APIResponse](https://playwright.dev/python/docs/api/class-apiresponse)
- [Pet Store Swagger documentation](https://petstore.swagger.io/)
