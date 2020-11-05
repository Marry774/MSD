import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Homepage:
    URL = 'https://www.alza.cz'
    SEARCH_INPUT = (By.ID, 'edtSearch')
    MENU = (By.ID, 'tpf')
    ITEMS_LIST_MENU = (By.ID, 'tabsc')

    def __init__(self, browser):
        self.browser = browser

    @classmethod
    def MENU_ITEM_BY_VALUE(cls, phrase):
        xpath = f"//ul[@id='tpf']//*[contains(text(), '{phrase}')]"
        return (By.XPATH, xpath)

    def load(self):
        self.browser.get(self.URL)

    def search(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.RETURN)

    def go_to_category(self, category):
        # menu_items = self.browser.find_elements(*self.MENU)
        # litp18842920 > div > a
        self.browser.find_element(*self.MENU_ITEM_BY_VALUE(category)).click()
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(self.ITEMS_LIST_MENU)).click()
