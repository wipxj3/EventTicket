Feature: Login to website
    Scenario: Access login form page
        Given I access the login url
        Then I see an input for username
    Scenario: Leave password input empty
        Given I access the login url
        When I dont fill the password input
        And I submit the form
        Then I get password empty error message
    