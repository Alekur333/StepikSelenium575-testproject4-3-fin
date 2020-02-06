from pages.basket_page import BasketPage
from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.login_page import LoginPage
import time
import pytest

link_base = "http://selenium1py.pythonanywhere.com/"
link_item = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

@pytest.mark.reg_checks
class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    @pytest.mark.reg
    def setup(self, browser):

        # открыть страницу регистрации
        link = link_base
        page = MainPage(browser, link)
        page.open()  # открываем страницу
        page.go_to_login_page()  # выполняем метод страницы - переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url)

        # зарегистрировать нового пользователя
        email = str(time.time()) + "@fakemail.org"
        password = "11111fakemail11111"
        login_page.register_new_user(email, password)

        # проверить, что пользователь залогинен
        login_page.should_be_authorized_user()

    @pytest.mark.fall
    @pytest.mark.product_to_basket
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):

        # 1. Открываем страницу товара
        link = link_item
        page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        product_page = ProductPage(browser, browser.current_url)

        # 2. Нажимаем на кнопку "Добавить в корзину"
        product_page.should_be_basket_btn()
        product_page.add_product_to_basket()

        # 3. Посчитать результат математического выражения и ввести ответ
        product_page.solve_quiz_and_get_code()

        # 4. Сообщение о том, что товар добавлен в корзину. Название товара в
        # сообщении должно совпадать с тем товаром, который вы действительно добавили.
        product_page.should_be_item_in_basket_message()
        product_page.itembasket_equal_itemproduct()

        # 5. Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара.
        product_page.should_be_cost_of_basket_message()
        product_page.costbasket_equal_costproduct()

    @pytest.mark.checks
    def test_user_cant_see_success_message(self, browser):

        # Открываем страницу товара
        link = link_item
        page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        product_page = ProductPage(browser, browser.current_url)

        # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
        product_page.should_not_be_success_message1()

@pytest.mark.fall
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):

    # 1. Открываем страницу товара
    link = link_item
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    product_page = ProductPage(browser, browser.current_url)

    # 2. Нажимаем на кнопку "Добавить в корзину"
    product_page.should_be_basket_btn()
    product_page.add_product_to_basket()

    # 3. Посчитать результат математического выражения и ввести ответ
    product_page.solve_quiz_and_get_code()

    # 4. Сообщение о том, что товар добавлен в корзину. Название товара в
    # сообщении должно совпадать с тем товаром, который вы действительно добавили.
    product_page.should_be_item_in_basket_message()
    product_page.itembasket_equal_itemproduct()

    # 5. Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара.
    product_page.should_be_cost_of_basket_message()
    product_page.costbasket_equal_costproduct()

@pytest.mark.checks
@pytest.mark.xfail(reason="it would be fail")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):

    # 1. Открываем страницу товара
    link = link_item
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    product_page = ProductPage(browser, browser.current_url)

    # 2. Нажимаем на кнопку "Добавить в корзину"
    product_page.should_be_basket_btn()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()

    # 3. Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    product_page.should_not_be_success_message1()


@pytest.mark.checks
@pytest.mark.xfail(reason="it would be fail")
def test_message_disappeared_after_adding_product_to_basket(browser):

    # 1. Открываем страницу товара
    link = link_item
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    product_page = ProductPage(browser, browser.current_url)

    # 2. Нажимаем на кнопку "Добавить в корзину"
    product_page.should_be_basket_btn()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()

    # 3. Проверяем, что нет сообщения об успехе с помощью is_disappeared
    product_page.should_not_be_success_message2()

@pytest.mark.login_checks
def test_guest_should_see_login_link_on_product_page(browser):

    link = link_item
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):

    link = link_item
    page = ProductPage(browser, link)
    page.open()
    page.basket_see()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_page()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):

    link = link_item
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

