Feature: Testing camera QR code capturing
    In order to scan the ticket(QR code)
    As the terminal
    I check if the error correction is small enough
    
    Scenario: Valid image sample
        Given camera device is connected
        When the snapshot is taken
        And the error correction is performed
        Then I get "Sample approved"
        
    Scenario: Invalid image sample
        Given camera device is connected
        When the snapshot is taken
        And the error correction is performed
        Then I get "Sample rejected. Try Again..."
