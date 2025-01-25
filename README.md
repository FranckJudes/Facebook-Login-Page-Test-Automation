# Facebook Login Page Test Automation  Behave for behavior-driven development (BDD) 

## Description
This project is an automated testing suite for the Facebook login page. It uses **Behave** for behavior-driven development (BDD) and **Selenium** for browser automation. The tests cover various scenarios for logging into Facebook, including successful login, failed login due to invalid credentials, and edge cases such as empty fields or overly long passwords.

## Project Structure

```
.
|-- features/
|   |-- steps/
|   |   |-- facebook_steps.py    # Step definitions for login scenarios
|   |-- facebook.feature  # Feature file defining test scenarios
|-- reports/                   # Directory for test reports and screenshots
|-- README.md                  # Project documentation
|-- requirements.txt           # Python dependencies
```

## Prerequisites

1. **Python 3.x**: Ensure Python is installed on your system.
2. **Google Chrome**: The Chrome browser must be installed.
3. **ChromeDriver**: Ensure you have the correct version of ChromeDriver for your Chrome browser.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/FranckJudes/Facebook-Login-Page-Test-Automation.git
   cd Facebook-Login-Page-Test-Automation
   ```

2. Install dependencies:
   ```bash
   pip install behave
   ```

3. Add the path to ChromeDriver to your system's PATH or provide its location in the `facebook_steps.py` file.

## Running the Tests

1. **Execute All Tests**:
   ```bash
   behave
   ```

2. **Run a Specific Feature**:
   ```bash
   behave features/facebook_login.feature
   ```

3. **Run a Specific Scenario**:
   Use the `--name` flag with the scenario name:
   ```bash
   behave --name "Successful login with valid credentials"
   ```

## Features and Scenarios

### Feature: Facebook Login Page

#### Scenarios:

1. **Successful Login**:
   - Valid email and password.
   - Expected result: User is redirected to the homepage.

2. **Failed Login with Invalid Password**:
   - Valid email but incorrect password.
   - Expected result: Redirected to a verification page.

3. **Failed Login with Nonexistent Username**:
   - Invalid email.
   - Expected result: Redirected to a verification page.

4. **Edge Cases**:
   - Empty username or password.
   - Passwords with special characters, too short, or too long.
   - Expected result: Appropriate error messages are displayed.

## Implementation Details

### Step Definitions

- **`login_steps.py`**:
  Contains the implementation of Gherkin steps such as navigating to the login page, entering credentials, and verifying outcomes.

### Error Handling

- Screenshots are captured for failed scenarios and stored in the `reports/screenshots` directory for debugging.
- Error messages are dynamically verified using Selenium's `WebDriverWait`.

### Profiling and Optimizations

- **Timeouts**: WebDriver waits (explicit waits) are used for dynamic element loading.
- **Error Assertions**: Validates the presence and content of error messages to ensure robust test coverage.

## Reporting

1. **Console Logs**: Test results are printed in the console.
2. **Screenshots**: Stored in `reports/screenshots/` for failed scenarios.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes with clear messages.
4. Submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

For questions or support, please contact franckjudes87@gmail.com

