from behave import step

from features.pages.login_page import LoginPage


@step("I open login page")
def step_impl(context):
    context.driver.get("https://www.instagram.com/accounts/login/")


@step('I type "{username}" in username field')
def step_impl(context, username):
    login_page = LoginPage(context.driver)
    login_page.enter_usermane(username)


@step('I type "{password}" in password field')
def step_impl(context, password):
    login_page = LoginPage(context.driver)
    login_page.enter_password(password)


@step("I click login button")
def step_impl(context):
    login_page = LoginPage(context.driver)
    login_page.click_login()


@step("I log in")
def step_impl(context):
    login_page = LoginPage(context.driver)
    login_page.enter_usermane(context.config.get("user", "username"))
    login_page.enter_password(context.config.get("user", "password"))
    login_page.click_login()


@then("I see validation message for")
def step_impl(context):
    login_page = LoginPage(context.driver)
    for row in context.table:
        login_page.enter_usermane(row["username"])
        login_page.enter_password(row["password"])
        login_page.click_login()
        context.execute_steps('''
        When I see element with text "Sorry, your password was incorrect. Please double-check your password."
        ''')
