Feature: Register on website
    Scenario: All fields are valid
        Given I access the register url
        When I enter a valid email
        And I enter a valid password
        And I manage to confirm the password
        And I submit the form
        Then I get register success message
    Scenario: Email is not valid
        Given I access the register url
        When I enter an invalid email
        And I enter a valid password
        And I manage to confirm the password
        And I submit the form
        Then I get register error message