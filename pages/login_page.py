from .main_page import MainPage
from .locators import LoginPageLocators
import time


class LoginPage(MainPage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
         assert 'login' in self.browser.current_url, "'login' is not in current url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Login form is not presented"


    def register_new_user(self, email, password):
        print(email)
        print(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_MAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.PASSWORD2).send_keys(password)
        time.sleep(1)
        self.browser.find_element(*LoginPageLocators.REGISTER_BTN).click()



