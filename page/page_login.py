from selenium.webdriver.common.by import By

from base.base import Base

loc_use = (By.ID,"com.vcooline.aike:id/etxt_username")
loc_pwd = (By.ID,"com.vcooline.aike:id/etxt_pwd")
loc_login_btn = (By.ID,"com.vcooline.aike:id/btn_login")

class PageLogin(Base):
    def page_input_username(self,text):
        self.base_input(loc_use,text)

    def page_input_pwd(self,text):
        self.base_input(loc_pwd, text)

    def page_login_btn_(self):
        self.base_click(loc_login_btn)