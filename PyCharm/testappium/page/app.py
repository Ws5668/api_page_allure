from appium import webdriver

from page.base_page import BasePage
from page.main_page import MainPage


class App(BasePage):
    def start(self):
        if self.driver == None:
            desire_caps = {  # capability 设置
                "platformName": "android",  # 要测试的平台
                "deviceName": "127.0.0.1:7555",  # 要启动设备的名称
                "appPackage": "com.tencent.wework",  # 包名
                "appActivity": ".launch.WwMainActivity",  # 要打开的活动页
                "noReset": "true",  # 不清理缓存
                "unicodeKeyBoard": "true",  # 设置允许输入中文
                "resetKeyBoard": "true",  # 同上
                "skipDeviceInitialization": "true",  # 跳过设备的初始化
                'automationName': "uiautomator2"  # 用到的平台工具名
            }
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)  # 打开设备，并传入capability参数
            self.driver.implicitly_wait(5)  # 隐式等待
        else:
            self.driver.launch_app()
        return self

    def quit(self):
        self.driver.quit()

    def goto_main(self):
        return MainPage(self.driver)




