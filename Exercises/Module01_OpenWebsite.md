## Exercise 01 — Opening a Website with Playwright

### 🎯 Goal

Learn how to start Playwright in synchronous mode, launch a browser, open a page, navigate to a website, and extract basic information such as the page title and main header.

### 📖 Background

#### Starting Playwright in synchronous mode

Use `sync_playwright()` as a context manager to initialize Playwright and ensure its resources are cleaned up correctly:

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Playwright commands go here
    pass
```

#### Launching a browser

Playwright supports Chromium, Firefox, and WebKit. In this exercise, use Chromium:

```python
browser = p.chromium.launch(
    headless=False,
    args=["--start-maximized"],
    slow_mo=1000,
)
```

| Setting | Purpose |
|---|---|
| `headless=False` | Displays the browser window while the test runs |
| `args=["--start-maximized"]` | Starts Chromium in a maximized window |
| `slow_mo=1000` | Adds a delay between actions for demonstration purposes |

#### Creating a page and navigating

A `Page` represents a browser tab. Use `new_page()` to create it and `goto()` to navigate:

```python
page = browser.new_page(viewport={"width": 1920, "height": 1080})
page.goto("https://the-internet.herokuapp.com")
```

#### Extracting information

Use `page.title()` to retrieve the browser tab title and `page.text_content("h1")` to retrieve the main heading:

```python
page_title = page.title()
main_header = page.text_content("h1")
```

### 🏗️ File to work in

| File | What to build |
|---|---|
| `tests/test_open_website.py` | All tasks for this exercise |

### ✅ Task 1 — Start Playwright

Create a test function named `test_open_website`.

Inside the function:
- Start Playwright using `sync_playwright()`
- Store the Playwright instance in the variable `p`
- Leave the browser work inside the `with` block

```python
from playwright.sync_api import sync_playwright


def test_open_website():
    with sync_playwright() as p:
        # TODO: launch the browser
        pass
```

### ✅ Task 2 — Launch Chromium

Launch Chromium with the following settings:
- Headed mode
- Maximized window
- A `slow_mo` value of 1000 milliseconds

```python
browser = p.chromium.launch(
    headless=____,
    args=[____________________],
    slow_mo=____,
)
```

### ✅ Task 3 — Create a page

Create a new page with a viewport of 1920 × 1080.

```python
page = browser.new_page(
    viewport={"width": ____, "height": ____}
)
```

### ✅ Task 4 — Open the website

Navigate to:

[https://the-internet.herokuapp.com](https://the-internet.herokuapp.com)

```python
page.goto(________________________________________)
```

Confirm that the page loads successfully before continuing.

### ✅ Task 5 — Print the page title

Retrieve the page title and print it in the following format:

```text
Title: The Internet
```

Complete the missing code:

```python
page_title = page.________()
print("Title:", __________)
```

### ✅ Task 6 — Print the main header

Retrieve the text from the page's `<h1>` element and print it in the following format:

```text
Header: Welcome to the-internet
```

Complete the missing code:

```python
main_header = page.____________("h1")
print("Header:", ___________)
```

### ✅ Task 7 — Add basic validations

Add assertions to verify that:
- The page title is `The Internet`
- The main header is `Welcome to the-internet`
- The current URL starts with `https://the-internet.herokuapp.com`

```python
assert page_title == __________________
assert main_header == _____________________________
assert page.url.startswith(________________________________________)
```

### ✅ Task 8 — Close the browser

Close the browser at the end of the test:

```python
browser.________()
```

For an additional challenge, place the browser actions inside a `try` block and close the browser in `finally` so it also closes when an assertion fails.

### ⭐ Bonus Task — Compare headed and headless execution

Run the test twice:
1. With `headless=False`
2. With `headless=True`

Observe the difference and answer these questions in comments below your test:
- Which mode displays the browser window?
- Which mode would normally be more suitable for automated pipeline execution?
- Does the test result change between the two modes?

### 🏃 Run your test

```bash
pytest tests/test_01_openwebsite.py -v --headed
```

### 💡 Tips

- Keep all browser operations inside the `sync_playwright()` block.
- Use straight quotation marks (`"`) in Python code, not typographic quotation marks.
- `page.title()` returns the document title shown in the browser tab.
- `page.text_content("h1")` returns the text content of the first matching `<h1>` element.
- Use `try/finally` to make sure the browser closes even if the test fails.
- `slow_mo` is useful for demonstrations but is usually unnecessary in normal automated runs.

### 📌 Reference

- [Playwright for Python — Getting started](https://playwright.dev/python/docs/intro)
- [Playwright for Python — Browser](https://playwright.dev/python/docs/api/class-browser)
- [Playwright for Python — Page](https://playwright.dev/python/docs/api/class-page)
- [The Internet test website](https://the-internet.herokuapp.com)