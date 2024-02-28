import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')  


@given('I am on the login page')
def step_given_i_am_on_login_page(context):
    context.browser = webdriver.Chrome(options=chrome_options)
    context.browser.get('http://192.168.1.192:3000/')

@when('I enter the email "{email}"')
def step_when_enter_email(context, email):
    email_input = context.browser.find_element(by=By.XPATH, value='//*[@id="sign-in-email-input"]')
    email_input.send_keys(email)
    time.sleep(2)

@when('I enter the password "{password}"')
def step_when_enter_password(context, password):
    password_input = context.browser.find_element(by=By.XPATH, value='//*[@id="sign-in-password-input"]')
    password_input.send_keys(password)
    time.sleep(2)
@when('I click the login button')
def step_when_click_login_button(context):
    login_button = context.browser.find_element("id","sign-in-button")
    login_button.click()
    time.sleep(6)
@then('I should be logged in successfully')
def step_then_logged_in_successfully(context):
    dashboardGraph=context.browser.find_element(by=By.XPATH, value='//*[@id="root"]/div[2]/div[1]/div[2]/div/div[2]/div/div/div[2]/canvas')
    assert dashboardGraph.is_displayed(), "the element is displayed. User may be logged in successfully."

@then('I should  get an error message')
def I_should_get_an_error_message(context):
    errorMessage=context.browser.find_element(by=By.XPATH, value='//*[@id="error-alert"]/div')
    assert errorMessage.is_displayed(), " error the element is not displayed."

@then('I can t click the button')
def I_can_t_click_the_button(context):
    login_button=context.browser.find_element("id","sign-in-button")
    assert not login_button.is_enabled(), "the element is clickable"


@then('I close the browser')
def step_then_close_browser(context):
    context.browser.quit()
