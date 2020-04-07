from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()
    
# реализуйте проверку на корректный url адрес
    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'wrong login page url'

# реализуйте проверку, что есть форма логина
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            'no login form found'

# реализуйте проверку, что есть форма регистрации на странице
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            'no register form found'
