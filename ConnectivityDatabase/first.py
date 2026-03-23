import mysql.connector as myconn

conn = myconn.connect(
    host="localhost",
    user="root",
    password="Dhansingh@637",
    database="mamabhanja" 
    
    
)

cursor = conn.cursor()
# print("Connected successfully!")
# create_table_query = """
# CREATE TABLE IF NOT EXISTS mamu (
#     p_id INT PRIMARY KEY,
#     p_name VARCHAR(50),
#     c_id INT
# );
# """
# cursor.execute(create_table_query)
# print("Table created successfully")

def create():
    query = "INSERT INTO product (p_id, p_name, c_id) VALUES (%s, %s, %s)"
    values = (1, "Laptop", 101)
    cursor.execute(query, values)
    conn.commit()
    print("Inserted successfully")
cursor.execute("SELECT * FROM mamu")

rows = cursor.fetchall()

for row in rows:
    print(row)