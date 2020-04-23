# -*- coding: utf-8 -*-
# @Time    : 2018/7/19 下午5:23
# @Author  : Danny
# @File    : Log.py

"""
封装log方法
创建一个log记录日志文件，获取每次执行脚本的名称
记录当前接口操作的日志写入


"""

import logging
import os
import time

LEVELS = {
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warning': logging.WARNING,
    'error': logging.ERROR,
    'critical': logging.CRITICAL
}

logger = logging.getLogger()
level = 'default'


def create_file():
    log_dir = os.path.dirname(os.getcwd()) + '//Log//'
    if not os.path.exists(log_dir):
        os.mkdir(log_dir)
    else:
        pass
    now_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    log_file = log_dir + now_time + '.log'
    return log_file


class MyLog:

    def getlog(self):
        log_file = create_file()
        handler = logging.FileHandler(log_file, encoding='utf-8')
        CP = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setLevel(LEVELS.get('debug'))
        CP.setLevel(LEVELS.get('debug'))
        handler.setFormatter(formatter)
        CP.setFormatter(formatter)
        logger.addHandler(handler)
        logger.addHandler(CP)
        return logger


"""
class MyLog(object):
    def __init__(self, **kwargs):
        log_file = create_file()
        # self.case_name = case_name
        # self.log_level = log_level
        self.kwargs = kwargs
        self.log_file = log_file
        self.handler = logging.FileHandler(log_file, encoding='utf-8')
        self.CP = logging.StreamHandler()

    def OutLog(self):
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        if self.kwargs == 'error':
            self.handler.setLevel(LEVELS.get('error'))
            self.CP.setLevel(LEVELS.get('error'))
            self.handler.setFormatter(formatter)
            self.CP.setFormatter(formatter)
            logger.addHandler(self.handler)
            logger.addHandler(self.CP)
            return logger
        elif self.kwargs == 'debug':
            self.handler.setLevel(LEVELS.get('debug'))
            self.CP.setLevel(LEVELS.get('error'))
            self.handler.setFormatter(formatter)
            self.CP.setFormatter(formatter)
            logger.addHandler(self.handler)
            logger.addHandler(self.CP)
            return logger
        elif self.kwargs == 'info':
            self.handler.setLevel(LEVELS.get('info'))
            self.CP.setLevel(LEVELS.get('error'))
            self.handler.setFormatter(formatter)
            self.CP.setFormatter(formatter)
            logger.addHandler(self.handler)
            logger.addHandler(self.CP)
            return logger
        elif self.kwargs == 'critical':
            self.handler.setLevel(LEVELS.get('critical'))
            self.CP.setLevel(LEVELS.get('error'))
            self.handler.setFormatter(formatter)
            self.CP.setFormatter(formatter)
            logger.addHandler(self.handler)
            logger.addHandler(self.CP)
            return logger
        else:
            print("等级入参有误，不符合评定标准，请给出指定的：error、debug、info、critical级别值！")
"""

    
if __name__ == "__main__":
    log = MyLog().getlog()
    log.info("123123123")
    # log.error("werwerwer")




