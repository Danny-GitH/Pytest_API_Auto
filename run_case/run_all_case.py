#!/usr/bin/python
# -*- coding: UTF-8 _*_
import pytest
from common import Shell
# from common import Email
from common.Logs import create_file
from common.Logs import Log

log = Log(__name__)
logger = log.Logger

if __name__ == "__main__":
    # 运行单个文件
    # pytest.main(['../test_case/test_login.py'])
    # 运行多个文件
    # pytest.main(['../test_case/test_login_getVar.py', '../test_case/test_login.py'])
    # 运行整个目录
    # pytest.main(['../test_case', '--html=../report/report.html'])
    logger.info("开始执行脚本")
    try:
        pytest.main(['../test_case', '--alluredir', '../report/reportallure'])
        logger.info("脚本执行完成")
    except Exception:
        logger.error("脚本批量执行失败！")
    shell = Shell.Shell()
    cmd = 'allure generate %s -o %s --clean' % ('../report/reportallure/', '../report/reporthtml/')
    try:
        logger.info("开始执行报告生成")
        shell.invoke(cmd)
        logger.info("报告生成完毕")
    except Exception:
        logger.error("报告生成失败，请重新执行")
        # log.error('执行用例失败，请检查环境配置')
        raise

    # try:
    #     print("3333333333")
    #     mail = Email.SendMail()
    #     print("444444")
    #     mail.sendMail()
    #     print("555555")
    # except Exception as e:
    #     print("2222222")
    #     # log.error('发送邮件失败，请检查邮件配置')
    #     raise
    # pytest.main(['../test_case/test_login_getVar.py'])
    # pytest.main(['../test_case/test001.py'])
