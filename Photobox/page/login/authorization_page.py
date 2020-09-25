from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException

from Photobox.page.login.Rotation_chart_Page import RotationchartPage
from Photobox.page.basepage import BasePage

#初次登录授权页面
from Photobox.page.login.revicery_page import ReviceryPage


class AuthorizationPage(BasePage):
    per_btn = (MobileBy.ID, "permissions_btn")#申请授权按钮
    per_allow_btn = (MobileBy.ID, "com.android.packageinstaller:id/permission_allow_button")#授权确认按钮
    confirm = (MobileBy.ID, "dialog_confirm")
    calcel = (MobileBy.ID, "dialog_cancel")

    #没有提示恢复删除
    def goto_authorization(self):
        self.find_and_click(self.per_btn)
        self.find_and_click(self.per_allow_btn)
        return RotationchartPage(self._driver)

    # 恢复数据方法
    def goto_authorization_revocery(self):
        try:
            self.find_and_click(self.per_btn)
            self.find_and_click(self.per_allow_btn)
            self.find(self.confirm).click()
        except NoSuchElementException:
            return RotationchartPage(self._driver)
            # print("没找到恢复按钮")
        else:
            return ReviceryPage(self._driver)

    #删除数据方法
    def goto_authorization_delete(self):
        try:
            self.find_and_click(self.per_btn)
            self.find_and_click(self.per_allow_btn)
            self.find(self.calcel).click()
        except NoSuchElementException:
            return RotationchartPage(self._driver)
            # print("没找到删除按钮")
        else:
            return RotationchartPage(self._driver)

'''
    # 恢复数据方法
    def goto_authorization_delete(self):
        self.find_and_click(self.per_btn)
        self.find_and_click(self.per_allow_btn)
        delete = self.find(self.confirm)
        # if delete != None:
        #     delete.click()
        #     return ReviceryPage(self._driver)
        # else:
        #     return RotationchartPage(self._driver)
            # print("没找到恢复按钮")

'''


