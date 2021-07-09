import pytest
import logging

class TestCalculator:
    def setup_method(self):
        logging.info("开始计算")

    def teardown_method(self):
        logging.info("结束计算")




    # 测试计算器的加法运算

    @pytest.mark.parametrize("a,b,expect", (
            [1, 1, 2], [0, 1, 1], [0, 0, 0], [0.1, 0.1, 0.2], [-1, -1, -2], [-1, 0, -1], [-0.1, -0.1, -0.2],
            [-1, 1, 0]),
                             ids=["整数", "整数加零", "零加零", "浮点数相加", "负数相加", "负数加零", "负浮点数相加", "负整数和正整数相加"])
    def test_add(self, a, b, expect):
        assert expect == a + b

    # 测试计算器的除法运算

    @pytest.mark.parametrize("a,b,quotient", (
    [2, 1, 2], [2, 0, 3], [3, -1, -3], [-2, -1, 2], [-0.2, -0.2, 1], [-0.2, 2, -0.1], [0.4, -4, -0.1]),
                             ids=["整数相除", "除数为零", "整数除以负数", "负数除以负数", "浮点数除以浮点数", "负浮点数除以正整数", "浮点数除以负整数"])
    def test_div(self, a, b, quotient):
        try:
            assert quotient == a / b

        except:
            raise Exception("ZeroDivisionError:除数不能为零")


