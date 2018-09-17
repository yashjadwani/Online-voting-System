import mysql.connector
import re

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
        menu()
    else:
        print("!!No Match Found!!")
        enter()
        
#NAME UPDATE
def Nupdate(eno,name):
           
    str="update voter set name='%s' where eno='%d'"
    args=(name,eno)
    try:
        c.execute(str % args)
        conn.commit()
        print("Updated  Sucessfully")
    except:
        print("Contact Manager/Devloper")
        conn.rollback()
    finally:
        c.close()
        conn.close()

        
def Nverify(veno,vname):
    i=0;
    ie=len(str(veno))
    while( ie != 12):
        veno=int(input("Enter Proper Enrollment Number:"))
        ie=len(str(veno))
    #NAME VERIFY
    for char in vname:
        if(char == ' '):
            pass
        else:
            i+=1
    while( i<3):
        vname=input("Enter proper Name :")
        i=0    
        for char in vname:
            if(char == ' '):
                pass
            else:
                i+=1
    Nupdate(veno,vname)
    
#AADHAR UPDATE    
def Aupdate(eno,ano):
           
    str="update voter set ano='%d' where eno='%d'"
    args=(ano,eno)
    try:
        c.execute(str % args)
        conn.commit()
        print("Updated  Sucessfully")
    except:
        print("Contact Manager/Devloper")
        conn.rollback()
    finally:
        c.close()
        conn.close()

def Averify(veno,vano):
    ia=len(str(vano))
    ie=len(str(veno))
    while( ie != 12):
        veno=int(input("Enter Proper Enrollment Number:"))
        ie=len(str(veno))
    while( ia != 12):
        vano=int(input("Enter Proper Aadhar Card Number:"))
        ia=len(str(vano))
    Aupdate(veno,vano)

#YEAR UPDATE
def Yupdate(eno,year):
           
    str="update voter set year='%d' where eno='%d'"
    args=(year,eno)
    try:
        c.execute(str % args)
        conn.commit()
        print("Updated  Sucessfully")
    except:
        print("Contact Manager/Devloper")
        conn.rollback()
    finally:
        c.close()
        conn.close()

    
def Yverify(veno,vyear):
    ie=len(str(veno))
    while( ie != 12):
        veno=int(input("Enter Proper Enrollment Number:"))
        ie=len(str(veno))
    while(vyear  not in (1,2,3,4)):
        vyear=int(input("In Which Year You Are Currently Studying?(1,2,3,4)"))
    Yupdate(veno,vyear)

#PASSWORD UPDATE
def Pupdate(eno,password):
           
    str="update voter set password='%s' where eno='%d'"
    args=(password,eno)
    try:
        c.execute(str % args)
        conn.commit()
        print("Updated  Sucessfully")
    except:
        print("Contact Manager/Devloper")
        conn.rollback()
    finally:
        c.close()
        conn.close()

#PASSSWORD VERIFY        
def Pverify(veno):
    ie=len(str(veno))
    while( ie != 12):
        veno=int(input("Enter Proper Enrollment Number:"))
        ie=len(str(veno))
    password(veno)

#PASSWORD    
def password(veno):
    while True:
        password = input('Enter New Password: ')
        if 6 <= len(password) < 12:
            break
        print ('The password must be between 6 and 12 characters.\n')

    password_scores = {0:'Horrible', 1:'Weak', 2:'Medium', 3:'Strong'}
    password_strength = dict.fromkeys(['has_upper', 'has_lower', 'has_num'], False)
    if re.search(r'[A-Z]', password):
        password_strength['has_upper'] = True
    if re.search(r'[a-z]', password):
        password_strength['has_lower'] = True
    if re.search(r'[0-9]', password):
        password_strength['has_num'] = True

    score = len([b for b in password_strength.values() if b])
    if (password_scores[score] == "Strong"):
        x=input("Enter your New password again:")
        if (x==password):
            pass
            #print ('Password is %s' % password_scores[score])
            #print(password)
            Pupdate(veno,password)
        else:
            print("password not matched")
            passwor(veno)
    else:
        print("Password is not strong. \n It should contain Digit[0-9].\n It should contain lowercase alphabets[a-z] & uppercase alphabet[A-Z]. ")
        passwor(veno)
        
def passwor():
    password(veno)

#PASSWORD VERIFICATION ENDS
    

    
#UPDATE MENU
def menu():
    eno=int(input("Enter Your Enrollment Number Again: "))
    print("\t \t \t UPDATE MENU ")
    print("1.NAME")
    print("2.AADHAR NUMBER")
    print("3.YEAR")
    print("4.PASSWORD")
    x=int(input("Enter your choice:"))
    while (x not in (1,2,3,4)):
        x=int(input("Enter correct choice(1,2,3):"))
    if (x==1):
        name=input("Enter Your Full Name:")
        Nverify(eno,name)
    elif(x==2):
        ano=int(input("Enter Your Aadhar Card Number:"))
        Averify(eno,ano)
    elif(x==3):
        year=int(input("In Which Year You Are Currently Studying?"))
        Yverify(eno,year)
    else:
        Pverify(eno)
        
#ENTER CREDENTIALS        
def enter():
    eno=int(input("Enter Your Enrollment Number: "))
    password=input("Enter Your Password: ")
    login(eno,password)
    
enter()

