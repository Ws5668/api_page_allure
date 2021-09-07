from utils.get_token import Utils
from wework.api_page.wework_tag import WeWorkTag


class Tag(WeWorkTag):
    # 描述接口的时候，把数据提取出来，通过传参的方式传入
    # 在测试用例层传入数据
    def create_tag(self, data):
        create_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token={self.token}"
        # r = requests.post(create_url, json=data)
        req = {
            "method":"POST",
            "url":create_url,
            "json":data
        }
        r = self.send_api(req)
        return r.json()

    def update_tag(self, data):
        update_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token={self.token}"
        # r = requests.post(update_url, json=data)
        req = {
            "method": "POST",
            "url": update_url,
            "json": data
        }
        r = self.send_api(req)
        return r.json()

    def delete_tag(self, tagid):
        delete_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token={self.token}&tagid={tagid}"
        # r = requests.get(delete_url)
        req = {
            "method":"GET",
            "url":delete_url
        }
        r = self.send_api(req)
        return r.json()

    def get_tags_list(self):
        get_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/list?access_token={self.token}"
        # r = requests.get(get_url)
        req = {
            "method": "GET",
            "url": get_url
        }
        r = self.send_api(req)
        return r.json()

    def clear_data(self):
        """
        清理已经存在的标签
        :return:
        """
        #查询当前存在的标签
        tag_list = self.get_tags_list()
        #提取标签id
        tag_id = Utils.base_jsonpath(tag_list,"$..tagid")
        #id为1的是"sa"，删除不为1的其他标签,需调用删除部门的借口完成
        for i in tag_id:
            if i != 1:
                self.delete_tag(i)



