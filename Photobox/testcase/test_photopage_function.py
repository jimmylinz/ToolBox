from Photobox.page.app import App


class TestPhotopageFunction():
    def setup_class(self):
        self.app = App()
        self.login = self.app.start().login().goto_login().input_password().goto_photo_page()


    def teardown_class(self):
        self.app.close()

    #隐藏照片视频
    def test_hide_picture(self):
        number = self.login.get_file_number()
        lastnumber = self.login.pdadd_picture_video().select_album().pd_select_photo().get_file_number()
        assert lastnumber == number + 1

    # #隐藏文件
    # def test_hide_pdfile(self):
    #     number = self.login.get_file_number()
    #     lastnumber = self.login.pdadd_file().pd_select_file().get_file_number()
    #     assert lastnumber == number + 1
    #
    # #取消隐藏
    # def test_unhide_pdfile(self):
    #     number = self.login.get_file_number()
    #     lastnumber = self.login.pd_unhide()
    #     assert lastnumber == number - 1
    #
    # #移动文件
    # def test_move_pdfile(self):
    #     firstto_number = self.login.get_file_number()
    #     last_number = self.login.pd_move()
    #     assert last_number == firstto_number - 1
    #
    # #删除文件
    # def test_delete_pdfile(self):
    #     firstto_number = self.login.get_file_number()
    #     last_number = self.login.pd_move()
    #     assert last_number == firstto_number - 1
