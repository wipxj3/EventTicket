Feature: Testing connection to server
    In order to connect to server
    As a eager client
    I want to attend events
    
    Scenario: Connect to default django's address
        Given the ip address of server "0.0.0.0"
        And the port number "8000"
        When I connect to server
        Then I get "Connection established"
        
    Scenario: Connect to localhost
        Given the ip address of server "localhost"
        And the port number "80"
        When I connect to server
        Then I get "Connection established"
