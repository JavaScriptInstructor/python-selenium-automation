from time import sleep
from selenium import webdriver
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test= 'cartless-title']")
TOTAL_TXT = (By. CSS_SELECTOR, "h2 [class*='styles_cart-summary-span']")
SEARCH_RESULTS_TEXT = (By.XPATH,"//div[contains(@class, 'styles_listingPageResultsCount')]")
ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*= 'addToCartButton']")
SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test= 'content-wrapper'] [id*= 'addToCart']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-tests= 'content-wrapper') h4")
TARGET_CIRCLE_RESULTS = (By.CSS_SELECTOR,"[data-test = 'storycardWrapperElement-div']")
COLOR_OPTIONS = (By.CSS_SELECTOR, "li[class*='CarouselItem'] img")
SELECTED_COLOR = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] div")

@given('Open Target main page')
def open_main(context):
    context.app.main_page.open_main_page()

@when('Open cart page')
def open_cart(context):
    context.driver.get('https://www.target.com/cart')


@then('Click on Add to Cart Button')
def click_add_to_cart(context):
   context.driver.find_element(*ADD_TO_CART_BTN).click()
   context.driver.wait.unti(
      EC.presence_of_element_located(SIDE_NAV_ADD_TO_CART_BTN),
      message='Side navigation add to cart Btn not clickable'
   )


@when('Confirm Add to cart button from side navigation')
def side_nav_click_add_to_cart(context):
    context.driver.find_element(*SIDE_NAV_ADD_TO_CART_BTN).click()


@then('Verify cart has {amount} item(s)')
def verify_cart_items(context, amount):
    context.driver.wait.until(
        EC.presence_of_element_located(TOTAL_TXT) ,
        message='Subtotal text did not appear'
)
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
    context.app.search_results_page.verify_search_results()

@then('Verify that every product has a name and an image')
def verify_products_name_img(context):
    products = context.driver.find_elements(*LISTINGS)  # [WebEl1, WebEl2, WebEl3, WebEl4]
    for product in products[:8]:
        title = product.find_element(*PRODUCT_TITLE).text
        assert title, 'Product title not shown'
        print(f'🟢{title}')
        product.find_element(*PRODUCT_IMG)

@given('Open Target Circle page')
def open_main(context):
    context.driver.get('https://www.target.com/circle')

@then('Confirm Two Storycard links are shown')
def verify_storycard_links_shown(context):
    context.driver.find_elements(*TARGET_CIRCLE_RESULTS)


@given('Open target product A-91269718 page')
def open_target(context):
    context.driver.get(f'https://www.target.com/p/wranglers-men-39-s-relaxed-fit-straight-jeans/-/A-91269718?preselect=90919011#lnk=sametab')
    sleep(5)


@then('Verify user can click through colors')
def click_and_verify_colors(context):
    expected_colors = ['Navy Denim', 'Dark Wash', 'Light Wash']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)  # [webelement1, webelement2, webelement3]
    print(colors)

    for c in colors:
        c.click()
        # for visibility only:
        sleep(0.5)

        selected_color = context.driver.find_element(*SELECTED_COLOR).text  # 'Color\nBlack'
        print('Current color', selected_color)

        selected_color = selected_color.split('\n')[1]  # remove 'Color\n' part, keep Black'
        actual_colors.append(selected_color)
        print(actual_colors)

    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'