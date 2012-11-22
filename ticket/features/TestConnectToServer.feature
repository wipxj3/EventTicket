Feature: Testing connection to server
    In order to connect to server
    As a eager client
    I want to attend events
    
    Scenario: Connect
        Given the ip address of server "0.0.0.0"
        And the port number "8000"
        When I connect to server
        Then I get "Connection established"
