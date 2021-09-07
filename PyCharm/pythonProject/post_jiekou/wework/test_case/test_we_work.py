import requests


class TestWeWork:
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
        self.tagid = 78


    def test_add_tag(self):
        """
        创建标签
        :return:
        """
        url = "https://qyapi.weixin.qq.com/cgi-bin/tag/create"
        data = {
            "tagname": "tags",
            "tagid": self.tagid
        }
        params = {
            "access_token": self.token
        }
        r = requests.post(url,json=data,params=params)
        print(r.json())
        assert r.json()["errcode"] == 0
        # 通过查询标签列表接口查看标签是否新建成功
        l = self.test_get_tags()
        assert l["taglist"][-1]["tagname"] == "tags"

    def test_update_tag(self):
        """
        更新、修改标签名称
        :return:
        """
        url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token={self.token}"
        data = {
            "tagname": "tag",
            "tagid": self.tagid
        }
        r= requests.post(url,json=data)
        print(r.json())
        assert r.json()["errmsg"] == "updated"
        l = self.test_get_tags()
        assert l["taglist"][-1]["tagname"] == "tag"

    def test_delete_tag(self):
        """
        删除标签
        :return:
        """
        url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token={self.token}&tagid={self.tagid}"
        r = requests.get(url)
        print(r.json())
        l = self.test_get_tags()
        assert len(l["taglist"]) == 1


    def test_get_tags(self):
        """
        获取当前所有标签
        :return:
        """
        url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/list?access_token={self.token}"
        r= requests.get(url)
        print(r.json())
        assert r.json()["errmsg"] == "ok"
        return r.json()

