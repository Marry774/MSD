import logging
from pytest_bdd import scenario, given, parsers


@scenario('../features/countdown.feature', 'CountDown')
def test_countdown():
    """CountDown."""


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
