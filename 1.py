"""
создание базы данных mysql с id и title
"""

import mysql.connector
from mysql.connector import Error
try:
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    ) as connection:
    if connection.is_connected():
                print("est conection!")
                with connection.cursor() as cursor:

                    cursor.execute("CREATE DATABASE IF NOT EXIST Salary") 
                    print("baza sozdana")
                    cursor.execute("Use Salary")

                    cursor.execute(""" 
                    CREATE TABLE IF NOT EXIST Employees
                        id INT AUTO_INCREMENT PRIMARY KEY, 
                        title VARCHAR(255) NOT NULL)                           
                        """)

                    sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
                    val = ("John Doe", "johndoe@example.com")
                    cursor.execute(sql, val)
                    print("table create yspeshno")

                    inser_query="""
                    INSERT INTO EMLOYEES (title)
                    VALUES (%s)
                    """
                    records = [
                        ('title_OgaBuga'),
                        ('name_of_title'),
                        ('sorry for too late')
                    ]

                    cursor.executemany(insert_query, records)
                    connection.commit()
                    
                    cursor.execute("SELECT * FROM Emoloyess")
                    rows = cursor.fetchall()
                    print("dannye: ")
                    for row in rows:
                         print(row)
except Error as e:
    print(f"error   {e}")  

print("close all")    
