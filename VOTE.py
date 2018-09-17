import mysql.connector
import random

conn = mysql.connector.connect(host='localhost',database='project',user='root',password='root')
c=conn.cursor()

#LOGIN PROCCESS
def login(eno,password):
    
    str="select * from voter where eno='%d' and password='%s'"
    args=(eno,password)
    c.execute(str % args)
    row=c.fetchone()
    if (c.rowcount == 1):
        print("!!Match Found!!")
        vote(eno)
    else:
        print("!!No Match Found!!")
        enter()


#REGISTER VOTE
def register_vote(eno,vno,vname):


    
    str_insert="insert into vote values('%d','%d','%s')"
    args=(eno,vno,vname)
    try:
        c.execute(str_insert % args)
        conn.commit()
        print("Voted Sucessfully")
    except:
        print("Vote already Exists")
        #enter()
        conn.rollback()
    



#VOTE
def vote(eno):
    print("\t \t YOUR VOTE IS VALUABLE!!")
    print("1.ABC \n2.XYZ \n3.PQR \n4.NOTA")
    vo=int(input("Enter Your vote:"))
    while ( vo not in (1,2,3,4)):
        print ("vote among the candidates")
        vo=int(input("Enter your vote (1 2 3 4):"))
    if(vo == 1):
        vname="ABC"
        register_vote(eno,vo,vname)
    elif(vo == 2):
        vname="XYZ"
        register_vote(eno,vo,vname)
    elif(vo == 3):
        vname="PQR"
        register_vote(eno,vo,vname)
    else:
        vname="NOTA"
        register_vote(eno,vo,vname)
        
    


                                   

#ENTER CREDENTIALS
def enter():
    eno=int(input("Enter Your Enrollment Number: "))
    password=input("Enter Your Password: ")
    login(eno,password)
    
enter()




