import pymysql

conn = pymysql.connect(
    host = 'localhost',
    user = 'root',
    passwd = '12345',
    db = 'world_database',
)

curr = conn.cursor()

str1 = "select * from student"
curr.execute(str1)
output = curr.fetchall()
# print(output)

output_dict = {}

for row in output:
    # print(row)
    # print(row[0], row[1])
    student_id = row[0]
    student_name = row[1]
    # print(student_id, student_name)
    output_dict[student_id] = {student_name}
print(output_dict)