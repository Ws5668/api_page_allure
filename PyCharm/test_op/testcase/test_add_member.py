from faker import Faker

from page.main_page import MainPage


class TestAddMember:
    def setup(self):
        self.main_page = MainPage()

        # 使用Faker
        self.faker = Faker(locale='zh_CN')  # 设置中文
        self.name = self.faker.name()  # 生成随机中文名
        self.id = self.faker.random_number(digits=5)  # 生成随机id
        self.phone = self.faker.phone_number()  # 生成随机手机号

    def test_add_member(self):
        num = self.main_page.goto_add_member().add_member(self.name, self.id,
                                                          self.phone).goto_address().address_book()  # 业务逻辑
        assert self.phone in num  # 添加断言
