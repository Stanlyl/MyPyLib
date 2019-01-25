#coding=utf8
from wxpy import *
import sys

if sys.platform.startswith('linux'):
	console_qr = True

elif sys.platform.startswith('win32'):
	console_qr = False


bot = Bot(cache_path=True, console_qr=console_qr, qr_path='F:\\Falcon_Proj\\MyPyLib\\filetest\\qrcode.png', qr_callback='qrcode', login_callback=True, logout_callback=None)

bot.file_helper.send('测试消息请无视')
groups = bot.groups()
print(groups)

#myfriend = bot.friends().search('彭泽宇')[0]
#myfriend.send('测试消息请无视')
#embed()