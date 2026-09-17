### Exercise 06 — Error Handling

#### 🎯 Goal

Learn how to recognize, diagnose, and correct common failures in Playwright tests without hiding genuine defects.

In this exercise, you will:

- Trigger and inspect a timeout caused by an incorrect locator
- Correct a visibility and synchronization problem
- Handle navigation before continuing with page interactions
- Repair an invalid selector
- correct an assertion mismatch
- Record the error type, cause, and solution
- Add one custom failure scenario
- Close the browser safely after the exercise

Before writing code, review the starter test and identify every section marked with `TODO`.

Each section represents a common automation problem. Run the test after completing one section, inspect the output, and continue until all corrected checks pass.

#### 📖 Background

##### Why error handling matters

Playwright failures normally provide useful information about the failing action, locator, expected value, and timeout. Effective error handling should help diagnose a problem without allowing a broken test to pass silently.

Use `try` and `except` when the exercise intentionally triggers an error that must be inspected. After identifying the cause, correct the failing action and validate the repaired behaviour.

##### Timeout errors

A timeout occurs when Playwright cannot complete an action within the configured time. A common cause is a locator that does not match the intended element.

```python
try:
    page.click("#incorrect-locator", timeout=1000)
except PlaywrightTimeoutError as error:
    print("Timeout caught:", error)
```

The correct solution is normally to repair the locator or synchronization logic rather than increasing the timeout without investigation.

##### Elements that are not visible

An element may exist in the DOM before it is visible or actionable. Dynamic pages often require an action followed by a visibility wait.

```python
message = page.locator("#finish h4")
message.wait_for(state="visible")
```

Attempting to interact with hidden content before it appears can cause a timeout.

##### Navigation-related failures

A click, redirect, refresh, or form submission can replace the current document. The test must wait for navigation before it continues with actions that depend on the new page.

```python
with page.expect_navigation():
    page.click("a#redirect")
```

After navigation, verify the destination before performing further interactions.

##### Invalid selectors

A selector typo can prevent Playwright from finding the intended element.

```python
page.fill("#username", "tomsmith")
```

Inspect the page, compare the locator with the HTML, and correct the selector rather than suppressing the resulting exception.

##### Assertion failures

An assertion fails when the actual page state does not match the expected result.

```python
expect(page.locator("h2")).to_have_text("Login Page")
```

Determine whether the application is wrong or the expected value is outdated before changing the assertion.

##### Error categories covered

| Error category | Example cause | Corrective action |
|---|---|---|
| Timeout | Element not found or not ready | Correct the locator or synchronization |
| Hidden element | Interaction happens before visibility | Wait for the appropriate element state |
| Navigation interruption | Test continues during page transition | Wait for navigation or page readiness |
| Invalid selector | Typo or incorrect selector strategy | Reinspect and repair the locator |
| Assertion mismatch | Incorrect expected value | Compare actual and expected behaviour |

#### 🏗️ File to work in

| File | What to build |
|---|---|
| `src/tests/test_06_error_handling.py` | Diagnose the intentional failures and implement the corrected actions |

#### ✅ Task 1 — Start Playwright

Start Playwright in synchronous mode, launch Chromium in headed mode, and create a page.

The setup is intentionally incomplete in the Python exercise.

#### ✅ Task 2 — Diagnose a timeout

Navigate to the login page and intentionally use the incorrect locator `#login` with a short timeout.

Catch the Playwright timeout and print:

- The error category
- The likely cause
- The correct locator

Then use the corrected locator to prove that the Login button is visible.

#### ✅ Task 3 — Correct a visibility problem

Navigate to the dynamic loading page.

Your test must:

- Locate the hidden message
- Demonstrate why it cannot be used before the loading action finishes
- Click **Start**
- Wait until the message is visible
- Verify that the message contains `Hello World!`

Complete the missing action, wait, and assertion yourself.

#### ✅ Task 4 — Correct navigation handling

Navigate to the redirector page and click the redirect link.

Wrap the click in the appropriate navigation wait, then verify that the browser reaches the status-codes page.

```python
with page.________________(url="**/status_codes"):
    page.________("a#redirect")
```

#### ✅ Task 5 — Repair an invalid selector

Navigate back to the login page.

The provided selector contains a typo:

```python
#usernme
```

Catch the resulting timeout, print the cause, then replace it with the correct username locator and enter a value.

#### ✅ Task 6 — Correct an assertion mismatch

The page heading is not `Wrong Title`.

First, inspect the assertion failure. Then implement the corrected assertion using the actual heading text displayed on the login page.

#### ✅ Task 7 — Add a custom error scenario

Add one additional error scenario of your own. Choose one of the following:

- A timeout caused by an incorrect locator
- A visibility or timing issue
- An assertion mismatch

Your scenario must include:

- The failing action inside `try`
- A suitable exception handler
- A short diagnostic message
- A corrected action or assertion after the error is handled

#### ✅ Task 8 — Clean up

Close the browser in a `finally` block so it closes even if an unexpected failure occurs.

#### 🏃 Run the exercise

```bash
pytest src/tests/test_06_error_handling.py -v --headed -s
```

The `-s` option displays the diagnostic messages printed by each exercise section.

#### 💡 Tips

- Import Playwright's `TimeoutError` with a clear alias such as `PlaywrightTimeoutError`.
- Catch the narrowest appropriate exception type.
- Do not leave corrected tests inside broad `except Exception` blocks.
- A caught error should be followed by a corrected action that proves the diagnosis.
- Use Playwright waits instead of `time.sleep()`.
- Do not increase a timeout until you understand why the original action failed.
- Keep the intentional failures short by using a small timeout.
- Always close the browser in `finally`.

#### 📌 Reference

- [Playwright Python errors](https://playwright.dev/python/docs/api/class-playwrighterror)
- [Playwright auto-waiting](https://playwright.dev/python/docs/actionability)
- [Playwright assertions](https://playwright.dev/python/docs/test-assertions)
- [Playwright navigation](https://playwright.dev/python/docs/navigations)
- [The Internet test website](https://the-internet.herokuapp.com)