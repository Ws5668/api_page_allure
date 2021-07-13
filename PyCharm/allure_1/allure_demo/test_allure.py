import pytest
import allure
import yaml
import logging


def get_data():
    with open("./datas/data.yaml") as f:
        datas = yaml.safe_load(f)
    return datas

    # 测试计算器的加法运算

@pytest.fixture(scope="function")
def adding():
    logging.info("开始测试加法运算")
    yield
    logging.info("结束加法运算测试")

@pytest.fixture(scope="function")
def floating():
    logging.info("开始测试非常规浮点数")
    yield
    logging.info("结束非常规浮点数测试")

@pytest.fixture(scope="function")
def error():
    logging.info("测试不同种数据类型相加")
    yield
    logging.info("结束不同数据类型相加测试")

@pytest.fixture(scope="function")
def diving():
    logging.info("开始测试除法运算")
    yield
    logging.info("结束除法运算测试")

@allure.feature("计算器")
class Testcalc():

    @allure.story("计算器加法运算-正常情况")
    @pytest.mark.parametrize("a,b,expect", get_data()["adddatas"], ids=get_data()["addids"])
    def test_normal_add(self,a, b, expect, adding,):
        logging.info(f"{a}和{b}相加的结果为{expect}")
        assert expect == a + b

    # 测试计算机浮点数计算
    @allure.story("计算器加法运算-浮点数情况")
    @pytest.mark.parametrize("a,b,expect2", get_data()["floatdatas"], ids=get_data()["floatids"])
    def test_float_add(self,a, b, expect2, floating):
        logging.info(f"{a}和{b}相加的结果为{expect2}")
        assert expect2 == round(a + b, 4)

    # 测试计算机字符与数字不同数据类型相加
    @allure.story("计算器加法运算-异常情况")
    def test_error_add(self,error):
        try:
            result = int + str
        except TypeError:
            print("字符和数字不能相加")

    # 测试计算器的除法运算
    @allure.story("计算器除法法运算-正常情况（分母不为零）")
    @pytest.mark.parametrize("a,b,quotient", get_data()["divdatas"], ids=get_data()["divids"])
    def test_div(self,a, b, quotient, diving):
        logging.info(f"{a}除以{b}的商为{quotient}")
        try:
            quotient == a / b

        except ZeroDivisionError:
            print("除数不能为零")
