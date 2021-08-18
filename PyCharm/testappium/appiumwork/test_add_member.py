import time

from appium import webdriver
from faker import Faker
from appium.webdriver.common.mobileby import MobileBy


class TestAppWork():
    def setup(self):
        desire_caps = {                         #capability 设置
            "platformName": "android",          #要测试的平台
            "deviceName": "127.0.0.1:7555",     #要启动设备的名称
            "appPackage": "com.tencent.wework", #包名
            "appActivity": ".launch.WwMainActivity",#要打开的活动页
            "noReset": "true", #不清理缓存
            "unicodeKeyBoard": "true", #设置允许输入中文
            "resetKeyBoard": "true",   #同上
            "skipDeviceInitialization": "true", #跳过设备的初始化
            'automationName': "uiautomator2" #用到的平台工具名
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)  #打开设备，并传入capability参数
        self.driver.implicitly_wait(5)  #隐式等待

        # 使用Faker
        self.faker = Faker(locale='zh_CN')  # 设置中文
        self.name = self.faker.name()  # 生成随机中文名
        self.phone = self.faker.phone_number()  # 生成随机手机号

    def teardown(self):
        self.driver.quit()


    def test_add_member(self):
        self.driver.find_element_by_xpath("//*[@text='通讯录']").click()  #点击通讯录控件
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 'text("添加成员").instance(0));').click()  #往下滑动到添加成员，并点击
        self.driver.find_element_by_xpath("//*[@text='手动输入添加']").click()  #点击“手动输入添加”
        self.driver.find_element_by_xpath("//*[contains(@text,'姓名')]/../*[3]").send_keys(self.name)  #传入faker生成的姓名
        self.driver.find_element_by_xpath("//*[contains(@text,'手机')]/../*[2]/*[2]/*").send_keys(self.phone)  #传入faker生成的手机号
        self.driver.find_element_by_xpath("//*[@text='保存']").click()  #点击保存
        time.sleep(2) #添加等待查看效果
        act = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']")  #获取Toast
        assert act.text == '添加成功'  #获取Toast的文本，并断言

