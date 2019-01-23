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

    def sendWithPng(self, title, content, layout, receivers, png):
        message = MIMEMultipart('related')
        message['From'] = Header(self.sender, 'utf-8')
        message['To'] = ",".join(receivers)
        message['Subject'] = Header(title, 'utf-8')
        msgAlternative = MIMEMultipart('alternative')
        message.attach(msgAlternative)

        mail_msg = content
        msgAlternative.attach(MIMEText(mail_msg, layout, 'utf-8'))
 
        # 指定图片为当前目录
        fp = open(png, 'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()
 
        # 定义图片 ID，在 HTML 文本中引用
        msgImage.add_header('Content-ID', '<image1>')
        message.attach(msgImage)
 
        try:
            smtpObj = smtplib.SMTP_SSL(self.mail_host, 465)
            smtpObj.login(self.mail_user, self.mail_pass)
            smtpObj.sendmail(self.sender, receivers, message.as_string())
            print ("mail has been send successfully.")
        except smtplib.SMTPException as e:
            print (e)

    def sendWithAtt(self):
        pass
 
def main():
    serv = EMail(mail_host = "smtp.qq.com", mail_user = "Falcon_Lab", mail_pass = "mqbbzmhlpdhdbgdi",sender = 'falcon_lab@qq.com')
    title = '通知邮件'
    receivers = ['Falcon_Lab@163.com','584747152@qq.com']
    content = """
                <p>Falcon 这是一封自动发送的邮件...</p>
                <p><a href="https://github.com/ASNFalcon/MyPyLib">GitHub: MyPyLib</a></p>
                <p>图片：</p>
                <p><img src="cid:image1"></p>
                """
    layout = 'html'
    png = 'F:\\Falcon_Proj\\MyPyLib\\filetest\\test.png'
    serv.sendWithPng(title, content, layout, receivers, png)

if __name__ == '__main__':
    main()
