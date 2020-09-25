from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException

from Photobox.page.basepage import BasePage

#选择隐藏文件页面

from Photobox.page.main.select_folder_page import SelectFolderPage


class SelectFilePage(BasePage):
    _file_mag = (MobileBy.XPATH,"//*[@text='文件管理器']")#文件管理器
    _share_file = "$MuMu共享文件夹"
    _select_file = (MobileBy.XPATH,"//*[contains(@resource-id,'navigation_view_item_size')]/../..[@clickable='true']")#选择可点击文件

    #main选择文件跳转
    def select_file(self):
        try:
            self.find_and_click(self._file_mag)
            self.find_by_scroll(self._share_file).click()
            self.find(self._select_file)
        except NoSuchElementException:
            print("没有隐藏文件")
        else:
            self.find_and_click(self._select_file)
            return SelectFolderPage(self._driver)

    #photodetails选择文件跳转
    def pd_select_file(self):
        try:
            self.find_and_click(self._file_mag)
            self.find_by_scroll(self._share_file).click()
            self.find(self._select_file)
        except NoSuchElementException:
            print("没有隐藏文件")
        else:
            self.find_and_click(self._select_file)
            from Photobox.page.main.PhotoDetails.photo_details_page import PhotoDetailsPage
            return PhotoDetailsPage(self._driver)