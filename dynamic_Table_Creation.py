import pymysql

def generate_dynamic_table_query():
    dynamic_query = "create table "
    get_table_name = input("Enter the name of the table you want to create: ")
    dynamic_query = dynamic_query + get_table_name + "("
    print(dynamic_query)
    # Define the total number of columns you want to include in this table
    get_column_count = int(input("Enter the number of columns of the table you want to create: "))
    # Specify the new column name and datatype
    for i in range(get_column_count):
        get_column_name = input("Enter the name of the column you want to create: ")
        get_column_type = input("Enter the type of the column you want to create: ")
        dynamic_query = dynamic_query + " " + get_column_name + " " + get_column_type + ","
    print(dynamic_query)
    # Remove the comma from the end using rstrip() function
    dynamic_query = dynamic_query.rstrip(",")
    print(dynamic_query)
    dynamic_query = dynamic_query + ")"
    return dynamic_query

conn = pymysql.connect(
    host = "localhost",
    user = "root",
    passwd = "12345",
    db = "world_database",
)
cur = conn.cursor()
dynamic_query = generate_dynamic_table_query()
cur.execute(dynamic_query)
print("Table created successfully")
conn.commit()
conn.close()