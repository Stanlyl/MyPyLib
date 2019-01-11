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


def main():
	conf = Confget(confname='F:\\Falcon_Proj\\MyPyLib\\filetest\\test.conf',section='server')
	print(conf.CheckKey('localtime'))


if __name__ == '__main__':
	main()

		
