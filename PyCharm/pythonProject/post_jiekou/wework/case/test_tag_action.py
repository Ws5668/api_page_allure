import allure

from utils.get_token import Utils
from wework.api_page.tag import Tag

@allure.feature("标签操作")
class TestTag:
    def setup_class(self):
        # 获取通讯录管理的token参数
        conf_data = Utils.get_id_secret("./config.yml")
        corpid = conf_data["corpid"]["id"]
        corpsecret = conf_data["secret"]["passward"]
        # 实例化标签类
        self.tag = Tag(corpid, corpsecret)
        #清除标签
        self.tag.clear_data()
        # 传入tagid
        self.tagid = 78
        # 创建要用数据
        self.create_data = {
            "tagname": "tags",
            "tagid": self.tagid
        }
        # 更新要用的数据
        self.update_data = {
            "tagname": "tag",
            "tagid": self.tagid
        }

    @allure.story("标签的增删改查操作场景用例")
    def test_tag(self):
        """
        标签的增改删查
        :return:
        """
        # 创建标签
        with allure.step("创建标签"):
            self.tag.create_tag(self.create_data)
        with allure.step("查询标签是否创建成功"):
            l = self.tag.get_tags_list()
            # assert l["taglist"][-1]["tagname"] == "tags"
            # 通过jsonpath断言查询是否创建成功
            tag_list = Utils.base_jsonpath(l, "$..tagname")
            print(tag_list)
            assert "tags" in tag_list
        # 更新标签
        with allure.step("更新标签"):
            self.tag.update_tag(self.update_data)
        with allure.step("查询标签更新结果"):
            l = self.tag.get_tags_list()
            # assert l["taglist"][-1]["tagname"] == "tag"
            tag_list = Utils.base_jsonpath(l, "$..tagname")
            print(tag_list)
            assert "tag" in tag_list
        # 删除标签
        with allure.step("删除标签"):
            self.tag.delete_tag(self.tagid)
        with allure.step("查询标签删除结果"):
            l = self.tag.get_tags_list()
            # 创建标签id列表
            id_list = Utils.base_jsonpath(l, "$..tagid")
            print(id_list)
            # 查询删除后标签的id不在id列表里
            assert self.tagid not in id_list
            # assert len(l["taglist"]) == 3
