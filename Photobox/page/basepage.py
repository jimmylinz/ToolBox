from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    email_ed = (MobileBy.ID, "email_ed")  # 输入邮箱

    def __init__(self,driver:WebDriver = None):
        self._driver = driver

    #find_element方法封装
    def find(self,locator):
        return self._driver.find_element(*locator)

    #find_elements方法封装
    def finds(self,locator):
        return self._driver.find_elements(*locator)

    #find_android_uiautomator方法封装
    def find_by_scroll(self,text):
        return self._driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,f'new UiScrollable(new UiSelector().scrollable(true).instance(0))\
                                                                            .scrollIntoView(new UiSelector()\
                                                                            .textContains("{text}").instance(0));')

    #显示等待封装
    def webdriverwait_until(self,text,timeout):
        return WebDriverWait(self._driver,15).until(lambda x: x.find_element(MobileBy.XPATH,f"//*[@text='{text}']"))

    #click方法封装
    def find_and_click(self,locator):
        self.find(locator).click()

    #sendkey方法封装
    def find_and_send(self,locator,text):
        self.find(locator).send_keys(text)

    #toast获取方法封装
    def get_toast(self):
        return self._driver.find_element(MobileBy.XPATH,"//*[@class = 'android.widget.Toast']").text

    #back封装
    def back(self,num=1):
        for i in range(num):
            self._driver.back()

    #清空输入邮箱信息
    def del_emile(self):
        return self.find_and_send(self.email_ed,"")

#滑动封装
    #左滑
    def swipe_right(self):
        x = self._driver.get_window_size()['width']
        y = self._driver.get_window_size()['height']
        self._driver.swipe(x * 6 / 7, y * 1 / 2, x * 1 / 7, y * 1 / 2, 500)
    #右滑
    def swipe_left(self):
        x = self._driver.get_window_size()['width']
        y = self._driver.get_window_size()['height']
        self._driver.swipe(x * 1 / 7, y * 1 / 2, x * 6 / 7, y * 1 / 2, 500)
    #上滑
    def swipe_up(self):
        x = self._driver.get_window_size()['width']
        y = self._driver.get_window_size()['height']
        self._driver.swipe(x * 1 / 2, y * 4 / 5, x * 1 / 2, y * 2 / 5, 500)
    #下滑
    def swipe_down(self):
        x = self._driver.get_window_size()['width']
        y = self._driver.get_window_size()['height']
        self._driver.swipe(x * 1 / 2, y * 1 / 7, x * 1 / 2, y * 6 / 7, 500)