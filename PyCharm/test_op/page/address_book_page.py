import time

from page.add_member_page import AddMemberPage
from page.base_page import BasePage


class AddressPage(BasePage):
    def goto_add_member(self):
        self.driver.implicitly_wait(3)  # 添加隐式等待
        self.driver.find_element_by_xpath("//*[@class='js_add_member']").click()  # 点击添加成员
        return AddMemberPage(self.driver)  # 跳转到添加成员界面

    def address_book(self):
        time.sleep(3)  # 添加等待
        phone_number = []  # 设置空列表

        tit = self.driver.find_elements_by_xpath("//*[@class='js_list']/tr/td[5]")  # 用变量传递手机号

        for value in tit:  # 循环遍历变量
            phone_number.append(value.get_attribute("title"))  # 在列表中添加新成员的手机号
        # self.driver.find_element_by_id("memberSearchInput").send_keys(phone_number[-1])  # 在通讯录搜索框输入新添加成员的手机号
        time.sleep(3)
        print(phone_number)
        return phone_number
