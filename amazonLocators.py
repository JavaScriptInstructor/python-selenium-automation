from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.target.com/')


#Amazon logo
#Email field
#Continue button
#Conditions of use link
#Privacy Notice link
#Need help link
#Forgot your password link
#Other issues with Sign-In link
#Create your Amazon account button


#Amazon logo
driver.find_element(By.XPath, value: "")
#email field
driver.find_element(By.ID, value: "ap_email_login"")
#Continue button
driver.find_element(by.XPATH, value: "//input[@class= 'a-button-input']")
#locator for 'Terms and Conditions'
driver.find_element(By.XPATH, value: "//a[contains(@href, 'signin_notification_condition_of_use')]")
#$x("//a[contains(@href, 'signin_notification_condition_of_use')]")
#Privacy Notice Link
driver.find_element(By.XPATH, value: "//a[contains(@href, 'signin_notification_privacy_notice')]")
#Need help
driver.find_element(By.XPATH, value: "//a[contains(@href, 'help/customer/account-issues')]")
#Forgot your password link
driver.find_element(By.ID, value: 'cu-select-firstNode')])"
#Forgot your password link (alternate?)
driver.find_element(By.XPATH, value: "//*[@placeholder= 'I forgot my password']")
#Other issues with Sign-In link-you get there by pressing Need Help
driver.find_element(By.XPATH, value: "//a[contains(@href, 'help/customer/account-issues')]")
#Other issues with Sign-In Link-
driver.find_element(By.XPATH, value: "//*[@placeholder= 'My password isn"t working']")
#Create your Amazon account button
driver.find_element(By.XPATH, value: "//a[contains(@href, 'ap/register?showRememberMe')]")