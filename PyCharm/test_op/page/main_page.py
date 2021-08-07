import time

from page.add_member_page import AddMemberPage
from page.address_book_page import AddressPage
from page.base_page import BasePage


class MainPage(BasePage):
    url = "https://work.weixin.qq.com/wework_admin/frame"  # 传入url
    time.sleep(2)  # 等待2秒

    def goto_add_member(self):
        self.driver.find_element_by_xpath("//*[@node-type='addmember']").click()  # 点击添加成员
        return AddMemberPage(self.driver)  # 跳转到添加成员界面

    def goto_import_address(self):
        self.driver.find_element_by_id("//*[@id='menu_contacts']").click()  # 点击通讯录
        return AddressPage(self.driver)  # 跳转到通讯录

    def goto_join_member(self):
        pass
