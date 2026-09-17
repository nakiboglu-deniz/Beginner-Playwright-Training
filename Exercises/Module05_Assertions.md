### Exercise 05 — Assertions

#### 🎯 Goal

Learn how to use Playwright assertions to validate that a web page and its elements are in the expected state.

In this exercise, you will:

- Open the login page
- Enter valid credentials
- Submit the login form
- Validate the page title and URL
- Check that the success message is visible and contains the expected text
- Verify the Logout link and its `href` attribute
- Confirm that the page body is visible
- Print a confirmation after all assertions pass

#### 📖 Background

##### Playwright assertions

Playwright's `expect()` assertions verify page and element conditions. They automatically retry until the condition is satisfied or the assertion timeout is reached.

```python
expect(page).to_have_title("The Internet")
expect(page.locator("h2")).to_have_text("Secure Area")
```

This retrying behaviour makes Playwright assertions suitable for dynamic web interfaces.

##### Page assertions

Page assertions validate information belonging to the complete browser page.

```python
expect(page).to_have_title("The Internet")
expect(page).to_have_url("https://the-internet.herokuapp.com/secure")
```

The module introduces title and URL assertions as ways to verify that the correct page has loaded and navigation completed successfully.

##### Text assertions

Use text assertions to verify the text displayed by an element.

```python
expect(message).to_contain_text("You logged into a secure area!")
```

Use `to_have_text()` when the complete text must match. Use `to_contain_text()` when the target text may be part of a longer value.

##### Attribute and class assertions

Assertions can validate HTML attributes and CSS classes.

```python
expect(logout_link).to_have_attribute("href", "/logout")
expect(button).to_have_class(re.compile(".*radius.*"))
```

Attribute assertions are useful for checking values such as `href`, `type`, and `data-*` attributes.

##### Element-state assertions

Element-state assertions verify whether an element is visible, enabled, or checked.

```python
expect(logout_link).to_be_visible()
expect(username_input).to_be_enabled()
```

Negative assertions verify that a condition is not true.

```python
expect(message).not_to_be_visible()
```

##### Assertion types introduced in Module 5

| Assertion type | Method | Purpose |
|---|---|---|
| Title | `to_have_title()` | Verify that the correct page loaded |
| Text | `to_have_text()` / `to_contain_text()` | Validate displayed content |
| URL | `to_have_url()` | Validate navigation |
| Attribute | `to_have_attribute()` | Validate an HTML attribute |
| Class | `to_have_class()` | Validate CSS class information |
| State | `to_be_visible()` / `to_be_enabled()` | Validate element readiness |
| Negative | `not_to_be_visible()` | Validate that an element is hidden |
| Checkbox | `to_be_checked()` | Validate checkbox state |
| Screenshot | `screenshot()` | Capture the UI for visual verification |

#### 🔐 Test data

| Field | Value |
|---|---|
| Username | `tomsmith` |
| Password | `SuperSecretPassword!` |
| Expected title text | `Internet` |
| Expected URL path | `/secure` |
| Expected success text | `You logged into a secure area!` |
| Expected Logout href | `/logout` |

#### 🏗️ File to work in

| File | What to build |
|---|---|
| `src/tests/test_05_assertions.py` | Complete the login workflow and required assertions |

#### ✅ Task 1 — Start Playwright

Start Playwright in synchronous mode and launch Chromium in headed mode.

The setup is intentionally incomplete in the Python exercise.

#### ✅ Task 2 — Open the login page

Create a page and navigate to:

[The Internet login page](https://the-internet.herokuapp.com/login)

Use the `target_url` constant from the starter script.

#### ✅ Task 3 — Complete the login flow

Locate and fill the username and password fields using the provided test data.

Then locate and click the Login button.

The locators and interactions are left for you to implement.

#### ✅ Task 4 — Validate the page title

Assert that the page title contains the word `Internet`.

Choose the suitable Playwright page assertion and use the provided `expected_title_text` constant.

#### ✅ Task 5 — Validate the URL

Assert that the URL contains `/secure` after login.

A regular expression can be used so that the assertion focuses on the required path rather than duplicating the complete URL.

#### ✅ Task 6 — Validate the success message

Locate the flash message using `#flash` and implement these assertions:

- The message is visible
- The message contains `You logged into a secure area!`

```python
success_message = page.locator(________)
expect(_______________).to_be_________()
expect(_______________).to_contain_text(_____________________)
```

#### ✅ Task 7 — Validate the Logout link

Locate the Logout link and implement these assertions:

- The link is visible
- Its `href` attribute is exactly `/logout`

```python
logout_link = page.____________("link", name="Logout")
expect(___________).to_be_________()
expect(___________).to_have_attribute(_______, _______________)
```

#### ✅ Task 8 — Validate the page body

Locate the `<body>` element and assert that it is visible.

This is the final basic page check from the module exercise.

#### ✅ Task 9 — Print the result

After all assertions pass, print:

```text
All assertions passed!
```

#### ✅ Task 10 — Clean up

Close the browser in a `finally` block so it closes even if an assertion fails.

#### ⭐ Optional extension — Checkbox assertion

Create a separate pytest test for [The Internet checkboxes page](https://the-internet.herokuapp.com/checkboxes).

Your optional test can:

- Locate the first checkbox
- Verify its initial checked state
- Change its state
- Assert its updated state with `to_be_checked()` or `not_to_be_checked()`

This extension is not included in the starter test.

#### 🏃 Run the exercise

```bash
pytest src/tests/test_05_assertions.py -v --headed
```

#### 💡 Tips

- Import Python's `re` module when matching only part of a title or URL.
- Use `to_contain_text()` when an element includes extra text or a close icon.
- Use role locators for user-facing controls such as the Login button and Logout link.
- Playwright assertions retry automatically.
- Do not replace assertions with fixed delays.
- Keep the test focused on the validations required by the exercise.
- Always close the browser in `finally`.

#### 📌 Reference

- [Playwright assertions](https://playwright.dev/python/docs/test-assertions)
- [Playwright locator assertions](https://playwright.dev/python/docs/api/class-locatorassertions)
- [Playwright page assertions](https://playwright.dev/python/docs/api/class-pageassertions)
- [The Internet login page](https://the-internet.herokuapp.com/login)
