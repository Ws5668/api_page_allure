from page.base_page import BasePage
from page.contact_page import ContactPage


class MainPage(BasePage):
    def click_contact(self):
        self.driver.find_element_by_xpath("//*[@text='通讯录']").click()
        return ContactPage(self.driver)