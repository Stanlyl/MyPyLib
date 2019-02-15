# coding=utf-8
import pymssql as sql
import time


class SQLServer:  
    def __init__(self,server,user,password,database):
    # 类的构造函数，初始化DBC连接信息
        self.server = server
        self.user = user
        self.password = password
        self.database = database

    def __GetConnect(self):
        if not self.database:
            raise(NameError,"没有设置数据库信息")
        self.conn = sql.connect(server=self.server,user=self.user,password=self.password,database=self.database)
        cur = self.conn.cursor()
        if not cur:
            raise(NameError,"连接数据库失败")  # 将DBC信息赋值给cur
        else:
            return cur
             
    def SelectQuery(self,sql):
        '''
        执行查询语句
        返回一个包含tuple的list，list是元素的记录行，tuple记录每行的字段数值
        '''
        cur = self.__GetConnect()
        cur.execute(sql) # 执行查询语句
        result = cur.fetchall() # fetchall()获取查询结果
        # 查询完毕关闭数据库连接
        self.conn.close()
        for (Value) in result:
            print(Value)
        return result

    def OperateQuery(self,sql):
        cur = self.__GetConnect()
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
        cur = self.__GetConnect()
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

    #use as : sql = SQLUpdate(Update={dictkey:dictvalue},Formname="formname",const="const = '??'")
    def SQLUpdate(self,**ctrlspace):
        dic = ctrlspace['Update']
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
        pass




if __name__ == '__main__':
    msg = SQLServer(server="192.168.0.105",user="ASN",password="741499686yqy",database="ADBS")
    msg.SelectQuery(msg.SQLSelect(Distinct=0,Listname=["*"],Formname="SNDA_Finance_List",const="FinaClass1Code = '10'"))
    #print(msg.SQLUpdate(Update={'CostType': 1.4,'BuyClass':'test','coflm':'QA'},Formname="SNDA_Finance_List",const="FinaC.4lass1Code = '10'"))
    #msg.BuckupQuery("D:\\SQLbackUP")
