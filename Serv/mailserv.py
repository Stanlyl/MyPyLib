# coding=utf-8
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

class EMail():
    def __init__(self, mail_host, mail_user, mail_pass, sender):
        self.mail_host = mail_host
        self.mail_user = mail_user
        self.mail_pass = mail_pass
        self.sender = sender

    def sendText(self, title, content, layout, receivers):
        message = MIMEText(content, layout, 'utf-8')  # 内容, 格式, 编码
        message['From'] = Header(self.sender, 'utf-8')
        message['To'] = ",".join(receivers)
        message['Subject'] = Header(title, 'utf-8')

        try:
            smtpObj = smtplib.SMTP_SSL(self.mail_host, 465)  # 启用SSL发信, 端口一般是465
            smtpObj.login(self.mail_user, self.mail_pass)  # 登录验证
            smtpObj.sendmail(self.sender, receivers, message.as_string())  # 发送
            print("mail has been send successfully.")
        except smtplib.SMTPException as e:
            print(e)

    def sendWithPng(self, title, content, layout, receivers, png):
        message = MIMEMultipart('related')
        message['From'] = Header(self.sender, 'utf-8')
        message['To'] = ",".join(receivers)
        message['Subject'] = Header(title, 'utf-8')
        msgAlternative = MIMEMultipart('alternative')
        message.attach(msgAlternative)

        msgAlternative.attach(MIMEText(content, layout, 'utf-8'))
 
        fp = open(png, 'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()
 
        # 定义图片 ID，在 HTML 文本中引用
        msgImage.add_header('Content-ID', '<image1>')
        message.attach(msgImage)
 
        try:
            smtpObj = smtplib.SMTP_SSL(self.mail_host, 465)  # 启用SSL发信, 端口一般是465
            smtpObj.login(self.mail_user, self.mail_pass)  # 登录验证
            smtpObj.sendmail(self.sender, receivers, message.as_string())  # 发送
            print("mail has been send successfully.")
        except smtplib.SMTPException as e:
            print(e)

    def sendWithAtt(self, title, content, layout, receivers, attach):
        message = MIMEMultipart()
        message['From'] = Header(self.sender, 'utf-8')
        message['To'] = ",".join(receivers)
        message['Subject'] = Header(title, 'utf-8')

        message.attach(MIMEText(content, layout, 'utf-8'))
 
        att1 = MIMEText(open(attach, 'rb').read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att1["Content-Disposition"] = 'attachment; filename="'+attach+'"'
        message.attach(att1)

        try:
            smtpObj = smtplib.SMTP_SSL(self.mail_host, 465)  # 启用SSL发信, 端口一般是465
            smtpObj.login(self.mail_user, self.mail_pass)  # 登录验证
            smtpObj.sendmail(self.sender, receivers, message.as_string())  # 发送
            print("mail has been send successfully.")
        except smtplib.SMTPException as e:
            print(e)
 
def main():
    serv = EMail(mail_host = "smtp.qq.com", mail_user = "Falcon_Lab", mail_pass = "fooswbhhmsvabjai",sender = 'falcon_lab@qq.com')
    title = '通知邮件'
    receivers = ['falcon_lab@qq.com','584747152@qq.com']
    
    content = """
                <p>Welconm to ues ...</p>
                <p><a href="https://github.com/ASNFalcon/MyPyLib">GitHub: MyPyLib</a></p>
                <p>Have a good day：</p>
                <p><img src="cid:image1"></p>
                """
    '''
    content = """
                <p>Welconm to ues ...</p>
                <p><a href="https://github.com/ASNFalcon/MyPyLib">GitHub: MyPyLib</a></p>
                <p>Have a good day</p>
                """
    '''
    layout = 'html'
    png = '/home/asnfalcon/Falcon_Proj/MyPyLib/filetest/logo.png'
    serv.sendWithPng(title, content, layout, receivers, png)

if __name__ == '__main__':
    main()
