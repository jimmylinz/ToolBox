from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from Photobox.page.basepage import BasePage
from Photobox.page.login.confirm_password_page import ConfirmpasswordPage

#设置登录密码页面
class SetpasswordPage(BasePage):


    number_0 = (MobileBy.ID,"number_0")#按钮0
    number_1 = (MobileBy.ID, "number_1")  # 按钮10
    number_ok = (MobileBy.ID, "number_ok")#按钮ok

    # 设置密码0000
    def set_password(self):
        for i in range(4):
            self.find_and_click(self.number_0)
        self.find_and_click(self.number_ok)
        return ConfirmpasswordPage(self._driver)

    # 设置密码000
    def set_short_password(self):
        for i in range(3):
            self.find_and_click(self.number_0)
        self.find_and_click(self.number_ok)
        toasttext = self.get_toast()
        return toasttext




