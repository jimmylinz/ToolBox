import random

from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException

from Photobox.page.basepage import BasePage

#照片隐藏首页
from Photobox.page.main.PhotoDetails.photo_details_page import PhotoDetailsPage
from Photobox.page.main.select_file_page import SelectFilePage
from Photobox.page.main.select_album_page import SellectAlbumPage
from Photobox.page.main.select_folder_page import SelectFolderPage
from Photobox.page.main.flash_page import FlashPage
from Photobox.page.main.set_up_page import SetUpPage
from Photobox.page.main.vip_page import VipPage
from Photobox.page.public_method import PublicMethod


class MainPage(PublicMethod,BasePage):
    _bt_add = (MobileBy.ID,"main_add")#"+"按钮
    _add_picture = (MobileBy.XPATH,'//*[@text="添加图片和视频"]')#添加照片视频按钮
    _add_folder = (MobileBy.XPATH, '//*[@text="新建文件夹"]')  # 新建文件夹按钮
    _add_file = (MobileBy.XPATH, '//*[@text="添加文件"]')  # 添加文件按钮
    _add_encrypted_file = (MobileBy.XPATH, '//*[@text="导入加密文件"]')  # 导入加密文件按钮
    _bt_photograph = (MobileBy.XPATH, '//*[@text="拍照"]')  # 拍照按钮
    _bt_videotape = (MobileBy.XPATH, '//*[@text="录像"]')  # 录像按钮
    _dialog_send = (MobileBy.ID, 'dialog_qq_ed')  # 输入框
    _btc_confirm = (MobileBy.ID, 'dialog_confirm')  # 确认按钮
    _bt_flash = (MobileBy.ID, 'main_flash')  # 闪照按钮
    _folder = (MobileBy.XPATH, "//*[@resource-id='com.cx.hiphoto:id/item_main_layout']")  # 文件夹
    _ty_folder = (MobileBy.ID, 'item_main_bottom_bg')  # 文件夹横条
    _rename = (MobileBy.XPATH, '//*[@text="重命名"]')  # 重命名
    _unhide = (MobileBy.XPATH, '//*[@text="取消隐藏"]')  # 取消隐藏
    _export = (MobileBy.XPATH, '//*[@text="导出"]')  # 导出
    _move = (MobileBy.XPATH, '//*[@text="移动"]')  # 移动
    _delete = (MobileBy.XPATH, '//*[@text="删除"]')  # 删除
    _OK = (MobileBy.ID, 'dialog_cancel')  # 分享"知道了"按钮
    _share = (MobileBy.ID, 'main_title_share')  # 分享
    _share_wechar = (MobileBy.XPATH, '//*[text="微信好友"]')  # 微信分享
    _set_up = (MobileBy.ID, 'main_title_setting')  # 设置
    _vip = (MobileBy.ID, 'main_title_vip_info')  # 会员
    _folder_n = (MobileBy.XPATH, "//*[@resource-id = 'com.cx.hiphoto:id/item_main_name']")  # 所有文件夹名
    _top = "我的照片"  # 用于回到顶部定位用的
    _finish = (MobileBy.ID, "dialog_finish")  # 完成按钮

#“+”功能
    #"+"添加图片/视频
    def btadd_add_picture_video(self):
        self.find_and_click(self._bt_add)
        self.find_and_click(self._add_picture)
        return SellectAlbumPage(self._driver)

    # “+”添加文件
    def btadd_add_file(self):
        self.find_and_click(self._bt_add)
        self.find_and_click(self._add_file)
        return SelectFilePage(self._driver)

    #“+”创建文件夹
    def btadd_add_folder(self,foldername):
        self.find_and_click(self._bt_add)
        self.find_and_click(self._add_folder)
        self.find_and_send(self._dialog_send,foldername)
        self.find_and_click(self._btc_confirm)
        # self.find_by_scroll(self._top)
        folfer_names = self.get_folder_text()
        folferns_lists = [folferns_lists.split(" ")[0] for folferns_lists in folfer_names]
        return folferns_lists

    # “+”创建异常文件夹
    def btadd_add_exfolder(self, foldername):
        self.find_and_click(self._bt_add)
        self.find_and_click(self._add_folder)
        self.find_and_send(self._dialog_send, foldername)
        self.find_and_click(self._btc_confirm)
        toasltext = self.get_toast()
        return toasltext

#文件夹操作
    #文件夹重命名
    def folder_rename(self,foldername,newname):
        try:
            self.find_by_scroll(foldername).click()
        except NoSuchElementException:
            print("没有找到相册")
        else:
            self.find_and_click(self._rename)
            self.find_and_send(self._dialog_send,newname)
            self.find_and_click(self._btc_confirm)
            foldernames = self.get_folder_text()
            folfern_list = [folferns_lists.split(" ")[0] for folferns_lists in foldernames]
            return folfern_list

    #首页取消隐藏
    def main_unhide(self,foldername):
        try:
            self.find_by_scroll(foldername).click()
        except NoSuchElementException:
            print("没有找到相册")
        else:
            self.find_and_click(self._unhide)
            self.find_and_click(self._unhide)
            self.find_by_scroll(foldername)
            number = self.get_folder_number(foldername)
            return number

    #首页导出
    def main_export(self):
        try:
            self.find(self._ty_folder)
        except NoSuchElementException:
            print("没有找到相册")
        else:
            numbers = self.get_have_photo_folder_name()
            number = random.choice(numbers).split(" ")[0]
            self.find_by_scroll(number).click()
            self.find_and_click(self._export)
            self.find_and_click(self._btc_confirm)
            tosttext = self.get_toast()
            return tosttext

    # 首页移动
    def main_move(self,folder_text):
        try:
            self.find(self._ty_folder)
        except NoSuchElementException:
            print("没有找到相册")
        else:
            self.find_by_scroll(folder_text).click()
            self.find_and_click(self._move)
            return SelectFolderPage(self._driver)

    #首页删除
    def main_delete(self,deletename):
        try:
            self.find_by_scroll(deletename).click()
        except NoSuchElementException:
            print("没有找到相册")
        else:
            self.find_and_click(self._delete)
            self.find_and_click(self._btc_confirm)
        deletename = self.get_folder_text()
        deletename_l = [folferns_lists.split(" ")[0] for folferns_lists in deletename]
        return deletename_l
#闪照
    #跳转闪照
    def goto_flash(self):
        self.find_and_click(self._bt_flash)
        return FlashPage(self._driver)

#分享
    #分享跳转
    def goto_share(self):
        try:
            self.find_and_click(self._share)
        except NoSuchElementException:
            self.find_and_click(self._share_wechar)
        else:
            self.find_and_click(self._OK)
            self.find_and_click(self._share_wechar)

#设置
    #设置跳转
    def goto_set_up(self):
        self.find_and_click(self._set_up)
        return SetUpPage(self._driver)

#会员
    #会员跳转
    def goto_vip(self):
        self.find_and_click(self._vip)
        return VipPage(self._driver)

#获取对应文件夹数量用于判断
    def get_folder_numbertest(self,foldername):
        number = self.find_by_scroll(foldername).get_attribute("text").split(" ")[1]
        return number

#进入相册
    def goto_photo_page(self):
        try:
            self.find(self._folder)
        except NoSuchElementException:
            print("没有找到相册")
        else:
            self.find(self._folder).click()
            return PhotoDetailsPage(self._driver)


