<div  align="center">    
	<img src="./filetest/logo.png" width = "300" height = "200" alt="logo" />
</div>

[![license](https://img.shields.io/github/license/ASNFalcon/MyPyLib.svg)](https://github.com/ASNFalcon/MyPyLib/blob/master/LICENSE)

--An operate framework by python
===========================

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
You can just clone this project and run `base.py` to install all the support  
## Catalog:bookmark_tabs:
* [MyPyLib](./)
	* [Opt](./Opt)
		* [confpy](./Opt/README.md#mypyliboptconfpy)
		* [filepy](./Opt/README.md#mypyliboptfilepy)
	* [SQL](./SQL)
		* [mysql](./SQL/README.md#mypylibsqlmysql)
		* [sqlserver](./SQL/README.md#mypylibsqlsqlserver)
	* [Serv](./Serv)
		* [mailserv](./Serv/README.md#mypylibservmailserv)
		* [socketserv](./Serv/README.md#mypylibservsocketserv)
	* [Client](./Client)
		* [socketclient](./Client/README.md#mypylibclientsocketclient)

# Brief Introduction
* You can learn the basic usage of these small modules here  
This is a Python3 based programming framework.You can build your own server or client based on this framework  
Framework contains database/file/communication aspects of the package.And developer are trying to figure out what else is needed to encapsulate the base class and update it.  
As you can see, you can use it directly as a library in your python3 project, directly copying it to the root of your project.   
Or use the `sys.path.append(path)` function to import the directory where the custom module resides   
```python
import sys
sys.path.append(r"./anypath/MyPyLib")
```
* Import into your project like(I'll take some of these packages as an example)
```python
from MyPyLib.Opt.filepy import *
from MyPyLib.Opt.confpy import *
from MyPyLib.SQL.mysql import *
```
* Next, instantiate the class you need.  
```python
example1 = FileMaker(filename="test.json", path="./anypath/filetest")
example2 = Configure(confname='./anypath/test.conf',section='section')
example3 = MySQL(server='serveraddr',port = 3306,user='user',password='password',database="database")
```
* Then enjoy using the functions you need.  
```python
example1.ReadFile('all')
example2.AddKeyandValue(dict)
example3.SelectQuery(example3.SQLSelect(Distinct=0,Listname=["*"],Formname="`user`",const=" "))
```
Damn, be handsome by myself.  

------
__The `README.md` reported by [OOgundam]__  
__MyPyLib is licensed under the GNU General Public License__   
__Copyright ©2019, ASNFalcon__
