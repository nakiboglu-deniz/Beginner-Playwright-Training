# Playwright with Python — Beginner Test Automation Training

This is a hands-on training program covering Python fundamentals, UI automation, API testing with Playwright using AI-powered coding assistants like GitHub Copilot.

## 📋 Overview

Beginner Self-Study Training Program  ** Organizatory curriculum **

This training is designed as a beginner self-study program. Participants will follow the instructions provided in the README.md file, clone the repository, and complete the required exercises independently.
To support the learning process, participants can refer to the videos linked within the README.md documentation. The expected duration of the training is up to 40 hours. However, if additional time is needed, participants may continue at a reasonable pace until they complete all requirements.

For questions or support during the training, a dedicated Microsoft Teams group will be available. Participants can post their questions there, and the trainers will respond as their availability permits.
Upon completing the training, participants must review their solutions using the AI agent provided in the .github folder. Instructions for running and using the agent are available in the README.md file. The resulting output should then be shared in the Microsoft Teams group for review and feedback.

### Part 1: Python Fundamentals and Playwright UI Testing

You will learn:

- Python syntax, variables, data types, operators, and type casting
- Control flow, loops, functions, variable scope, and error handling
- Playwright browser, browser context, and page concepts
- Navigation, locators, interactions, synchronization, and assertions
- Page Object Model design
- Screenshots and HTML test reports

### Part 2: Playwright API Testing and AI-Assisted Automation

You will learn:

- REST API concepts, endpoints, request methods, headers, parameters, and bodies
- GET, POST, PUT, and DELETE requests
- Response status, headers, and JSON body validation
- Negative testing and unsuccessful requests
- API test refactoring and reusable base URLs
- GitHub Copilot and MCP concepts
- Using an AI agent to explore an application, generate tests, run them, and fix failures

**************************************************************************************************************************
This project demonstrates advanced test automation using:

- **Playwright for Python** for UI/Web and API testing
- **pytest** as the testing framework
- **pytest-playwright** for Playwright fixtures and browser management

