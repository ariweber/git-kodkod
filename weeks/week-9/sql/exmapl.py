import mysql.connector
import time

conn = mysql.connector.connect(host= "localhost", port = 3306, user="root", password= "root", database ="soldiers_db")


cursor = conn.cursor()

create_table_sql= """CREATE TABLE IF NOT EXISTS soldiers(
id INT PRIMARY KEY AUTO_INCREMENT,
 name VARCHAR(100) NOT NULL, `rank` VARCHAR(50),
   unit VARCHAR(100), active BOOLEAN DEFAULT TRUE)"""

cursor.execute(create_table_sql)
conn.commit()
cursor.execute("SHOW DATABASES")
cursor.fetchall()

cursor.execute("SHOW TABLES")
print (cursor.fetchall())

cursor.execute("DESCRIBE soldiers")
print(cursor.fetchall())

cursor.close()
conn.close()


