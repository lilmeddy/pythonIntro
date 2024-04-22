import mysql.connector as connection
conn= connection.connect(host='127.0.0.1', user='root', password='osamede18', db='Playing')
cursor =conn.cursor()
cursor.execute('CREATE TABLE info(Name VARCHAR(20))')
conn.commit()
print('Table Successfully created')