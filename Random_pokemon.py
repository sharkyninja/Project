import random
import matplotlib.pyplot as pl
import pandas as pd

info = pd.read_csv('Pokemons.csv')
df = pd.DataFrame(info)

print("How many draws would u like to take?")
a = int(input())
y = 1
for i in range(0, a):
    x = random.randint(1, 799)
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
    print("Draw No ", y,f": {name}")

    
    ids=['Total', 'Health', 'Attack', 'Defense', 'special_attack', 'Special_Defense', 'Speed']
    values=[total,hp,attack,defense,sp_atk,sp_def,speed]
    y = y+1
    pl.barh(ids,values,)
    if df.iloc[x,12]==True:
        pl.title(f"{df.iloc[x, 1]},Legendary\nGeneration:{df.iloc[x, 11]}")
        pl.show()
    else:
        pl.title(f"{df.iloc[x, 1]}\nGeneration:{df.iloc[x, 11]}")
        pl.show()
input("Thank You For Using My Program, Press Enter key to continue...")