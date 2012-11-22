Feature: Send email reminder about booked event
    Scenario: Send email about an upcoming booked event
        Given I am a registered user
        And I have a booked non-expired event
        And no previous reminder was sent
        When there are 3 days left till the event date
        Then I receive an email reminder

    Scenario: Send feedback email about expired event
        Given I am a registered user
        And I have an expired event
        And no previous feedback reminder was sent
        When 1 day has passed after event
        Then I receive a feedback email reminder