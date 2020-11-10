#!/usr/bin/env bash
#python3 prepare.sh

# run all tests
#pytest

#pytest -n 1 -v -m selective test_some.py --cucumberjson=./output.json --gherkin-terminal-reporter

rm report/*

#pytest -s -vvv step_defs/test_alza.py --alluredir=./allure_report
pytest -n 1 -s -vvv --cucumberjson=report/cucumber.json --html=report/report.html --self-contained-html --gherkin-terminal-reporter -m web
#allure serve ./allure_report
