# Created by alexkardash at 12/15/18
Feature: Login
  Validate user can login witn valid username and password

  Background:
    Given I open login page

  Scenario: Valid login
    When I log in
    When I click not now button
    When I type "fitness" in search field
    When I select search result with "#fitness" text
    When I see element with text "Top Posts"


  Scenario Outline: Invalid login using examples
    When I type "<username>" in username field
    When I type "<password>" in password field
    When I click element with text "Log in"
    When I see element with text "Sorry, your password was incorrect. Please double-check your password."

    Examples:
      | username | password |
      | qwe      | qwqweee  |
      | qwe      | rqwe     |
      | qwe      | sdasd    |


  Scenario: Invalid login using data table
    Then I see validation message for
      | username | password |
      | qwe      | qwqweee  |
      | qwe      | rqwe     |
      | qwe      | sdasd    |
    When I log in
