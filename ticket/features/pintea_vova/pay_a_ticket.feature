Feature: Pay a ticket
    Scenario: Press buy ticket button
        Given I am logged in
        When I press pay ticket
        Then I receive the ticket

    Scenario: Pay button active
        Given I filled all required form fields
        Then Pay button becomes active