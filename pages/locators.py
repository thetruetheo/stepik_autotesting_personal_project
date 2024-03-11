from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CLASS_NAME, "login_form")
    REGISTER_FORM=(By.CLASS_NAME, "register_form")

class BookPageLocators():
    ADD_TO_BASKET_BUTTON=(By.CLASS_NAME, "btn-add-to-basket")
    BOOK_NAME=(By.XPATH, "//div/h1")
    ADDED_TO_BASKET_MESSAGE=(By.XPATH, "//div[@id='messages']/div/div/strong")
    BOOK_PRICE=(By.XPATH,"//p[@class='price_color']")
    BASKET_PRICE=(By.XPATH,"//div[@class='alertinner ']/p/strong")