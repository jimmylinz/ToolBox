from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from Photobox.page.basepage import BasePage
from Photobox.page.main.main_page import MainPage

#恢复数据输入密码页面
class ReviceryPage(BasePage):
    number_0 = (MobileBy.ID,"number_0")#按钮0
    recovery_confirm = (MobileBy.ID, "recovery_confirm")#继续按钮

    def revicery_password(self):
        for i in range(4):
            sleep(1)
            self.find_and_click(self.number_0)
        self.find_and_click(self.recovery_confirm)
        return MainPage(self._driver)