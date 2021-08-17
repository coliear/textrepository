import pymysql

# 打开数据库连接
db = pymysql.connect(host="localhost", user="root", password="111111", database="test")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询

sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""
cursor.execute(sql)
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

# print("Database version : %s " % data)

# 关闭数据库连接
# db.close()
