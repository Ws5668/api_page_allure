from appium.webdriver.common.mobileby import MobileBy

from page.add_member_page import AddMemberPage
from page.base_page import BasePage


class ContactPage(BasePage):
    def click_add_member(self):
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 'text("添加成员").instance(0));').click()  # 滑动寻找并点击'添加成员'
        return AddMemberPage(self.driver)  # 跳转到添加成员界面

    def delete_member(self, name):
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 f'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("{name}").instance(0));').click()  # 滑动寻找并点击成员姓名
        self.driver.find_element_by_xpath("//*[contains(@text,'个人信息')]/../../../../../*[2]").click()  # 点击更多
        self.driver.find_element_by_xpath("//*[@text='编辑成员']").click()  # 点击'编辑成员'
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 'text("删除成员").instance(0));').click()  # 滑动寻找并点击'删除成员'
        self.driver.find_element_by_xpath("//*[@text='确定']").click()  # 点击确定
        return AddMemberPage(self.driver)

