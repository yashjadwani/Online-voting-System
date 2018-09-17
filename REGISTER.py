import mysql.connector
import re
import random

def register(eno,name,ano,year,password):
    conn = mysql.connector.connect(host='localhost',database='project',user='root',password='root')
    c=conn.cursor()
    str="insert into voter values('%d','%s','%d','%d','%s')"
    args=(eno,name,ano,year,password)
    try:
        c.execute(str % args)
        conn.commit()
        print("Registered Sucessfully")
    except:
        print("Enrollment Number already Exists")
        enter()
        conn.rollback()
    finally:
        c.close()
        conn.close()
        
#password 
def password(veno,vname,vano,vyear):
    while True:
        password = input('Enter Your Password: ')
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
        x=input("Enter your password again: ")
        if (x==password):
            pass
            #print ('Password is %s' % password_scores[score])
            #print(password)
            register(veno,vname,vano,vyear,password)
        else:
            print("password not matched")
            passwor(veno,vname,vano,vyear)
    else:
        print("Password is not strong. \n It should contain Digit[0-9].\n It should contain lowercase alphabets[a-z] & uppercase alphabet[A-Z]. ")
        passwor(veno,vname,vano,vyear)
    
    
def passwor(veno,vname,vano,vyear):
     password(veno,vname,vano,vyear)

def verify(veno,vname,vano,vyear):
    i=0
    ia=len(str(vano))
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
    while( ia != 12):
        vano=int(input("Enter Proper Aadhar Card Number:"))
        ia=len(str(vano))    
    while(vyear  not in (1,2,3,4)):
        vyear=int(input("In Which Year You Are Currently Studying?(1,2,3,4)"))
    #ONE-TIME-PASSWORD    
    x=random.randint(100000,1000000)
    print("Your One Time password is : " +str(x))
   # print(x)
    z=int(input("Enter the One Time Password:"))
    for i in (0,3,1):
        if(z == x):
            password(veno,vname,vano,vyear)
            break
        else:
            z=int(input("Enter the One Time Password:"))
    
        
#INITIAL CREDENTIALS
def enter():
    c=0
    c=c+1
    if(c==1):
        eno=int(input("Enter Your Enrollment Number:"))
        name=input("Enter Your Full Name:")
        ano=int(input("Enter Your Aadhar Card Number:"))
        year=int(input("In Which Year You Are Currently Studying?"))
        verify(eno,name,ano,year)
    else:
        pass

enter()
