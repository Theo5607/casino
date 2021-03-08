import sys, time, pygame
from sqlite3 import *
from pygame.locals import *
from Casino_Matvei.slot_machine import slot_partie
from casino_leonardo.roulette_fin import roulette

#Création de la base de données

conn = connect("data.txt")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS membres (identifiant TEXT, mdp TEXT, argent INTEGER)")

#Couleur RGB pour le fond de l'écran

black = 0, 0, 0
white = 255, 255, 255

#Tant que la valeur est à 1, le jeu continuera
jouer=1

#La valeur 'tableau' est utilisée pour vérifier dans quel écran le joueur se situe
tableau='bienvenue'

#Inititalisation de Pygame
pygame.init()

#Déclaration de l'écran Pygame
screen = pygame.display.set_mode((1600, 900))

#Chargement images connexion
connexion = pygame.image.load("Images/Connexion/connexion.png")
connexion_pos = (600, 400)
inscription = pygame.image.load("Images/Connexion/inscription.png")
inscription_pos = (600, 600)

rectangle = pygame.image.load("Images/Connexion/rectangle.png")

curseur = pygame.image.load("Images/Connexion/curseur.png")

alerte = pygame.image.load("Images/Connexion/alerte.png")

retour = pygame.image.load("Images/Connexion/retour.png")

#Chargement images entree casino

entreecasino = pygame.image.load("Images/Menu/entree_casino.png")
btn_entrer = pygame.image.load("Images/Menu/btn_entrer.png")
btn_entrer_pos = (650, 700)

#Chargement images menu choix du jeu
fond = pygame.image.load("Images/Menu_jeu/hall_casino.png")

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

#Chargement images roulette

roulette_tapis = pygame.image.load("Images/Jeux/Roulette/tapis.png")
roulette_tapis_bleu = pygame.image.load("Images/Jeux/Roulette/tapis_bleu.png")

fond_nb_vert = pygame.image.load("Images/Jeux/Roulette/fond_nb_vert.png")
fond_nb_bleu = pygame.image.load("Images/Jeux/Roulette/fond_nb_bleu.png")

zero_vert = pygame.image.load("Images/Jeux/Roulette/zero_vert.png")
zero_bleu = pygame.image.load("Images/Jeux/Roulette/zero_bleu.png")
zero_pos = (21, 83)

ligne_vert = pygame.image.load("Images/Jeux/Roulette/ligne_vert.png")
ligne_bleu = pygame.image.load("Images/Jeux/Roulette/ligne_bleu.png")

#Chargement images machine à sous

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

#-----------
#Chargement polices

font = pygame.font.Font("Polices/dejavu_sansbold.ttf", 100)
font2 = pygame.font.Font("Polices/dejavu_sansbold.ttf", 50)

#-----------
#Affichage de l'image de connexion au début du programme
screen.fill(white)
phrase = font2.render('Bienvenue dans le casino Umthombo !', 1, (0, 0, 0))
longueur_phrase = phrase.get_rect().width
screen.blit(phrase, ((1600-longueur_phrase)/2, 200))
screen.blit(inscription, inscription_pos)
screen.blit(connexion, connexion_pos)
pygame.display.flip()

def ret_spec(nb):
    """Prend en argument un nombre correspondant à celui des cartes de jeu et retourne une string contenant le nom de la carte"""
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
    """Crée un dictionnaire de cartes contenant pour chaque carte qui est une clé sa valeur, son nom et sa couleur"""
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

#Crée un dictionnaire de cartes grâce à la fonction ci-dessus
liste_cartes=crea_liste_cartes()

#Liste des touches correspondant au nombres/lettres du clavier
liste_nb = (K_0, K_1, K_2, K_3, K_4, K_5, K_6, K_7, K_8, K_9)
liste_lettres = (K_a, K_b, K_c, K_d, K_e, K_f, K_g, K_h, K_i, K_j, K_k, K_l, K_m, K_n, K_o, K_p, K_q, K_r, K_s, K_t, K_u, K_v, K_w, K_x, K_y, K_z)

#La boucle assigne à chaque touche qui est la clé sa valeur numérique
dico_nb = {}
var=0
for el in liste_nb:
    dico_nb[el]=str(var)
    var+=1

