from .pages.book_page import BookPage
import time

# def test_should_be_add_to_basket_button(browser):
#     link="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#     page=BookPage(browser,link)
#     page.open()
#     page.should_be_add_to_basket_button()

# def test_add_to_basket_button_click(browser):
#     link="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#     page=BookPage(browser,link)
#     page.open()
#     page.add_to_basker_button_click()
#     page.solve_quiz_and_get_code()
#




def test_text_extraction(browser,link):

    page = BookPage(browser, link)
    page.open()
    page.add_to_basker_button_click()
    page.solve_quiz_and_get_code()
    time.sleep(3)
    page.book_name_comparison()
    page.book_price_comparison()

