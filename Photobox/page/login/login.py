
#登录页

from Photobox.page.login.authorization_page import AuthorizationPage
from Photobox.page.basepage import BasePage
from Photobox.page.login.input_password_page import InputPasswordPage


#输入密码登录APP
class LoginPage(BasePage):
    def goto_login_first(self):
        return AuthorizationPage(self._driver)

    def goto_login(self):
        return InputPasswordPage(self._driver)
'''
    def goto_login(self):
        number_0 = self._driver.find_element(MobileBy.ID,"number_0")
        if number_0 == None:
            return AuthorizationPage(self._driver)
        else:
            number_0.click()
            number_0.click()
            number_0.click()
            number_0.click()
        return MainPage(self._driver)
'''