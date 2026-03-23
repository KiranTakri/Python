import mysql.connector as myconn
conn = myconn.connect(
    host="localhost",
    user="root",
    password="Dhansingh@637",
    database="book_db"     
    
)
cursor=conn.cursor()
# print("successfully connect to database")
# create_table_query = """
# CREATE TABLE IF NOT EXISTS books(
#     b_id INT PRIMARY KEY,
#     b_name VARCHAR(50),
#     b_price INT
# );
# """
# cursor.execute(create_table_query)
# print("Table created successfully")


#Insert
# query = """INSERT INTO books (b_id, b_name, b_price) VALUES 
# (3, "CN", 210),
# (4,"OS",150),
# (5,"C++",220);"""
# cursor.execute(query)
# conn.commit()
# print("Inserted successfully")

#Select
# cursor.execute("SELECT * FROM books")
# rows=cursor.fetchall()
# print("Table data")
# for row in rows:
#     print(row)


#update
# query="""UPDATE books set b_name= 'C' where b_id=5;"""
# cursor.execute(query)
# conn.commit()
# print("Update successfully")


#delete query
# delete_query="""DELETE FROM books where b_id=5; """
# cursor.execute(delete_query)
# conn.commit()
# print("Delete successfully")
