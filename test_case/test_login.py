#!/usr/bin/python
# -*- coding: UTF-8 _*_
import requests
from Conf.conf import *
from common.get_excel_data import *
import pytest
import json
from common.Request import RequestsHandler
from requests import session
from common.Logs import Log
log = Log(__name__)
logger = log.Logger


def test_login_pass():
    login_url = server_ip('test') + "/fanwe/index.php?ctl=user&act=dologin&fhash=IzHHyOyDiNsiYYYbamPlHqPQuWrWsCPGUKafBrbgqEymWQcfUP"
    username, password = get_excel_value(1)

    params = {
        "email": username,
        "user_pwd": password,
        "ajax": 1,
        "auto_login": 1

    }

    login_result = RequestsHandler().post_Req(url=login_url, data=params)
    re_login_cookie = login_result.cookies
    content = login_result.text.encode('utf-8').decode('unicode_escape')
    content = json.loads(content)
    statusCode = content["status"]
    print(statusCode)
    try:
        assert statusCode == 2, "登录失败"
        logger.info("statusCode返回正确------》 %s", statusCode)
        return re_login_cookie
    except Exception:
        logger.error("statusCode返回错误------》 %s", statusCode)
        raise


def test_login_name_error():
    login_url = server_ip('test') + "/fanwe/index.php?ctl=user&act=dologin&fhash=IzHHyOyDiNsiYYYbamPlHqPQuWrWsCPGUKafBrbgqEymWQcfUP"
    username, name_error = get_excel_value(2)

    params = {
        "email": username,
        "user_pwd": name_error,
        "ajax": 1,
        "auto_login": 1

    }

    login_result = RequestsHandler().post_Req(url=login_url, data=params)
    re_login_cookie = login_result.cookies
    content = login_result.text.encode('utf-8').decode('unicode_escape')
    content = json.loads(content)
    statusCode = content["status"]
    print(statusCode)
    try:
        assert statusCode == 0, "登录异常"
        logger.info("statusCode返回正确，用户名错误无法登录逻辑正确------》 %s", statusCode)
        return re_login_cookie
    except Exception:
        logger.error("statusCode返回错误------》 %s", statusCode)
        raise


def test_login_pass_error():
    login_url = server_ip('test') + "/fanwe/index.php?ctl=user&act=dologin&fhash=IzHHyOyDiNsiYYYbamPlHqPQuWrWsCPGUKafBrbgqEymWQcfUP"
    username, password_error = get_excel_value(3)

    params = {
        "email": username,
        "user_pwd": password_error,
        "ajax": 1,
        "auto_login": 1

    }

    login_result = RequestsHandler().post_Req(url=login_url, data=params)
    re_login_cookie = login_result.cookies
    content = login_result.text.encode('utf-8').decode('unicode_escape')
    content = json.loads(content)
    statusCode = content["status"]
    print(statusCode)
    try:
        assert statusCode == 0, "登录异常"
        logger.info("statusCode返回正确，密码错误无法登录逻辑正确------》 %s", statusCode)
        return re_login_cookie
    except Exception:
        logger.error("statusCode返回错误------》 %s", statusCode)
        raise