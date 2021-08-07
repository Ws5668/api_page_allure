"""
1. 把 selenium 操作，放到 basepage
2. 子类会主动调用 __init__
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    url = "https://work.weixin.qq.com/"

    def __init__(self, driver: WebDriver = None):

        # 如果没有传递 driver ，说明是第一层调用，比如企业微信的官网
        if not driver:
            option = Options()
            option.debugger_address = "localhost:9222"  # 复用浏览器
            self.driver = webdriver.Chrome(options=option)
            self.driver.get(self.url)  # 传入url
            self.driver.maximize_window()  # 窗口最大化
            self.driver.implicitly_wait(3)  # 隐式等待
        # 如果传递了 driver ,说明不是第一次调用，比如企业微信官网 -> 登陆界面
        else:
            self.driver = driver
