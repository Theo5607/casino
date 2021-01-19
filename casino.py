import sys, time, pygame
from tkinter import *
from sqlite3 import *
from pygame.locals import *
from Casino_Matvei.test import slot_partie

conn = connect("data.txt")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS membres (identifiant TEXT, mdp TEXT, argent INTEGER)")

black = 0, 0, 0
white = 255, 255, 255
jouer=1
tableau='entree'

pygame.init()

screen = pygame.display.set_mode((1600, 900))

connexion = pygame.image.load("Images/connexion.png")

#Images entree casino

entreecasino = pygame.image.load("Images/Menu/entree_casino.png")
btn_entrer = pygame.image.load("Images/Menu/btn_entrer.png")
btn_entrer_pos = (650, 700)

#Images menu choix du jeu

banderole = pygame.image.load("Images/Menu_jeu/banderole.png")
blackjack_icone = pygame.image.load("Images/Menu_jeu/blackjack_icone.png")
blackjack_icone_pos = (250, 170)
slot_icone = pygame.image.load("Images/Menu_jeu/slot_icone.png")
slot_icone_pos = (900, 170)
roulette_icone = pygame.image.load("Images/Menu_jeu/roulette_icone.png")
roulette_icone_pos = (500, 550)
quitter = pygame.image.load("Images/Menu_jeu/quitter.png")
quitter_pos = (1300, 770)

profil = pygame.image.load("Images/Menu_jeu/profil.png")
profil_pos = (1450, 20)
icone_profil = pygame.image.load("Images/Menu_jeu/Profil/icone_profil.png")
icone_profil_pos = (200, 200)
retour_profil = pygame.image.load("Images/Menu_jeu/Profil/retour_profil.png")
retour_profil_pos = (1300, 770)
oeil = pygame.image.load("Images/Menu_jeu/Profil/oeil.png")

rect_blanc = pygame.image.load("Images/Menu_jeu/Profil/rect_blanc.png")
rect_blanc_pos = (550, 370)


#-----------

#Images roulette

roulette_tapis = pygame.image.load("Images/Jeux/Roulette/tapis.png")
roulette_tapis_bleu = pygame.image.load("Images/Jeux/Roulette/tapis_bleu.png")

fond_nb_vert = pygame.image.load("Images/Jeux/Roulette/fond_nb_vert.png")
fond_nb_bleu = pygame.image.load("Images/Jeux/Roulette/fond_nb_bleu.png")

zero_vert = pygame.image.load("Images/Jeux/Roulette/zero_vert.png")
zero_bleu = pygame.image.load("Images/Jeux/Roulette/zero_bleu.png")
zero_pos = (21, 83)

ligne_vert = pygame.image.load("Images/Jeux/Roulette/ligne_vert.png")
ligne_bleu = pygame.image.load("Images/Jeux/Roulette/ligne_bleu.png")

#Images machine à sous

mas_jouer = pygame.image.load("Images/Jeux/Machine_a_sous/jouer.png")
mas_jouer_pos = (300, 300)
mas_retour = pygame.image.load("Images/Jeux/Machine_a_sous/retour.png")
mas_retour_pos = (900, 300)

mas_somme = pygame.image.load("Images/Jeux/Machine_a_sous/texte_somme.png")
mas_rectangle_somme = pygame.image.load("Images/Jeux/Machine_a_sous/rectangle_somme.png")
mas_rectangle_somme_pos = (500, 600)

mas_gains = pygame.image.load("Images/Jeux/Machine_a_sous/gains.png")
mas_gains_pos = (500, 400)

mas_somme_non_valide = pygame.image.load("Images/Jeux/Machine_a_sous/somme_non_valide.png")

mas_rejouer = pygame.image.load("Images/Jeux/Machine_a_sous/rejouer.png")
mas_rejouer_pos = (550, 700)
mas_quitter = pygame.image.load("Images/Jeux/Machine_a_sous/quitter.png")
mas_quitter_pos = (1050, 700)


screen.blit(connexion, (0, 0))
pygame.display.flip()

