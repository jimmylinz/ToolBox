import random

from appium.webdriver.common.mobileby import MobileBy

from Photobox.page.basepage import BasePage
from Photobox.page.main.select_album_page import SellectAlbumPage
from Photobox.page.main.select_file_page import SelectFilePage
from Photobox.page.public_method import PublicMethod


class PhotoDetailsPage(PublicMethod,BasePage):
    _add_floating = (MobileBy.ID,'add_floating')# ”+“按钮
    _add_photo = (MobileBy.XPATH, "//*[@text='添加图片和视频']")
    _add_folder = (MobileBy.XPATH, "//*[@text='添加文件']")
    _add_hfolder = (MobileBy.XPATH, "//*[@text='导入加密文件']")
    _photograph = (MobileBy.XPATH, "//*[@text='拍照']")
    _videotape = (MobileBy.XPATH, "//*[@text='录像']")
    _select = (MobileBy.ID, 'encrypt_list_edit') #右上角选择按钮
    _unhide = (MobileBy.XPATH, "//*[@text='取消隐藏']") #取消隐藏按钮
    _select_file = (MobileBy.ID, 'item_main_img_icon') #选择文件
    _move_file = (MobileBy.XPATH, "//*[@text='移动到']")  # 选择文件
    _delete = (MobileBy.XPATH, "//*[@text='删除']")  # 删除文件
    _black = (MobileBy.ID, 'encrypt_list_back')  # 选择文件
    _select_folder = (MobileBy.ID, "item_target_folder_title")
    _confirm = (MobileBy.XPATH, "//*[@text='确认']")#确认按钮

#"+"功能
    #隐藏图片或视频
    def pdadd_picture_video(self):
        self.find(self._add_floating).click()
        self.find(self._add_photo).click()
        return SellectAlbumPage(self._driver)

    #隐藏文件
    def pdadd_file(self):
        self.find(self._add_floating).click()
        self.find(self._add_folder).click()
        return SelectFilePage(self._driver)

    #导入加密文件
    def pdadd_encrypted_file(self):
        pass

#页面功能
    #取消隐藏
    def pd_unhide(self):
        self.find_and_click(self._select)
        self.find_and_click(self._select_file)
        self.find_and_click(self._unhide)
        self.find_and_click(self._unhide)
        number = self.get_file_number()
        return number

    #移动文件
    def pd_move(self):
        self.find_and_click(self._select)
        self.find_and_click(self._select_file)
        self.find_and_click(self._move_file)
        folders = self.finds(self._select_folder)
        folder_list = [foldertext.get_attribute("text") for foldertext in folders]
        folder = random.choice(folder_list)
        self.find_by_scroll(folder).click()
        number = self.get_file_number()
        return number

    #删除文件
    def pd_delete(self):
        self.find_and_click(self._select)
        self.find_and_click(self._select_file)
        self.find_and_click(self._delete)
        self.find_and_click(self._confirm)
        number = self.get_file_number()
        return number

#文件详情页面功能
