Feature: Register on website
    Scenario: All fields are valid
        Given I access the url "/register/"
        When email is "a@a.com"
        And password is "qwerty"
        And confirm password is "qwerty"
        Then I am redirected to "/"
    Scenario: Email is not valid
        Given I access the url "/register/"
        When email is "a"
        And password is "qwerty"
        And confirm password is "qwerty"
        Then I get error message "Invalid email"