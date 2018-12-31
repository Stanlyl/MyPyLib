import smtplib
from email.header import Header
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
    title = '模块化邮件服务测试--Falcon'
    receivers = ['584747152@qq.com']
    content = 'hello everybody in "电子创新实验室"，\nhere is a test for my python EMail server \n I wish you can print "收到测试邮件"in "电子创新招新-坚持"when you receive this email\nhave a good day in the last day of 2018\n\t--15级物联网赵润彤.Falcon'

    serv.sendEmail(title, content, receivers)

if __name__ == '__main__':
    main()
