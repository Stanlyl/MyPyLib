#coding=utf8
from wxpy import *
import sys

if sys.platform.startswith('linux'):
	console_qr = True

elif sys.platform.startswith('win32'):
	console_qr = False


bot = Bot(cache_path=True, console_qr=console_qr, qr_path=False, qr_callback=None, login_callback=None, logout_callback=None)

bot.file_helper.send('测试消息请无视')
groups = bot.groups().search('全家福')[0]
print(groups)
for i in range(10):
	groups.send('测试微信消息推送接口，第'+str(i)+'次')

#myfriend = bot.friends().search('彭泽宇')[0]
#myfriend.send('测试消息请无视')
#embed()