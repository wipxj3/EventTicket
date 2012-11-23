Feature: Add even
    Scenario: Add event button
        Given I am logged in "/"
        Then I see button "Add Event"

    Scenario: Press add event button
        Given I am logged in "/"
        When I press "Add Event"
        Then I see new event form

