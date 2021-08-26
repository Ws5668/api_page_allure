from faker import Faker


class GetData:
    def __init__(self):
        self.faker = Faker("zh-CN")

    def get_name(self):
        return self.faker.name()

    def get_phonenum(self):
        return self.faker.phone_number()

if __name__ == '__main__':
    print(GetData().get_name())
    print(GetData().get_phonenum())
