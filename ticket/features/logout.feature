Feature: Logout from website
    Scenario: Logged in user logs out
        Given I access the url "/logout/"
        When I am logged in
        Then I am redirected to "/"
    Scenario: Guest logs out
        Given I access the url "/logout/"
        When I am not logged in
        Then I get the message "Logout error"