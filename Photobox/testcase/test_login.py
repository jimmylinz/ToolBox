import pytest
import yaml

from Photobox.page.app import App

with open ("../data/login_emile.yml",encoding='UTF-8') as f:
    datas_yaml = yaml.safe_load(f)
    emlie = datas_yaml['emile']
    qq = datas_yaml['qq']
    bad_format = datas_yaml['bad_format']
    wrong_char_type = datas_yaml['wrong_char_type']

#登录用例
class TestLogin:
    def setup_class(self):
        self.app = App()
        self.login = self.app.start().login()

    def teardown_class(self):
        self.app.close()

#登陆用例
    #第一次安装APP，第一次登录用例
    @pytest.mark.parametrize('emile',emlie)
    def test_login_first(self,emile):
        self.login.goto_login_first().goto_authorization_delete().goto_register().set_password().confirm_password().set_emile(emlie)

    #非第一次安装，第一次登录，删除数据用例
    @pytest.mark.parametrize('emile', emlie)
    def test_login_delete(self, emile):
        self.login.goto_login_first().goto_authorization_delete().goto_register().set_password().confirm_password().set_emile(emlie)

    #非第一次安装，第一次登录，恢复数据用例
    def test_login_revicery(self):
        self.login.goto_login_first().goto_authorization_revocery().revicery_password()

    #已安装APP登录
    def test_login(self):
        self.login.goto_login().input_password()

#登陆密码设置校验用例
    #校验设置密码小于4位能否通过
    def test_lessthan4_pwd(self):
        result = self.login.goto_login_first().goto_authorization_delete().goto_register().set_short_password()
        assert result == "密码至少包含4个字符"

    #校验前后两次密码不一致是否通过
    def test_confirm_pwd(self):
        result = self.login.goto_login_first().goto_authorization_delete().goto_register().set_password().confirm_confirm_password()
        assert result == "密码错误，请重新输入"

    # 校验确认密码小于4位能否通过
    def test_confirm_lessthan4_pwd(self):
        result = self.login.goto_login_first().goto_authorization_delete().goto_register().set_password().confirm_confirm_password()
        assert result == "密码至少包含4个字符"

    #校验后一次密码与前一位密码相似是否通过（0000-00000）
    def test_similar_pwd(self):
        result = self.login.goto_login_first().goto_authorization_delete().goto_register().set_password().confirm_similar_password()
        assert result == "密码错误，请重新输入"

#登陆校验校验
    #校验邮箱错误格式是否通过
    @pytest.mark.parametrize('bad_format',bad_format)
    def test_bad_format_emile(self,bad_format):
        result = self.login.goto_login_first().goto_authorization_delete().goto_register().set_password().confirm_password().set_error_emile(bad_format)
        assert result == "邮箱地址不规范"
        self.login.back()

    # 校验邮箱错误字符类型是否通过
    @pytest.mark.parametrize('wrong_char_type', wrong_char_type)
    def test_wrong_char_type_emile(self, wrong_char_type):
        self.login.goto_login_first().goto_authorization_delete().goto_register().set_password().confirm_password().set_emile(wrong_char_type)
