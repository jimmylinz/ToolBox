import random

from appium.webdriver.common.mobileby import MobileBy

from Photobox.page.basepage import BasePage

from Photobox.page.main.select_photo_page import SelectPhotoPage

#选择相册
class SellectAlbumPage(BasePage):
    _album = (MobileBy.XPATH,"//*[contains(@resource-id,'item_category_iv')]/..[@clickable='true']")#可用相册

    #随机选取一个相册
    def select_album(self):
        albums = self.finds(self._album)
        try:
            if len(albums)>0:
                albums_c = random.choice(albums)
                albums_c.click()
            return SelectPhotoPage(self._driver)
        except Exception as e:
            print("没有相册，请先添加相册",e)

