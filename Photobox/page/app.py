from appium import webdriver

from Photobox.page.basepage import BasePage
from Photobox.page.login.login import LoginPage

#APP配置页
class App(BasePage):
    def start(self):
        if self._driver == None:
            caps = {}
            caps['platformName'] = 'android'
            # caps['deviceName'] = '55CDU16C07017103'
            caps['deviceName'] = '127.0.0.1:7555'
            caps['appPackage'] = 'com.cx.hiphoto'
            # com.cxab.magicbox / com.cxab.magicbox_sdk.ui.activity.HomeActivity小隐
            caps['appActivity'] = '.ZPYinCangAlias'
            caps['noReset'] = True
            caps['skipDeviceInitialization'] = True
            caps['resetKeyboard'] = 'true'
            caps['unicodeKeyboard'] = 'true'
            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        else:
            self._driver.launch_app()
        self._driver.implicitly_wait(10)
        return self

    def close(self):
        self._driver.quit()

    def restart(self):
        pass

    def login(self):
        return LoginPage(self._driver)