dico_lettre = {}
liste_lettre_str = ('a','b','c','d','e','f','g','h','i','j','q','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
var=0
for el in liste_lettres:
    dico_lettre[el]=liste_lettre_str[var]
    var+=1

dico_touches = {}
for el in dico_nb.keys():
    dico_touches[el]=str(dico_nb[el])
for el in dico_lettre.keys():
    dico_touches[el]=dico_lettre[el]

def go():
    """Pour se connecter au casino et lancer le casino avec Pygame"""
    print('Bienvenue au Casino ! Veuillez commencer par créer un compte ou vous connecter.')

    #Variable pour les entrées utilisateurs
    var=''

    #Liste qui contient les informations du compte
    compte=[]

    #Si la variable 'var' est différente de 0 ou 1, qui sont les deux possibilités pour se connecter ou s'inscrir
    while var!='1' and var!='0':
        var = input('Voulez vous vous connecter (0) ou vous inscrire (1)? ')

    #Si la variable 'var'=0, l'utilisateur veut se connecter
    if var=='0':
        #Le nom d'utilisateur entré par le joueur
        id_entre=''
        #Mis dans un singulet (pour vérifier avec la table de données)
        sing=(id_entre,)
        #Le mot de pass entré par l'utilisateur
        mdp_entre=''

        #Tant que le nom d'utilisateur est invalide, on lui redemande
        while len(id_entre)<4 or len(id_entre)>20 or check_identifiant_existe(sing)==False:
            id_entre=input("Veuillez entrer un identifiant valide et qui existe ")
            sing=(id_entre,)

        #Tant que le mot de passe est invalide, on lui redemande
        mdp_entre=input("Entrez votre mot de passe ")
        while len(mdp_entre)<4 or len(mdp_entre)>20 or check_mdp(id_entre)!=mdp_entre:
            mdp_entre=input("Mot de passe invalide ")

        #On récupère l'argent de l'utilisateur depuis la base de données
        cur.execute("SELECT argent FROM membres WHERE identifiant = ?",(id_entre,))
        argent_sing=cur.fetchone()

        #On rentre toutes les données dans la variable 'compte'
        compte=[id_entre, mdp_entre, argent_sing[0]]
            
        print('Bienvenue, '+id_entre)

        #Affichage de l'entrée du casino
        screen.fill(black)
        screen.blit(entreecasino, (0, 0))
        screen.blit(btn_entrer, btn_entrer_pos)
        pygame.display.flip()

        #Retourne le compte de l'utilisateur
        return compte

    #Si la variable 'var'=1, l'utilisateur veut s'inscrire
    if var=='1':
        #On appelle la fonction 'creation_compte' qui retourne une liste avec les informations du compte
        compte=creation_compte()
        print('Bienvenue, '+compte[0])

        #Affichage de l'entrée du casino
        screen.fill(black)
        screen.blit(entreecasino, (0, 0))
        screen.blit(btn_entrer, btn_entrer_pos)
        pygame.display.flip()

        #Retourne le compte de l'utilisateur
        return compte

def creation_compte():
    """Fonction qui permet à l'utilisateur de créer un compte et qui retourne une liste avec ses informations"""
    #Le nom d'utilisateur entré par le joueur
    identifiant=''
    #Mis dans un singulet (pour vérifier avec la table de données)
    sing=(identifiant,)
    #Le mot de pass entré par l'utilisateur
    mdp=''

    #Tant que le nom d'utilisateur est invalide, on lui redemande
    identifiant=input("Choisissez un identifiant. ")
    while len(identifiant)<4 or len(identifiant)>20 or check_identifiant_existe(sing)==True:
        identifiant=input("Veuillez choisir un identifiant entre 4 et 20 caractères qui n'existe pas. ")
        sing=(identifiant,)

    #Tant que le mot de passe est invalide, on lui redemande
    mdp=input('Choisissez un mot de passe. ')
    while len(mdp)<4 or len(mdp)>20:
        mdp=input('Veuillez choisir un mot de passe entre 4 et 20 caractères. ')

    #On rentre les informations du compte dans la base de données
    var =[(identifiant, mdp, 10000)]
    for i in var:
        cur.execute("INSERT INTO membres(identifiant, mdp, argent) VALUES(?,?,?)", i)
    conn.commit()

    #On rentre toutes les données dans la variable 'compte'
    compte=[identifiant,mdp,10000]

    #Retourne le compte de l'utilisateur
    return compte

def check_identifiant_existe(sing):
    """Fonction qui recherche un identifiant pris en paramètre dans la base de données et renvoir un booléen pour savoir s'il existe"""
    #On récupère tous les utilisateurs de la base de données
    cur.execute("SELECT identifiant FROM membres")
    liste_identifiants=cur.fetchall()

    #Variable booléenne qui sera renvoyée
    id_existe_deja=False

    #Pour chaque identifiant, on vérifie s'il est égal à celui pris en paramètre
    #Si oui, 'id_existe_deja' est vrai. Si non, 'id_existe_deja' est faux
    for el in liste_identifiants:
        if el[0]==sing[0]:
            id_existe_deja=True

    #Renvoie 'id_existe_deja'
    return id_existe_deja

def check_mdp(identifiant):
    """Renvoie le mot de passe lié à un identifiant pris en paramètre"""
    #Récupération du mot de passe à partirde l'identifiant
    cur.execute("SELECT mdp FROM membres WHERE identifiant = ?",(identifiant,))
    mdp_sing=cur.fetchone()

    #On renvoie cet identifiant
    return mdp_sing[0]

#Cette variable sera utlisée dans la boucle infinie de Pygame
#compte=go()
compte=[]

#variables connexion
str_uti=''
long_uti=0
str_mdp=''
str_mdp_cache=''
mdp_cache_verification=True
long_mdp=0
long_mdp_cache=0

#variables profil
font_profil = pygame.font.Font("Polices/coolvetica.ttf", 70)
font_argent = font2 = pygame.font.Font("Polices/dejavu_sansbold.ttf", 30)
mdp_cache_verif=True
pos_oeil_gauche=0

#variables roulette
paris={"mise_rouge" : 0, "mise_noir" : 0,"mise_colone1" : 0,"mise_colone2" : 0,"mise_colone3" : 0,"mise_douzaine1" : 0,"mise_douzaine2" : 0,"mise_douzaine3" : 0,"mise_1_à_18" : 0,"mise_19_à_36" : 0,"mise_impair" : 0,"mise_pair" : 0,"ligne_1" : 0,"ligne_2" : 0,"ligne_3" : 0}
for i in range(0, 37):
    paris[i]=0
somme=''
pari_actuel=[]
nb_actuel=[0]

#variables machine à sous
somme=''
gains=0

def conn_inscr(n):
    screen.fill(white)
    utilisateur = font2.render("Nom d'utilisateur:", 1, (0, 0, 0))
    longueur_utilisateur = utilisateur.get_rect().width
    screen.blit(utilisateur, ((1600-longueur_utilisateur)/2, 100))

    mdp = font2.render("Mot de passe:", 1, (0, 0, 0))
    longueur_mdp = mdp.get_rect().width
    screen.blit(mdp, ((1600-longueur_mdp)/2, 500))

    screen.blit(rectangle, (300, 250))
    screen.blit(rectangle, (300, 650))
    screen.blit(oeil, (1320, 700))
    screen.blit(curseur, (310, 260))
    screen.blit(retour, (1350, 800))

def dessine_menu():
    """Fonction qui dessine le menu"""
    screen.blit(fond, (0,0))
    screen.blit(banderole, (0, 0))
    screen.blit(profil, profil_pos)
    screen.blit(blackjack_icone, blackjack_icone_pos)
    screen.blit(slot_icone, slot_icone_pos)
    screen.blit(roulette_icone, roulette_icone_pos)
    screen.blit(quitter, quitter_pos)

def check_tapis(clic):
    """Fonction qui vérifie un clic dans le tapis de la roulette pour parier, si il correspond à un nombre ou un pari spécifique, la fonction le renvoie"""
    liste_nb_roulette=[3,2,1]
    nombre=0
    ligne=1
    colonne=1
    #Coordonées à vérifier pour le clic des nombres
    coordonnees=[187, 84]
    coordonnees_zero=[18, 82]
    #Boucle for qui traverse les 3 lignes
    for ligne in range(0,3):
        #Boucle for qui traverse toutes les colonnes
        for colonne in range(0,12):
            #On récupère le nombre correspondant à la ligne et colonne
            nombre=liste_nb_roulette[ligne]+3*(colonne)
            #On vérifie les coordonnées du clic
            if(clic[0]>=coordonnees[0] and clic[0]<=coordonnees[0]+103) and (clic[1]>=coordonnees[1] and clic[1]<=coordonnees[1]+103):
                #On retourne le nombre et on change le fond du nombre selon si il avait été sélectionné ou pas
                if paris[nombre]==0:
                    screen.blit(fond_nb_bleu, (coordonnees[0], coordonnees[1]))
                    pygame.display.flip()
                    return [nombre, 1]
                elif paris[nombre]==1:
                    screen.blit(fond_nb_vert, (coordonnees[0], coordonnees[1]))
                    pygame.display.flip()
                    return [nombre, 0]
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

    #Coordonées à vérifier pour le clic des lignes
    coordonnees_ligne=[1465, 84]
    #Boucle qui traverse les 3 lignes
    for i in range(0,3):
        #On vérifie les coordonnées du clic
        if(clic[0]>=coordonnees_ligne[0] and clic[0]<=coordonnees_ligne[0]+102) and (clic[1]>=coordonnees_ligne[1]+i*111 and clic[1]<=coordonnees_ligne[1]+i*(111)+105):
            #On retourne le nom de la ligne et on change le fond du nombre selon si il avait été sélectionné ou pas
            if paris['ligne_'+str(i+1)]==0:
                screen.blit(ligne_bleu, (coordonnees_ligne[0], coordonnees_ligne[1]+i*111))
                pygame.display.flip()
                return ['ligne_'+str(i+1), 1]
            elif paris['ligne_'+str(i+1)]==1:
                screen.blit(ligne_vert, (coordonnees_ligne[0], coordonnees_ligne[1]+i*111))
                pygame.display.flip()
                return ['ligne_'+str(i+1), 0]

    #On vérifie si on clique sur 0
    if(clic[0]>=coordonnees_zero[0] and clic[0]<=coordonnees_zero[0]+165) and (clic[1]>=coordonnees_zero[1] and clic[1]<=coordonnees_zero[1]+330) and tableau=='roulette_tapis':
        if paris[0]==0:
            screen.blit(zero_bleu, zero_pos)
            pygame.display.flip()
            return [0, 1]
        elif paris[0]==1:
            screen.blit(zero_vert, zero_pos)
            pygame.display.flip()
            return [0, 0]

    #On retourne une liste vide si les vérifications de clic n'ont pas été concluantes.
    return []

def pari(nom_pari):
    """Affiche à l'écran Combien voulez-vous parier sur 'nom_du_pari'"""
    screen.fill(white)
    phrase = font2.render("Combien voulez vous miser sur "+str(nom_pari)+" ?", 1, (0, 0, 0))
    longueur_phrase = phrase.get_rect().width
    screen.blit(phrase, ((1600-longueur_phrase)/2, 420))

    #On enlève le premier élément de la liste 'pari_actuel' et on l'assigne à 'nb'
    nb=pari_actuel.pop(0)
                        
    screen.blit(mas_rectangle_somme, mas_rectangle_somme_pos)
    pygame.display.flip()

    #On retourne le pari supprimé de 'par_actuel'
    return nb

#Début de la boucle infinie de Pygame
while jouer==1:
    pygame.display.flip()
    #Event listener
    for event in pygame.event.get():
        #Si on clique sur la croix en haut à croite, on arrête la boucle de jeu
        if event.type == QUIT:
            jouer = 0

        #On vérifie l'événement est clic gauche relâché
        if event.type == MOUSEBUTTONUP and event.button == 1:
            #boutons bienvenue

            #bouton connexion
            if(event.pos[0]>=600 and event.pos[0]<=1000) and (event.pos[1]>=400 and event.pos[1]<=500) and tableau=='bienvenue':
                tableau='conn_entrer_uti'
                conn_inscr(0)

            #bouton inscription
            elif(event.pos[0]>=600 and event.pos[0]<=1000) and (event.pos[1]>=600 and event.pos[1]<=700) and tableau=='bienvenue':
                tableau='inscr_entrer_uti'
                conn_inscr(1)

            #----------------
            #boutons inscription
            elif(event.pos[0]>=300 and event.pos[0]<=1300) and (event.pos[1]>=250 and event.pos[1]<=400) and tableau=='inscr_entrer_mdp':
                tableau='inscr_entrer_uti'
                
                screen.blit(rectangle, (300, 250))
                screen.blit(rectangle, (300, 650))
                uti = font.render(str_uti, 1, (0, 0, 0))
                screen.blit(uti, (300, 250))
                mdp = font.render(str_mdp, 1, (0, 0, 0))
                screen.blit(mdp, (300, 650))
                
                screen.blit(curseur, (300+long_uti+10, 260))
                pygame.display.flip()

            elif(event.pos[0]>=300 and event.pos[0]<=1300) and (event.pos[1]>=650 and event.pos[1]<=800) and tableau=='inscr_entrer_uti':
                tableau='inscr_entrer_mdp'

                screen.blit(rectangle, (300, 250))
                screen.blit(rectangle, (300, 650))
                uti = font.render(str_uti, 1, (0, 0, 0))
                screen.blit(uti, (300, 250))
                mdp = font.render(str_mdp, 1, (0, 0, 0))
                screen.blit(mdp, (300, 650))
                
                screen.blit(curseur, (300+long_mdp+10, 660))
                pygame.display.flip()
                
                
            #boutons connexion
            elif(event.pos[0]>=300 and event.pos[0]<=1300) and (event.pos[1]>=250 and event.pos[1]<=400) and tableau=='conn_entrer_mdp':
                tableau='conn_entrer_uti'
                
                screen.blit(rectangle, (300, 250))
                screen.blit(rectangle, (300, 650))
                uti = font.render(str_uti, 1, (0, 0, 0))
                screen.blit(uti, (300, 250))
                mdp = font.render(str_mdp, 1, (0, 0, 0))
                screen.blit(mdp, (300, 650))
                
                screen.blit(curseur, (300+long_uti+10, 260))
                pygame.display.flip()

            elif(event.pos[0]>=300 and event.pos[0]<=1300) and (event.pos[1]>=650 and event.pos[1]<=800) and tableau=='conn_entrer_uti':
                tableau='conn_entrer_mdp'

                screen.blit(rectangle, (300, 250))
                screen.blit(rectangle, (300, 650))
                uti = font.render(str_uti, 1, (0, 0, 0))
                screen.blit(uti, (300, 250))
                mdp = font.render(str_mdp, 1, (0, 0, 0))
                screen.blit(mdp, (300, 650))
                
                screen.blit(curseur, (300+long_mdp+10, 660))
                pygame.display.flip()
                

            #bouton retour
            elif(event.pos[0]>=1350 and event.pos[0]<=1550) and (event.pos[1]>=800 and event.pos[1]<=850) and (tableau=='conn_entrer_uti' or tableau=='conn_entrer_mdp' or tableau=='inscr_entrer_uti' or tableau=='inscr_entrer_mdp'):
                tableau='bienvenue'

                str_uti=''
                long_uti=0
                str_mdp=''
                str_mdp_cache=''
                mdp_cache_verification=True
                long_mdp=0
                long_mdp_cache=0
                
                screen.fill(white)
                phrase = font2.render('Bienvenue dans le casino Umthombo !', 1, (0, 0, 0))
                longueur_phrase = phrase.get_rect().width
                screen.blit(phrase, ((1600-longueur_phrase)/2, 200))
                screen.blit(inscription, inscription_pos)
                screen.blit(connexion, connexion_pos)
                pygame.display.flip()

            #bouton oeil pour cacher ou montrer le mdp
            elif(event.pos[0]>=1320 and event.pos[0]<=1420) and (event.pos[1]>=700 and event.pos[1]<=750) and (tableau=='connexion' or tableau=='conn_entrer_uti' or tableau=='conn_entrer_mdp' or tableau=='inscr_entrer_uti' or tableau=='inscr_entrer_mdp'):
                screen.blit(rectangle, (300, 650))
                if mdp_cache_verification==True:
                    mdp = font.render(str_mdp, 1, (0, 0, 0))
                    screen.blit(mdp, (300, 650))
                    screen.blit(curseur, (300+10+long_mdp, 660))
                    mdp_cache_verification=False
                elif mdp_cache_verification==False:
                    mdp_cache = font.render(str_mdp_cache, 1, (0, 0, 0))
                    screen.blit(mdp_cache, (300, 650))
                    screen.blit(curseur, (300+10+long_mdp_cache, 660))
                    mdp_cache_verification=True
                
            #----------------
            #bouton entree
            if(event.pos[0]>=650 and event.pos[0]<=950) and (event.pos[1]>=700 and event.pos[1]<=800) and tableau=='entree':
                tableau='menu'

                dessine_menu()
                pygame.display.flip()
                
            #boutons menu jeu

            #Bouton pour accéder au profil
            elif(event.pos[0]>=1450 and event.pos[0]<=1550) and (event.pos[1]>=20 and event.pos[1]<=70) and tableau=='menu':
                tableau='profil'

                #Déclaration du mot de passe caché, c'est à dire sous cette forme : *****
                mdp_cache_str=''
                for car in compte[1]:
                    mdp_cache_str=mdp_cache_str+'*'

                #Affichage du profil
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

            #Bouton icône machine à sous
            elif(event.pos[0]>=900 and event.pos[0]<=1350) and (event.pos[1]>=170 and event.pos[1]<=420) and tableau=='menu':
                tableau='mas_menu'

                #Affichage du menu de la machine à sous
                screen.fill(white)
                screen.blit(mas_jouer, mas_jouer_pos)
                screen.blit(mas_retour, mas_retour_pos)
                pygame.display.flip()

            #Bouton icône roulette
            elif(event.pos[0]>=500 and event.pos[0]<=1100) and (event.pos[1]>=550 and event.pos[1]<=800) and tableau=='menu':
                tableau='roulette_menu'

                #Affichage du menu de la roulette
                screen.fill(white)
                screen.blit(mas_jouer, mas_jouer_pos)
                screen.blit(mas_retour, mas_retour_pos)
                pygame.display.flip()

            #Bouton quiter le casion
            elif(event.pos[0]>=1300 and event.pos[0]<=1550) and (event.pos[1]>=770 and event.pos[1]<=850) and tableau=='menu':
                #Stopper la boucle infinie
                jouer = 0
            #----------------
            #boutons profil

            #Bouton de retour
            elif(event.pos[0]>=1300 and event.pos[0]<=1550) and (event.pos[1]>=770 and event.pos[1]<=850) and tableau=='profil':
                tableau='menu'

                #Affichage du menu
                dessine_menu()
                pygame.display.flip()

            #Bouton oeil pour cacher ou montrer le mot de passe
            elif(event.pos[0]>=pos_oeil_gauche and event.pos[0]<=pos_oeil_gauche+100) and (event.pos[1]>=360 and event.pos[1]<=410) and tableau=='profil':
                screen.blit(rect_blanc, rect_blanc_pos)

                #La variable booléenne 'mdp_cache_verif' nous dit si le mot de passe est caché ou pas
                if mdp_cache_verif==True:
                    mdp_cache_verif=False

                    #Affichage du mot de passe
                    mdp = font_argent.render('Votre mot de passe : '+compte[1], 1, (0, 0, 0))
                    mdp_long = mdp.get_rect().width
                    screen.blit(mdp, (550, 370))
                    pos_oeil_gauche=mdp_long+30+550
                    screen.blit(oeil, (pos_oeil_gauche, 360))
                else:
                    mdp_cache_verif=True

                    #Affichage du mot de passe caché
                    mdp_cache = font_argent.render('Votre mot de passe : '+mdp_cache_str, 1, (0, 0, 0))
                    mdp_long = mdp_cache.get_rect().width
                    screen.blit(mdp_cache, (550, 370))
                    pos_oeil_gauche=mdp_long+30+550
                    screen.blit(oeil, (pos_oeil_gauche, 360))

                pygame.display.flip()

            #------------
            #boutons roulette

            #Bouton retour
            elif(event.pos[0]>=900 and event.pos[0]<=1300) and (event.pos[1]>=300 and event.pos[1]<=500) and tableau=='roulette_menu':
                tableau='menu'

                #Affichage du menu
                dessine_menu()
                pygame.display.flip()

            #Bouton jouer
            elif(event.pos[0]>=300 and event.pos[0]<=700) and (event.pos[1]>=300 and event.pos[1]<=500) and tableau=='roulette_menu':
                tableau='roulette_tapis'

                #Affichage du tapis pour parier
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

            #Clic sur le tapis
            elif tableau=='roulette_tapis':
                liste_paris=check_tapis(event.pos)
                if len(liste_paris)!=0:
                    paris[liste_paris[0]]=liste_paris[1]

                    print(paris)
                    
            #bouton rejouer
            elif(event.pos[0]>=550 and event.pos[0]<=850) and (event.pos[1]>=700 and event.pos[1]<=800) and tableau=='roulette_gains':
                tableau='roulette_tapis'

                #Affichage du tapis pour parier
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

            #Bouton quitter
            elif(event.pos[0]>=1050 and event.pos[0]<=1350) and (event.pos[1]>=700 and event.pos[1]<=800) and tableau=='roulette_gains':
                tableau='menu'

                #Affiche le menu
                dessine_menu()
                pygame.display.flip()

            #------------
            #boutons menu machine à sous

            #Bouton jouer
            elif(event.pos[0]>=300 and event.pos[0]<=700) and (event.pos[1]>=300 and event.pos[1]<=500) and tableau=='mas_menu':
                tableau='mas_somme'

                #Affichage du rectangle pour parier
                screen.fill(white)
                screen.blit(mas_somme, (0, 0))
                screen.blit(mas_rectangle_somme, mas_rectangle_somme_pos)
                pygame.display.flip()

            #Bouton retour
            elif(event.pos[0]>=900 and event.pos[0]<=1300) and (event.pos[1]>=300 and event.pos[1]<=500) and tableau=='mas_menu':
                tableau='menu'

                dessine_menu()
                pygame.display.flip()

            #boutons rectangle somme machine à sous
            elif(event.pos[0]>=600 and event.pos[0]<=1000) and (event.pos[1]>=600 and event.pos[1]<=700) and tableau=='mas_somme':
                somme=''
                tableau='mas_entrer_somme'

                #Affiche 0 dans le rectangle si on clique sur le rectangle
                afficher = font.render('0', 1, (0, 0, 0))
                screen.blit(afficher, (500,600))
                pygame.display.flip()

            #bouton rejouer
            elif(event.pos[0]>=550 and event.pos[0]<=850) and (event.pos[1]>=700 and event.pos[1]<=800) and tableau=='mas_gains':
                tableau='mas_somme'

                screen.fill(white)
                screen.blit(mas_somme, (0, 0))
                screen.blit(mas_rectangle_somme, mas_rectangle_somme_pos)
                pygame.display.flip()

            #Bouton quitter
            elif(event.pos[0]>=1050 and event.pos[0]<=1350) and (event.pos[1]>=700 and event.pos[1]<=800) and tableau=='mas_gains':
                tableau='menu'

                #Affiche le menu
                dessine_menu()
                pygame.display.flip()

        #On vérifie si on clique sur une touche lors de la connexion
        if event.type == KEYDOWN and (tableau=='conn_entrer_uti' or tableau=='conn_entrer_mdp' or tableau=='inscr_entrer_uti' or tableau=='inscr_entrer_mdp'):
            liste_touches=liste_nb+liste_lettres
            for el in liste_touches:
                if tableau=='conn_entrer_uti' or tableau=='inscr_entrer_uti':
                    if el==event.key:
                        if len(str_uti)<12:
                            screen.blit(rectangle, (300, 250))

                            str_uti=str_uti+str(dico_touches[el])
                            afficher = font.render(str_uti, 1, (0, 0, 0))
                            screen.blit(afficher, (300, 250))

                            long_uti=afficher.get_rect().width
                            screen.blit(curseur, (300+long_uti+10,260))
                        
                            pygame.display.flip()
                        else:
                            str_uti=str_uti[0:11]+dico_touches[el]
                            
                            screen.blit(rectangle, (300, 250))
                            
                            afficher = font.render(str_uti, 1, (0, 0, 0))
                            screen.blit(afficher, (300, 250))

                            long_uti=afficher.get_rect().width
                            screen.blit(curseur, (300+long_uti+10,260))
                            
                            pygame.display.flip()
                elif tableau=='conn_entrer_mdp' or tableau=='inscr_entrer_mdp':
                    if el==event.key:
                        if len(str_mdp)<12:
                            screen.blit(rectangle, (300, 650))

                            str_mdp=str_mdp+str(dico_touches[el])
                            str_mdp_cache+='*'
                            
                            afficher_cache = font.render(str_mdp_cache, 1, (0, 0, 0))
                            long_mdp_cache=afficher_cache.get_rect().width
                            afficher = font.render(str_mdp, 1, (0, 0, 0))
                            long_mdp=afficher.get_rect().width
                            
                            if mdp_cache_verification==True:
                                screen.blit(afficher_cache, (300, 650))
                                screen.blit(curseur, (300+long_mdp_cache+10,660))
                            elif mdp_cache_verification==False:
                                screen.blit(afficher, (300, 650))
                                screen.blit(curseur, (300+long_mdp+10,660))

                            long_mdp=afficher.get_rect().width
                        
                            pygame.display.flip()
                        else:
                            str_mdp=str_mdp[0:11]+dico_touches[el]
                            
                            screen.blit(rectangle, (300, 650))

                            afficher_cache = font.render(str_mdp_cache, 1, (0, 0, 0))
                            long_mdp_cache=afficher_cache.get_rect().width
                            afficher = font.render(str_mdp, 1, (0, 0, 0))
                            long_mdp=afficher.get_rect().width
                            
                            if mdp_cache_verification==True:
                                screen.blit(afficher_cache, (300, 650))
                                screen.blit(curseur, (300+long_mdp_cache+10,660))
                            elif mdp_cache_verification==False:
                                screen.blit(afficher, (300, 650))
                                screen.blit(curseur, (300+long_mdp+10,660))

                            long_mdp=afficher.get_rect().width
                            
                            pygame.display.flip()
                        
            if event.key == K_BACKSPACE:
                if tableau=='conn_entrer_uti' or tableau=='inscr_entrer_uti':
                    screen.blit(rectangle, (300, 250))
                    
                    str_uti=str_uti[0:len(str_uti)-1]
                    afficher = font.render(str_uti, 1, (0, 0, 0))
                    screen.blit(afficher, (300,250))

                    long_uti=afficher.get_rect().width
                    screen.blit(curseur, (300+long_uti+10,260))
                    
                    pygame.display.flip()
                elif tableau=='conn_entrer_mdp' or tableau=='inscr_entrer_mdp':
                    screen.blit(rectangle, (300, 650))
                    
                    str_mdp=str_mdp[0:len(str_mdp)-1]
                    str_mdp_cache=str_mdp_cache[0:len(str_mdp_cache)-1]
                    afficher_cache = font.render(str_mdp_cache, 1, (0, 0, 0))
                    long_mdp_cache=afficher_cache.get_rect().width
                    afficher = font.render(str_mdp, 1, (0, 0, 0))
                    long_mdp=afficher.get_rect().width
                    if mdp_cache_verification==True:
                        screen.blit(afficher_cache, (300, 650))
                        screen.blit(curseur, (300+long_mdp_cache+10,660))
                    elif mdp_cache_verification==False:
                        screen.blit(afficher, (300, 650))
                        screen.blit(curseur, (300+long_mdp+10,660))

                    screen.blit(curseur, (300+long_mdp+10,660))
                    
                    pygame.display.flip()

            if event.key == K_RETURN:
                if tableau=='conn_entrer_uti' or tableau=='conn_entrer_mdp':
                    sing_id=(str_uti,)
                    sing_mdp=(str_mdp,)
                    if check_identifiant_existe(sing_id)==True and check_mdp(str_uti)==str_mdp:
                        cur.execute("SELECT argent FROM membres WHERE identifiant = ?",(str_uti,))
                        argent_sing=cur.fetchone()

                        compte=[str_uti, str_mdp, argent_sing[0]]

                        tableau='entree'

                        screen.fill(black)
                        screen.blit(entreecasino, (0, 0))
                        screen.blit(btn_entrer, btn_entrer_pos)
                        pygame.display.flip()

                    else:
                        screen.blit(alerte, (300, 800))
                elif tableau=='inscr_entrer_uti' or tableau=='inscr_entrer_mdp':
                    sing_id=(str_uti,)
                    sing_mdp=(str_mdp,)
                    
                    if len(str_uti)>3 or len(str_uti)<21 or check_identifiant_existe(sing_id)==False:
                        var =[(str_uti, str_mdp, 10000)]
                        for i in var:
                            cur.execute("INSERT INTO membres(identifiant, mdp, argent) VALUES(?,?,?)", i)
                        conn.commit()
                        
                        compte=[str_uti,str_mdp,10000]

                        tableau='entree'

                        screen.fill(black)
                        screen.blit(entreecasino, (0, 0))
                        screen.blit(btn_entrer, btn_entrer_pos)
                        pygame.display.flip()

                    else:
                        screen.blit(alerte, (300, 800))
                    
        #On vérifie si on clique sur une touche lors du pari de la machine à sous
        if event.type == KEYDOWN and tableau=='mas_entrer_somme':
            #On vérifie si la touche cliquée est un nombre
            for el in liste_nb:
                if el==event.key:
                    #On vérifie si la taille du nombre parié est inférieur à 8 (la taille maximum)
                    if len(somme)<8:
                        #Si oui, on affiche le nombre parié avec le nouveau chiffre et on l'ajoute à la variable 'somme'
                        screen.blit(mas_rectangle_somme, mas_rectangle_somme_pos)
                    
                        somme=somme+dico_nb[el]
                        afficher = font.render(somme, 1, (0, 0, 0))
                        screen.blit(afficher, (500,600))
                        pygame.display.flip()
                    else:
                        #Si elle égale à 8, on supprime le dernier chiffre et on ajoute le nouveau
                        somme=somme[0:7]+dico_nb[el]

                        screen.blit(mas_rectangle_somme, mas_rectangle_somme_pos)
                        
                        afficher = font.render(somme, 1, (0, 0, 0))
                        screen.blit(afficher, (500,600))
                        pygame.display.flip()

            #On vérifie si la touche cliquée est 'Retour'
            if event.key == K_BACKSPACE:
                #On supprime le dernier chiffre de l'affichage et de la variable 'somme'
                screen.blit(mas_rectangle_somme, mas_rectangle_somme_pos)
                
                somme=somme[0:len(somme)-1]
                afficher = font.render(somme, 1, (0, 0, 0))
                screen.blit(afficher, (500,600))
                pygame.display.flip()

            #On vérifie si la touche cliquée est 'Entrée'
            elif event.key == K_RETURN:
                #Sil la somme est nulle, alors elle sera égale à 0 (et invalide)
                if somme=='':
                    somme='0'

                #Si le joueur a assez d'argent pour parier et que 'somme'>0, alors il peut jouer
                if compte[2]>=int(somme) and int(somme)>0:
                    tableau='mas_gains'

                    #On appelle la fonction roulette qui retourne les gains ou 0 si on perd
                    gains=slot_partie(int(somme))

                    screen.fill(white)

                    #Si les gains sont supérieurs à 0, le joueur à gagné
                    if gains[0] > 0 :
                        #On met à jour la variable 'compte'
                        compte[2]=compte[2]-int(somme)+gains[0]

                        #On met à jour la base de données
                        cur.execute("UPDATE membres SET argent = ? WHERE identifiant = ?", (compte[2], compte[0]))
                        conn.commit()

                        #On affiche les gains du joueur
                        screen.blit(mas_gains, mas_gains_pos)
                        afficher = font2.render('Vous avez gagné '+str(gains[0])+' dollars', 1, (0, 0, 0))
                        screen.blit(afficher, (500,400))
                        screen.blit(mas_rejouer, mas_rejouer_pos)
                        screen.blit(mas_quitter, mas_quitter_pos)
                        pygame.display.flip()
                    #Si il a perdu
                    else:
                        #On met à jour la variable 'compte' en faisant la différence de son solde et de sa mise
                        compte[2]=compte[2]-int(somme)

                        #On met à jour la base de données
                        cur.execute("UPDATE membres SET argent = ? WHERE identifiant = ?", (compte[2], compte[0]))
                        conn.commit()

                        #On affiche que le joueur a perdu
                        screen.blit(mas_gains, mas_gains_pos)
                        afficher = font2.render('Vous avez perdu votre mise', 1, (0, 0, 0))
                        screen.blit(afficher, (500,400))
                        screen.blit(mas_rejouer, mas_rejouer_pos)
                        screen.blit(mas_quitter, mas_quitter_pos)
                        pygame.display.flip()
                        
                #Sinon, on affiche que la somme misée est invalide
                else:
                    tableau='mas_somme'

                    screen.fill(white)
                    screen.blit(mas_somme_non_valide, (0, 0))
                    screen.blit(mas_rectangle_somme, mas_rectangle_somme_pos)
                    pygame.display.flip()

        #On vérifie si on clique sur une touche lors du pari de la roulette
        if event.type == KEYDOWN and tableau=='roulette_miser':
            #On vérifie si la touche cliquée est un nombre
            for nb in liste_nb:
                if nb==event.key:
                    #On vérifie si la taille du nombre parié est inférieur à 8 (la taille maximum)
                    if len(somme)<8:
                        #Si oui, on affiche le nombre parié avec le nouveau chiffre et on l'ajoute à la variable 'somme'
                        somme=somme+dico_nb[nb]
                        afficher = font.render(somme, 1, (0, 0, 0))
                        screen.blit(afficher, (500,600))
                        pygame.display.flip()
                        #Si elle égale à 8, on supprime le dernier chiffre et on ajoute le nouveau
                    else:
                        somme=somme[0:7]+dico_nb[nb]
                                            
                        screen.blit(mas_rectangle_somme, (500,600))
                        afficher = font.render(somme, 1, (0, 0, 0))
                        screen.blit(afficher, (mas_rectangle_somme_pos))
                        pygame.display.flip()
            #On vérifie si la touche cliquée est 'Retour'
            if event.key == K_BACKSPACE:
                #On supprime le dernier chiffre de l'affichage et de la variable 'somme'
                screen.blit(mas_rectangle_somme, mas_rectangle_somme_pos)
                    
                somme=somme[0:len(somme)-1]
                afficher = font.render(somme, 1, (0, 0, 0))
                screen.blit(afficher, (500,600))
                pygame.display.flip()

            #On vérifie si la touche cliquée est 'Entrée'
            elif event.key == K_RETURN:
                #Si le pari est invalide on affiche un message à l'utilisateur
                if somme == '':
                    screen.fill(white)
                    phrase = font2.render("La valeur doit être supérieure à 0. Combien voulez vous miser sur "+str(nb_actuel[0])+" ?", 1, (0, 0, 0))
                    longueur_phrase = phrase.get_rect().width
                    screen.blit(phrase, ((1600-longueur_phrase)/2, 420))
                                        
                    screen.blit(mas_rectangle_somme, mas_rectangle_somme_pos)
                    pygame.display.flip()

                #On appelle la fonction 'pari' pour afficher le prochain pari
                if len(pari_actuel)>0 and somme!='':
                    paris[nb_actuel[0]]=int(somme)
                    nb_actuel[0]=pari(pari_actuel[0])
                    somme=''
                #Si on a fait tous les paris, on appelle la fonction 'roulette' pour jouer à la roulette
                elif len(pari_actuel)==0 and somme!='':
                    tableau='roulette_gains'
                    
                    paris[nb_actuel[0]]=int(somme)
                    nb_actuel[0]=0
                    somme=''

                    #L'argent gagné sur la roulette
                    dico_gains=roulette(paris)
                    gains=0
                    mises_perdues=0
                    
                    for el in dico_gains.keys():
                        if dico_gains[el]>paris[el]:
                            gains+=dico_gains[el]
                        else:
                            mises_perdues-=paris[el]
                            
                    if gains+mises_perdues>=0:
                        screen.fill(white)
                        phrase = font.render('Vous avez gagné '+str(gains+mises_perdues), 1, (0, 0, 0))
                        longueur_phrase = phrase.get_rect().width
                        screen.blit(phrase, ((1600-longueur_phrase)/2, 420))
                        pygame.display.flip()
                        
                        compte[2]=compte[2]+gains+mises_perdues
                        
                        cur.execute("UPDATE membres SET argent = ? WHERE identifiant = ?", (compte[2], compte[0]))
                        conn.commit()
                        
                        screen.blit(mas_rejouer, mas_rejouer_pos)
                        screen.blit(mas_quitter, mas_quitter_pos)
                        pygame.display.flip()
                        
                    else:
                        screen.fill(white)
                        phrase = font2.render('Vous avez perdu '+str((gains+mises_perdues)*-1)+' dollars', 1, (0, 0, 0))
                        longueur_phrase = phrase.get_rect().width
                        screen.blit(phrase, ((1600-longueur_phrase)/2, 420))
                        pygame.display.flip()
                        
                        compte[2]=compte[2]+gains+mises_perdues
                        
                        cur.execute("UPDATE membres SET argent = ? WHERE identifiant = ?", (compte[2], compte[0]))
                        conn.commit()
                        
                        screen.blit(mas_rejouer, mas_rejouer_pos)
                        screen.blit(mas_quitter, mas_quitter_pos)
                        pygame.display.flip()
                        
        #On vérifie si on clique sur une touche lors du choix des paris sur le tapis de la roulette
        if event.type == KEYDOWN and tableau=='roulette_tapis':
            #Si on clique sur 'Entrée', on met en place la boucle pour les paris
            if event.key == K_RETURN:
                tableau='roulette_miser'
                for el in paris.keys():
                    if paris[el]==1:
                        pari_actuel.append(el)

                        print(pari_actuel)

                nb_actuel[0]=pari(pari_actuel[0])
pygame.quit()
