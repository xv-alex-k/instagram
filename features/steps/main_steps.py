from behave import step

from features.pages.main_page import MainPage


@step("I click not now button")
def step_impl(context):
    main_page = MainPage(context.driver)
    main_page.click_not_now_button()


@step('I type "{query}" in search field')
def step_impl(context, query):
    main_page = MainPage(context.driver)
    main_page.type_in_search_field(query)


@step('I select search result with "{text}" text')
def step_impl(context, text):
    main_page = MainPage(context.driver)
    main_page.click_result_with_text(text)
