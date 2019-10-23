#coding:utf-8  #强制使用utf-8编码格式
import smtplib #加载smtplib模块
import socket
import json
from email.mime.text import MIMEText
from email.utils import formataddr
my_sender='' #发件人邮箱账号
my_user='' #收件人邮箱账号

def mail():
    ret=True
    try:
        readData = json.loads(open("e:/ftpdir/lmk_fin/program/lianmingka.txt").read())
        my_sender = readData['sender']
        my_user = readData['user']
        ip = readData['ip']
        port = readData['port']
        password = readData['password']

        msg=MIMEText('测试','plain','utf-8')
        msg['From']=formataddr(["千方金融",my_sender])  #括号里的对应发件人邮箱昵称、发件人邮箱账号
#        msg['To']=my_user  #括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject']="主题" #邮件的主题，也可以说是标题
        socket.setdefaulttimeout(10)
        server=smtplib.SMTP_SSL(ip,port)
        server.login(my_sender,password)  #括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender,my_user.split(','),msg.as_string())  #括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  #这句是关闭连接的意思
    except Exception:  #如果try中的语句没有执行，则会执行下面的ret=False
        ret=False
    return ret
 
ret=mail()
if ret:
    print("ok") #如果发送成功则会返回ok，稍等20秒左右就可以收到邮件
else:
    print("filed") #如果发送失败则会返回filed