import logging
import uuid
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Basket:
    URL = 'https://www.alza.cz'
    BASKET_BUTTON = (By.XPATH, '//*[@id="price"]')
    BASKET_NAVIGATION = (By.XPATH, '//*[@id="ordernav"]')

    def __init__(self, browser):
        self.browser = browser

    @classmethod
    def MENU_ITEM_BY_VALUE(cls, phrase):
        xpath = f"//ul[@id='tpf']//*[contains(text(), '{phrase}')]"
        return (By.XPATH, xpath)

    def go_to(self):
        self.browser.get(self.URL)
        self.browser.find_element(*self.BASKET_BUTTON).click()
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(self.BASKET_NAVIGATION))

    def check_items_count(self, count):
        screen = "report/%s_screenshot.png" % time.time()
        a = self.browser.save_screenshot(screen)
        logging.info('!!!! check_items_count SCREENSHOT :: <a href="./%s">link</a>' % screen)
        links = self.browser.find_elements_by_class_name('alzaico-f-cross')
        assert len(links) == int(count)


