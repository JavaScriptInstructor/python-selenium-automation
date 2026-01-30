Feature: Test Scenarios for cart

  Scenario: User can see Empty Cart message
    Given Open Target main page
    When Click on cart icon
    Then Empty Cart message is shown

 Scenario Outline: User can search for a product
    Given Open Target main page
    When Search for <product>
    Then Search results for <product_result> are shown
    Examples:
    |product  |product_result   |
    |book      |book            |
    |cup      |cup              |
    |coffee   |coffee           |

  Scenario: User can add a product to cart
    Given Open Target main page
    When Search for mug
    And Click on Add to Cart button
    And Confirm Add to Cart button
    And Confirm Add to Cart button from side navigation
    And Open cart page
    Then Verify cart has 1 item(s)

    Scenario: User can see Empty Cart message
    Given Open Target main page
    When Click on cart icon
    Then Empty Cart message is shown

  Scenario: User can see Storycard
    Given Open Target Circle page
    Then Confirm Two Storycard links are shown