import os,sys
sys.path.append(os.getcwd())

from page.page_login import PageLogin
from base.get_driver import get_driver

class TestLogin():

    def setup_class(self):

        self.login=PageLogin(get_driver())
    def teardown_class(self):
        self.login.driver.quit()
    def test_login(self,username="13011111111",pwd="123456"):
        self.login.page_input_username(username)
        self.login.page_input_pwd(pwd)
        self.login.page_login_btn_()