def ret_spec(nb): #Retourne le nom de la carte
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

def crea_liste_cartes(): #Renvoie un dictionnaire qui renvoie pour une clé qui va de 1 à 52 pour le numéro cartes une liste qui contient la valeur de la carte, son nom et sa couleur
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

liste_nb = (K_0, K_1, K_2, K_3, K_4, K_5, K_6, K_7, K_8, K_9)
dico_nb = {}
var=0
for el in liste_nb:
    dico_nb[el]=str(var)
    var+=1


def go(): #Pour se connecter au casino et lancer le programme
    print('Bienvenue au Casino ! Veuillez commencer par créer un compte ou vous connecter.')

    var=''
    jeu=4
    compte=[]
    while var!='1' and var!='0':
        var = input('Voulez vous vous connecter (0) ou vous inscrire (1)? ')
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

        screen.fill(black)
        screen.blit(entreecasino, (0, 0))
        screen.blit(btn_entrer, btn_entrer_pos)
        pygame.display.flip()

        return compte

    if var=='1':
        compte=creation_compte()
        print('Bienvenue, '+compte[0])
                
        screen.fill(black)
        screen.blit(entreecasino, (0, 0))
        screen.blit(btn_entrer, btn_entrer_pos)
        pygame.display.flip()

        return compte

    #hall(compte)

def creation_compte(): #Fonction pour créer un compte
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

def check_identifiant_existe(sing): #Cherche dans la base de donnée si l'identifiant pris en paramètre (qui doit être un singulet) existe
    cur.execute("SELECT identifiant FROM membres")
    liste_identifiants=cur.fetchall()

    id_existe_deja=False
    for el in liste_identifiants:
        if el[0]==sing[0]:
            id_existe_deja=True

    return id_existe_deja #Renvoie une valeur true ou false

def check_mdp(identifiant): #Renvoie le mot de passe attaché à un identifiant
    cur.execute("SELECT mdp FROM membres WHERE identifiant = ?",(identifiant,))
    mdp_sing=cur.fetchone()

    return mdp_sing[0]

def creer_copie_jdc(jeu_de_base): #Renvoie une copie du jeu de carte pris en paramètre
    nouveau_jeu = jeu_de_base.copy()

    return nouveau_jeu



def hall(compte): #(SERA PROBABLEMENT BIENTOT OBSOLETE) Fonction "menu" qui permet de choisir son jeu et de sortir du casino
    jeu='4'

    while jeu!='0' and jeu!='1' and jeu!='2' and jeu!='3':
        jeu=input('A quel jeu voulez-vous jouer ? Vous avez '+str(compte[2])+' dollars. Pour le blackjack, entrez 1. Pour la machine à sous, entrez 2. Pour la roulette, entrez 3. Si vous voulez sortir du Casino et vous déconnecter, entrez 0. ')

    if jeu==0:
        return

compte=go()

#variables profil
font_profil = pygame.font.Font("Polices/coolvetica.ttf", 70)
font_argent = font2 = pygame.font.Font("Polices/dejavu_sansbold.ttf", 30)
mdp_cache_verif=True
pos_oeil_gauche=0

#variables roulette
paris=[]

#variables machine à sous
font = pygame.font.Font("Polices/dejavu_sansbold.ttf", 100)
font2 = pygame.font.Font("Polices/dejavu_sansbold.ttf", 50)
somme=''
gains=0

#fonction qui dessine le menu
def dessine_menu():
    screen.fill(white)
    screen.blit(banderole, (0, 0))
    screen.blit(profil, profil_pos)
    screen.blit(blackjack_icone, blackjack_icone_pos)
    screen.blit(slot_icone, slot_icone_pos)
    screen.blit(roulette_icone, roulette_icone_pos)
    screen.blit(quitter, quitter_pos)

