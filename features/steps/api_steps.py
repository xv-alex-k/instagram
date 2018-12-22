import api
from behave import when


@when('I send get with "{url}" and "{params}" headers')
def step_impl(context, url, params):
    api.send_get(url, params)


@when('I send post with "{url}" and "{params}" headers')
def step_impl(context, url, params):
    api.send_get(url, params)
