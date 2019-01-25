## MyPyLib.Opt
* File basic operations package library

### MyPyLib.Opt.confpy
-----
Config file action library with 2 different class:  
`Confget(confname, section)`   
Used to extract section information from a configuration file(Whitch suffix is '.conf')  
###### Example:  
```python
	example = Confget(confname='./anypath/test.conf',section='anysection')
	example.CheckSection()	#Check to see if this section exists, returns true or false
	example.CheckKey(key)	#Check if the key exists in the section, returns true or false
	example.GetKey()	#Gets all the keys in the section and returns a list
	example.GetKeyandValue()#Gets all keys and their values and returns a list of traversable tuples
	example.GetValuestr(key)#Returns the value of key as a string
	example.GetValueint(key)#Returns the value of key as an integer
```
`Configure(confname, section)`   
Used to edit and generate sections in a configuration file(Whitch suffix is '.conf')
###### Example: 
```python
	example = Configure(confname='./anypath/test.conf',section='anysection')
	dict = {'Name': 'ASNFalcon', 'Email': '584747152@qq.com'}
	example.AddKeyandValue(dict)#Add key and value to section in dictionary form
```

### MyPyLib.Opt.filepy
-----
File action library has 1 class:
`FileMaker(filename, path)`   
Used for file operations(which suffix is '.txt','.csv','.json')
###### Example:  
```python
	example = FileMaker(filename='filename.txt',path='./anypath')
	example.Rewritemsg('message')
	example.Addmsg('message')
	example.ReadFile()
	example.Backup()
	example.CopyFile(path)
	
```


