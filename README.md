MyPyLib--python operating library 
===========================
****
|Author|ASNFalcon :octocat:|
|---|---
|E-mail|584747152@qq.com
|Location|Hefei-Anhui-China
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
		* [confpy](./Opt/confpy.py)
		* [filepy](./Opt/filepy.py)
	* [SQL](./SQL)
		* [mysql](./SQL/mysql.py)
		* [sqlserver](./SQL/sqlserver.py)
	* [Serv](./Serv)
		* [mailserv](./Serv/mailserv.py)
		* [socketserv](./Serv/socketserv.py)
	* [Client](./Client)
		* [socketclient](./Client/socketclient.py)

# Brief Introduction
* You can learn the basic usage of these small modules here  

## MyPyLib.Opt
* File system basic operations package library

### MyPyLib.Opt.confpy
Config file action library with 2 different class:  
`Confget(confname, section)`   
Used to extract section information from a configuration file(Whitch suffix is '.conf')  
`Configure(confname, section)`   
Used to edit and generate sections in a configuration file(Whitch suffix is '.conf')
