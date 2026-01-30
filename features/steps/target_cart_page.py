from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test= 'cartless-title']")
TOTAL_TXT = (By. CSS_SELECTOR, "h2 [class*='styles_cart-summary-span']")
SEARCH_RESULTS_TEXT = (By.XPATH,"//div[contains(@class, 'styles_listingPageResultsCount')]")
ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*= 'addToCartButton']")
SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test= 'content-wrapper'] [id*= 'addToCart']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-tests= 'content-wrapper') h4")
TARGET_CIRCLE_RESULTS = (By.CSS_SELECTOR,"[data-test = 'storycardWrapperElement-div']")

when('Open cart page')
def open_cart(context):
    context.driver.get('https://www.target.com/cart')
    sleep(4)

#def click_add_tocart(context):
 #   context.driver.find_element(*ADD_TO_CART_BTN).click()
#    sleep(3)

@when('Confirm Add to cart button from side navigation')
def side_nav_click_add_to_cart(context):
    context.driver.find_element(*SIDE_NAV_ADD_TO_CART_BTN).click()

@then('Verify cart has {amount} item(s)')
def verify_cart_items(context, amount):
    cart_summary = context.driver.find_element(*TOTAL_TXT).text
    assert f'{amount} item' in cart_summary, f"Expected {amount} item but got {cart_summary}"

@then('Verify product in cart is correct')
def verify_product(context):
    product_in_cart = context.driver.find_element(*PRODUCT_NAME).text
    # print('\nProduct in cart:')
    # print(product_in_cart)
    expected = context.product_before_adding
    assert product_in_cart[:20] == expected[:20],\
        f'Expected product {expected[:20]} but got {product_in_cart[:20]}'

#@then('Search results for {product_expected} are shown')
#def verify_search_results(context, product_expected):
#    actual_text = context.driver.find_element(*SEARCH_RESULTS_TEXT).text
#    assert product_expected in actual_text, f'Expected text {product_expected} not in {actual_text}'

@then('Search results for {expected_product} are shown')
def verify_search_results(context, expected_product):
    actual_text = context.driver.find_element(*SEARCH_RESULTS_TEXT).text
    assert expected_product in actual_text, f'Expected text {expected_product} not in actual text {actual_text}'

@given('Open Target Circle page')
def open_main(context):
    context.driver.get('https://www.target.com/circle')

@then('Confirm Two Storycard links are shown')
def verify_storycard_links_shown(context):
    context.driver.find_elements(*TARGET_CIRCLE_RESULTS)