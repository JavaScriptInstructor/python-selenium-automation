from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys
from time import sleep




#@given('Open Target main page')
#def open_main(context):
#    context.driver.get('https://www.target.com/')

@when('Click on cart icon')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartIcon']").click()


@when('Search for {product}')
def search_product(context, product):
    context.app.header.search(product)

#@then('Search results for {expected_product} are shown')
#def verify_search_results(context, expected_product):
#    actual_text = context.driver.find_element(*SEARCH_RESULTS_TEXT).text
#    assert expected_product in actual_text, f'Expected text {expected_product} not in actual text {actual_text}'

@then('Empty Cart message is shown')
def verify_empty_cart_msg(context):
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "[data-test= 'boxEmpty']")
    assert 'Your cart is empty' in actual_text, f"Expected 'Your cart is empty' text"


@when('Click on Account')
def click_account(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/AccountLink']").click()

@when('Click on sign in')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR,'[class*="styles_ndsBaseButton__4Gp2_ styles_md__Lvk4a styles_fullWidth__gA46D"]')

@then('Verify sign in form')
def verify_sign_in_form(context):
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "[class *='styles_ndsHeading__phw6r styles_fontSize1__OL7f3 styles_x2Margin__ZKMpf']")
    assert 'Sign in form' in actual_text, f"Expected 'Sign in or create account' text"