Feature: Possibility to un-subscribe from emails
    Scenario: User wants to un-subscribe from all emails
        Given I am a registered user
        And I access the url "/email-unsubscribe"
        And I press the un-subscribe button
        Then I add the user to the un-subscribers list
        And I redirect him to the homepage

    Scenario: User wants to un-subscribe from certain emails
        Given I am a registered user
        And I access the url "/email-unsubscribe/select"
        And I check some checkboxes
        And I press the un-subscribe button
        Then I add the user to the un-subscribers list with the specified options
        And I redirect him to the homepage