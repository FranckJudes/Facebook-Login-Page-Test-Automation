Feature: Facebook Login Page

  # Successful login with valid credentials
  Scenario: Successful login with valid credentials
    Given The user is on the Facebook login page
    When The user enters "email@gmail.com" in the email field
    And The user enters "Password." in the password field
    And The user clicks the "Login" button
    Then The user should be redirected to the page web.facebook.com/two_step_verification

  # Failed login with invalid password
  Scenario: Failed login with invalid password
    Given The user is on the Facebook login page
    When The user enters "hngallagher@gmail.com" in the email field
    And The user enters "opppssssssp" in the password field
    And The user clicks the "Login" button
    Then The user should be redirected to the page web.facebook.com/two_step_verification

  # Username scenarios
  Scenario: Failed login with a nonexistent username
    Given The user is on the Facebook login page
    When The user enters "enail" in the email field
    And The user enters "56poyb" in the password field
    And The user clicks the "Login" button
    Then The user should be redirected to the page web.facebook.com/two_step_verification

  Scenario: Failed login with an empty username
    Given The user is on the Facebook login page
    When  The user enters "CorrectPassword123" in the password field
    And The user clicks the "Login" button
    Then An error message The password you’ve entered is incorrect. should be displayed

  # Password scenarios
  Scenario: Failed login with an empty password
    Given The user is on the Facebook login page
    When The user enters "valid_user@gmail.com" in the email field
    And The user clicks the "Login" button
    Then An error message The email you entered isn’t connected to an account. Find your account and log in. should be displayed

  Scenario: Failed login with a password containing special characters
    Given The user is on the Facebook login page
    When The user enters "valid_user@gmail.com" in the email field
    And The user enters "P@$$w0rd!" in the password field
    And The user clicks the "Login" button
    Then An error message The email you entered isn’t connected to an account. Find your account and log in. should be displayed

  Scenario: Failed login with a password that is too short
    Given The user is on the Facebook login page
    When The user enters "valid_user@gmail.com" in the email field
    And The user enters "123" in the password field
    And The user clicks the "Login" button
    Then An error message The email you entered isn’t connected to an account. Find your account and log in. should be displayed

  Scenario: Failed login with a password that is too long
    Given The user is on the Facebook login page
    When The user enters "valid_user@gmail.com" in the email field
    And The user enters "ThisIsAVeryLongPasswordThatExceedsLimits12345" in the password field
    And The user clicks the "Login" button
    Then An error message The email you entered isn’t connected to an account. Find your account and log in. should be displayed
