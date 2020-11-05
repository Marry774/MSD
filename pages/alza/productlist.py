import logging
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductList:
    PRODUCTS_DIVS = (By.CSS_SELECTOR, '#boxes > div')
    SEARCH_INPUT = (By.ID, 'search_form_input')
    LOADER = (By.CSS_SELECTOR, 'body > span.circle-loader-container')


    @classmethod
    def TAB_MENU(cls, phrase):
        xpath = f"//div[@id='tabs']//*[contains(text(), '{phrase}')]"
        return (By.XPATH, xpath)

    def __init__(self, browser):
        self.browser = browser

    def products_count(self, phrase):
        phrase_results = self.browser.find_elements(*self.PRODUCTS_DIVS)
        return len(phrase_results)

    def check_ordered_by_price_desc(self):
        products = self.browser.find_elements(*self.PRODUCTS_DIVS)
        price = 99999999
        for i in products:
            try:
                pprice = i.find_element(By.CSS_SELECTOR, 'div.bottom > div.price > div > span.c2')
                pprice = pprice.text.replace("&nbsp;", "").replace(",-", "").replace(" ", "").strip()
                # logging.info("!!!!! > " + pprice)
                if price < int(pprice):
                    assert False, "Products not ordered DESC by price"
                else:
                    price = int(pprice)
            except NoSuchElementException as e:
                if i.get_attribute('class') != 'clear':
                    logging.info("!!!!!!!!!!! ALERT !!!!!!!!!!")
                    assert False, "NON IDENTIFIED PRODUCT BOX"
        logging.info("!!! Products ordered DESC by price")
        assert True, "Products ordered DESC by price"

    def reorder_by(self, phrase):
        self.browser.find_element(*self.TAB_MENU(phrase)).click()
        x = len(self.browser.find_elements(*self.LOADER))
        WebDriverWait(self.browser, 10).until_not(
            EC.visibility_of_element_located(self.LOADER))

    def add_item_by_position(self, i):
        WebDriverWait(self.browser, 10).until_not(
            EC.visibility_of_element_located(self.LOADER))
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="boxes"]/div[%s]/div[2]/div[1]/span/a[1]' % i))).click()
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="varABackButton"]/span[2]'))).click()
