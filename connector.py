import mysql.connector as db

con=db.connect(username="root",
           password="Dileep@08",
           host="localhost")


cur=con.cursor()
#cur.execute('select*from moto.employee')
cur.execute('select empname,salary from moto.employee')

data=cur.fetchall()
#print(data)

#print('Employee Name','      ','Total Salary')
for row in data:
    print(row[1])
cur.close()
con.close()
