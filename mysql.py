import mysql.connector as connection
mydb= connection.connect(host='localhost', user='root', password='osamede18', db='sqi')
mycursor = mydb.cursor()
#mycursor.execute("Show Databases")
# To create a database "create database sqi"

mycursor.execute("Create Table Students (id INT AUTO_INCREMENT PRIMARY KEY, name varchar(255), address varchar(255), age INT )")
mycursor.execute("ALTER TABLe students And Column height varchar(255)")
mycursor.execute("INSERT INTO students(name,address,age,height) VALUES ('timi','apata',46,'6ft')")
print(mycursor)