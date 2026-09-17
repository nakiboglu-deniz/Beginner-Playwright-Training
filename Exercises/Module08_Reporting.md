### Exercise 08 — Test Report & Screenshot

#### 🎯 Goal

Learn how to capture screenshots during a Playwright test and generate a self-contained HTML report with pytest.

In this exercise, you will:

- Create a folder for screenshots
- Open the login page
- Capture the initial page state
- Submit intentionally invalid credentials
- Add an assertion that is expected to fail
- Catch the assertion failure
- Capture the failure state
- Print the error to the console
- Close the browser in a `finally` block
- Generate an HTML test report

Before writing code, explore the page manually:

- Open [The Internet login page](https://the-internet.herokuapp.com/login)
- Enter an invalid username or password
- Submit the form
- Observe the failed-login message
- Consider which screenshots would be useful when investigating the failure

#### 📖 Background

##### Why screenshots are useful

Screenshots preserve the visible state of the application at a particular point in the test. They can help show:

- What the page looked like before an action
- Which values or messages were visible after an action
- The UI state when an assertion failed

This exercise captures both an initial screenshot and a failure screenshot.

##### Creating the screenshot folder

The destination folder must exist before a screenshot is saved.

```python
os.makedirs("screenshots", exist_ok=True)
```

Using `exist_ok=True` prevents an error when the folder already exists.

##### Capturing screenshots

Use `page.screenshot()` and provide a destination path.

```python
page.screenshot(path="screenshots/before_login.png")
```

A full-page screenshot includes content outside the current viewport.

```python
page.screenshot(
    path="screenshots/failure.png",
    full_page=True,
)
```

##### Capturing a failure state

The exercise intentionally performs an assertion that should fail. The assertion is placed inside a `try` block so the failure state can be captured in `except`.

```python
try:
    expect(message).to_contain_text("expected success text")
except AssertionError as error:
    page.screenshot(path="screenshots/failure.png")
    print(error)
    raise
```

After taking the screenshot, re-raise the assertion so pytest still records the test as failed. A diagnostic screenshot should not hide a genuine test failure.

##### HTML reports

The slide deck uses `pytest-html` to generate a self-contained report.

```bash
pytest src/tests/test_08_report_screenshot.py \
  --html=report.html \
  --self-contained-html
```

The generated report contains the pytest execution result in a single HTML file.

##### Features covered

| Feature | Command or method | Purpose |
|---|---|---|
| Screenshot folder | `os.makedirs(..., exist_ok=True)` | Ensure the output folder exists |
| Viewport screenshot | `page.screenshot(path=...)` | Capture the visible browser area |
| Full-page screenshot | `page.screenshot(..., full_page=True)` | Capture the complete page |
| Failure screenshot | Screenshot inside `except` | Preserve the UI state at failure |
| HTML report | `pytest --html=... --self-contained-html` | Generate a portable pytest report |

#### 🔐 Test data

| Field | Value |
|---|---|
| Username | `tomsmith` |
| Invalid password | `wrongpassword` |
| Initial screenshot | `screenshots/before_login.png` |
| Failure screenshot | `screenshots/failure.png` |
| HTML report | `report.html` |

#### 🏗️ File to work in

| File | What to build |
|---|---|
| `src/tests/test_08_report_screenshot.py` | Complete the failed-login flow, screenshot handling, and intentional assertion failure |

#### ✅ Task 1 — Create the screenshot directory

Use `os.makedirs()` to create the folder stored in `screenshot_directory`.

The test must continue successfully when the folder already exists.

#### ✅ Task 2 — Start Playwright

Start Playwright in synchronous mode, launch Chromium in headed mode, and create a page.

The setup is intentionally incomplete in the Python exercise.

#### ✅ Task 3 — Open the login page

Navigate to the URL stored in `target_url`.

#### ✅ Task 4 — Capture the initial state

Before entering credentials, save a screenshot to `before_screenshot`.

Use a normal viewport screenshot for this step.

#### ✅ Task 5 — Submit invalid credentials

Complete the login interaction using:

- Username: `tomsmith`
- Password: `wrongpassword`

Then click the Login button.

#### ✅ Task 6 — Add the intentional failure

Locate the flash message and assert that it contains the successful-login text:

```text
You logged into a secure area!
```

This assertion is intentionally incorrect because the submitted password is invalid.

#### ✅ Task 7 — Capture the failure

Catch the assertion failure and:

- Save a full-page screenshot to `failure_screenshot`
- Print the error to the console
- Re-raise the error so pytest marks the test as failed

#### ✅ Task 8 — Clean up

Close the browser in `finally`, regardless of whether the assertion passed or failed.

#### ✅ Task 9 — Generate the report

After completing the script, install the reporting plug-in if it is not already available:

```bash
pip install pytest-html
```

Then run:

```bash
pytest src/tests/test_08_report_screenshot.py -v --headed -s \
  --html=report.html \
  --self-contained-html
```

The test is intentionally expected to fail, while still creating:

- `screenshots/before_login.png`
- `screenshots/failure.png`
- `report.html`

#### ⭐ Optional extension — Passing diagnostic test

Create a second test that validates the actual invalid-login message and passes. Capture an `after_error.png` screenshot before the correct assertion.

Keep the intentional-failure test unchanged so learners can compare failed and passed report entries.

#### 💡 Tips

- Create the screenshot folder before calling `page.screenshot()`.
- Use `full_page=True` for the failure screenshot if you want the complete page.
- Catch `AssertionError` for the intentionally failing Playwright assertion.
- Re-raise the error after capturing evidence.
- Use `-s` to display the printed error in the terminal.
- Keep screenshot paths in constants to avoid duplicated strings.
- Always close the browser in `finally`.

#### 📌 Reference

- [Playwright screenshots](https://playwright.dev/python/docs/screenshots)
- [Playwright assertions](https://playwright.dev/python/docs/test-assertions)
- [pytest-html documentation](https://pytest-html.readthedocs.io/)
- [The Internet login page](https://the-internet.herokuapp.com/login)
