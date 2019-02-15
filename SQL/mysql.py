# coding=utf-8
import pymysql as sql
import time

class MySQL():
	def __init__(self, server, port, user, password, database):
		self.conn = sql.connect(
			host= server,
            port = port,
            user = user,
            password = password,
            database = database
            )

	def SelectQuery(self,sql):
		cur = self.conn.cursor()
		cur.execute(sql) # 执行查询语句
		result = cur.fetchall() # fetchall()获取查询结果
		# 查询完毕关闭数据库连接
		self.conn.close()
		for (Value) in result:
			print(Value)
		return result

	def OperateQuery(self,sql):
		cur = self.conn.cursor()
		try:
			# 执行SQL语句
			cur.execute(sql)
			# 向数据库提交
			self.conn.commit()
			print('~~~Commit Success~~~'+sql)
		except:
			# 发生错误时回滚
			self.conn.rollback()
			print('~~~Wrong~~~')
		self.conn.close()

	def ExecQuery(self,sql):
		cur = self.conn.cursor()
		cur.execute(sql) # 执行查询语句
		result = cur.fetchall() # fetchall()获取查询结果
		# 查询完毕关闭数据库连接
		self.conn.close()
		#for (Value) in result:
			#print(Value)
		return result

	def BuckupQuery(self, path):
		sql = "BACKUP DATABASE " + self.database + " To disk= '"
		sql = sql + path +"\\"+ self.database
		sql = sql + time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time())) +".bak'"
		return sql

    #use as : sql = SQLSelect(Distinct=1,Listname="Listname",Formname="Formname",const="const = '??'")
	def SQLSelect(self,**ctrlspace):
		sql = "SELECT "
		if ctrlspace['Distinct'] == 1:
			sql = sql + 'DISTINCT '
		for index, item in enumerate(ctrlspace['Listname']):
			sql = sql + item
			if index != len(ctrlspace['Listname']) - 1:
				sql = sql + ", "
		sql = sql + " FROM " + ctrlspace['Formname']
		try:
			sql = sql + " WHERE " + ctrlspace['const']
		except:
			pass
		return sql

	#use as : sql = SQLUpdate(dict={dictkey:dictvalue},Formname="formname",const="const = '??'")
	def SQLUpdate(self,**ctrlspace):
		dic = ctrlspace['dict']
		key = list(dic.keys())
		value = list(dic.values())
		sql = "UPDATE "
		sql = sql + ctrlspace['Formname'] + " SET "
		for index in range(len(key)):
			if type(value[index]) == int:
				sql = sql + key[index] + " = "+ str(value[index])
			elif type(value[index]) == float:
				sql = sql + key[index] + " = "+ str(value[index])
			else:
				sql = sql + key[index] + " = '"+ value[index] +"'"
			if index != len(key) - 1:
				sql = sql + ", "
		sql = sql + " WHERE " + ctrlspace['const']
		return sql

	def SQLInsert(self,**ctrlspace):
		dic = ctrlspace['dict']
		key = list(dic.keys())
		value = list(dic.values())
		sql = "INSERT INTO "+ ctrlspace['Formname']+" ("
		for index in range(len(key)):
			sql = sql + key[index] 
			if index != len(key) - 1:
				sql = sql + ", "
		sql = sql + ") VALUES ("
		for index in range(len(key)):
			if type(value[index]) == int:
				sql = sql + str(value[index])
			elif type(value[index]) == float:
				sql = sql + str(value[index])
			else:
				sql = sql + "'"+ value[index] +"'"
			if index != len(key) - 1:
				sql = sql + ", "
		sql = sql + ")"
		return sql

if __name__ == '__main__':
	msg = MySQL(server="192.168.0.105",port = 3306,user="ASN",password="741499686yqy",database="ADBS")
	#msg.SelectQuery(msg.SQLSelect(Distinct=0,Listname=["*"],Formname="`user`",const="username like '%陆金卫%'"))
	msg.OperateQuery(msg.SQLInsert(dict={'text':'MyPyLib'},Formname="test",const=""))
