from behave import when, then


@when("I click element with text "{}"")
def step_impl -> object:
    element = (By.XPATH, "//*[]" ()