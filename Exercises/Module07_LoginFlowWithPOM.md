### Exercise 07 — Login Flow with Page Object Model

#### 🎯 Goal

Learn how to structure a Playwright login test with the Page Object Model (POM), separating page-specific locators and actions from test logic.

In this exercise, you will:

- Create a reusable `LoginPage` class
- Store page locators inside the page object
- Implement navigation and login methods
- Implement successful-login validation
- Add a failed-login validation method
- Write separate valid and invalid login tests
- Keep selectors out of the test file

#### 📖 Background

##### What is the Page Object Model?

The Page Object Model separates:

- **Test logic**, which describes what the test verifies
- **Page structure**, which contains locators and reusable UI actions

Instead of placing selectors directly in every test, a page-object class represents the page and exposes methods such as `navigate()`, `login()`, and `assert_login_success()`.

```python
login_page = LoginPage(page)
login_page.navigate()
login_page.login("tomsmith", "SuperSecretPassword!")
login_page.assert_login_success()
```

##### The LoginPage class

The page object receives Playwright's `Page` object through its constructor.

```python
class LoginPage:
    def __init__(self, page: Page):
        self.page = page
```

The constructor is also used to define the locators required by the page.

##### Reusable methods

A page object should provide meaningful methods that represent user actions or page checks.

| Method | Responsibility |
|---|---|
| `navigate()` | Open the login page |
| `login(user, password)` | Enter credentials and submit the form |
| `assert_login_success()` | Validate a successful login |
| `assert_login_failed()` | Validate an unsuccessful login |

##### Separation of responsibilities

The page-object file should contain:

- The page URL
- Locators
- UI interactions
- Page-specific assertions

The test file should contain:

- Test data
- Test scenarios
- Calls to page-object methods

The test file must not use CSS or XPath selectors directly.

#### 🔐 Test data

| Scenario | Username | Password | Expected result |
|---|---|---|---|
| Valid login | `tomsmith` | `SuperSecretPassword!` | User reaches the secure area |
| Invalid login | `tomsmith` | `wrongpassword` | Error message is shown and URL remains on `/login` |

#### 🏗️ Files to work in

| File | What to build |
|---|---|
| `src/pages/login_page.py` | Complete the `LoginPage` class, locators, actions, and assertions |
| `src/tests/test_07_login_pom.py` | Complete the valid and invalid login tests |

#### ✅ Task 1 — Complete the LoginPage constructor

Store the Playwright page and define locators for:

- Username field
- Password field
- Login button
- Flash message

The important locator values are left incomplete in `login_page.py`.

#### ✅ Task 2 — Implement navigation

Complete the `navigate()` method so that it opens the login page.

Use the URL constant defined in the page-object class.

#### ✅ Task 3 — Implement the login action

Complete `login(user, password)` so it:

- Fills the username
- Fills the password
- Clicks the Login button

The method should work for both valid and invalid credentials.

#### ✅ Task 4 — Implement successful-login validation

Complete `assert_login_success()` so it verifies:

- The flash message is visible
- The message contains `You logged into a secure area!`
- The URL contains `/secure`

Keep these assertions inside the page object.

#### ✅ Task 5 — Implement failed-login validation

Complete `assert_login_failed()` so it verifies:

- The flash message is visible
- The message contains `Your password is invalid!`
- The URL still contains `/login`

#### ✅ Task 6 — Complete the valid-login test

In the test file:

- Start Playwright
- Launch Chromium
- Create a page
- Instantiate `LoginPage`
- Navigate to the login page
- Log in with valid credentials
- Call `assert_login_success()`

Do not add selectors to the test.

#### ✅ Task 7 — Complete the invalid-login test

Create a second test that:

- Instantiates `LoginPage`
- Navigates to the login page
- Uses the valid username and an incorrect password
- Calls `assert_login_failed()`

#### ✅ Task 8 — Clean up

Close the browser in a `finally` block in both tests.

#### 🏃 Run the exercise

```bash
pytest src/tests/test_07_login_pom.py -v --headed
```

#### 💡 Tips

- Import `Page` and `expect` in the page-object file.
- Store locators once in the constructor.
- The test should communicate intent without exposing selector details.
- Reuse the same `login()` method for positive and negative scenarios.
- Keep page-specific assertions inside `LoginPage`.
- Do not duplicate login actions in the test file.
- Always close the browser in `finally`.

#### 📌 Reference

- [Playwright page-object models](https://playwright.dev/python/docs/pom)
- [Playwright locators](https://playwright.dev/python/docs/locators)
- [Playwright assertions](https://playwright.dev/python/docs/test-assertions)
- [The Internet login page](https://the-internet.herokuapp.com/login)