import time

from .base_page import BasePage
from .locators import BookPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math
from selenium.webdriver.common.by import By

class BookPage(BasePage):
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*BookPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button is not found"

    def add_to_basker_button_click(self):
        button=self.browser.find_element(*BookPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def added_to_basket_message(self):
        book_name=self.browser.find_element()
        message=self.browser.find_element(*BookPageLocators.ADDED_TO_BASKET_MESSAGE)

        print("test")

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def book_name_comparison(self):
        book_name_main=self.browser.find_element(*BookPageLocators.BOOK_NAME).text
        book_name_message=self.browser.find_element(*BookPageLocators.ADDED_TO_BASKET_MESSAGE).text
        assert book_name_main == book_name_message, "The books are different"
        time.sleep(3)

    def book_price_comparison(self):
        book_price_main=self.browser.find_element(*BookPageLocators.BOOK_PRICE).text
        basket_price=self.browser.find_element(*BookPageLocators.BASKET_PRICE).text
        assert book_price_main==basket_price, "The prices are different"


    # def book_name_extraction(self):
    #
    #     book_name=self.browser.find_element(By.XPATH, "//div/h1").text
    #     print(book_name)
    #     print("\n")
    #     time.sleep(3)
    #     message_book_name=self.browser.find_element(By.XPATH, "//div[@id='messages']/div/div/strong").text
    #     print(message_book_name)
