from tkinter import *
from sqlite3 import *

conn = connect("data.txt")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS membres (identifiant TEXT mot de passe TEXT, argent INTEGER)")

def go():
    print('Bienvenue au Casino ! Veuillez commencer par créer un compte ou vous connecter.')
    
    connexion = False

    if connexion==False:
        var=''
        while var!='1' and var!='0':
            var = input('Voulez vous vous connecter (0) ou vous inscrire (1)? ')
            print(var)

def creation_compte():
    identifiant=''
    mdp=''
    argent=10000
    
    while len(identifiant)<4 or len(identifiant)>20:
        cur.execute("SELECT pseudo FROM membres")
        liste_identifiants=cur.fetchall()
        identifiant=input('Veuillez choisir un identifiant entre 4 et 20 caractères. ')

    while len(mdp)<4 or len(mdp)>20:
        mdp=input('Veuillez choisir un mot de passe entre 4 et 20 caractères. ')

go()
