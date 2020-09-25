from appium.webdriver.common.mobileby import MobileBy

from Photobox.page.basepage import BasePage
from Photobox.page.main.main_page import MainPage

#设置邮箱页面
class SetemilePage(BasePage):
    email_ed = (MobileBy.ID,"email_ed")#输入邮箱
    email_btn = (MobileBy.ID,"email_btn")#邮箱提交按钮
    dia_confirm = (MobileBy.ID, "dialog_confirm")#QQ提交确认按钮
    qq_confirm = (MobileBy.ID, "dialog_qq_ed")  # QQ输入框
    no_emile = (MobileBy.ID, "no_email")#没有邮箱按钮


    #输入设置邮箱
    def set_emile(self,emile):
        self.find_and_send(self.email_ed,emile)
        self.find_and_click(self.email_btn)
        return MainPage(self._driver)

    # 输入错误邮箱
    def set_error_emile(self, bad_format):
        self.find_and_send(self.email_ed, bad_format)
        self.find_and_click(self.email_btn)
        toasttext = self.get_toast()
        return toasttext

    #输入QQ邮箱
    def set_emile_not(self,qq):
        self.find_and_click(self.no_emile)
        self.find_and_send(self.qq_confirm,qq)
        self.find_and_click(self.dia_confirm)
        self.find_and_click(self.email_btn)
        return MainPage(self._driver)
