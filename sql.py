import mysql.connector as mycon
from numpy import select
import pandas as pd

x=-1
info=pd.read_csv("Pokemons.csv")
df=pd.DataFrame(info)
mydb = mycon.connect(
  host="localhost",
  user="root",
  password="12345678",
  database="project"
)

mycursor = mydb.cursor()

pd.set_option('display.max_rows', 800)
pd.set_option('display.max_column', 15)


for i in range(0,800):
    x=x+1
    name=df.iloc[x,1]
    type_1=df.iloc[x,2]
    type_2=df.iloc[x,3]
    total=df.iloc[x,4]
    hp=df.iloc[x,5]
    attack=df.iloc[x,6]
    defense=df.iloc[x,7]
    sp_atk=df.iloc[x,8]
    sp_def=df.iloc[x,9]
    speed=df.iloc[x,10]
    generation=df.iloc[x,11]
    legendary=df.iloc[x,12]
    sql=(f"insert into pokemones value('{name}','{type_1}','{type_2}',{total},{hp},{attack},{defense},{sp_atk},{sp_def},{speed},{generation},'{legendary}')")
    print(x+1,sql)  
    mycursor.execute(sql)
    mydb.commit()
print(f"inserted {x+1} values into test")
input()
  