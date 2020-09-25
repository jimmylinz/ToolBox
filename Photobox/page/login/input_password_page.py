from appium.webdriver.common.mobileby import MobileBy

from Photobox.page.basepage import BasePage

from Photobox.page.main.main_page import MainPage


#正常登录页面
class InputPasswordPage(BasePage):
    number_0 = (MobileBy.ID, "number_0")  # 按钮0
    number_ok = (MobileBy.ID, "number_ok")  # 按钮ok

    def input_password(self):
        for i in range(4):
            self.find_and_click(self.number_0)
        return MainPage(self._driver)