import mysql.connector

#LOGIN PROCCESS
def login(eno,password):
    conn = mysql.connector.connect(host='localhost',database='project',user='root',password='root')
    c=conn.cursor()
    str="select * from voter where eno='%d' and password='%s' "
    args=(eno,password)
    c.execute(str % args)
    row=c.fetchone()
    if (c.rowcount == 1):
        print("!!Match Found!!")
    else:
        print("!!No Match Found!!")
        enter()
    finally:
        c.close()
        conn.close()

                                   

#ENTER CREDENTIALS
def enter():
    eno=int(input("Enter Your Enrollment Number: "))
    password=input("Enter Your Password: ")
    login(eno,password)
    
enter()
