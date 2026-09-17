### Exercise 04 — Waits & Synchronization

#### 🎯 Goal

Learn how to synchronize Playwright tests with dynamic web pages by waiting for the page, elements, and UI states to become ready.

In this exercise, you will:

- Open a dynamically loaded page
- Wait until the DOM is ready
- Locate the Start button
- Wait until the button is visible
- Start the dynamic loading process
- Wait until the loading indicator disappears
- Wait until the result message becomes visible
- Verify the final message text
- Print the final message to the console

#### 📖 Background

##### Why synchronization is needed

Modern web applications often update elements asynchronously. An element may exist after a delay, become enabled after an action, or appear only after a loading indicator disappears.

A test that continues before the interface is ready can fail even when the application works correctly. Playwright provides waiting methods and retrying assertions to synchronize tests with the actual UI state.

##### Page load waits

Use `wait_for_load_state()` when a test needs to wait for a specific page-loading milestone.

```python
page.wait_for_load_state("domcontentloaded")
```

The load states introduced in this module are:

| Load state | Description |
|---|---|
| `domcontentloaded` | The HTML has been parsed and the DOM is ready |
| `load` | The page and its dependent resources have loaded |
| `networkidle` | The network has been inactive for the required period |

For this exercise, use `domcontentloaded`.

##### Waiting for element visibility

Use a locator's `wait_for()` method when an element must reach a particular state.

```python
start_button.wait_for(state="visible")
```

Common locator states include:

| State | Meaning |
|---|---|
| `visible` | The element is displayed |
| `attached` | The element exists in the DOM |
| `hidden` | The element is no longer visible |
| `detached` | The element has been removed from the DOM |

##### Waiting for an element to disappear

Dynamic pages often show a spinner or loading indicator while work is in progress. Wait for it to become hidden before continuing.

```python
page.wait_for_selector("#loading", state="hidden")
```

This prevents the test from checking the result while the loading process is still active.

##### Waiting for text

Playwright assertions automatically retry until the expected condition is met or the timeout is reached.

```python
expect(message).to_have_text("Hello World!")
```

This is more reliable than reading the text immediately after clicking the Start button.

##### Wait types introduced in Module 4

| Wait type | Method | Typical use |
|---|---|---|
| Page load | `wait_for_load_state()` | Wait for page or DOM readiness |
| Element visible | `locator.wait_for(state="visible")` | Wait for dynamically displayed content |
| Text or state change | `expect(locator).to_have_text()` / `to_be_enabled()` | Wait for the UI to update |
| Navigation | `expect_navigation()` | Wait for a redirect or page transition |
| Element hidden | `wait_for_selector(..., state="hidden")` | Wait for a spinner or overlay to disappear |

#### 🏗️ File to work in

| File | What to build |
|---|---|
| `src/tests/test_04_waits.py` | Complete the dynamic loading workflow and synchronization steps |

#### ✅ Task 1 — Start Playwright

Start Playwright in synchronous mode and launch Chromium in headed mode.

The browser setup is intentionally incomplete in the Python exercise.

#### ✅ Task 2 — Open the dynamic loading page

Create a new page and navigate to:

[The Internet dynamic loading page](https://the-internet.herokuapp.com/dynamic_loading/1)

Use the `target_url` constant from the starter script.

#### ✅ Task 3 — Wait for the DOM

After navigation, wait for the `domcontentloaded` load state.

```python
page.____________________("domcontentloaded")
```

Do not use `time.sleep()`.

#### ✅ Task 4 — Locate and wait for the Start button

Locate the Start button using an ARIA role locator.

Then explicitly wait until it is visible before clicking it.

```python
start_button = page.____________("button", name="Start")
start_button.________(state="visible")
```

#### ✅ Task 5 — Start dynamic loading

Click the Start button and locate:

- The loading indicator with `#loading`
- The final message with `#finish h4`

The locator creation and click action are left for you to implement.

#### ✅ Task 6 — Wait for the loading indicator to disappear

Wait until the loading indicator is hidden.

Choose either the page-level or locator-level waiting method covered in the module.

```python
page._________________("#loading", state="hidden")
```

#### ✅ Task 7 — Wait for the final message

Wait until the message becomes visible.

```python
message.________(state="visible")
```

#### ✅ Task 8 — Verify the message

Implement one essential assertion that waits until the message text is:

```text
Hello World!
```

The assertion is intentionally incomplete in the Python file.

#### ✅ Task 9 — Print the result

Retrieve the final message text and print it in this format:

```text
Final message: Hello World!
```

#### ✅ Task 10 — Clean up

Close the browser in a `finally` block so it closes even if a wait or assertion fails.
#### 🏃 Run the exercise

```bash
pytest src/tests/test_04_waits.py -v --headed
```

#### 💡 Tips

- Use Playwright waits instead of fixed delays.
- Create locators before waiting for their states.
- `wait_for(state="visible")` waits for an element to be displayed.
- `state="hidden"` is suitable for loading indicators and overlays.
- Playwright `expect()` assertions retry automatically.
- Keep the test focused on the synchronization steps from the exercise.
- Always close the browser in `finally`.

#### 📌 Reference

- [Playwright auto-waiting](https://playwright.dev/python/docs/actionability)
- [Playwright page load states](https://playwright.dev/python/docs/api/class-page#page-wait-for-load-state)
- [Playwright locator waiting](https://playwright.dev/python/docs/api/class-locator#locator-wait-for)
- [Playwright assertions](https://playwright.dev/python/docs/test-assertions)
- [The Internet dynamic loading page](https://the-internet.herokuapp.com/dynamic_loading/1)
