import random

import pytest
import yaml

from Photobox.page.app import App

with open("../data/test_folder_name.yml",encoding="utf-8") as f:
        data_yml = yaml.safe_load(f)
        foldername = data_yml['foldername']
        deletename = data_yml['deletename']
        samefolder = data_yml['samefolder']
        newname = data_yml['newname']
        hidename = data_yml['hidename']

class TestMainFunction():
    #初始化直接跳过登录
    def setup_class(self):
        self.app = App()
        self.login = self.app.start().login().goto_login().input_password()

    def teardown_class(self):
        self.app.close()

#“+”功能
    #隐藏照片
    def test_hide_photo(self):
        foldertext,foldernumber = self.login.get_folder_name_and_number()
        lastnumber = self.login.btadd_add_picture_video().select_album().select_photo().select_afolder(foldertext).get_folder_numbertest(foldertext)
        assert int(lastnumber) == int(foldernumber) + 1

    #隐藏文件
    def test_hide_file(self):
        toast = self.login.btadd_add_file().select_file().select_folder("name").get_toast()
        assert toast == "添加成功"
#
#     #创建文件夹(校验新建文件夹是否在列表内)
#     @pytest.mark.parametrize("foldername",foldername)
#     def test_creat_folder(self,foldername):
#          folder_name = self.login.btadd_add_folder(foldername)
#          assert foldername in folder_name
#
#     #校验创建空文件夹
#     def test_creat_null_folder(self):
#          tosaltext = self.login.btadd_add_exfolder("")
#          assert tosaltext == "名称不能为空"
#
#     #校验创建已存在文件夹
#     @pytest.mark.parametrize("samefolder", samefolder)
#     def test_creat_same_folder(self,samefolder):
#          tosaltext = self.login.btadd_add_exfolder(samefolder)
#          assert tosaltext == "已有相同名称文件夹"
#
# #文件夹功能
#     #删除文件夹(校验删除的文件名是否还在列表内)
#     @pytest.mark.parametrize("deletename",deletename)
#     def test_delete_folder(self,deletename):
#         delete_name = self.login.main_delete(deletename)
#         assert deletename not in delete_name
#
#     #文件夹重命名(校验修改后的名称是否在列表内)
#     @pytest.mark.parametrize("newname", newname)
#     def test_rename(self,newname):
#         foldernames = self.login.folder_rename("123",newname)
#         assert newname in foldernames
#
#     #文件夹取消隐藏(校验隐藏后文件数量是否为0)
#     @pytest.mark.parametrize("hidename", hidename)
#     def test_unhide(self,hidename):
#         photo_number = self.login.main_unhide(hidename)
#         assert photo_number == "0"
#
#     #文件夹导出
#     def test_export_file(self):
#         toasttext = self.login.main_export()
#         assert toasttext == "导出完成"
#
#     #文件夹移动(验证文件数量是否有变化)
#     def test_move_file(self):
#         firstfolder_t = self.login.get_folder_name_and_number()[0]
#         last_number = self.login.main_move(firstfolder_t).select_folder("新建文件夹").get_folder_numbertest(firstfolder_t)
#         assert last_number == "0"

