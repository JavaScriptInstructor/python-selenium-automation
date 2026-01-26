Feature: Test Scenarios for cart

  Scenario: User can see Empty Cart message
    Given Open Target main page
    When Click on cart icon
    Then Empty Cart message is shown
