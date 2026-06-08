import mysql.connector



conn = mysql.connector.connect(host = "localhost", port = 3306,
          user="root",
            password= "secret",
              database ="soldiers_db")

cur = conn.cursor()

