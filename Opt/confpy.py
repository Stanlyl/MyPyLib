# coding=utf-8
import configparser

class Confget():
	def __init__(self, confname, section):
		self.confname = confname
		self.section = section

	def CheckSection(self):
		cf = configparser.ConfigParser()
		cf.read(self.confname)
		return (self.section in cf)

	def CheckKey(self, key):
		if self.CheckSection():
			cf = configparser.ConfigParser()
			cf.read(self.confname)
			return (key in cf[self.section])
		else:
			return False

	def GetKey(self):
		cf = configparser.ConfigParser()
		cf.read(self.confname)
		return cf.options(self.section)

	def GetKeyandValue(self):
		cf = configparser.ConfigParser()
		cf.read(self.confname)
		return cf.items(self.section)

	def GetValuestr(self, key):
		cf = configparser.ConfigParser()
		cf.read(self.confname)
		return cf[self.section][key]

	def GetValueint(self, key):
		cf = configparser.ConfigParser()
		cf.read(self.confname)
		return cf.getint(self.section, key)

class Configure():
	def __init__(self, confname, section):
		self.confname = confname
		self.section = section

	def __CheckSection(self):
		cf = configparser.ConfigParser()
		cf.read(self.confname)
		return (self.section in cf)

	def __CheckKey(self, key):
		if self.__CheckSection() == True:
			cf = configparser.ConfigParser()
			cf.read(self.confname)
			return (key in cf[self.section])
		else:
			return False

	def AddKeyandValue(self, keyword):
		cf = configparser.ConfigParser()
		cf.read(self.confname)
		if self.__CheckSection() == False:
			cf.add_section(self.section)
		for key in keyword:
			cf.set(self.section, key, str(keyword[key]))
		with open(self.confname, 'w') as configfile:
			cf.write(configfile)

		

def main():
	get = Confget(confname='C:\\project\\MyPyLib\\filetest\\test.conf',section='server')
	print(get.GetValueint('server'))
	dict = {'345': '789', 'Age': 99, 'crt': '10.36'}
	config = Configure(confname='C:\\project\\MyPyLib\\filetest\\test.conf',section='test')
	config.AddKeyandValue(dict)


if __name__ == '__main__':
	main()

		
