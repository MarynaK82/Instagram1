# Created by marynakaminska at 10/23/19
Feature: login
  Check user login to Instagram
  # Enter feature description here

  Scenario: Valid login
    Given open login page
    When I type "pyautomation" in username field
    When I type "erweew" in password field
    When I click login button

  Scenario: Invalid login
    Given I log in


  Scenario: Valid login
    Given open login page
    When I click element with text ""
    When I see element with text ""

