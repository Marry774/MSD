@web @alza
Feature: Alza Web Browsing
  As a web tester,
  I want to check if alza basket works fine

  # The "@" annotations are tags
  # One feature can have multiple scenarios
  # The lines immediately after the feature title are just comments

  Scenario: Basic Alza basket test
    Given go to alza homepage
    When go to category Notebooky
    When order category by Od nejdražšího
    When add first 2 items in list
    Then there should be 2 items in basket

  Scenario: CountDown
    Given number 1000 by user to countdown
