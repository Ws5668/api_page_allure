import pytest
import requests
from ruamel import yaml

from utils.get_data import get_tags


class TestAddTag:
    """
    单接口验证
    """

    def setup_class(self):
        # 定义凭证
        corpid = "ww70a66fb3c2e3627a"
        corpsecret = "3U64SYjnblt22Ce-2fxyC6l1i8bswzgvvfGHIem9T8E"

        # 请求地址
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"

        # 发出 get 请求
        r = requests.get(url)

        # 提取 access_token 值
        self.token = r.json()["access_token"]
        

    @pytest.mark.parametrize(
        "tagname, tagid,expect",
        get_tags()["addtags"]
    )
    def test_add_tags(self, tagname, tagid, expect):
        """
        创建标签
        :param tagname:
        :param tagid:
        :param expect:
        :return:
        """
        url = "https://qyapi.weixin.qq.com/cgi-bin/tag/create"
        data = {
            "tagname": tagname,
            "tagid": tagid,
            "expect": expect
        }
        params = {
            "access_token": self.token
        }
        # 发送请求
        r = requests.post(url, params=params, json=data)
        print(r.json())
        # 断言
        assert r.json()["errcode"] == expect
