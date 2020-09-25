from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from Photobox.page.basepage import BasePage
from Photobox.page.login.set_password_page import SetpasswordPage

#广告轮播图页面
class RotationchartPage(BasePage):
    nextstep = (MobileBy.XPATH, "//*[@text='下一步']")#下一步按钮

    def goto_register(self):
        for i in range(2):
            sleep(1)
            self.swipe_right()
        self.find_and_click(self.nextstep)
        return SetpasswordPage(self._driver)

'''
    def goto_register(self):
        nextstep = self._driver.find_element(MobileBy.XPATH,"//*[@text=''下一步]")
        while nextstep == None:
            x = self._driver.get_window_size()['width']
            y = self._driver.get_window_size()['height']
            self._driver.swipe(x*6/7,y*1/2,x*1/7,y*1/2,1)
        else:
            nextstep.click()
            return SetpasswordPage(self._driver)
'''