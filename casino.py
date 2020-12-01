from tkinter import *
from sqlite3 import *
from pygame import *

conn = connect("data.txt")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS membres (identifiant TEXT, mdp TEXT, argent INTEGER)")


def ret_spec(nb):
    if nb==11:
        return 'valet'
    elif nb==12:
        return 'dame'
    elif nb==13:
        return 'roi'
    elif nb==1:
        return 'as'
    else:
        return str(nb)

def crea_liste_cartes():
    liste_cartes={}

    for i in range(1,53):
        nb=i
        famille_nb=0

        while nb > 13:
            nb=nb-13
            famille_nb=famille_nb+1

        if famille_nb==0:
            liste_cartes[i]=[nb,ret_spec(nb),'coeur']
        elif famille_nb==1:
            liste_cartes[i]=[nb,ret_spec(nb),'carreau']
        elif famille_nb==2:
            liste_cartes[i]=[nb,ret_spec(nb),'pique']
        elif famille_nb==3:
            liste_cartes[i]=[nb,ret_spec(nb),'trèfle']
    
    return liste_cartes

liste_cartes=crea_liste_cartes()
print(liste_cartes)


def go():
    print('Bienvenue au Casino ! Veuillez commencer par créer un compte ou vous connecter.')

    var=''
    jeu=4
    compte=[]
    while var!='1' and var!='0':
        var = input('Voulez vous vous connecter (0) ou vous inscrire (1)? ')
        print(var)
    if var=='0':
        id_entre=''
        sing=(id_entre,)
        mdp_entre=''

        while len(id_entre)<4 or len(id_entre)>20 or check_identifiant_existe(sing)==False:
            id_entre=input("Veuillez entrer un identifiant valide et qui existe ")
            sing=(id_entre,)
                
        mdp_entre=input("Entrez votre mot de passe ")
        while len(mdp_entre)<4 or len(mdp_entre)>20 or check_mdp(id_entre)!=mdp_entre:
            mdp_entre=input("Mot de passe invalide ")

        cur.execute("SELECT argent FROM membres WHERE identifiant = ?",(id_entre,))
        argent_sing=cur.fetchone()

        compte=[id_entre, mdp_entre, argent_sing[0]]
            
        print('Bienvenue, '+id_entre)
                
                
    if var=='1':
        compte=creation_compte()
        print('Bienvenue, '+compte[0])

    hall(compte)


def creation_compte():
    identifiant=''
    sing=(identifiant,)
    mdp=''

    identifiant=input("Choisissez un identifiant. ")
    while len(identifiant)<4 or len(identifiant)>20 or check_identifiant_existe(sing)==True:
        identifiant=input("Veuillez choisir un identifiant entre 4 et 20 caractères qui n'existe pas. ")
        sing=(identifiant,)

    mdp=input('Choisissez un mot de passe. ')
    while len(mdp)<4 or len(mdp)>20:
        mdp=input('Veuillez choisir un mot de passe entre 4 et 20 caractères. ')

    var =[(identifiant, mdp, 10000)]
    for i in var:
        cur.execute("INSERT INTO membres(identifiant, mdp, argent) VALUES(?,?,?)", i)
    conn.commit()

    compte=[identifiant,mdp,10000]

    return compte

def check_identifiant_existe(sing):
    cur.execute("SELECT identifiant FROM membres")
    liste_identifiants=cur.fetchall()

    id_existe_deja=False
    for el in liste_identifiants:
        if el[0]==sing[0]:
            id_existe_deja=True

    return id_existe_deja

def check_mdp(identifiant):
    cur.execute("SELECT mdp FROM membres WHERE identifiant = ?",(identifiant,))
    mdp_sing=cur.fetchone()

    return mdp_sing[0]

def creer_copie_jdc(jeu_de_base):
    nouveau_jeu = []
    nouveau_jeu = nouveau_jeu+jeu_de_base

    return nouveau_jeu



def hall(compte):
    jeu='4'

    while jeu!='0' and jeu!='1' and jeu!='2' and jeu!='3':
        jeu=input('A quel jeu voulez-vous jouer ? Vous avez '+str(compte[2])+' dollars. Pour le blackjack, entrez 1. Pour la machine à sous, entrez 2. Pour la roulette, entrez 3. Si vous voulez sortir du Casino et vous déconnecter, entrez 0. ')

    if jeu==0:
        return

go()