The training targets a real, live application: [https://the-internet.herokuapp.com](https://the-internet.herokuapp.com)

### 🚀 Getting Started 
### Prerequisites

#### 1. Python 3.11+
- Download: https://www.python.org/downloads/
- Installation: Run the installer. On Windows, check **"Add Python to PATH"** during setup
- Verify: Open terminal and run `python --version`

#### 2. PyCharm (Recommended IDE)
- Download: https://www.jetbrains.com/help/pycharm/installation-guide.html#standalone

#### 3. Git
- Download: https://git-scm.com/downloads
- Verify: `git --version`

#### 4. GitHub Account
- Sign up: https://github.com/join
- Required for GitHub Copilot (even the free version)

#### 5. Node.js LTS
- Node.js is required for the MCP tooling used in the AI-assisted part of the training.
- Download the LTS version from [Node.js Downloads](https://nodejs.org/).
- Verify the installation: 'node --version'
- Verify npm installation: 'npm --version'

#### 6. GitHub Copilot
1. Open VS Code
2. Click the Copilot icon at the top of the window
3. Sign in to your GitHub account when prompted
4. Optional: activate the 30-day free trial at https://github.com/github-copilot/pro

#### 7. Clone the repository (Clone in PyCharm or terminal)
1. Open PyCharm.
2. Select **Get from Version Control**.
3. Choose **Git**.
4. Enter the repository URL.
5. Select a local destination folder.
6. Select **Clone**.
7. Alternatively, use the terminal:
```bash
git clone <repository-url>
cd <repository-folder>
```
> **Note:** If this is your first time using GitHub with PyCharm, you will be prompted to sign in during the clone process.

#### 8. Set up the Python environment
##### Let PyCharm Create the Virtual Environment

1. Open the project in PyCharm.
2. Open **Settings**.
3. Select **Python > Interpreter**.
4. Select **Add Interpreter**.
5. Choose **Add Local Interpreter**.
6. Select **Virtualenv**.
7. Use `.venv` as the environment location.
8. Choose your installed Python version as the base interpreter.
9. Apply the configuration.

##### Create the Virtual Environment in the Terminal

```bash
python -m venv .venv
```

Activate it.

**Windows Command Prompt:**

```bat
.venv\Scripts\activate
```

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

**macOS or Linux:**

```bash
source .venv/bin/activate
```

Ensure that PyCharm uses the interpreter inside `.venv`.

---
```bash
python -m venv .venv
source .venv/bin/activate        # macOS / Linux
.venv\Scripts\activate           # Windows


```
#### 8. Install the Project Dependencies

Open the PyCharm terminal and make sure the virtual environment is active.

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
playwright install
```
#### 9. Verify your setup

```bash
pytest src/tests/smoke_test.py -v
```
All 5 smoke tests should pass — you are ready to start.

## 📋 Verification of the training

### GitHub Copilot, Playwright, and MCP Setup in PyCharm

This guide explains how to configure GitHub Copilot, Playwright, and the PyCharm MCP Server for AI-assisted test automation.

With this setup, an AI agent can use the project context and available MCP tools to help generate, run, debug, and improve Playwright tests.

## Overview

GitHub Copilot provides two main capabilities inside PyCharm:

1. **Code completion**: Copilot suggests code while you type. Press `Tab` to accept a useful suggestion or continue typing to ignore it.
2. **Copilot Chat**: Ask questions about your project and request help with code generation, debugging, explanations, and tests.

Example Copilot Chat prompts:

```text
Explain this function.
```

```text
Write a test case for this block of code.
```

```text
How can I fix the error in this test?
```

## Prerequisites

Before starting, make sure you have:

- PyCharm installed
- A configured Python interpreter or virtual environment
- Node.js LTS installed
- GitHub Copilot access
- Playwright and its browser dependencies
- The PyCharm MCP Server enabled

## 1. Install Node.js

Download and install the LTS version of Node.js from [Node.js](https://nodejs.org/).

Verify the installation in a terminal:

```bash
node --version
npm --version
```

## 2. Configure Node.js in PyCharm

1. Open PyCharm.
2. Open **Settings** with `Ctrl+Alt+S`.
3. Select **Languages & Frameworks > Node.js**.
4. Check the **Node interpreter** field.
5. If PyCharm has detected Node.js correctly, keep the detected interpreter.
6. If the field shows **Not configured**, select the browse button and add the path to the Node.js executable.
7. Verify that the **Package manager** field contains the npm executable.
8. Apply the changes.

Common Node.js interpreter paths:

**Windows**

```text
C:\Program Files\nodejs\node.exe
```

**macOS or Linux**

```text
/usr/local/bin/node
```

You can locate the executable from a terminal.

**Windows**

```bat
where node
```

**macOS or Linux**

```bash
which node
```

## 3. Install Playwright and Browser Dependencies

Open the terminal inside PyCharm and activate the project's virtual environment.

Install the Playwright Python package:

```bash
pip install playwright
```

Install the required browser binaries:

```bash
playwright install
```

If the project uses a `requirements.txt` file, install the project dependencies first:

```bash
pip install -r requirements.txt
playwright install
```

## 4. Install GitHub Copilot in PyCharm

1. Open **Settings > Plugins**.
2. Search for **GitHub Copilot**.
3. Install the plugin.
4. Restart PyCharm when prompted.
5. Sign in with your GitHub account.
6. Confirm that your GitHub Copilot plan is active.
7. Open Copilot Chat and verify that it is available in the IDE.

GitHub Copilot acts as the AI client that communicates with the tools exposed through MCP.

## 5. Enable the PyCharm MCP Server

1. Open **Settings** with `Ctrl+Alt+S`.
2. Select **Tools > MCP Server**.
3. Enable the MCP Server.
4. Review the available clients in the **Clients** section.
5. Locate the GitHub Copilot client available in your environment.
6. Select **Auto-Configure** or **Configure**, depending on the option displayed.
7. Apply and save the changes.

After the MCP Server is enabled and Copilot is configured as a client, the agent can use the approved IDE and project tools available through the connection.

> The client names and configuration options can vary depending on the installed PyCharm and GitHub Copilot versions. Use the options shown in your PyCharm MCP Server settings.

## 6. Create the Agent Instruction File

Create a Markdown file in the project, for example:

```text
ai-mentor.md
```

Add instructions that clearly define how the agent should work.

```markdown
# Playwright Test Generation Instructions

1. Use the available Playwright MCP tools to explore and validate the scenario before writing code.
2. Use resilient and readable locators, preferably role, label, or test-ID based locators.
3. Generate Python tests that follow the existing project structure and conventions.
4. Use pytest as the test runner.
5. Add meaningful assertions for the expected behavior.
6. Run the generated tests.
7. If a test fails, analyze the failure, correct the implementation, and rerun it.
8. Do not change the original test requirements.
9. Close the MCP browser when the task is finished, including when a browser step fails.
10. Do not expose or add passwords, tokens, client secrets, or other credentials to the source code.
```

## 7. Generate a Playwright Test with the Agent

Open Copilot Chat in PyCharm and use an agent-capable mode when available.

Add `ai-mentor.md` to the chat context and enter a prompt such as:

```text
Generate a Python Playwright test for the following scenario.

First use the available Playwright MCP tools to explore and verify the steps. Then create the test code following the instructions in mcp_instructions.md.

Scenario:
1. Navigate to https://practicesoftwaretesting.com.
2. Find a product marked as Out of Stock.
3. Open the product details page.
4. Assert that the increase and decrease quantity buttons are disabled.
5. Use resilient Playwright locators and web-first assertions.
6. Run the test and correct any failures before finishing.
```

During execution, the agent may request permission before running commands or using tools. Review each requested action before approving it.

## 8. Run and Validate the Generated Test

After the agent creates the test, run it manually from the PyCharm terminal:

To see printed output:

```bash
pytest -v -s
```

To run a specific file:

```bash
pytest tests/test_out_of_stock_product.py -v
```

Check that:

- The test follows the requested scenario.
- The locators are reliable and readable.
- The assertions validate the intended behavior.
- Browser and context resources are closed correctly.
- The test passes consistently.

## Additional GitHub Copilot and MCP Use Cases

### Context-Aware Debugging

Ask Copilot to analyze a failing test and explain the cause.

```text
Analyze this failing Playwright test. Explain the root cause, correct the implementation, and rerun the test.
```

You can also use the available fix action or `/fix` command when supported by the installed Copilot version.

### Project Analysis and Scaffolding

Ask the agent to inspect an existing file and create a new component that follows the same conventions.

```text
Analyze HomePageModel.py and create SettingsPageModel.py using the same structure, naming conventions, and locator strategy.
```

### Code Explanation and Documentation

Select a block of code and ask Copilot to explain it.

```text
Explain this code step by step for a beginner and identify any Playwright best-practice issues.
```

You can also use the available explanation action or `/explain` command when supported.

### Command Execution

The agent can help with project commands such as installing packages, running tests, applying formatting, or running a linter.

Example:

```text
Install the radon package and run a code-complexity analysis on the project source directory. Summarize the results without changing the source code.
```

Always review commands before approving them, especially commands that install software or modify files.

### Version Control Support

Copilot can help summarize local changes and prepare a commit-message suggestion.

```text
Review the current Git changes, summarize them, and suggest a concise commit message. Do not commit or push anything.
```

## Safety and Review Guidelines

- Review all generated code before accepting it.
- Review every requested command or tool action before approval.
- Do not share passwords, tokens, client secrets, or confidential data in prompts.
- Do not allow the agent to commit, push, delete, or overwrite files unless that action is explicitly required and has been reviewed.
- Run generated tests manually before treating the result as complete.
- Confirm that browser sessions are closed after execution.
- Keep generated code aligned with the repository's established structure and conventions.

### Option 2 — Claude Code (CLI)

1. Open a terminal in the project root and run:
   ```bash
   claude --agent ai-mentor
   ```
2. Choose **mode A** (Review) or **mode D** (All of the above)
3. Share the generated `REVIEW_REPORT_YYYY-MM-DD.md` with us

## 🎯 Training Exercises

The training is divided into a series of progressively advanced exercises located in the **`Exercises/`** folder. Each exercise focuses on a specific area of Playwright, pytest, and modern test automation practices.

Work through the exercises in order, as later topics build on concepts introduced in earlier modules.

---
# Part 1: Python Fundamentals

## Module 1: Syntax, Variables, and Data Types

Topics:

- Indentation and code blocks
- Comments
- Variable naming and `snake_case`
- `int`, `float`, `str`, `bool`, `list`, `tuple`, and `dict`
- Type casting with `int()`, `float()`, and `str()`
- Checking data types with `type()`

## Module 2: Operators and Control Flow

Topics:

- Arithmetic, comparison, and logical operators
- `if`, `elif`, and `else`
- `for` and `while` loops
- `break`, `continue`, and `pass`

## Module 3: Functions and Scope

Topics:

- Defining functions with `def`
- Parameters and return values
- Default and keyword arguments
- Local and global scope

## Module 4: Error Handling

Topics:

- `try`, `except`, and `finally`
- Handling invalid input
- Handling division by zero
- Providing meaningful error messages

## Python Exercises

1. **Prime Number Checker**: Create a function that checks whether a number is prime.
2. **Simple Calculator**: Create functions for addition, subtraction, multiplication, and division.
3. **Even Numbers Loop**: Print all even numbers from 1 to 100.
4. **Bonus Exercise**: Solve the even-number task using a list comprehension.

---

# Part 1: Playwright UI Testing

## Module 1: Opening a Website

Learn how to start Playwright, launch Chromium, open a page, navigate, and read page information.

**Exercise:** Open [The Internet Test Site](https://the-internet.herokuapp.com), then print its title and main header.

## Module 2: Browser and Page Fundamentals

Learn the difference between:

- **Browser**: The browser application, such as Chromium, Firefox, or WebKit
- **Browser Context**: An isolated session with separate cookies and storage
- **Page**: A browser tab inside a context

**Exercise:** Open the Add/Remove Elements page, add two elements, and print the number of Delete buttons.

## Module 3: Locators and Element Interaction

Locator strategies include:

- CSS selectors
- XPath
- Text locators
- `get_by_role()`
- `get_by_label()`
- Test IDs
- Playwright Codegen

Prefer semantic and readable locators where possible.

**Exercise:** Automate a successful login on [The Internet Login Page](https://the-internet.herokuapp.com/login) using different locator types.

## Module 4: Waits and Synchronization

Topics:

- Page load states
- Element states
- Text and attribute changes
- Navigation
- Loaders and spinners
- Playwright web-first assertions

Avoid fixed delays when Playwright can wait for a meaningful state.

## Module 5: Assertions

Covered assertions include title, URL, text, attributes, CSS classes, visibility, enabled state, negative assertions, and checkbox state.

**Exercise:** Complete the login flow and validate the title, URL, success message, Logout button, and page visibility.

## Module 6: Error Handling in UI Tests

Investigate and fix failures caused by incorrect locators, missing waits, timeouts, navigation during actions, and incorrect assertions.

**Exercise:** Run the failing examples, fix them one by one, and add one custom failure scenario.

## Module 7: Page Object Model

- Page objects contain locators and reusable UI actions.
- Tests contain scenarios and validations.
- Reusable behavior is implemented only once.

**Exercise:** Add an `assert_login_failed()` method to the login page object and create a negative-login test that uses the page object.

## Module 8: Reports and Screenshots

Generate an HTML report:

```bash
pytest --html=report.html --self-contained-html
```

Capture a screenshot:

```python
page.screenshot(path="screenshots/failure.png", full_page=True)
```

**Exercise:** Trigger an intentional login failure, capture the failure state, print the error, and close the browser in a `finally` block.

---

# Part 2: Playwright API Testing

The API exercises use the [Swagger Petstore](https://petstore.swagger.io/).

## API Fundamentals

An API request contains a method, endpoint, headers, parameters, and optionally a body. A response contains a status code, headers, and a response body. Playwright provides `APIRequestContext` for sending HTTP requests.

## Module 1: GET Requests

Learn how to create an `APIRequestContext`, send GET requests, pass parameters and headers, read the status, and process JSON responses.

**Exercises:**

1. Find how many pets have the status `sold`.
2. Check whether the pet with ID `1` is sold.
3. Add relevant assertions.
4. Print the IDs of all sold pets.

## Module 2: POST Requests

Learn how to create a request body as a Python dictionary, send JSON data, set headers, and read the returned resource ID.

**Exercise:** Create a pet, store its returned ID, retrieve it with GET, and investigate empty or missing request bodies.

## Module 3: PUT Requests

Learn how to update an existing resource and compare the update body with the creation body.

**Exercise:** Update the pet created earlier and verify the updated data with GET.

## Module 4: Unsuccessful Requests

Learn how to test nonexistent resources, assert error status codes, inspect `content-type`, read non-JSON bodies, and compare documented with actual behavior.

**Exercise:** Create negative tests for nonexistent pet IDs, unsupported status values, and updates using nonexistent IDs.

## Module 5: DELETE Requests

Learn how to add an API-key header, include the resource ID in the URL, delete a resource, and verify that it is no longer available.

**Exercise:** Delete the pet created earlier and verify the expected not-found response.

## Module 6: Refactoring API Tests

Avoid repeating the base URL:

```python
BASE_URL = "https://petstore.swagger.io/v2/"
request_context = playwright.request.new_context(base_url=BASE_URL)
response = request_context.get("pet/findByStatus")
```

Keep the trailing slash in the base URL and use relative request paths consistently.

**Exercise:** Move the base URL into `constants.py`, update the GET tests, rerun them, and compare behavior with the Petstore v3 base URL.

---

## 📁 Project Structure

```text
Beginner-Playwright-Training/
├── .github/
│   ├── agents/
│   │   └── ai-mentor.md
│   └── workflows/
│       └── playwright.yml
├── Exercises/
│   ├── APITesting01_GetRequest.md
│   ├── APITesting02_Assertions.md
│   ├── APITesting03_PostRequest.md
│   ├── APITesting04_PutRequest.md
│   ├── APITesting05_UnsuccessfulRequests.md
│   ├── APITesting06_DeleteRequest.md
│   ├── APITesting07_Refactoring.md
│   ├── Module01_OpenWebsite.md
│   ├── Module02_BrowserPageFundementals.md
│   ├── Module03_Locators.md
│   ├── Module04_WaitAndSynchronization.md
│   ├── Module05_Assertions.md
│   ├── Module06_ErrorHandling.md
│   ├── Module07_LoginFlowWithPOM.md
│   ├── Module08_Reporting.md
│   └── Python_Exercises.md
├── src/
│   ├── conftest.py
│   ├── pages/
│   │   ├── __pycache__/
│   │   ├── constants.py
│   │   └── login_page.py
│   ├── tests/
│   │   ├── __pycache__/
│   │   ├── api_test_01_get_request.py
│   │   ├── api_test_02_assertions.py
│   │   ├── api_test_03_post_request.py
│   │   ├── api_test_04_put_request.py
│   │   ├── api_test_05_unsuccessful_requests.py
│   │   ├── api_test_06_delete_request.py
│   │   ├── api_test_07_refactoring.py
│   │   ├── python_exercises.py
│   │   ├── smoke_test.py
│   │   ├── test_01_openwebsite.py
│   │   ├── test_02_browser_page.py
│   │   ├── test_03_locators.py
│   │   ├── test_04_waits.py
│   │   ├── test_05_assertions.py
│   │   ├── test_06_error_handling.py
│   │   ├── test_07_login_pom.py
│   │   ├── test_08_reporting.py
│   │   └── test_python_exercises.py
│   └── __pycache__/
├── .gitignore
├── README.md
├── pytest.ini
├── requirements.txt
├── .venv/
├── .pytest_cache/
├── .idea/
└── .claude/
```

---

## 💡 Best Practices

- Page object code goes in `src/pages/` — locators and actions only
- Test code goes in `src/tests/` — test functions, no raw selectors
- Shared fixtures go in `src/conftest.py`
- Every test that creates API data **must clean it up** — use `try/finally`
- Use `uuid` to generate unique task titles — prevents cross-test interference
- Prefer `get_by_role`, `get_by_label`, `get_by_placeholder` over CSS selectors
- Use `expect()` for assertions — it retries automatically

---

## 🔧 Configuration

```bash
pytest --browser=firefox --headed --slowmo=500   # custom browser run
pytest -n 4                                       # parallel
pytest -m fast                                    # fast tests only
pytest --alluredir=allure-results                 # with Allure
```

---

## 📚 Dependencies

- Playwright 1.44+  ·  pytest 8+  ·  pytest-playwright 0.5+
- pytest-xdist 3.5+  ·  pytest-shard 0.1.2+  ·  allure-pytest 2.13+

---

## 🤝 Contributing

This is a training project. Feel free to add test cases, improve page objects, or share your learnings.

---

## 📖 Resources

The resources below are aligned with the actual exercises in the `Exercises/` folder and are intended to support each stage of the training.

### Python Fundamentals

- [Python Official Tutorial](https://docs.python.org/3/tutorial/)
- [Python Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Python Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Pytest Documentation](https://docs.pytest.org/en/stable/)

### Python exercises (`Exercises/Python_Exercises.md`)

- [Python Basics](https://docs.python.org/3/tutorial/introduction.html)
- [Control Flow](https://docs.python.org/3/tutorial/controlflow.html)
- [Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Lists and Loops](https://docs.python.org/3/tutorial/introduction.html#lists)

### UI exercises

#### Module 01 — Open Website (`Exercises/Module01_OpenWebsite.md`) & Module 02 — Browser Page Fundamentals (`Exercises/Module02_BrowserPageFundementals.md`)

- [Playwright with Python and Pytest (Playlist)](https://www.youtube.com/watch?v=XSHERugHQCY)

#### Module 03 — Locators (`Exercises/Module03_Locators.md`)

- [Locators](https://www.youtube.com/watch?v=MXFAHvcqh7I)

#### Module 04 — Waits and Synchronization (`Exercises/Module04_WaitAndSynchronization.md`)

- [Auto-waiting, Timeouts, Assertions, Codagen](https://www.youtube.com/watch?v=drW3w7ESaJo)

#### Module 05 — Assertions (`Exercises/Module05_Assertions.md`)

- [Playwright Assertions](https://www.youtube.com/watch?v=hYNOFle3zic)

#### Module 06 — Error Handling (`Exercises/Module06_ErrorHandling.md`)

- [Debugging tests](https://playwright.dev/python/docs/debug)
- [Trace viewer](https://playwright.dev/python/docs/trace-viewer)
- [Playwright troubleshooting](https://playwright.dev/python/docs/troubleshooting)

#### Module 07 — Login Flow with POM (`Exercises/Module07_LoginFlowWithPOM.md`)

- [Page Object Model in Playwright](https://playwright.dev/python/docs/pom)
- [Reusable page objects](https://playwright.dev/python/docs/test-pom)
- [Login flow examples](https://playwright.dev/python/docs/test-auth)

#### Module 08 — Reporting (`Exercises/Module08_Reporting.md`)

- [HTML report](https://playwright.dev/python/docs/test-reporters)
- [Screenshots and videos](https://playwright.dev/python/docs/screenshots)
- [Allure integration](https://allurereport.org/docs/playwright/)

### API exercises

#### API Testing foundations (`Exercises/APITesting01_GetRequest.md`, `Exercises/APITesting02_Assertions.md`)

- [API Test](https://www.youtube.com/watch?v=22xbuLgAzZY)
- [APIRequestContext](https://playwright.dev/python/docs/api/class-apirequestcontext)
- [Swagger Petstore API](https://petstore.swagger.io/)

#### API CRUD exercises (`Exercises/APITesting03_PostRequest.md`, `Exercises/APITesting04_PutRequest.md`, `Exercises/APITesting06_DeleteRequest.md`)

- [HTTP Methods overview](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)
- [REST API basics](https://restfulapi.net/)
- [JSON and HTTP requests](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON)

#### Negative and refactoring exercises (`Exercises/APITesting05_UnsuccessfulRequests.md`, `Exercises/APITesting07_Refactoring.md`)

- [Playwright API error handling](https://playwright.dev/python/docs/api-testing#making-requests)
- [Test refactoring patterns](https://playwright.dev/python/docs/test-fixtures)
- [Pytest fixtures](https://docs.pytest.org/en/stable/explanation/fixtures.html)

### Suggested learning order

1. Complete the Python exercises first.
2. Move through the UI modules in order from Module 01 to Module 08.
3. Finish with the API modules from GET to DELETE and refactoring.
4. Use the official Playwright and Python docs whenever a concept feels unclear.

---

# UI Testing — Browser & Page

## Point 1 — Browser Context Management

### Video
- [Playwright with Python and Pytest (Playlist)](https://www.youtube.com/watch?v=XSHERugHQCY)

---

## Point 2 — Network Interception

### Videos
- [Network Interception Video 1](https://www.youtube.com/watch?v=egqzRXOc7cU)
- [Network Interception Video 2](https://www.youtube.com/watch?v=qjqAe8qe0kY)

---

# UI Testing — Locators & Interactions

## Point 3 — Advanced Locator Strategies

### Video
- [Advanced Locator Strategies](https://www.youtube.com/watch?v=MXFAHvcqh7I)

### Additional Material
For the advanced parts:
- `filter()`
- `nth()`
- `first`
- `last`
- Dynamic loops
- Board-column scoping

Use:

```text
6-Playwright_MOD3_MOD4.pptx
```

---

## Point 4 — Performance and Tracing

### Videos
- [Performance and Tracing Video 1](https://www.youtube.com/watch?v=LrOXygsYnnk)
- [Performance and Tracing Video 2](https://www.youtube.com/watch?v=Zu_qzwH8zSs)
- [Performance and Tracing Video 3](https://www.youtube.com/watch?v=HNGPAjk_BCI)

### Documentation
- [HAR Replay and Analysis](https://ray.run/videos/148-network-replay-har-playwright-tutorial-part-79)

---

# UI Testing — Test Quality

## Point 5 — Visual Testing

### Videos
- [Visual Testing Video 1](https://www.youtube.com/watch?v=O5AyMSxfFbg)
- [Visual Testing Video 2](https://www.youtube.com/watch?v=LrOXygsYnnk)

---

## Point 6 — Advanced POM Patterns

### Videos
- [Advanced POM Patterns Video 1](https://www.youtube.com/watch?v=h-fpoNZdWCg)
- [Advanced POM Patterns Video 2](https://www.youtube.com/watch?v=AGYZk9ZlA4s&list=PLP5_A7hnY1Tj4pbbDY29wPdEgWu65uiWL)
- [Advanced POM Patterns Video 3](https://www.youtube.com/watch?v=lDK7UKWC0ak)
- [Advanced POM Patterns Video 4](https://www.youtube.com/watch?v=k488kAtT-Pw)

### Documentation
- [Reusable Components with Playwright Page Objects](https://python.plainenglish.io/enhancing-the-page-object-pattern-with-reusable-components-in-playwright-python-5a6d4481de30)

---

# Advanced Test Design

## Point 7 — Fixtures and Test Lifecycle

### Video
- [Fixtures and Test Lifecycle](https://www.youtube.com/watch?v=N_rCdPoltWo)

### Documentation
- [Playwright Test Runners](https://playwright.dev/python/docs/test-runners)
- [Pytest Fixtures Documentation](https://docs.pytest.org/en/stable/reference/fixtures.html)

---

## Point 8 — Parallel Execution and Sharding

### Videos
- [Parallel Execution Video 1](https://www.youtube.com/watch?v=TSWXTqjMDkI)
- [Parallel Execution Video 2](https://www.youtube.com/watch?v=tBnfDaPAH44)

### Documentation
- [pytest-xdist Documentation](https://pytest-xdist.readthedocs.io/en/stable/how-to.html)

---

## Point 9 — Allure Reporting

### Video
- [Allure Reporting](https://www.youtube.com/watch?v=VHwl78QXF_0)

### Documentation
- [Allure Official Documentation](https://allurereport.org/docs/playwright/)
- [Allure Attachments and Trace Guide](https://qaskills.sh/blog/playwright-allure-attachment-trace-guide)
- [BrowserStack Guide: Allure Integration](https://www.browserstack.com/guide/integrate-allure-with-playwright)
- [Playwright Python Allure Example Project](https://github.com/nirtal85/Playwright-Python-Example)

---

# API Testing

## Point 10 — API Authentication

### Playlists & Videos
- [API Authentication Playlist 1](https://www.youtube.com/playlist?list=PLHT5rv7PEE4Oa19_17xS4I5Rbn297WJkt)
- [API Authentication Playlist 2](https://www.youtube.com/playlist?list=PLhW3qG5bs-L8WcAa9cfXaqGe0-Cq85y4X)
- [Playwright API Fundamentals](https://www.youtube.com/watch?v=XSHERugHQCY)

---

## Point 11 — Advanced Response Validation

### Documentation
- [Playwright API Testing Documentation](https://playwright.dev/python/docs/api-testing)
- [Pagination, Filtering and Sorting Validation](https://medium.com/@gunashekarr11/handling-pagination-filtering-sorting-validations-through-the-playwright-api-layer-612f010f0943)

### Video
- [Advanced API Validation](https://www.youtube.com/watch?v=qyCPtbEztvw)

---

## Point 12 — API Fixtures and Test Data

Already covered in previous videos regarding:

- Fixtures
- API Testing
- Parallel Execution

### Video
- [API Fixtures and Test Data](https://www.youtube.com/watch?v=HPP_62VJQ3g)

---

## Point 13 — Chained Workflows and Hybrid Tests

### Video
- [Hybrid UI + API Testing](https://www.youtube.com/watch?v=dv95_b8F8qM)

### Documentation
- [Playwright API Testing Documentation](https://playwright.dev/python/docs/api-testing)
- [Using Playwright for API and UI Testing Together](https://dev.to/ramamallika_kadali_49a08f/day-7-how-i-use-playwright-for-api-and-ui-testing-together-lh)

---

## Point 14 — Multi-User and Role-Based Testing

### Documentation
- [Testing Multiple Users and Roles with Playwright](https://playwrightqa.blogspot.com/2024/10/testing-multiple-users-and-roles-with.html)
- [Multi-User Testing with Playwright Fixtures](https://medium.com/@edtang44/isolate-and-conquer-multi-user-testing-with-playwright-fixtures-f211ad438974)
- [Handling Authentication for Multiple Users](https://www.neovasolutions.com/2024/11/14/handling-authentication-for-multiple-user-logins-in-playwright/)

### Videos
- [Multi-User Testing Video 1](https://www.youtube.com/watch?v=XSHERugHQCY)
- [Multi-User Testing Video 2](https://www.youtube.com/watch?v=o-R1PTJ5Lws)
- [Multi-User Testing Video 3](https://www.youtube.com/watch?v=0mfLHPLZ7_k)

---

## Point 15 — Resilience and Edge Cases

### Videos
- [Resilience and Edge Cases Video 1](https://www.youtube.com/watch?v=NSDdeDYr3dY)
- [Resilience and Edge Cases Video 2](https://www.youtube.com/watch?v=axBr9gnITOo)

---

## 📝 License

This project is created for educational purposes.
