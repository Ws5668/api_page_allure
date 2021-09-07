from ruamel import yaml
from jsonpath import jsonpath


class Utils:
    @classmethod
    def base_jsonpath(cls,obj,json_exp):
        """
        封装jsonpath断言
        :param obj:要断言的json格式的响应内容
        :param json_exp:jsonpath表达式
        :return:断言结果
        """
        return jsonpath(obj,json_exp)

    @classmethod
    def get_id_secret(cls,file_path):
       """
       封装读取文件方法
       :param file_path: yaml路径
       :return: 返回字典格式的内容
       """
       with open(file_path) as f:
           result = yaml.safe_load(f)
       return result