#fonction qui vérifie un clic dans le tapis de la roulette
def check_tapis(clic):
    liste_nb_roulette=[3,2,1]
    nombre=0
    ligne=1
    colonne=1
    coordonnees=[187, 84]
    coordonnees_zero=[18, 82]
    for ligne in range(0,3):
        for colonne in range(0,12):
            nombre=liste_nb_roulette[ligne]+3*(colonne)
            if(clic[0]>=coordonnees[0] and clic[0]<=coordonnees[0]+103) and (clic[1]>=coordonnees[1] and clic[1]<=coordonnees[1]+103) and tableau=='roulette_tapis':
                screen.blit(fond_nb_bleu, (coordonnees[0], coordonnees[1]))
                pygame.display.flip()
                return nombre
            else:
                if nombre==36:
                    coordonnees[0]=187
                    coordonnees[1]=84+110
                elif nombre==35:
                    coordonnees[0]=187
                    coordonnees[1]=84+110*2
                elif nombre==34:
                    coordonnees[0]=187
                elif nombre==16:
                    coordonnees[0]=coordonnees[0]+109
                elif nombre==17:
                    coordonnees[0]=coordonnees[0]+109
                elif nombre==18:
                    coordonnees[0]=coordonnees[0]+109
                else:
                    coordonnees[0]=coordonnees[0]+106

    coordonnees_ligne=[1465, 84]
    for i in range(0,3):
        if(clic[0]>=coordonnees_ligne[0] and clic[0]<=coordonnees_ligne[0]+102) and (clic[1]>=coordonnees_ligne[1]+i*111 and clic[1]<=coordonnees_ligne[1]+i*(111)+105):
            screen.blit(ligne_bleu, (coordonnees_ligne[0], coordonnees_ligne[1]+i*111))
            pygame.display.flip()
            return 'ligne_'+str(i+1)

    if(clic[0]>=coordonnees_zero[0] and clic[0]<=coordonnees_zero[0]+165) and (clic[1]>=coordonnees_zero[1] and clic[1]<=coordonnees_zero[1]+330) and tableau=='roulette_tapis':
        screen.blit(zero_bleu, zero_pos)
        pygame.display.flip()
        return 0
        
