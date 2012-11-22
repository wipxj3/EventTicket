Feature: Send an email reminder about hot event
    Scenario: Send email about upcoming most liked events in user region
        Given I am a registered user
        And no previous reminder was sent in the last 2 weeks
        When I wait for 2 weeks
        Then I receive an email reminder with the most liked events

    Scenario: Send email about upcoming, most booked events in user region
        Given I am a registered user
        And no previous reminder was sent in the last 2 weeks
        When I wait for 2 weeks
        Then I receive an email reminder with the most booked events