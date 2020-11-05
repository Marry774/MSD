import logging
from time import sleep

import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver

# Constants
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.alza.basket import Basket
from pages.alza.homepage import Homepage

# Scenarios
from pages.alza.productlist import ProductList

scenarios('../features/websearch.feature')


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        # always add url to report
        extra.append(pytest_html.extras.url('http://www.example.com/'))
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            extra.append(pytest_html.extras.html('<div>Additional HTML</div>'))
        report.extra = extra


# Fixtures
@pytest.fixture
def browser():
    b = webdriver.Chrome("./chromedriver")
    b.implicitly_wait(10)
    b.maximize_window()
    yield b
    b.quit()


# Given Steps
@given(parsers.parse('number {count} by user to countdown'))
def countdown(count):
    for i in range(int(count)+1):
        ii = int(count)-i
        five = (ii % 5 == 0)
        three = (ii % 3 == 0)
        if five and three and int(count) != i:
            logging.info("%s - Testing" % ii)
        elif five and int(count) != i:
            logging.info("%s - Agile" % ii)
        elif three and int(count) != i:
            logging.info("%s - Software" % ii)
        else:
            logging.info("%s" % ii)


# Given Steps
@given('go to alza homepage')
def alza_go_home(browser):
    homepage = Homepage(browser)
    homepage.load()


# When Steps
@when(parsers.parse('go to category {category}'))
def go_to_category(browser, category):
    homepage = Homepage(browser)
    homepage.go_to_category(category)


@when(parsers.parse('order category by {phrase}'))
def order_category(browser, phrase):
    productlist = ProductList(browser)
    productlist.reorder_by(phrase)
    if phrase == "Od nejdražšího":
        productlist.check_ordered_by_price_desc()


@when(parsers.parse('add first {count} items in list'))
def add_to_basket(browser, count):
    productlist = ProductList(browser)
    for i in range(1, int(count)+1):
        productlist.add_item_by_position(i)


# Then Steps
@then(parsers.parse('there should be {count} items in basket'))
def check_basket(browser, count):
    # go to basket

    basket = Basket(browser)
    basket.go_to()
    basket.check_items_count(count)
