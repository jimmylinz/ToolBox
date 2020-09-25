import random

from appium.webdriver.common.mobileby import MobileBy

from Photobox.page.basepage import BasePage


from Photobox.page.main.select_folder_page import SelectFolderPage

#选择照片
class SelectPhotoPage(BasePage):
    _photo = (MobileBy.XPATH, "//*[contains(@resource-id,'item_main_img_layout')]/.[@clickable='true']")  # 可用照片
    _add_media = (MobileBy.XPATH, "//*[@text='添加']")  # 添加按钮
    _finish = (MobileBy.XPATH, "//*[@text='完成']")  # 完成按钮
    _all_select = (MobileBy.ID, "all_select")  # 全选按钮

#main页面添加照片（需要选择对应文件夹）
    #选择照片添加
    def select_photo(self):
        photos = self.finds(self._photo)
        try:
            if len(photos) > 0:
                photos_c = random.choice(photos)
                photos_c.click()
            self.find_and_click(self._add_media)
            return SelectFolderPage(self._driver)
        except Exception as e:
            print("没有照片，请先添加照片", e)

    # 全选照片添加
    def select_all_photo(self):
        photos = self.finds(self._photo)
        try:
            if len(photos) > 0:
                self.find_and_click(self._all_select)
            self.find_and_click(self._all_select)
            return SelectFolderPage(self._driver)
        except Exception as e:
            print("没有照片，请先添加照片", e)

#照片详情页面添加照片
    #选择照片添加
    def pd_select_photo(self):
        photos = self.finds(self._photo)
        try:
            if len(photos) > 0:
                photos_c = random.choice(photos)
                photos_c.click()
            self.find_and_click(self._add_media)
            # self.webdriverwait_until(self._driver,"文件已添加")
            self.find(self._finish).click()
            from Photobox.page.main.PhotoDetails.photo_details_page import PhotoDetailsPage
            return PhotoDetailsPage(self._driver)
        except Exception as e:
            print("没有照片，请先添加照片", e)

    # 全选照片添加
    def pd_select_all_photo(self):
        photos = self.finds(self._photo)
        try:
            if len(photos) > 0:
                self.find_and_click(self._all_select)
            self.find_and_click(self._all_select)
            self.webdriverwait_until(self._driver,"完成")
            self.find(self._finish).click()
            from Photobox.page.main.PhotoDetails.photo_details_page import PhotoDetailsPage
            return PhotoDetailsPage(self._driver)
        except Exception as e:
            print("没有照片，请先添加照片", e)