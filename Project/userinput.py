import mysql.cursors 
import mysql.connector 
import databaseconfig as con

# data access object

class UserDAO:
    db=""

    def __init__(self):
        self.db = pymysql.connect(
        host=con.pymysql['host'],
        user=con.pymysql['user'],
        password=con.pymysql['password'],
        database=con.pymysql['database']
        )


    
    def checkUser(self, email, password):
        cursor = self.db.cursor()
        sql="SELECT * FROM usertable where email = %s and password=%s"
        values = (email, password)
        cursor.execute(sql, values)
        
        account = cursor.fetchone()
        return self.convertToDictionary(account)
       
        
        print("Hello Hugh")
    
    def convertToDictionary(self, account):
        colnames=["id", "name", "email", "password"]
        print(colnames)
        item = {}
        
        if account:
            for i, colname in enumerate(colnames):
                print(colnames)
                value = account[i]
                item[colname] = value
        return item    
        
     
userinput = UserDAO()