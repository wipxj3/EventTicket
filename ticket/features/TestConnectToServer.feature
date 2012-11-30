Feature: Testing connection to server
    In order to connect to server
    As a eager client
    I want to attend events
    
    Scenario: Connect to default django's address
        Given the ip address of server
        And the port number
        When I connect to server
        Then I get "Connection established"
        
    Scenario: Connect to localhost
        Given the ip address of the localhost
        And the port number
        When I connect to server
        Then I get "Connection established"
