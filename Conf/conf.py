#!/usr/bin/python
# -*- coding: UTF-8 _*_


# 动态调用本地接口还是服务端接口
def server_ip(env):
    """
    dev_ip 开发环境地址
    sit_ip 测试环境服务器地址
    :return:
    """
    if env == "test":
        server_ip = 'http://106.12.126.197'
        return server_ip
    elif env == "local":
        server_ip = 'http://127.0.0.1:8000'
        return server_ip
    else:
        print("get envorment ip error")
