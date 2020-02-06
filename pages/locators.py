from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, ".login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, ".register_form")
    REGISTER_MAIL = (By.CSS_SELECTOR, 'input[name="registration-email"]')
    PASSWORD1 = (By.CSS_SELECTOR, 'input[name="registration-password1"]')
    PASSWORD2 = (By.CSS_SELECTOR, 'input[name="registration-password2"]')
    REGISTER_BTN = (By.CSS_SELECTOR, 'button[name="registration_submit"]')

class ProductPageLocators:
    ADDTO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ITEM_ON_PRODUCT_PAGE = (By.CSS_SELECTOR, ".product_main h1")
    ITEM_IN_BASKET = (By.CSS_SELECTOR, ".alert-success:nth-child(1) strong")
    COST_ON_PRODUCT_PAGE = (By.CSS_SELECTOR, ".product_main .price_color")
    COST_IN_BASKET = (By.CSS_SELECTOR, ".alert-info strong")

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini [href]")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators:
    BASKET_NOT_EMPTY = (By.CSS_SELECTOR, ".basket_summary")
    BASKET_EMPTY_MESSAGE_EXIST = (By.CSS_SELECTOR, " #content_inner> p")





