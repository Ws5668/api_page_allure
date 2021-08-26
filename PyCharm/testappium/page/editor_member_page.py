
from page.base_page import BasePage


class Editor(BasePage):
    def editor_member(self,name,phonenumber):
        self.driver.find_element_by_xpath(
            "//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(name)
        self.driver.find_element_by_xpath(
            "//*[contains(@text,'手机')]/../android.widget.RelativeLayout/android.widget.RelativeLayout"
            "/android.widget.EditText").send_keys(phonenumber)
        self.driver.find_element_by_xpath("//*[@text='保存']").click()
        from page.add_member_page import AddMemberPage
        return AddMemberPage(self.driver)


