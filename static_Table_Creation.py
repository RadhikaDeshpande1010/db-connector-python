import pymysql
conn = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = "12345",
    db = 'world_database'
)
curr = conn.cursor()
create_table_sql = "create table test(id varchar(20), name varchar(20))"
curr.execute(create_table_sql)
print("Table created successfully")
conn.commit()
conn.close()