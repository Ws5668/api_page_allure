import logging

import requests


class BaseApi:
    #设置 loging
    fileHandler = logging.FileHandler(filename="../logs/apitest.log", encoding="utf-8")
    # 设置日志等级
    logging.getLogger().setLevel(0)
    # 设置日志内容格式
    formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(module)s:%(lineno)d %(message)s')
    fileHandler.setFormatter(formatter)
    # 设置生效
    logging.getLogger().addHandler(fileHandler)

    def log_info(self,msg):
        """
        写日志的方法
        :param msg: 要打印到日志中的信息
        :return: info级别的日志
        """
        return logging.info(msg)

    def send_api(self,req):
        """
        对requests进行二次封装
        :param req:
        :return: 返回借口响应结果
        """
        self.log_info("----------request data----------")
        self.log_info(req)
        r = requests.request(**req)
        self.log_info("----------response data----------")
        self.log_info(r.json())
        return r



