print("Importing Libraries..")
import os 
import random
import pandas as pd
import matplotlib.pyplot as pl
import mysql.connector as myconn
db=open("Users.txt","r")
print("MySQL:Connecting to Database")
sql=myconn.connect(host="localhost",user="root",passwd="12345678",database="project")
mycon=sql.cursor()
if sql.is_connected():
    print("MySQL: Connected")
else:
    print("MySQL: Unable to connect")

def Startup():
    print("Welcome")
    print("1.Login\n2.Signup")
    o=int(input())
    return(0)
def Signup():
    print("******Signup******")
    print("Create a User_name")
    n_user=input()
    print("Create Password")
    n_passwd=input()
    print("Confirm Password")
    c_passwd=input()
    if len(n_passwd)<8:
        print("Password must contain atleast 8 characters.")
    elif n_passwd!=c_passwd:
        print("Passwords don't match.")
    else:
        try:
            insert_user=(f"insert into Users value('{n_user}','{n_passwd}',50)")
            mycon.execute(insert_user)
            create_table=(f"create table {n_user}(Name varchar(25),Type_1 varchar(20),Type_2 varchar(20),Total int,Health_Points int,Attack int,Defense int,Special_Attack int,Special_defense int,Speed int,Generation int,Legendery char(5));")
            mycon.execute(create_table)
            sql.commit()
            print("Successfuly created an account.")
        except:
            print("User_name already taken.\nTry again")
def Login():
    print("*******Login*******")
    print("Enter Username")
    user=input()
    print("Enter Password")
    passwd=input()
    print("'Welcome!")

    return(user)
def Main():
    print("welcome,{user}")
    print("Choose an option from below to Continue:")
    print("1.Take a Draw for pokemones.")
    print("2.View all your pokemones.")#m_stephin
    print("3.Match.")
    print("4.Check my balance.")#JJ
def random_poki():
    print("Your Coins:{coins}")
    print("Cost per draw: 1 coin")
    print("Enter the number of draw u would like to take.")
    x=int(input())
    return(x)
Signup()