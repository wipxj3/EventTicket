Feature: Logout from website
    Scenario: Logged in user logs out
        Given I am logged in
        When I access the logout url
        Then I dont see my profile block on the page
    