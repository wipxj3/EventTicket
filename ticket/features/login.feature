Feature: Login to website
    Scenario: Access login form page
        Given I access the url "/login/"
        Then I see the input with id "id_username"
    
    Scenario: Submit form with no password
        Given I access the url "/login/"
        When I dont fill field "id_password"
        And I submit the form "login-submit"
        Then I am redirected to "/"