import pymysql

conn = pymysql.connect(
    host = 'localhost',
    user = 'root',
    passwd = '12345',
    db = 'world_database',
)

curr = conn.cursor()

str1 = "select @@version"

curr.execute(str1)

output = curr.fetchall()

print(output)