# Created by alexkardash at 12/15/18
Feature: Login
  Validate user can login witn valid username and password

  Background:
    Given I open login page

  Scenario: Valid login
    When I log in

  Scenario Outline: Invalid login
    When I type "<username>" in username field
    When I type "<password>" in password field
    When I click element with text "Log in"
    When I see element with text "Sorry, your password was incorrect. Please double-check your password."

    Examples:
      | username | password |
      | qwe      | qwqweee  |
      | reqwe    | rqwe     |
      | reqwerwq | sdasd    |


  Scenario: Invalid login 1
    Then I see validation message for
      | username | password |
      | qwe      | qwqweee  |
      | reqwe    | rqwe     |
      | reqwe    | sdasd    |
    When I type " " in password field