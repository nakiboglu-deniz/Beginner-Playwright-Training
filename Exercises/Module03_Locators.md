## Exercise 03 — Locators & Element Interaction

### 🎯 Goal

Learn how to locate and interact with web elements using different Playwright locator strategies.

In this exercise, you will:

- Open the login page
- Locate the username field with a CSS ID selector
- Locate the password field with an XPath selector
- Locate the Login button with an ARIA role
- Enter valid credentials
- Submit the form
- Verify that the login was successful

### 📖 Background

#### CSS selectors

CSS selectors locate elements using properties such as IDs, classes, and attributes.

```python
page.locator("#username")
page.locator("input[name='username']")
page.locator("button[type='submit']")
```

An ID selector starts with `#`. Use it when the element has a stable and unique ID.

#### XPath selectors

XPath locates elements by their attributes or position in the document structure.

```python
page.locator("//input[@id='password']")
```

XPath can be useful when an element does not have a convenient semantic locator, but it should remain short and understandable.

#### ARIA role locators

Role locators identify elements in the same way users and assistive technologies understand them.

```python
page.get_by_role("button", name="Login")
```

Playwright recommends user-facing locators such as roles and labels where possible.

#### Filling and clicking

Use `fill()` to enter text and `click()` to activate an element.

```python
username.fill("tomsmith")
login_button.click()
```

#### Locator strategies covered

| Locator type | Example | Typical use |
|---|---|---|
| CSS ID | `#username` | Element with a stable unique ID |
| CSS attribute | `input[name='username']` | Element with a stable attribute |
| XPath | `//input[@id='password']` | Attribute or structure-based lookup |
| Text | `text=Login` | Element with unique visible text |
| ARIA role | `get_by_role("button", name="Login")` | Accessible, user-facing control |
| Label | `get_by_label("Username")` | Form field associated with a label |
| Test ID | `[data-testid='login-button']` | Application-provided test identifier |

### 🔐 Test data

| Field | Value |
|---|---|
| Username | `tomsmith` |
| Password | `SuperSecretPassword!` |

### 🏗️ File to work in

| File | What to build |
|---|---|
| `test_03_locators.py` | Complete the login workflow and its validations |

### ✅ Task 1 — Start Playwright

Start Playwright in synchronous mode and launch Chromium in headed mode.

Most of this setup is left for you to implement in the Python exercise.

### ✅ Task 2 — Open the login page

Create a page and navigate to:

[The Internet login page](https://the-internet.herokuapp.com/login)

Use the `TARGET_URL` constant from the starter script.

### ✅ Task 3 — Locate the username field with CSS

Create a locator for the username field using its element ID.

```python
username_field = page.locator(____________)
```

Then fill it with the value stored in `VALID_USERNAME`.

### ✅ Task 4 — Locate the password field with XPath

Create an XPath locator targeting the input element whose ID is `password`.

```python
password_field = page.locator(______________________________)
```

Then fill it with the value stored in `VALID_PASSWORD`.

### ✅ Task 5 — Locate the Login button with an ARIA role

Use `get_by_role()` to locate the button by role and accessible name.

```python
login_button = page.____________(
    __________,
    name=__________,
)
```

Click the button to submit the form.

### ✅ Task 6 — Verify the login

Implement only the following essential validations:

- The URL contains `/secure`
- The success message contains `You logged into a secure area!`

The assertions are intentionally incomplete in the Python file and must be implemented by the learner.

### ✅ Task 7 — Add another locator strategy

Choose one field or button and locate it again using a different strategy from the table above.

Examples:

- Locate the username field by label
- Locate the Login button with a CSS attribute selector
- Locate the password field with a CSS ID selector

Use the alternative locator in a meaningful check or interaction. This task is intentionally open-ended.

### ✅ Task 8 — Clean up

Close the browser in a `finally` block so it closes even when the test fails.

### 🏃 Run the exercise

```bash
pytest test_03_locators_element_interaction.py -v -s
```

### 💡 Tips

- CSS ID selectors begin with `#`.
- XPath selectors commonly begin with `//`.
- `get_by_role()` requires a role and can include an accessible name.
- Prefer stable, readable locators over long selectors based on page structure.
- Do not add fixed sleeps. Playwright automatically waits for elements before interacting with them.
- Keep only the two required assertions unless you want to test an additional locator strategy.

### 📌 Reference

- [Playwright locator documentation](https://playwright.dev/python/docs/locators)
- [Playwright assertions documentation](https://playwright.dev/python/docs/test-assertions)
- [The Internet login page](https://the-internet.herokuapp.com/login)
