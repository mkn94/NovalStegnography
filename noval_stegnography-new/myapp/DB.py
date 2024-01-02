import mysql.connector
class DbConnection:
    __mydb=""
    __mycursor=""
    def __init__(self,host,user,passwd,database,port):
        self.host=host
        self.user=user
        self.passwd=passwd
        self.database=database
        self.port=port

        self.__mydb=mysql.connector.connect(
        host=self.host,
        user=self.user,
        passwd=self.passwd,
        database=self.database,
	    port=self.port)

        self.__mycursor=self.__mydb.cursor()

    def selectfullrecords(self, sql):
        self.__mycursor.execute(sql)
        myresult=self.__mycursor.fetchall()
        return myresult
    
    def selectsinglerecord(self,sql,val):
        self.__mycursor.execute(sql,val)
        #myresult=self.__mycursor.fetchone()
        return self.__mycursor.rowcount

    def selectrecords(self, sql,val):
        self.__mycursor.execute(sql,val)
        myresult=self.__mycursor.fetchall()
        return myresult

    def executenonquery(self,sql,val):
        # self.__mycursor.execute(sql,val)
        # self.__mydb.commit()
        try:
            self.__mycursor.execute(sql,val)
            self.__mydb.commit()
            return True
        except:
            return False
    
    def dispose(self):
        self.__mycursor.close()
        self.__mydb.close()
    def __del__(self):
        try:
            self.__mycursor.close()
            self.__mydb.close()
        except:
            print()
