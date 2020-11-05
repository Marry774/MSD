#!/bin/bash -x

#brew cask install chromedriver

## Install
  # BDD  TESTING PLUGINS
    pip3 install pytest pytest_bdd pytest-logger pytest-dependency
    pip3 install pytest-xdist pytest-html
    pip3 install python-dateutil
    pip3 install allure-pytest-bdd
    pip3 install pyslack mandrill redis pytest-selenium
#    pip3 uninstall allure-pytest
#    pip3 install allure-pytest
    # DATABASE DRIVERS
    pip3 install psycopg2-binary
    # TODO: https://pypi.org/project/psycopg2/

#    brew install geckodriver
#    pip3 install
#        pytest-airflow
#        pytest-selenium
#        pytest-slack
#        pytest-ok
#        pytest-assertutil
#        pytest-redmine
#        pytest-django
#        pytest-jira
#   ??? allure-pytest-bdd
