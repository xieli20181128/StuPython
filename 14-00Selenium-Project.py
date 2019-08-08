#-*- coding: utf-8 -*-
#1.使用python发送邮件

# import smtplib
# from email.mine.text import MIMEText
# from email.header import Header
#
# #收件人
# sender = "yyqx1128@126.com"
# receiver = "lx1017@126.com"
#
# #不用密码发送，而是用授权码
# auth_code = "yyx123"
#
# #主题
# subject = "自动化测试报告"
#
# #定义发送内容
# msg = MIMEText("<html> <h2>欢迎来到小D课堂</h2></html>",_subtype="html",_charset="utf-8")
# msg["Subject"] = subject
# msg["from"] = sender
# msg["to"] = receiver
#
# smtp = smtplib.SMTP()
# smtp.connect("smtp.126.com")
# smtp.login(sender,auth_code)
#
# smtp.sendmail(sender,receiver,msg.as_string())
# smtp.quit()


# 2.发送测试报告
# import smtplib
# import  os,time,datetime
# from email.mine.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from email.header import Header
#
# sender = "yyqx1128@126.com"
# receiver = "lx1017@126.com"
# auth_code = "yyx123"
#
# smtpserver = 'smtp.126.com'
# subject = "自动化测试报告"
#
# #读取文件内容
# f = open("./result.html",'rb')
# mail_body = f.read()
# f.close()
#
# html = MIMEText(mail_body,_subtype="html",_charset="utf-8")
# html["Subject"] = subject
# html["from"] = sender
# html["to"] = receiver
#
# att1 = MIMEText(mail_body,'base64','gb2312')
# att1["Content-Type"] = 'application/octet-stream'
# att1["Content-Disposition"] = 'attachment;filename="XDclassTestReport.html"'  #这里的filename可以任意写
#
# msg = MIMEMultipart()
# msg["Subject"] = subject  #邮件的标题
# msg.attach(html)         #将html附加在msg里
# msg.attach(att1)         #新增一个附件
#
# smtp = smtplib.SMTP()
# smtp.connect("smtp.126.com")
# smtp.login(sender,auth_code)
#
# smtp.sendmail(sender,receiver,msg.as_string())
# smtp.quit()


# 3.整合发送测试报告邮件
#
# import smtplib
# import  os,time,datetime
# from email.mine.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from email.header import Header
#
# class MailUtils():
#     @classmethod    #表示一个类方法,不需要实例化，可以直接调用
#     def send_test_report(cls):
#         sender = "yyqx1128@126.com"
#         receiver = "lx1017@126.com"
#         auth_code = "yyx123"
#
#         smtpserver = 'smtp.126.com'
#         subject = "自动化测试报告"
#
#         #读取文件内容
#         f = open("./result.html",'rb')
#         mail_body = f.read()
#         f.close()
#
#         html = MIMEText(mail_body,_subtype="html",_charset="utf-8")
#         html["Subject"] = subject
#         html["from"] = sender
#         html["to"] = receiver
#
#         att1 = MIMEText(mail_body, 'base64', 'gb2312')
#         att1["Content-Type"] = 'application/octet-stream'
#         att1["Content-Disposition"] = 'attachment;filename="XDclassTestReport.html"'  #这里的filename可以任意写
#
#         msg = MIMEMultipart()
#         msg["Subject"] = subject  #邮件的标题
#         msg.attach(html)         #将html附加在msg里
#         msg.attach(att1)         #新增一个附件
#
#         smtp = smtplib.SMTP()
#         smtp.connect("smtp.126.com")
#         smtp.login(sender,auth_code)
#
#         smtp.sendmail(sender,receiver,msg.as_string())
#         smtp.quit()