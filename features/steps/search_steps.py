from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

#SEARCH_RESULTS_TEXT = (By.XPATH,"//div[contains(@class, 'styles_listingPageResultsCount')]")
#ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*= 'addToCartButton']")
#SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test= 'content-wrapper'] [id*= 'addToCart']")
#SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-tests= 'content-wrapper') h4")

#@when('Click on Add to Cart button')
#def click_add_tocart(context):
 #   context.driver.find_element(*ADD_TO_CART_BTN).click()
  #  sleep(3)

#@when('Confirm Add to cart button from side navigation')
#def side_nav_click_add_to_cart(context):
 #   context.driver.find_element(*SIDE_NAV_ADD_TO_CART_BTN).click()
  #  sleep(2)

#@then('Search results for {expected_product} are shown')
#def verify_search_results(context, expected_product):
 #   actual_text = context.driver.find_element(*SEARCH_RESULTS_TEXT).text
  #  assert expected_product in actual_text, f'Expected text {expected_product}' not in actual_text