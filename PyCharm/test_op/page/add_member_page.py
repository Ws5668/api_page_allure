from page.base_page import BasePage


class AddMemberPage(BasePage):
    def add_member(self, name, id, phone):
        '''
        添加成员的信息
        :param name: 姓名
        :param id: 账号
        :param phone: 手机号
        :return:
        '''
        self.driver.find_element_by_id("username").send_keys(name)
        self.driver.find_element_by_id("memberAdd_acctid").send_keys(id)
        self.driver.find_element_by_id("memberAdd_phone").send_keys(phone)
        self.driver.find_element_by_class_name("js_btn_save").click()
        return self  # 切记return

    def goto_address(self):
        from page.address_book_page import AddressPage  # 解决循环导入
        return AddressPage(self.driver)  # 跳转到通讯录界面
