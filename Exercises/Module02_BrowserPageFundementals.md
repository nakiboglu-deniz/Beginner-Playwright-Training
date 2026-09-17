## Exercise 02 — Browser, Context, and Page Fundamentals

### 🎯 Goal

Understand the relationship between a Playwright `Browser`, `BrowserContext`, and `Page`, then use them to open an isolated browser session and interact with a web page.

In this exercise, you will:

- Launch a Chromium browser
- Create an isolated browser context
- Open a page inside the context
- Navigate to the Add/Remove Elements page
- Click **Add Element** twice
- Count the Delete buttons
- Add pytest assertions to validate the result
- Close the context and browser safely

### 📖 Background

#### Browser

A `Browser` is the browser application controlled by Playwright, such as Chromium, Firefox, or WebKit.

```python
browser = p.chromium.launch(headless=False)
```

The browser can run in:

- **Headed mode**, where the browser window is visible
- **Headless mode**, where the browser runs without displaying a window

#### BrowserContext

A `BrowserContext` is an isolated browser session. It has its own cookies, local storage, and session data.

```python
context = browser.new_context()
```

A context behaves similarly to an incognito browser window. Multiple contexts can be created inside one browser to simulate independent users.

#### Page

A `Page` represents a single browser tab inside a context. Browser interactions such as navigation, clicking, filling fields, and taking screenshots are performed through the page.

```python
page = context.new_page()
```

The hierarchy is:

```text
Browser
└── BrowserContext
    └── Page
```

#### Navigation and interaction

Use `goto()` to open a website and `click()` or a locator to interact with elements.

```python
page.goto("https://the-internet.herokuapp.com/add_remove_elements/")
page.get_by_role("button", name="Add Element").click()
```

#### Counting matching elements

A Playwright locator can represent multiple matching elements. Use `count()` to determine how many elements currently match.

```python
delete_buttons = page.get_by_role("button", name="Delete")
button_count = delete_buttons.count()
```

### 🏗️ File to work in

| File | What to build |
|---|---|
| `test_02_browser_page_fundamentals.py` | Complete the Playwright exercise and pytest assertions |

### ✅ Task 1 — Start Playwright

Import `sync_playwright` and start it inside the test with a context manager.

```python
from playwright.sync_api import sync_playwright


def test_add_and_remove_elements():
    with __________________________ as p:
        # Continue the exercise here
```

### ✅ Task 2 — Launch Chromium

Launch Chromium with:

- `headless=False`
- `slow_mo=1000`

```python
browser = p.________.launch(
    headless=____,
    slow_mo=____,
)
```

### ✅ Task 3 — Create an isolated context

Create a new browser context.

```python
context = browser._____________()
```

The page must be created from the context, not directly from the browser.

### ✅ Task 4 — Open a page

Create a page inside the isolated context.

```python
page = context.__________()
```

### ✅ Task 5 — Navigate to the exercise page

Navigate to:

[The Internet: Add/Remove Elements](https://the-internet.herokuapp.com/add_remove_elements/)

```python
page.________(TARGET_URL)
```

### ✅ Task 6 — Locate the Add Element button

Use an accessible role locator to locate the button by its visible name.

```python
add_button = page.____________(
    "button",
    name=_____________,
)
```

### ✅ Task 7 — Add two elements

Click the Add Element button exactly twice.

```python
for _ in range(____):
    add_button.________()
```

### ✅ Task 8 — Locate and count the Delete buttons

Locate all buttons named `Delete`, then count them.

```python
delete_buttons = page.____________("button", name="Delete")
delete_button_count = delete_buttons._______()
```

Print the result:

```text
Delete buttons found: 2
```

### ✅ Task 9 — Implement the assertions

Add assertions that verify:

- The page title is `The Internet`
- The current URL is the expected URL
- The Add Element button is visible
- The first Delete button is visible

Use a combination of regular Python assertions and Playwright's `expect()` assertions.

```python
assert page.________() == EXPECTED_TITLE
assert page.____ == TARGET_URL
expect(add_button).to_be_________()
assert delete_button_count == ____
expect(delete_buttons._______).to_be_________()
```

### ✅ Task 11 — Clean up safely

Use `finally` to close both the context and browser, even if an assertion fails.

```python
finally:
    context.________()
    browser.________()
```

### 🧩 Starter test

The accompanying Python file contains the complete exercise structure with important methods, values, locators, assertions, and cleanup steps left for the learner to implement.

### 🏃 Run the exercise

```bash
pytest test_02_browser_page_fundamentals.py -v --headed
```

The test should pass only after all placeholders have been replaced correctly.

### 💡 Tips

- Create the page with `context.new_page()`, not `browser.new_page()`.
- Prefer accessible locators such as `get_by_role()` for visible buttons.
- A locator remains connected to the page, so calling `count()` again reflects the current page state.
- Use `.first` to access the first matching locator.
- Put cleanup operations in `finally` so resources are released after failures.
- Do not use `time.sleep()`. Playwright automatically waits for elements to become actionable.

### 📌 Reference

- [Playwright Browser documentation](https://playwright.dev/python/docs/api/class-browser)
- [Playwright BrowserContext documentation](https://playwright.dev/python/docs/api/class-browsercontext)
- [Playwright Page documentation](https://playwright.dev/python/docs/api/class-page)
- [Playwright locator documentation](https://playwright.dev/python/docs/locators)
- [The Internet test website](https://the-internet.herokuapp.com/add_remove_elements/)