while jouer==1:
    for event in pygame.event.get():
        if event.type == QUIT:
            jouer = 0
            
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            #bouton entree
            if(event.pos[0]>=650 and event.pos[0]<=950) and (event.pos[1]>=700 and event.pos[1]<=800) and tableau=='entree':
                tableau='menu'

                dessine_menu()
                pygame.display.flip()

            #boutons menu jeu
            if(event.pos[0]>=1450 and event.pos[0]<=1550) and (event.pos[1]>=20 and event.pos[1]<=70) and tableau=='menu':
                tableau='profil'

                mdp_cache_str=''
                for car in compte[1]:
                    mdp_cache_str=mdp_cache_str+'*'

                screen.fill(white)
                screen.blit(retour_profil, retour_profil_pos)
                screen.blit(icone_profil, icone_profil_pos)
                pseudo = font_profil.render(compte[0].upper(), 1, (0, 0, 0))
                longueur_pseudo = pseudo.get_rect().width
                screen.blit(pseudo, (200+((200-longueur_pseudo)/2), 420))
                argent = font_argent.render('Vous avez actuellement '+str(compte[2])+' dollars sur votre compte', 1, (0, 0, 0))
                screen.blit(argent, (550, 300))
                mdp_cache = font_argent.render('Votre mot de passe : '+mdp_cache_str, 1, (0, 0, 0))
                mdp_long = mdp_cache.get_rect().width
                screen.blit(mdp_cache, (550, 370))
                pos_oeil_gauche=mdp_long+30+550
                screen.blit(oeil, (pos_oeil_gauche, 360))
                pygame.display.flip()
                    
            if(event.pos[0]>=900 and event.pos[0]<=1350) and (event.pos[1]>=170 and event.pos[1]<=420) and tableau=='menu':
                tableau='mas_menu'
                
                screen.fill(white)
                screen.blit(mas_jouer, mas_jouer_pos)
                screen.blit(mas_retour, mas_retour_pos)
                pygame.display.flip()

            if(event.pos[0]>=500 and event.pos[0]<=1100) and (event.pos[1]>=550 and event.pos[1]<=800) and tableau=='menu':
                tableau='roulette_menu'

                screen.fill(white)
                screen.blit(mas_jouer, mas_jouer_pos)
                screen.blit(mas_retour, mas_retour_pos)
                pygame.display.flip()

            if(event.pos[0]>=1300 and event.pos[0]<=1550) and (event.pos[1]>=770 and event.pos[1]<=850) and tableau=='menu':
                jouer = 0

            #boutons profil
            if(event.pos[0]>=1300 and event.pos[0]<=1550) and (event.pos[1]>=770 and event.pos[1]<=850) and tableau=='profil':
                tableau='menu'

                dessine_menu()
                pygame.display.flip()

            if(event.pos[0]>=pos_oeil_gauche and event.pos[0]<=pos_oeil_gauche+100) and (event.pos[1]>=360 and event.pos[1]<=410) and tableau=='profil':
                screen.blit(rect_blanc, rect_blanc_pos)

                if mdp_cache_verif==True:
                    mdp_cache_verif=False
                    
                    mdp = font_argent.render('Votre mot de passe : '+compte[1], 1, (0, 0, 0))
                    mdp_long = mdp.get_rect().width
                    screen.blit(mdp, (550, 370))
                    pos_oeil_gauche=mdp_long+30+550
                    screen.blit(oeil, (pos_oeil_gauche, 360))
                else:
                    mdp_cache_verif=True
                    
                    mdp_cache = font_argent.render('Votre mot de passe : '+mdp_cache_str, 1, (0, 0, 0))
                    mdp_long = mdp_cache.get_rect().width
                    screen.blit(mdp_cache, (550, 370))
                    pos_oeil_gauche=mdp_long+30+550
                    screen.blit(oeil, (pos_oeil_gauche, 360))

                pygame.display.flip()

            #------------

            #boutons roulette
            if(event.pos[0]>=900 and event.pos[0]<=1300) and (event.pos[1]>=300 and event.pos[1]<=500) and tableau=='roulette_menu':
                tableau='menu'

                dessine_menu()
                pygame.display.flip()

            if(event.pos[0]>=300 and event.pos[0]<=700) and (event.pos[1]>=300 and event.pos[1]<=500) and tableau=='roulette_menu':
                tableau='roulette_tapis'

                screen.fill(white)
                screen.blit(roulette_tapis, (0, 0))
                liste_nb_roulette=[3,2,1]
                nombre=0
                ligne=1
                colonne=1
                coordonnees=[187, 84]
                for ligne in range(0,3):
                    for colonne in range(0,12):
                        nombre=liste_nb_roulette[ligne]+3*(colonne)
                        screen.blit(fond_nb_vert, (coordonnees[0], coordonnees[1]))
                        if nombre==36:
                            coordonnees[0]=187
                            coordonnees[1]=84+110
                        elif nombre==35:
                            coordonnees[0]=187
                            coordonnees[1]=84+110*2
                        elif nombre==34:
                            coordonnees[0]=187
                        elif nombre==16:
                            coordonnees[0]=coordonnees[0]+109
                        elif nombre==17:
                            coordonnees[0]=coordonnees[0]+109
                        elif nombre==18:
                            coordonnees[0]=coordonnees[0]+109
                        else:
                            coordonnees[0]=coordonnees[0]+106

                screen.blit(zero_vert, (18, 82))

                coordonnees_ligne=[1465, 84]
                for i in range(0,3):
                    screen.blit(ligne_vert, (coordonnees_ligne[0], coordonnees_ligne[1]+i*(111)))
                    
                pygame.display.flip()
                
            nv_pari=check_tapis(event.pos)
            paris.append(nv_pari)
            nv_pari=0

            #boutons menu machine à sous
            if(event.pos[0]>=300 and event.pos[0]<=700) and (event.pos[1]>=300 and event.pos[1]<=500) and tableau=='mas_menu':
                tableau='mas_somme'

                screen.fill(white)
                screen.blit(mas_somme, (0, 0))
                screen.blit(mas_rectangle_somme, mas_rectangle_somme_pos)
                pygame.display.flip()
                
            if(event.pos[0]>=900 and event.pos[0]<=1300) and (event.pos[1]>=300 and event.pos[1]<=500) and tableau=='mas_menu':
                tableau='menu'

                dessine_menu()
                pygame.display.flip()

            #boutons rectangle somme machine à sous
            if(event.pos[0]>=600 and event.pos[0]<=1000) and (event.pos[1]>=600 and event.pos[1]<=700) and tableau=='mas_somme':
                somme=''
                tableau='mas_entrer_somme'
                
                afficher = font.render('0', 1, (0, 0, 0))
                screen.blit(afficher, (500,600))
                pygame.display.flip()

            #boutons quitter et rejouer machine à sous
            if(event.pos[0]>=550 and event.pos[0]<=850) and (event.pos[1]>=700 and event.pos[1]<=800) and tableau=='mas_gains':
                tableau='mas_somme'

                screen.fill(white)
                screen.blit(mas_somme, (0, 0))
                screen.blit(mas_rectangle_somme, mas_rectangle_somme_pos)
                pygame.display.flip()

            if(event.pos[0]>=1050 and event.pos[0]<=1350) and (event.pos[1]>=700 and event.pos[1]<=800) and tableau=='mas_gains':
                tableau='menu'

                dessine_menu()
                pygame.display.flip()

        #jouer à la machine à sous
        if event.type == KEYDOWN and tableau=='mas_entrer_somme':
            for el in liste_nb:
                if el==event.key:
                    if len(somme)<8:
                        screen.blit(mas_rectangle_somme, mas_rectangle_somme_pos)
                    
                        somme=somme+dico_nb[el]
                        afficher = font.render(somme, 1, (0, 0, 0))
                        screen.blit(afficher, (500,600))
                        pygame.display.flip()
                    else:
                        somme=somme[0:7]+dico_nb[el]

                        screen.blit(mas_rectangle_somme, mas_rectangle_somme_pos)
                        
                        afficher = font.render(somme, 1, (0, 0, 0))
                        screen.blit(afficher, (500,600))
                        pygame.display.flip()

            if event.key == K_BACKSPACE:
                screen.blit(mas_rectangle_somme, mas_rectangle_somme_pos)
                
                somme=somme[0:len(somme)-1]
                afficher = font.render(somme, 1, (0, 0, 0))
                screen.blit(afficher, (500,600))
                pygame.display.flip()

            if event.key == K_RETURN:
                if somme=='':
                    somme='0'
                if compte[2]>=int(somme) and int(somme)>0:
                    tableau='mas_gains'

                    gains=slot_partie(int(somme))
                    
                    screen.fill(white)

                    if gains > 0 :
                        compte[2]=compte[2]-int(somme)+gains
                        
                        cur.execute("UPDATE membres SET argent = ? WHERE identifiant = ?", (compte[2], compte[0]))
                        conn.commit()
                        
                        screen.blit(mas_gains, mas_gains_pos)
                        afficher = font2.render('Vous avez gagné '+str(gains)+' dollars', 1, (0, 0, 0))
                        screen.blit(afficher, (500,400))
                        screen.blit(mas_rejouer, mas_rejouer_pos)
                        screen.blit(mas_quitter, mas_quitter_pos)
                        pygame.display.flip()
                    else:
                        compte[2]=compte[2]-int(somme)

                        cur.execute("UPDATE membres SET argent = ? WHERE identifiant = ?", (compte[2], compte[0]))
                        conn.commit()

                        screen.blit(mas_gains, mas_gains_pos)
                        afficher = font2.render('Vous avez perdu votre mise', 1, (0, 0, 0))
                        screen.blit(afficher, (500,400))
                        screen.blit(mas_rejouer, mas_rejouer_pos)
                        screen.blit(mas_quitter, mas_quitter_pos)
                        pygame.display.flip()
                else:
                    tableau='mas_somme'

                    screen.fill(white)
                    screen.blit(mas_somme_non_valide, (0, 0))
                    screen.blit(mas_rectangle_somme, mas_rectangle_somme_pos)
                    pygame.display.flip()

                

            
