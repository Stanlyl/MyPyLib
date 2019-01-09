# coding=utf-8
import smtplib
from email.mime.text import MIMEText

class EMail():
    def __init__(self, mail_host, mail_user, mail_pass, sender):
        self.mail_host = mail_host
        self.mail_user = mail_user
        self.mail_pass = mail_pass
        self.sender = sender

    def sendEmail(self, title, content, layout, receivers):
 
        message = MIMEText(content, layout, 'utf-8')  # 内容, 格式, 编码
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
    content = '<div style="“width：600px;" text-align：left;="" color：＃000;="" font：normal="" 12px="" 15px="" simsun;="" background：＃d9d9d9;”=""><div style="“height：268px;" background：url（images="" bg1.jpg）no-repeat;”=""><div style="“height：228px;”"><div style="“padding：21px" 0="" 21px;”="">Falcon邮件服务HTML<!-- DIV--><h2 style="“margin：0;" padding：0;="" width：0;="" height：0;="" overflow：hidden;="" text-indent：-2000px;”="">此次邮件为HTML邮件功能的集中测试<!-- H2--><!-- DIV--></h2></div></div></div></div>'
    layout = 'html'

    serv.sendEmail(title, content, layout, receivers)

if __name__ == '__main__':
    main()
