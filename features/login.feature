Feature: Login Scenarios

@test1
Scenario: Log in with valid credentials
  Given I am on the login page
  When I enter the email "hamza.ramy.ing@gmail.com"
  And I enter the password "Aziz@123"
  And I click the login button
  Then I should be logged in successfully

@test2
Scenario Outline: Log in with  invalid credentials
  Given I am on the login page
  When I enter the email "<email>"
  And I enter the password "<password>"
  And I click the login button
  Then I should  get an error message

  Examples:
    | email                      | password   |
    | hamza.ramy@gmail.com       | jhztuzheuh |
    | hamza.ramy.ing@gmail.com   | azjnaiujr  |

@test3

Scenario Outline: Log in with  invalid format 
    Given I am on the login page
    When I enter the email "<email>"
    And I enter the password "<password>"
    Then I can t click the button 

    Examples:
      | email                      | password   |
      | hamza.ramy.gmail.com       | jhztuzheuh |
      | hamza.ramy.ing@gmail.com   | aa  |
