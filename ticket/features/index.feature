Feature: Rocking with lettuce and django
    Scenario: Simple Hello World
        Given I access the url "/admin"
        Then I see the header "Django administration"