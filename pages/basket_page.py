from .main_page import MainPage
from .locators import BasketPageLocators


class BasketPage(MainPage):

    def should_be_basket_page(self):
        self.should_be_basket_url()
        self.basket_empty()
        self.basket_empty_message_exist()

    # реализуйте проверку на корректный url адрес
    def should_be_basket_url(self):
         assert 'basket' in self.browser.current_url, "'basket' is not in current url" #True

    # Ожидаем, что в корзине нет товаров
    def basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_NOT_EMPTY), "Basket not empty"

    # Ожидаем, что есть текст о том что корзина пуста
    def basket_empty_message_exist(self):
        assert self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_MESSAGE_EXIST), "Empty basket message not exist"




