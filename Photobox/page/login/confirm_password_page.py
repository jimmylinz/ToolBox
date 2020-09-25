from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from Photobox.page.login.set_emile_Page import SetemilePage
from Photobox.page.basepage import BasePage

#确认设置的密码页面
class ConfirmpasswordPage(BasePage):
    number_0 = (MobileBy.ID, "number_0")  # 按钮0
    number_1 = (MobileBy.ID, "number_1")  # 按钮10
    number_ok = (MobileBy.ID, "number_ok")  # 按钮ok

    def confirm_password(self):
        for i in range(4):
            self.find_and_click(self.number_0)
        self.find_and_click(self.number_ok)
        return SetemilePage(self._driver)

    # 设置密码00000
    def confirm_similar_password(self):
        for i in range(5):
            self.find_and_click(self.number_0)
        self.find_and_click(self.number_ok)
        toasttext = self.get_toast()
        return toasttext

    # 设置密码0001
    def confirm_confirm_password(self):
        for i in range(3):
            self.find_and_click(self.number_0)
        self.find_and_click(self.number_1)
        self.find_and_click(self.number_ok)
        toasttext = self.get_toast()
        return toasttext

    # 设置密码000
    def confirm_short_password(self):
        for i in range(3):
            self.find_and_click(self.number_0)
        self.find_and_click(self.number_ok)
        toasttext = self.get_toast()
        return toasttext