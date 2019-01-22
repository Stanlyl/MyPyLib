#coding=utf8
import itchat

itchat.auto_login(hotReload=True,enableCmdQR=2)

itchat.send('Hello, filehelper', toUserName='filehelper')

users=itchat.search_friends("唐伯顶")
userName= users[0]['UserName']
print(userName)
itchat.send('pythonNB',toUserName=userName)