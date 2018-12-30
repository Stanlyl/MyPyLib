# coding=utf-8
import os
import re
import csv
import json
import demjson
import shutil
import time

class FileMaker():
	def __init__(self, filename, path):
		self.filename = filename
		self.path = path
		self.orig = path + "\\" + filename
		self.type = os.path.splitext(filename)[-1][1:]

	def __typeErrorReport(self, line):
		raise Exception("input massage "+line+" whitch type can not be add in file please use Rewritemsg() func")

	def __txtwrite(self, line, way):
		with open(self.orig, way) as file:
			file.write(line)

	def __csvwrite(self, line, way):
		with open(self.orig, way, encoding='utf-8',newline="") as datacsv:
			csvwriter = csv.writer(datacsv, dialect="excel")
			for lis in line:
				csvwriter.writerow(lis)

	def __jsonwrite(self, line, way):
		with open(self.orig, way) as file:
			file.write(json.dumps(demjson.decode(line)))

	def Rewritemsg(self, line):
		switch = {
			"txt": lambda line:self.__txtwrite(line, 'w'),
			"csv": lambda line:self.__csvwrite(line, 'w'),
			"json": lambda line:self.__jsonwrite('['+demjson.encode(line)+']', 'w')
		}
		try:
			switch[self.type](line)
		except KeyError as e:
			pass

	def Addmsg(self, line):
		switch = {
			"txt": lambda line:self.__txtwrite(line + '\n', 'a'),
			"csv": lambda line:self.__csvwrite(line + '\n', 'a'),
			"json": lambda line:self.__typeErrorReport(demjson.encode(line))
		}
		try:
			switch[self.type](line)
		except KeyError as e:
			pass

	def ReadFile(self, way):
		if way != 'line':
			file = open(self.orig, 'r')
			msg = file.read()
			file.close()
		else:
			msg = []
			for line in open(self.orig,"r"): #设置文件对象并读取每一行文件
				msg.append(line)               #将每一行文件加入到list中
		return msg

	def Backup(self):
		shutil.copy(self.orig, self.path+'\\Backup\\'+time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))+self.filename)

	def CopyFile(self, path):
		shutil.copy(self.orig, path+'\\'+self.filename)

	def Uplode(self, server):
		pass


def main():
	file = FileMaker(filename="test.json", path="C:\\Falcon_Proj\\MyPyLib\\filetest")
	#trble = {'class':'outside','ability':{"a":2,"b":{"path":"C:\\Falcon_Proj\\MyPyLib\\filetest","filename":"test.json"}}}
	#file.Rewritemsg(trble)
	print(file.type)
	print(file.ReadFile('all'))
	#file.Backup()
	#file.CopyFile('C:\\Users\\zhaoruntong.falcon\\Documents\\Downloads')

if __name__ == '__main__':
	main()
