from page.base_page import BasePage
from page.editor_member_page import Editor


class AddMemberPage(BasePage):
    def add_member(self):
        self.driver.find_element_by_xpath("//*[@text='手动输入添加']").click()
        return Editor(self.driver)

    def find_toast(self):
        ele = self.driver.find_element_by_xpath("//*[@text='添加成功']")
        return ele

