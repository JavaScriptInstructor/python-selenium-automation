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

sleep(5)

#click the account button
#driver.find_element(By.ID,'account-sign-in').click()
driver.find_element(By.ID, 'account-sign-in').click()

#click sign in button
driver.find_element(by.XPATH,"//button[@class='styles_ndsBaseButton__4Gp2_ styles_md__Lvk4a styles_fullWidth__gA46D styles_ndsButton__XOOOH styles_md__Yc3tr styles_filled___MOAP']")
#driver.find_element(//*[@id="headerPrimary"]/div[7]/div/div/button

#verify sign in or create account is shown
expected_text = 'sign in or create account'
actual_text = driver.find_element(By.XPATH, "//div[contains(@class, 'h-margin-t-x2')]")

#verify sign in button
driver.find_element(By.XPATH, "//button(@class= 'styles_ndsBaseButton__4Gp2_ styles_lg__jONdz styles_fullWidth__gA46D styles_ndsButton__XOOOH styles_lg__T5sAi styles_filled___MOAP')]")