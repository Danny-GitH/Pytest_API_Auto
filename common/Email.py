# -*- coding: utf-8 -*-
# @Time    : 2018/7/19 下午5:23
# @Author  : WangJuan
# @File    : Email.py

"""
封装发送邮件的方法

"""
import smtplib
import time
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from common import Consts


class SendMail:
    #
    # def __init__(self):
    #     # self.config = Config()
    #     # self.log = Log.MyLog()

    def sendMail(self):
        msg = MIMEMultipart()
        # body = """
        # <h3>Hi，all</h3>
        # <p>本次接口自动化测试报告如下。</p>
        # """
        # mail_body = MIMEText(body, _subtype='html', _charset='utf-8')
        stress_body = "123"
        result_body = "234"
        body2 = ('Hi，all\n本次接口自动化测试报告如下：\n')
        mail_body2 = MIMEText(body2, _subtype='plain', _charset='utf-8')
        tm = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        msg['Subject'] = Header("接口自动化测试报告" + "_" + tm, 'utf-8')
        msg['From'] = "15656550098@163.com"
        receivers = "babyyuzhu@163.com"
        toclause = receivers.split(',')
        msg['To'] = ",".join(toclause)
        username = '15656550098@163.com'
        password = 'EOICJHECUERXCMTN'
        # msg.attach(mail_body)

        msg.attach(mail_body2)

        try:
            smtp = smtplib.SMTP()
            smtp.connect('smtp.163.com', 25)
            smtp.login(username, password)
            smtp.sendmail('sender', toclause, msg.as_string())
        except Exception as e:
            print(e)
            print("发送失败")
            # self.log.error("邮件发送失败，请检查邮件配置")


def email():
    # 第三方 SMTP 服务
    mail_host = "smtp.163.com"  # 设置服务器
    mail_user = "15656550098@163.com"  # 用户名
    mail_pass = "e299Bb738E38a4e8"  # 口令

    sender = '15656550098@163.com'
    receivers = 'babyyuzhu@163.com'  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
    message['From'] = Header("菜鸟教程", 'utf-8')
    message['To'] = Header("测试", 'utf-8')

    subject = 'Python SMTP 邮件测试'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        print("ewrewrewwerwer")
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")


email()

# sender = '15656550098@163.com'
# receivers = ['babyyuzhu@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
#
# # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
# message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
# message['From'] = Header("菜鸟教程", 'utf-8')  # 发送者
# message['To'] = Header("测试", 'utf-8')  # 接收者
#
# subject = 'Python SMTP 邮件测试'
# message['Subject'] = Header(subject, 'utf-8')
#
# try:
#     smtpObj = smtplib.SMTP('smtp.163.com', 25)
#     smtpObj.sendmail(sender, receivers, message.as_string())
#     print("邮件发送成功")
# except smtplib.SMTPException:
#     print("Error: 无法发送邮件")
