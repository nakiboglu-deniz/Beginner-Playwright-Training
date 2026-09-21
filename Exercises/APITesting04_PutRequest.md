### Exercise 04 — Update a Pet with a PUT Request

#### 🎯 Goal

Learn how to update an existing Pet Store resource with `PUT /pet` and verify the updated data with a GET request.

In this exercise, you will:

- Compare the POST and PUT request bodies
- Create a pet that can be updated safely
- Change selected pet information
- Send a PUT request with a JSON body
- Validate the returned updated pet
- Retrieve the pet by ID
- Confirm that the update was persisted
- Dispose of the API request context safely

#### 📖 Background

A POST request creates a new resource, while a PUT request replaces or updates a resource using the complete representation supplied in the request body. The slide deck uses the same `/pet` path for both methods, but calls `post()` for creation and `put()` for the update.

```python
response = request_context.put(
    "pet",
    headers=headers,
    data=updated_body,
)
```

The PUT body includes the ID of the pet to update. The response contains the updated pet data.

#### 🏗️ File to work in

| File | What to build |
|---|---|
| `src/tests/test_04_api_put_request.py` | Create a pet, update it with PUT, and verify it with GET |

#### ✅ Tasks

1. Create JSON request headers.
2. Create a new pet with POST and store the returned ID.
3. Copy or rebuild the original body for the PUT request.
4. Keep the same pet ID but change its name and status.
5. Send `PUT /pet` using `data=updated_body`.
6. Assert that the PUT response returns status `200`.
7. Verify the returned ID, name, and status.
8. Retrieve the same pet with `GET /pet/{petId}`.
9. Verify that the retrieved data contains the updated values.
10. Dispose of the request context in `finally`.

#### 🏃 Run the exercise

```bash
pytest src/tests/test_04_api_put_request.py -v -s
```

#### 💡 Tips

- The PUT body must contain the ID of the pet being updated.
- Use a generated ID to reduce conflicts in the shared Pet Store environment.
- Pass Python dictionaries through `data=`.
- Verify the update with a separate GET request.

#### 📌 Reference

- [Playwright API testing](https://playwright.dev/python/docs/api-testing)
- [Pet Store Swagger documentation](https://petstore.swagger.io/)
