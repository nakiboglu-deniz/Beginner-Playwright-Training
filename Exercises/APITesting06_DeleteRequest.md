### Exercise 06 — Delete a Pet

#### 🎯 Goal

Learn how to delete a Pet Store resource with `DELETE /pet/{petId}` and prove with a GET request that the pet can no longer be found.

The slides specify that the pet ID belongs in the URL path, the request contains an `api_key` header, and `special-key` can be used as its value. Exercise 6 asks learners to delete a previously created pet and assert that a subsequent GET cannot find it.

#### 📖 Background

```python
headers = {
    "Accept": "application/json",
    "api_key": "special-key",
}
response = request_context.delete(f"pet/{pet_id}", headers=headers)
```

A robust exercise creates its own pet before deleting it, so the test does not depend on data from another test run.

#### 🏗️ File to work in

| File | What to build |
|---|---|
| `src/tests/test_06_api_delete_request.py` | Create, delete, and verify removal of a pet |

#### ✅ Tasks

1. Build the creation and deletion headers.
2. Create a unique pet with POST.
3. Store the created pet ID.
4. Delete it with `DELETE /pet/{petId}`.
5. Assert that the DELETE request succeeds.
6. Request the same ID with GET.
7. Assert that the pet is no longer found.
8. Print the DELETE and verification status codes.
9. Dispose of the request context.

#### 🏃 Run the exercise

```bash
pytest src/tests/test_06_api_delete_request.py -v -s
```

#### 💡 Tips

- Use `api_key: special-key` for DELETE.
- Create the pet inside the same test before deleting it.
- Build relative paths when the request context uses `base_url`.
- Verify deletion with a separate GET request.

#### 📌 Reference

- [Playwright APIRequestContext delete](https://playwright.dev/python/docs/api/class-apirequestcontext#api-request-context-delete)
- [Pet Store Swagger documentation](https://petstore.swagger.io/)
