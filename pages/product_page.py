from .locators import ProductPageLocators
from .main_page import MainPage


class ProductPage(MainPage):

    def should_be_basket_btn(self):
        assert self.is_element_present(*ProductPageLocators.ADDTO_BASKET),  "Add to basket button is not presented"

    def add_product_to_basket(self):
        addto_basket = self.browser.find_element(*ProductPageLocators.ADDTO_BASKET)
        addto_basket.click()

    def should_be_item_in_basket_message(self):
        assert self.is_element_present(*ProductPageLocators.ITEM_IN_BASKET),  "No message about Item in basket"

    def itembasket_equal_itemproduct(self):
        itembasket = self.browser.find_element(*ProductPageLocators.ITEM_IN_BASKET).text
        print(itembasket)
        itemproduct = self.browser.find_element(*ProductPageLocators.ITEM_ON_PRODUCT_PAGE).text
        print(itemproduct)
        assert itembasket == itemproduct, "Item in basket not equal to item on product page"

    def should_be_cost_of_basket_message(self):
        assert self.is_element_present(*ProductPageLocators.COST_IN_BASKET), "No message about cost in basket"

    def costbasket_equal_costproduct(self):
        costbasket = self.browser.find_element(*ProductPageLocators.COST_IN_BASKET).text
        print(costbasket)
        costproduct = self.browser.find_element(*ProductPageLocators.COST_ON_PRODUCT_PAGE).text
        print(costproduct)
        assert costbasket == costproduct, "Cost in basket not equal to cost on product page"

    def should_not_be_success_message1(self):
        assert self.is_not_element_present(*ProductPageLocators.ITEM_IN_BASKET), \
            "Success message is presented"

    def should_not_be_success_message2(self):
        assert self.is_disappeared(*ProductPageLocators.ITEM_IN_BASKET), \
            "Success message is presented"

