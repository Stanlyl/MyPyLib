# coding=utf-8
import smtplib
from email.mime.text import MIMEText

class EMail():
    def __init__(self, mail_host, mail_user, mail_pass, sender):
        self.mail_host = mail_host
        self.mail_user = mail_user
        self.mail_pass = mail_pass
        self.sender = sender

    def sendEmail(self, title, content, receivers):
 
        message = MIMEText(content, 'plain', 'utf-8')  # 内容, 格式, 编码
        message['From'] = "{}".format(self.sender)
        message['To'] = ",".join(receivers)
        message['Subject'] = title
 
        try:
            smtpObj = smtplib.SMTP_SSL(self.mail_host, 465)  # 启用SSL发信, 端口一般是465
            smtpObj.login(self.mail_user, self.mail_pass)  # 登录验证
            smtpObj.sendmail(self.sender, receivers, message.as_string())  # 发送
            print("mail has been send successfully.")
        except smtplib.SMTPException as e:
            print(e)
 
def main():
    serv = EMail(mail_host = "smtp.163.com", mail_user = "Falcon_Lab", mail_pass = "741499686YqY",sender = 'Falcon_Lab@163.com')
    title = '测试通知邮件'
    receivers = ['584747152@qq.com']
    content = '如接收到本邮件，则代表本次测试为通过状态，如非本人收到，请退回该邮件，谢谢\n 来自赵润彤的邮件服务设备'

    serv.sendEmail(title, content, receivers)

if __name__ == '__main__':
    main()
