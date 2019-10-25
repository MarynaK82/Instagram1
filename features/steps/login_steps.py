@given("open login page")

class LoginPage(BasePage):


@when('I type "{password}" in password field')
def step_impl()
    login_page = LoginPage(context.driver)