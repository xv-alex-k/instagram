# Created by alexkardash at 12/15/18
Feature: Login
  Validate user can login witn valid username and password

  Background:
    Given I open login page

  Scenario: Valid login
    When I log in
    

  Scenario: Invalid login 1
    Then I see validation message for
      | username | password |
      | qwe      | qwqweee  |
      | reqwe    | rqwe     |
      | reqwe    | sdasd    |
    When I type " " in password field