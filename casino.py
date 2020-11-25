from tkinter import *
from sqlite3 import *

def go():
    conn = connect("data.txt")
    cur = conn.cursor()
    cur.execute("CREATE TABLE membres (identifiant TEXT mot de passe TEXT, argent INTEGER)")

    print('Bienvenue au Casino ! Veuillez commencer par créer un compte ou vous connecter.')
    
    connexion = False

    if connexion==False:
        
        print(creation_compte())

def creation_compte():
    
