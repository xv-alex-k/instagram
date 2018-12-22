from behave import when

from features.pages.main_page import MainPage


@when("I click not now button")
def step_impl(context):
    main_page = MainPage(context.driver)
    main_page.click_not_now_button()

