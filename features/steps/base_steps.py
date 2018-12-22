from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from behave import when


@when('I click element with text "{text}"')
def step_impl(context, text):
    WebDriverWait(context.driver, 10).until(ec.element_to_be_clickable((By.XPATH, "//*[text() = '{}']".format(text))))


@when('I see element with text "{text}"')
def step_impl(context, text):
    WebDriverWait(context.driver, 10).until(ec.text_to_be_present_in_element((By.TAG_NAME, "body"), text))