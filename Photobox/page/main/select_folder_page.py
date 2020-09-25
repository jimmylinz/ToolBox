import random
from time import sleep

from appium.webdriver.common.mobileby import MobileBy


from Photobox.page.basepage import BasePage




#选择隐藏的文件夹
class SelectFolderPage(BasePage):
    _folder = (MobileBy.XPATH, "//*[contains(@resource-id,'item_target_folder_layout')]/.[@clickable='true']")  # 可用文件夹
    _add_folder = (MobileBy.ID, "add_folde")  # 新建文件夹
    _cr_folder = (MobileBy.ID, "dialog_qq_ed")  # 新建文件夹命名
    _confirm = (MobileBy.XPATH, "//*[@text='确认']")  # 确认按钮
    _finish = (MobileBy.ID, "dialog_finish")  # 完成按钮

    #选择文件夹，没有就创建文件夹
    def select_folder(self,foldername):

        folders = self.finds(self._folder)
        while len(folders) == 0:
            try:
                self.find_and_click(self._add_folder)
                self.find_and_send(self._cr_folder, foldername)
                self.find_and_click(self._confirm)
                if len(folders) > 0:
                    break
            except Exception as e:
                print("创建失败",e)
                break
        folder_C = random.choice(folders)
        folder_C.click()
        # self.find_and_click(self._finish)
        from Photobox.page.main.main_page import MainPage
        return MainPage(self._driver)

    #选择对应文件夹
    def select_afolder(self,foldertext):
        self.find_by_scroll(foldertext).click()
        # self.webdriverwait_until(self._driver,"完成")
        sleep(3)
        self.find_and_click(self._finish)
        from Photobox.page.main.main_page import MainPage
        return MainPage(self._driver)


