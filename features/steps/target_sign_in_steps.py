from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then

#Don't need this page. I included all functions on the target search_steps page to run Target_sign_in.feature

#@given('Open Target main page')
#def open_main(context):
   # context.driver.get('https://www.target.com/')

#@when('Click on Account')
#def click_account(context):
 #   context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/AccountLink']").click()

#@when('Click on sign in')
#def click_sign_in(context):
#    context.driver.find_element(By.CSS_SELECTOR,'[class*="styles_ndsBaseButton__4Gp2_ styles_md__Lvk4a styles_fullWidth__gA46D"]')

#@then('Verify sign in form')
#def verify_sign_in_form(context):
 #   actual_text = context.driver.find_element(By.CSS_SELECTOR, "[class *='styles_ndsHeading__phw6r styles_fontSize1__OL7f3 styles_x2Margin__ZKMpf']")
 #   assert 'Sign in form' in actual_text, f"Expected 'Sign in or create account' text"