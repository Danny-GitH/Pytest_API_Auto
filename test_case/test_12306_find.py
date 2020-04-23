#!/usr/bin/python
# -*- coding: UTF-8 _*_
import requests
from Conf.conf import *
from common.get_excel_data import *
from common.Request import RequestsHandler
from common.Logs import Log

log = Log(__name__)
logger = log.Logger


def test_find12306_care():
    find_url = "https://kyfw.12306.cn/otn/zwdch/query"
    headers = {
        'Cookie': 'JSESSIONID=850EFF3FBF945C2FF718D3776878B911; _jc_save_wfdc_flag=dc; RAIL_EXPIRATION=1587919712423; RAIL_DEVICEID=NYtRP-RiCnLvqmSmBYUrwuQRr1hZfVP2VEE3f61RtTcpL1rPV0yti0WYqPf3oGO5r6ECBOs2kWbK2_hIyhaC_DeXp4BCK_180GxJHeWxrF5l1KbHrX4mkosSfmRyekcRGnv2FxodRhrTCOe2ayau3uqJvNZP4k0W; BIGipServerpool_passport=200081930.50215.0000; route=6f50b51faa11b987e576cdb301e545c4; _jc_save_toDate=2020-04-23; _jc_save_fromDate=2020-05-22; _jc_save_fromStation=%u4E0A%u6D77%2CSHH; _jc_save_toStation=%u5317%u4EAC%2CBJP; BIGipServerotn=2246574346.24610.0000; _jc_save_zwdch_fromStation=%u4E0A%u6D77%2CSHH; _jc_save_zwdch_cxlx=0'
    }
    data = {
        "cxlx": 0,
        "cz": "上海",
        "cc": "G7259",
        "czEn": '-E4-B8-8A-E6-B5-B7',
        "randCode": ''
    }
    r = RequestsHandler().post_Req(url=find_url, data= data, headers=headers)
    print(r.content.decode())
    # print(r.text.encode('utf-8').decode('unicode_escape'))
    statusCode = r.json()['httpstatus']
    print(statusCode)
    try:
        assert statusCode == 200, "返回状态码错误，接口请求失败"

        logger.info("statusCode返回正确------》 %s", statusCode)
    except Exception:
        logger.error("statusCode返回错误------》 %s", statusCode)
        raise


test_find12306_care()
