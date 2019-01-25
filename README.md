MyPyLib<br/>--python operating library
===========================
<div  align="center">    
	<img src="./filetest/logo.png" width = "300" height = "200" alt="logo" />
</div>

****
|Author|ASNFalcon :octocat:|OOgundam :octocat:|
|:---:|:---:|:---:
|E-mail|584747152@qq.com|94359703@qq.com
|Location|Hefei-Anhui-China|Liupanshui-Guizhou-China
****

# Basic Environment & Catalog
## Environment:warning:
`python3.5.4` :arrow_up:  
`demjson`   
`pymssql`   
`pymysql`   
`configparser`   
`wxpy`   
`pillow`   
`matplotlib`   
You can just clone this project and run `base.py` to install all the support  
## Catalog:bookmark_tabs:
* [MyPyLib](./)
	* [Opt](./Opt)
		* [confpy](./Opt/README.md)
		* [filepy](./Opt/README.md)
		* [chartpy](./Opt/README.md)
	* [SQL](./SQL)
		* [mysql](./SQL/README.md)
		* [sqlserver](./SQL/README.md)
	* [Serv](./Serv)
		* [mailserv](./Serv/README.md)
		* [socketserv](./Serv/README.md)
		* [wechatserv](./Serv/README.md)
	* [Client](./Client)
		* [socketclient](./Client/README.md)

# Brief Introduction
* You can learn the basic usage of these small modules here  
This is a Python3 based programming framework.You can build your own server or client based on this framework  
Framework contains database/file/communication aspects of the package.And developer are trying to figure out what else is needed to encapsulate the base class and update it.  
As you can see, you can use it directly as a library in your python3 project, directly copying it to the root of your project.   
Import into your project like(I'll take some of these packages as an example)
```python
from MyPyLib.Opt.filepy import *
from MyPyLib.Opt.confpy import *
from MyPyLib.SQL.mysql import *
```
Next, instantiate the class you need.  
```python
example1 = FileMaker(filename="test.json", path="./anypath/filetest")
example2 = Configure(confname='./anypath/test.conf',section='section')
example3 = MySQL(server='serveraddr',port = 3306,user='user',password='password',database="database")
```
Then enjoy using the functions you need.  
```python
example1.ReadFile('all')
example2.AddKeyandValue(dict)
example3.SelectQuery(example3.SQLSelect(Distinct=0,Listname=["*"],Formname="`user`",const=" "))
```
Damn, be handsome by myself.  
__The `README.md` reported by [OOgundam]__  
__Copyright [2019/01/21] by [ASNFalcon]__
