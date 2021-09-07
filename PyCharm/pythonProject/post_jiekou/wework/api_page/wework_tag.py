
from wework.api_page.base_api import BaseApi


class WeWorkTag(BaseApi):
    def __init__(self,corpid,corpsecret):
        self.token = self.get_access_token(corpid,corpsecret)

    def get_access_token(self,corpid,corpsecret):
        '''
        获取 access_token
        :return: access_token 的值
        '''
        # 定义凭证
        # corpid = "ww70a66fb3c2e3627a"
        # corpsecret = "3U64SYjnblt22Ce-2fxyC6l1i8bswzgvvfGHIem9T8E"
        # 请求地址
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        # 发出 get 请求
        # r = requests.get(url)
        req = {
            "method":"GET",
            "url": url
        }
        r = self.send_api(req)
        # 提取 access_token 值
        token = r.json()["access_token"]
        return token

