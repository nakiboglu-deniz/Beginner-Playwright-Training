### Exercise 07 — Refactor API Tests with a Base URL

#### 🎯 Goal

Learn how to remove duplicated URLs by defining a shared API base URL and passing it to Playwright's `APIRequestContext`.

The slides recommend placing the base URL in `constants.py`, creating the request context with `base_url=...`, and using relative paths such as `pet`. They also stress that the base URL needs a trailing slash. Exercise 7 then asks learners to run the GET tests and change from the v2 base URL to the v3 base URL to observe API-side differences.

#### 📖 Background

```python
request_context = playwright.request.new_context(
    base_url=BASE_URL,
)
response = request_context.get("pet/findByStatus")
```

Use:

```python
BASE_URL = "https://petstore.swagger.io/v2/"
```

The trailing slash is required so relative paths resolve correctly.

#### 🏗️ Files to work in

| File | What to build |
|---|---|
| `src/config/constants.py` | Define the shared `BASE_URL` constant |
| `src/tests/test_07_get_refactored.py` | Refactor two GET tests to use `base_url` and relative paths |

#### ✅ Tasks

1. Complete `BASE_URL` in `constants.py` with the v2 URL and trailing slash.
2. Import `BASE_URL` into the test script.
3. Create each request context with `base_url=BASE_URL`.
4. Replace full URLs with relative paths.
5. Complete a successful `findByStatus` GET test.
6. Complete a missing-pet GET test.
7. Run both tests with the v2 base URL.
8. Change the constant to the v3 base URL shown in the slides.
9. Run the tests again and record any unexpected API differences.
10. Optionally create an HTML report.

#### 🏃 Run the exercise

```bash
pytest src/tests/test_07_get_refactored.py -v -s   --html=report_ex7.html   --self-contained-html
```

To run all tests with a report:

```bash
pytest --html=report_all.html --self-contained-html
```

#### 💡 Tips

- Keep the trailing slash in `BASE_URL`.
- Relative paths must not start with a slash in this exercise.
- Change the base URL in one place only.
- Unexpected v2 and v3 differences should be reported, not hidden.

#### 📌 Reference

- [Playwright APIRequest new context](https://playwright.dev/python/docs/api/class-apirequest#api-request-new-context)
- [Pet Store v2 documentation](https://petstore.swagger.io/)
- [Pet Store v3 endpoint](https://petstore3.swagger.io/)
