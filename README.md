MyPyLib--python operating library 
===========================
****
|Author|ASNFalcon :octocat:|OOgundam :octocat:|
|---|---|---
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
		* [confpy](./Opt/README.md)
		* [filepy](./Opt/README.md)
	* [SQL](./SQL)
		* [mysql](./SQL/README.md)
		* [sqlserver](./SQL/README.md)
	* [Serv](./Serv)
		* [mailserv](./Serv/README.md)
		* [socketserv](./Serv/README.md)
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
