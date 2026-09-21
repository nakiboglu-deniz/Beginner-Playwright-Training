### Exercise 05 — Unsuccessful API Requests

#### 🎯 Goal

Learn how to test unsuccessful Pet Store requests by validating status codes, response headers, and raw response bodies.

The slides introduce unsuccessful requests with `GET /pet/{petId}`, a `404` assertion, an assertion error message, and inspection of the `content-type` header and raw body. Exercise 5 also asks learners to test a non-existing pet ID, a non-existing status, and a PUT using a non-existing pet ID.

#### 📖 Background

Not every API response contains JSON. Inspect the content type before deciding whether to call `response.json()`.

```python
content_type = response.headers.get("content-type", "")
raw_body = response.body()
```

Use a clear assertion message:

```python
message = f"Expected 404, received {response.status}"
assert response.status == 404, message
```

#### 🏗️ File to work in

| File | What to build |
|---|---|
| `src/tests/test_05_unsuccessful_requests.py` | Implement three unsuccessful-request scenarios |

#### ✅ Tasks

1. Request a pet ID that should not exist and assert status `404`.
2. Print its content type and raw response body.
3. Query `findByStatus` with a non-existing status and record the actual response.
4. Compare the actual result with the API documentation before choosing an assertion.
5. Send a PUT request containing a non-existing pet ID.
6. Print the expected result from the documentation and the actual result.
7. Do not force an assertion where the shared API behaves differently from its documentation.
8. Dispose of the request context safely.

#### 🏃 Run the exercise

```bash
pytest src/tests/test_05_unsuccessful_requests.py -v -s
```

#### 💡 Tips

- Use a very large generated ID to reduce the chance of finding an existing pet.
- `response.body()` returns bytes.
- Use `response.text()` when you want printable text.
- Record observed API behaviour honestly instead of changing expected values without investigation.

#### 📌 Reference

- [Playwright APIResponse](https://playwright.dev/python/docs/api/class-apiresponse)
- [Pet Store Swagger documentation](https://petstore.swagger.io/)
