Feature: Testing QR code authencity
    In order to assure ticket validation
    As the terminal
    I check if the hash of the code is in DB
    
    Scenario: Valid ticket
        Given a QR.PNG file with the encoded code
        When I decode the QR code from PNG
        And lookup the hash in the database
        Then I get "Valid Ticket"
        
    Scenario: Invalid ticket
        Given a QR.PNG file with the encoded code
        When I decode the QR code from PNG
        And lookup the hash in the database
        Then I get "Invalid Ticket"
