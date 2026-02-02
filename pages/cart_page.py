from selenium.webdriver.common.by import By

from pages.base_page import Page


class CartPage(Page):
    EMPTY_ACRT_MSG = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")
    empty_cart_msg = 'Your cart is empty'

    def open_cart_page(self):
        self.open_url('/cart')

    def verify_empty_cart_msg(self):
        self.verify_partial_text(self.empty_cart_msg, *self.EMPTY_ACRT_MSG)