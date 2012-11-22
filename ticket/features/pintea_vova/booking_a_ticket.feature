Feature: Booking a ticket
    Scenario: Access form fields
        Given I am logged in
        When I select event type
        Then I see event form

    Scenario: Select event type
        Given I am logged in
        Then I can select event type