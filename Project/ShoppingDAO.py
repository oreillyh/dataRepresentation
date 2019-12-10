import mysql.connector 
class ShoppingDAO:
  db=""
  def __init__(self):
    self.db = mysql.connector.connect( 
    
    host="localhost",
    user="root",
    password="",
    database="",
    )

  def getAllGroceries(self):
    cursor = self.db.cursor() 
    sql="select * from groceries" 
    cursor.execute(sql)
    results = cursor.fetchall() 
    returnArray = []
    for result in results:
      returnArray.append(self.groceriesDict(result))
    return returnArray

  def findGroceriesByItem(self, item):
    cursor = self.db.cursor()
    sql="select * from groceries where item = %s" 
    values = (item,)
    cursor.execute(sql, values) 
    result = cursor.fetchone() 
    return self.groceriesDict(result)

  def createGroceries(self, values):
    cursor = self.db.cursor()
    sql="insert into groceries item, name, quantity) values (%s,%s, %s)" 
    cursor.execute(sql, values)
    self.db.commit() 
    return cursor.lastrowid  

  def updateGroceries(self, values):
    cursor = self.db.cursor()
    sql="update groceries set item = %s, name= %s, quantity=%s where id = %s" 
    cursor.execute(sql, values)
    self.db.commit()

  def deleteGroceries(self, id):
    cursor = self.db.cursor()
    sql="delete from groceries where name = %s"
    values = (id,) 
    cursor.execute(sql, values)
    self.db.commit() 
    print("Delete Completed")

  # convert groceries result to a dictionary
  def groceriesDict(self,result):
    colnames = ['id', 'item','name']
    item ={}
    # check if there is a result, otherwise return empty {}
    if result:
      for i, colName in enumerate(colnames):
        value = result[i]
        item[colName] = value
    return item

  # convert groceries result to a dictionary
  def groceriesDict(self,result):
    colnames = ['id','item','name','result']
    item ={}
    # check if there is a result, otherwise return empty {}
    if result:
      for i, colName in enumerate(colnames):
        value = result[i]
        item[colName] = value
      return item

ShoppingDAO = ShoppingDAO()