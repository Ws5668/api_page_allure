import time

import yaml
from selenium import webdriver
import selenium
from selenium.webdriver import TouchActions
from selenium.webdriver.chrome.options import Options


class TestWeb():

    def test_web(self):
        # 实例化Options
        option = Options()
        # 设定chrome debug 模式的一个地址
        # 需要写入刚刚启动命令的端口号
        option.debugger_address = "localhost:9222"
        # 实例化一个driver,设定了刚刚的debugger address属性
        self.driver = webdriver.Chrome(options=option)
        driver = self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
        time.sleep(2)
        # 获取cookie
        cookie = self.driver.get_cookies()
        print(cookie)
        # 用yaml储存cookie
        yaml.safe_dump(cookie, open("cookie.yaml", mode='w', encoding="utf-8"))

    def test_cookie(self):
        # 拿到cookie
        cookie = yaml.safe_load(open("cookie.yaml", encoding="utf-8"))
        # 打开浏览器
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        driver = self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # 将cookie写入到浏览器中
        for i in cookie:
            self.driver.add_cookie(i)
        time.sleep(5)
        # 刷新一下
        driver = self.driver.get("https://work.weixin.qq.com/wework_admin/frame")

        # 点击添加成员
        self.driver.find_element_by_css_selector(".ww_indexImg_AddMember").click()
        # 强制等待
        time.sleep(2)
        # 填写信息
        self.driver.find_element_by_xpath("//*[@id='username']").send_keys("李四")
        self.driver.find_element_by_id("memberAdd_acctid").send_keys("170356878")
        self.driver.find_element_by_xpath("//*[@id='js_contacts53']/div/div[2]/div/div[4]/div/form/div[2]/div[1]/div[3]/div[2]/label[1]/input").click()
        self.driver.find_element_by_xpath("//*[@id='memberAdd_phone']").send_keys("15127996159")
        self.driver.find_element_by_xpath("//*[@id='js_contacts53']/div/div[2]/div/div[4]/div/form/div[1]/a[2]").click()
        time.sleep(2)
        self.driver.quit()
