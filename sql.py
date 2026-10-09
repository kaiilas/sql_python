import pymysql 
conn=pymysql.connect(
    host='localhost',
    port=3307,
    user='root',
    password='BMC22CS074!',
    database='aug2026',
)    
cursor=conn.cursor()
#sql="create table employee(id int primary key,name varchar(20),salary int,dept varchar(20))"
#sql="insert into employee values(1,'Arun',25000,'Developer')"
#sql="insert into employee values(3,'Aravind',35000,'Hr')"
#sql="insert into employee values(4,'Arjun',4000,'Hr')"
#sql="insert into employee values(5,'Arun',4500,'Finance')"
#sql="insert into employee values(6,'Arjun',50000,'It')"
sql="select * from employee"
cursor.execute(sql)
#row=cursor.fetchmany(2)
row=cursor.fetchone()
print(row)
print(row[0],row[1],row[2],row[3])  


#for i in row:
#     print(i[0],i[1],i[2],i[3])  
#row=cursor.fetchall(),fetchmany
#print(row)
#for i in row:
#    print(i)
#for i in row:
#    print(i[0],i[1],i[2],i[3])    
conn.commit()
conn.close()