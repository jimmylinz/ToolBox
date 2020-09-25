import random
import re

from appium.webdriver.common.mobileby import MobileBy

from Photobox.page.basepage import BasePage


class PublicMethod(BasePage):
    _folder_n = (MobileBy.XPATH, "//*[@resource-id = 'com.cx.hiphoto:id/item_main_name']")  # 所有文件夹名
    _top = "我的照片"  # 用于回到顶部定位用的
    _find_folder = (MobileBy.XPATH, "//*[@resource-id = 'com.cx.hiphoto:id/item_main_name']")  # 选择页所有文件夹名
    _title_text = (MobileBy.XPATH, "//*[@resource-id = 'com.cx.hiphoto:id/title_count']")  # 文件数量

#main用例使用公共方法
    # 获取所有文件夹text返回用于校验
    def get_folder_text(self):
        self.find_by_scroll(self._top)
        folderns_list = []
        while True:
            folderns = self.finds(self._folder_n)
            foldern_list = [foldern.get_attribute("text") for foldern in folderns]
            if set(foldern_list) < set(folderns_list):
                break
            folderns_list = folderns_list + foldern_list
            self.swipe_up()
        # folferns_lists = [folferns_lists.split(" ")[0] for folferns_lists in folferns_list]
        return folderns_list

    #获取对应文件夹数量返回用于校验
    def get_folder_number(self,foldername):
        folder_number = self.find_by_scroll(foldername).text
        number = folder_number.split(" ",1)[1]
        return number

    #获取所有有隐藏文件的文件夹名称用于特殊处理
    def get_have_photo_folder_name(self):
        foldertext = self.get_folder_text()
        k = 0
        for i in range(0, len(foldertext)):
            i -= k
            if foldertext[i].split(" ")[1] == '0' or foldertext[i].split(" ")[1] == "":
                foldertext.pop(i)
                k += 1
        return foldertext

    #随机获取有隐藏文件的文件名或文件数量
    def get_folder_name_and_number(self):
        foldertext = random.choice(self.get_have_photo_folder_name())
        folder_text = foldertext.split(" ")[0]
        folder_number = foldertext.split(" ")[1]
        return folder_text,folder_number

#photofunction使用公共方法
    #获取文件总数
    def get_file_number(self):
        numbertext = self.find(self._title_text).get_attribute("text")
        numberlist = re.findall(r'\d+',numbertext)
        number = 0
        for n in range(0,len(numberlist)):
            number = number + int(numberlist[n])
        return number