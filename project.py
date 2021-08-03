print("Importing Libraries..")
import os
import mysql.connector as myconn
import matplotlib.pyplot as pl
import pandas as pd
from Userdata import all_user
print("Connecting to MySQL...")
con = myconn.connect(user="root", passwd="12345678", database="project")
if con.is_connected():
    print("MySQL:Connected to the Database")
else:
    print("MySQL:Connection Error")

def signup():
    print("Create a User Id:")
    nuser=input()
    print("Create Password:")
    Npass=input()
    print("Confirm Password:")
    npass1=input()
    
    
def post_login():
    print("Welcome {user}!")
    print("Choose an option from below to Continue:")
    print("1.Take a Draw for pokemones")