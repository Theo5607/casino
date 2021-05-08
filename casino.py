import sys, time, pygame
from sqlite3 import *
from pygame.locals import *
from Casino_Matvei.slot_machine import slot_partie
from Casino_Matvei.animation_slot import animation_machine
from casino_leonardo.roulette_fin import roulette
from casino_leonardo.roulette_fin import animation_roulette
from Casino_Teis.bj import play_blackjack
from Casino_Teis.bj import action
from Casino_Teis.bj import dessin_carte
from fonctions import *

#Création de la base de données

conn = connect("data.txt")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS membres (identifiant TEXT, mdp TEXT, argent INTEGER)")

#Couleur RGB pour le fond de l'écran

black = 0, 0, 0
white = 255, 255, 255

#importation symbole machine à sous

bar= pygame.image.load("Images/Jeux/Machine_a_sous/Symboles/lemon.png")
bar_2= pygame.image.load("Images/Jeux/Machine_a_sous/Symboles/bar.png")
bar_3= pygame.image.load("Images/Jeux/Machine_a_sous/Symboles/watermelon.png")
symb_7= pygame.image.load("Images/Jeux/Machine_a_sous/Symboles/7.png")
scatter= pygame.image.load("Images/Jeux/Machine_a_sous/Symboles/scatter.png")
cloche=pygame.image.load("Images/Jeux/Machine_a_sous/Symboles/cloche.png")
cherry = pygame.image.load("Images/Jeux/Machine_a_sous/Symboles/cherry.png")

#Tant que la valeur est à 1, le jeu continuera
jouer=1

#La valeur 'tableau' est utilisée pour vérifier dans quel écran le joueur se situe
tableau='bienvenue'

#Inititalisation de Pygame
pygame.init()

#Déclaration de l'écran Pygame
screen = pygame.display.set_mode((1600, 900))

ecran_de_demarrage(screen)

#Liste des touches correspondant au nombres/lettres du clavier
liste_nb = (K_0, K_1, K_2, K_3, K_4, K_5, K_6, K_7, K_8, K_9)
liste_lettres = (K_a, K_b, K_c, K_d, K_e, K_f, K_g, K_h, K_i, K_j, K_k, K_l, K_m, K_n, K_o, K_p, K_q, K_r, K_s, K_t, K_u, K_v, K_w, K_x, K_y, K_z)

#La boucle assigne à chaque touche qui est la clé sa valeur numérique
dico_nb = {}
var=0
for el in liste_nb:
    dico_nb[el]=str(var)
    var+=1

#La boucle assigne à chaque touche qui est la clé sa lettre associée
dico_lettre = {}
liste_lettre_str = ('a','b','c','d','e','f','g','h','i','j','q','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
var=0
for el in liste_lettres:
    dico_lettre[el]=liste_lettre_str[var]
    var+=1

#On crée un dictionnaire contenant les lettres et les nombres
dico_touches = {}
for el in dico_nb.keys():
    dico_touches[el]=str(dico_nb[el])
for el in dico_lettre.keys():
    dico_touches[el]=dico_lettre[el]

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
font_argent = font2 = pygame.font.Font("Polices/ADAM.CG_PRO.otf", 30)
mdp_cache_verif=True
pos_oeil_gauche=0

#variables roulette
def re_paris():
    paris_new={"le rouge" : 0, "le noir" : 0,"la première colonne" : 0,"la deuxième colonne" : 0,"la troisième colonne" : 0,"la première douzaine" : 0,"la deuxième douzaine" : 0,"la troisième douzaine" : 0,"la première moitié" : 0,"la deuxième moitié" : 0,"les nombres impairs" : 0,"les nombres pairs" : 0}
    for i in range(0, 37):
        paris_new[i]=0
    return paris_new
paris=re_paris()
pari_actuel=[]
nb_actuel=[0]

#variables machine à sous
gains=0

#variables blackjack
ct_jr=[]
cr_crp=[]

#variable pour entrer un pari
somme=''

def check_clic(clic, posx, posy, tableau_demande):
    """Fonction qui prend en paramètres un clic, des coordonnées et et une liste des tableaux à vérifier et qui renvoie un booléen pour vérifier si le clic est dans la zone demandée"""
    tableau_bool=False

    #la boucle parcourt la liste des tableaux à vérifier et renvoie True si il est dedans
    for el in tableau_demande:
        if el==tableau:
            tableau_bool=True

    #Vérifie les coordonnées du clic
    if tableau_bool==True:
        if(clic[0]>=posx[0] and clic[0]<=posx[1]) and (clic[1]>=posy[0] and clic[1]<=posy[1]):
            return True
        else:
            return False
    else:
        return False

def pari(nom_pari):
    """Affiche à l'écran Combien voulez-vous parier sur 'nom_du_pari'"""
    affichage_image(screen, fond_roulette, (0, 0))
    phrase = font2.render("Combien voulez vous miser sur "+str(nom_pari)+" ?", 1, (255, 255, 255))
    longueur_phrase = phrase.get_rect().width
    screen.blit(phrase, ((1600-longueur_phrase)/2, 420))

    #On enlève le premier élément de la liste 'pari_actuel' et on l'assigne à 'nb'
    nb=pari_actuel.pop(0)
                        
    screen.blit(mas_rectangle_somme, mas_rectangle_somme_pos)
    screen.blit(curseur_bj, (510, 610))
    argent = font2.render(str(compte[2])+'$', 1, (255, 255, 255))
    screen.blit(argent, (30, 30))
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
            if check_clic(event.pos, (600, 1000), (400, 500), ['bienvenue'])==True:
                tableau='conn_entrer_uti'
                time.sleep(0.15)
                conn_inscr(screen, 0)

            #bouton inscription
            elif check_clic(event.pos, (600, 1000), (600, 700), ['bienvenue'])==True:
                tableau='inscr_entrer_uti'
                conn_inscr(screen, 1)

            #----------------
            #boutons inscription/connexion (servent à replacer le curseur)
            elif check_clic(event.pos, (300, 1300), (250, 400), ['inscr_entrer_mdp', 'conn_entrer_mdp'])==True:
                if tableau=='inscr_entrer_mdp':
                    tableau='inscr_entrer_uti'
                else:
                    tableau='conn_entrer_uti'

                affichage_image(screen, curseur, (300+long_uti+10, 260))
                screen.blit(rectangle, (290, 640))

                if mdp_cache_verification==False:
                    mdp = taper_font.render(str_mdp, 1, (0, 0, 0))
                    screen.blit(mdp, (300, 650))
                else:
                    mdp_cache = taper_font.render(str_mdp_cache, 1, (0, 0, 0))
                    screen.blit(mdp_cache, (300, 650))
                    
                pygame.display.flip()
            elif check_clic(event.pos, (300, 1300), (650, 800), ['inscr_entrer_uti', 'conn_entrer_uti'])==True:
                if tableau=='inscr_entrer_uti':
                    tableau='inscr_entrer_mdp'
                else:
                    tableau='conn_entrer_mdp'

                screen.blit(rectangle, (290, 240))
                screen.blit(rectangle, (290, 640))
                uti = taper_font.render(str_uti, 1, (0, 0, 0))
                screen.blit(uti, (300, 250))

                if mdp_cache_verification==False:
                    mdp = taper_font.render(str_mdp, 1, (0, 0, 0))
                    screen.blit(mdp, (300, 650))
                    affichage_image(screen, curseur, (300+long_mdp+10, 660))
                else:
                    mdp_cache = taper_font.render(str_mdp_cache, 1, (0, 0, 0))
                    screen.blit(mdp_cache, (300, 650))
                    long_mdp_cache=mdp_cache.get_rect().width
                    affichage_image(screen, curseur, (300+long_mdp_cache+10, 660))
                pygame.display.flip()
                

            #bouton retour
            elif check_clic(event.pos, (1350, 1550), (800, 850), ['inscr_entrer_uti', 'conn_entrer_uti', 'conn_entrer_mdp', 'inscr_entrer_mdp'])==True:
                tableau='bienvenue'

                str_uti=''
                long_uti=0
                str_mdp=''
                str_mdp_cache=''
                mdp_cache_verification=True
                long_mdp=0
                long_mdp_cache=0
                
                ecran_de_demarrage(screen)

            #bouton oeil pour cacher ou montrer le mdp
            elif check_clic(event.pos, (1320, 1420), (700, 750), ['connexion','inscr_entrer_uti', 'conn_entrer_uti', 'conn_entrer_mdp', 'inscr_entrer_mdp'])==True:
                affichage_image(screen, rectangle, (290, 640))
                if mdp_cache_verification==True:
                    mdp = taper_font.render(str_mdp, 1, (0, 0, 0))
                    affichage_image(screen, mdp, (300, 650))
                    affichage_image(screen, cache_oeil, (1320, 700))
                    affichage_image(screen, oeil, (1320, 700))
                    if tableau == 'conn_entrer_mdp' or tableau == 'inscr_entrer_mdp':
                        affichage_image(screen, curseur, (300+10+long_mdp, 660))
                    mdp_cache_verification=False
                elif mdp_cache_verification==False:
                    mdp_cache = taper_font.render(str_mdp_cache, 1, (0, 0, 0))
                    screen.blit(mdp_cache, (300, 650))
                    affichage_image(screen, oeil_ferme, (1320, 700))
                    if tableau == 'conn_entrer_mdp' or tableau == 'inscr_entrer_mdp':
                        affichage_image(screen, curseur, (300+10+long_mdp_cache, 660))
                    mdp_cache_verification=True
                
            #----------------
            #boutons menu jeu

            #Bouton pour accéder au profil
            elif check_clic(event.pos, (1450, 1550), (20, 70), ['menu'])==True:
                tableau='profil'

                #Déclaration du mot de passe caché, c'est à dire sous cette forme : *****
                mdp_cache_str=''
                for car in compte[1]:
                    mdp_cache_str=mdp_cache_str+'*'

                #Affichage du profil
                affichage_image(screen, fond_profil, (0,0))
                
                affichage_image(screen, retour_profil, retour_profil_pos)
                affichage_image(screen, icone_profil, icone_profil_pos)
                
                pseudo = font_profil.render(compte[0].upper(), 1, (0, 0, 0))
                longueur_pseudo = pseudo.get_rect().width
                screen.blit(pseudo, (200+((200-longueur_pseudo)/2), 420))
                
                argent = font_argent.render('Vous avez actuellement '+str(compte[2])+' dollars sur votre compte', 1, (0, 0, 0))
                screen.blit(argent, (550, 300))
                
                mdp_cache = font_argent.render('Votre mot de passe : '+mdp_cache_str, 1, (0, 0, 0))
                mdp_long = mdp_cache.get_rect().width
                screen.blit(mdp_cache, (550, 370))
                
                affichage_image(screen, deco, (550, 430))
                
                pos_oeil_gauche=mdp_long+30+550
                affichage_image(screen, oeil_ferme, (pos_oeil_gauche, 360))
                
                pygame.display.flip()

            #Bouton icône blackjack
            elif check_clic(event.pos, (250, 700), (170, 420), ['menu'])==True:
                tableau='bj_menu'

                #Affichage du menu du blackjack
                affichage_menu_jeu(screen)

            #Bouton icône machine à sous
            elif check_clic(event.pos, (900, 1350), (170, 420), ['menu'])==True:
                tableau='mas_menu'

                #Affichage du menu de la machine à sous
                affichage_menu_jeu(screen)

            #Bouton icône roulette
            elif check_clic(event.pos, (560, 1040), (550, 820), ['menu'])==True:
                tableau='roulette_menu'

                #Affichage du menu de la roulette
                affichage_menu_jeu(screen)

            #Bouton quiter le casion
            elif check_clic(event.pos, (1300, 1550), (770, 850), ['menu'])==True:
                if tableau=='menu':
                    #Stopper la boucle infinie
                    jouer = 0        
                
            #----------------
            #boutons profil
            #Bouton oeil pour cacher ou montrer le mot de passe
            elif check_clic(event.pos, (pos_oeil_gauche, pos_oeil_gauche+100), (360, 410), ['profil'])==True:

                #La variable booléenne 'mdp_cache_verif' nous dit si le mot de passe est caché ou pas
                if mdp_cache_verif==True:
                    mdp_cache_verif=False

                    #Affichage du mot de passe
                    affichage_image(screen, fond_profil, (0,0))
                
                    affichage_image(screen, retour_profil, retour_profil_pos)
                    affichage_image(screen, icone_profil, icone_profil_pos)
                    
                    pseudo = font_profil.render(compte[0].upper(), 1, (0, 0, 0))
                    longueur_pseudo = pseudo.get_rect().width
                    screen.blit(pseudo, (200+((200-longueur_pseudo)/2), 420))
                    
                    argent = font_argent.render('Vous avez actuellement '+str(compte[2])+' dollars sur votre compte', 1, (0, 0, 0))
                    screen.blit(argent, (550, 300))
                    
                    mdp = font_argent.render('Votre mot de passe : '+str_mdp, 1, (0, 0, 0))
                    mdp_long = mdp.get_rect().width
                    screen.blit(mdp, (550, 370))
                    
                    affichage_image(screen, deco, (550, 430))
                    
                    pos_oeil_gauche=mdp_long+30+550
                    affichage_image(screen, oeil, (pos_oeil_gauche, 360))

                else:
                    mdp_cache_verif=True

                    #Affichage du mot de passe caché
                    affichage_image(screen, fond_profil, (0,0))
                
                    affichage_image(screen, retour_profil, retour_profil_pos)
                    affichage_image(screen, icone_profil, icone_profil_pos)
                    
                    pseudo = font_profil.render(compte[0].upper(), 1, (0, 0, 0))
                    longueur_pseudo = pseudo.get_rect().width
                    screen.blit(pseudo, (200+((200-longueur_pseudo)/2), 420))
                    
                    argent = font_argent.render('Vous avez actuellement '+str(compte[2])+' dollars sur votre compte', 1, (0, 0, 0))
                    screen.blit(argent, (550, 300))
                    
                    mdp_cache = font_argent.render('Votre mot de passe : '+mdp_cache_str, 1, (0, 0, 0))
                    mdp_long = mdp_cache.get_rect().width
                    screen.blit(mdp_cache, (550, 370))
                    
                    affichage_image(screen, deco, (550, 430))
                    
                    pos_oeil_gauche=mdp_long+30+550
                    affichage_image(screen, oeil_ferme, (pos_oeil_gauche, 360))

                pygame.display.flip()

            #bouton se déconnecter
            elif check_clic(event.pos, (550, 700), (430, 480), ['profil'])==True:
                tableau='bienvenue'
                compte=[0,'','']

                str_uti=''
                long_uti=0
                str_mdp=''
                str_mdp_cache=''
                mdp_cache_verification=True
                long_mdp=0
                long_mdp_cache=0
                
                ecran_de_demarrage(screen)

            #bouton retour
            elif check_clic(event.pos, (1300, 1550), (770, 850), ['profil'])==True:
                tableau="menu"
                
                #Affichage du menu
                dessine_menu(screen)
                pygame.display.flip()
                
            #------------
            #boutons blackjack
            
            #Bouton retour
            elif check_clic(event.pos, (900, 1300), (300, 500), ['bj_menu'])==True:
                tableau='menu'

                #Affichage du menu
                dessine_menu(screen)
                pygame.display.flip()

            #Bouton jouer
            elif check_clic(event.pos, (300, 700), (300, 500), ['bj_menu'])==True:
                tableau='pari_bj'
                somme=''

                #Affichage du pari
                affichage_image(screen, fond_blackjack, (0, 0))
                affichage_image(screen, mas_rectangle_somme, (250, 750))
                affichage_image(screen, curseur_bj, (260, 760))
                afficher = font2.render('Combien voulez-vous parier ?', 1, (0, 0, 0))
                longueur_afficher = afficher.get_rect().width
                screen.blit(afficher, ((1100-longueur_afficher)/2, 680))
                
                argent = font2.render(str(compte[2])+'$', 1, (0, 0, 0))
                screen.blit(argent, (30, 30))
                
                pygame.display.flip()

                somme=''
                
            #------------
            #boutons roulette
            
            #Bouton retour
            elif check_clic(event.pos, (900, 1300), (300, 500), ['roulette_menu'])==True:
                tableau='menu'

                #Affichage du menu
                dessine_menu(screen)
                pygame.display.flip()

            #Bouton jouer
            elif check_clic(event.pos, (300, 700), (300, 500), ['roulette_menu'])==True:
                tableau='roulette_tapis'

                #Affichage du tapis pour parier
                affichage_tapis(screen)

            #Clic sur le tapis
            elif tableau=='roulette_tapis':
                liste_paris=check_tapis(screen, event.pos, paris, tableau)
                if len(liste_paris)!=0:
                    paris[liste_paris[0]]=liste_paris[1]

                    print(paris)
                    
            #bouton rejouer
            elif check_clic(event.pos, (500, 700), (700, 770), ['roulette_gains'])==True:
                tableau='roulette_tapis'

                #Affichage du tapis pour parier
                affichage_tapis(screen)

            #Bouton quitter
            elif check_clic(event.pos, (900, 1100), (700, 770), ['roulette_gains'])==True:
                tableau='menu'

                #Affiche le menu
                dessine_menu(screen)
                pygame.display.flip()

                somme=''

            #------------
            #boutons menu machine à sous

            #Bouton jouer
            elif check_clic(event.pos, (300, 700), (300, 500), ['mas_menu'])==True:
                somme=''
                tableau='mas_entrer_somme'

                #Affichage du pari
                affichage_image(screen, mas_fond, (0, 0))
                
                afficher = font2.render('Combien voulez-vous parier ?', 1, (0, 0, 0))
                longueur_afficher = afficher.get_rect().width
                screen.blit(afficher, ((1600-longueur_afficher)/2, 400))
                
                affichage_image(screen, mas_rectangle_somme, mas_rectangle_somme_pos)
                affichage_image(screen, curseur_bj, (510, 610))
                
                argent = font2.render(str(compte[2])+'$', 1, (0, 0, 0))
                screen.blit(argent, (30, 30))
                pygame.display.flip()

            #Bouton retour
            elif check_clic(event.pos, (900, 1300), (300, 500), ['mas_menu'])==True:
                tableau='menu'

                dessine_menu(screen)
                pygame.display.flip()

            #bouton rejouer
            elif check_clic(event.pos, (500, 700), (800, 850), ['mas_gains'])==True:
                somme=''
                tableau='mas_entrer_somme'

                #Affichage du pari
                affichage_image(screen, mas_fond, (0, 0))
                affichage_image(screen, mas_rectangle_somme, mas_rectangle_somme_pos)
                affichage_image(screen, curseur_bj, (510, 610))
                
                argent = font2.render(str(compte[2])+'$', 1, (0, 0, 0))
                screen.blit(argent, (30, 30))
                pygame.display.flip()

            #Bouton quitter
            elif check_clic(event.pos, (900, 1100), (800, 850), ['mas_gains'])==True:
                tableau='menu'

                #Affiche le menu
                dessine_menu(screen)
                pygame.display.flip()

                somme=''
                
            #------------
            #boutons blackjack

            #bouton tirer
            elif check_clic(event.pos, (325, 625), (750, 870), ['jeu_bj'])==True:
                infos=action(1, ct_jr, ct_crp, screen)
                #L'indice 0 de infos correspond aux gains. Si il est nul, c'est que le joueur a perdu, et on l'affiche
                if infos[0]==0:
                    tableau='fin_bj'

                    compte[2]=compte[2]-int(somme)

                    cur.execute("UPDATE membres SET argent = ? WHERE identifiant = ?", (compte[2], compte[0]))
                    conn.commit()

                    affichage_image(screen, rectangle_bj, (310, 610))
                    afficher = font2.render('Somme des cartes supérieure à 21, vous avez perdu '+str(somme)+' dollars', 1, (0, 0, 0))
                    longueur_afficher = afficher.get_rect().width
                    screen.blit(afficher, ((1100-longueur_afficher)/2, 750))
                    affichage_image(screen, mas_rejouer, (375, 810))
                    affichage_image(screen, mas_quitter, (775, 810))
                    dessin_carte(ct_jr[len(ct_jr)-1][3], 400, 300+(len(ct_jr)-1)*40, screen)
                    if len(ct_crp)>2:
                        dessin_carte(ct_crp[len(ct_crp)-1][3], 800, 300+(len(ct_crp)-1)*40, screen)
                    pygame.display.flip()
                #Si il est égal à 1, le joueur double sa mise et on l'affiche
                elif infos[0]==1:
                    tableau='fin_bj'

                    compte[2]=compte[2]+int(somme)

                    cur.execute("UPDATE membres SET argent = ? WHERE identifiant = ?", (compte[2], compte[0]))
                    conn.commit()

                    affichage_image(screen, rectangle_bj, (310, 610))
                    afficher = font2.render('Blackjack ! Vous avez gagné '+str(somme)+' dollars', 1, (0, 0, 0))
                    longueur_afficher = afficher.get_rect().width
                    screen.blit(afficher, ((1100-longueur_afficher)/2, 750))
                    affichage_image(screen, mas_rejouer, (375, 810))
                    affichage_image(screen, mas_quitter, (775, 810))
                    dessin_carte(ct_jr[len(ct_jr)-1][3], 400, 300+(len(ct_jr)-1)*40, screen)
                    if len(ct_crp)>2:
                        dessin_carte(ct_crp[len(ct_crp)-1][3], 800, 300+(len(ct_crp)-1)*40, screen)
                        affichage_image(screen, blackjack, (375, 325))
                    pygame.display.flip()
                else:
                    ct_jr=infos[1]
                    ct_crp=infos[2]

            #bouton stand
            elif check_clic(event.pos, (725, 1025), (750, 870), ['jeu_bj'])==True:
                infos=action(2, ct_jr, ct_crp, screen)
                #Même principe que le bouton tirer sauf qu'on vérifie si le croupier a plus que nous avec la fonction action
                if infos[0]==0:
                    tableau='bj_rejouer'

                    compte[2]=compte[2]-int(somme)

                    cur.execute("UPDATE membres SET argent = ? WHERE identifiant = ?", (compte[2], compte[0]))
                    conn.commit()

                    affichage_image(screen, rectangle_bj, (310, 610))

                    afficher = font2.render(infos[1], 1, (0, 0, 0))
                    longueur_afficher = afficher.get_rect().width
                    screen.blit(afficher, ((1100-longueur_afficher)/2, 680))
                    
                    afficher = font2.render('Vous avez perdu '+str(somme)+' dollars', 1, (0, 0, 0))
                    longueur_afficher = afficher.get_rect().width
                    screen.blit(afficher, ((1100-longueur_afficher)/2, 750))
                    
                    affichage_image(screen, mas_rejouer, (375, 810))
                    affichage_image(screen, mas_quitter, (775, 810))
                    dessin_carte(ct_jr[len(ct_jr)-1][3], 400, 300+(len(ct_jr)-1)*40, screen)
                    
                    if len(ct_crp)>2:
                        dessin_carte(ct_crp[len(ct_crp)-1][3], 800, 300+(len(ct_crp)-1)*40, screen)
                    pygame.display.flip()
                elif infos[0]==1:
                    tableau='bj_rejouer'

                    compte[2]=compte[2]+int(somme)

                    cur.execute("UPDATE membres SET argent = ? WHERE identifiant = ?", (compte[2], compte[0]))
                    conn.commit()

                    affichage_image(screen, rectangle_bj, (310, 610))
                    
                    afficher = font2.render(infos[1], 1, (0, 0, 0))
                    longueur_afficher = afficher.get_rect().width
                    screen.blit(afficher, ((1100-longueur_afficher)/2, 680))
                    
                    afficher = font2.render('Vous avez gagné '+str(somme)+' dollars', 1, (0, 0, 0))
                    longueur_afficher = afficher.get_rect().width
                    screen.blit(afficher, ((1100-longueur_afficher)/2, 750))
                    
                    affichage_image(screen, mas_rejouer, (375, 810))
                    affichage_image(screen, mas_quitter, (775, 810))
                    dessin_carte(ct_jr[len(ct_jr)-1][3], 400, 300+(len(ct_jr)-1)*40, screen)
                    if len(ct_crp)>2:
                        dessin_carte(ct_crp[len(ct_crp)-1][3], 800, 300+(len(ct_crp)-1)*40, screen)
                    pygame.display.flip()
                
                tableau='fin_bj'
                    
            #bouton rejouer
            elif check_clic(event.pos, (375, 575), (810, 880), ['fin_bj'])==True:
                tableau='pari_bj'
                somme=''

                #Affichage du pari
                affichage_image(screen, fond_blackjack, (0, 0))
                affichage_image(screen, mas_rectangle_somme, (250, 750))
                affichage_image(screen, curseur_bj, (260, 760))
                afficher = font2.render('Combien voulez-vous parier ?', 1, (0, 0, 0))
                longueur_afficher = afficher.get_rect().width
                screen.blit(afficher, ((1100-longueur_afficher)/2, 680))
                
                argent = font2.render(str(compte[2])+'$', 1, (0, 0, 0))
                screen.blit(argent, (30, 30))
                
                pygame.display.flip()
                
                pygame.display.flip()

            #Bouton quitter
            elif check_clic(event.pos, (775, 975), (810, 880), ['fin_bj'])==True:
                tableau='menu'

                #Affiche le menu
                dessine_menu(screen)
                pygame.display.flip()

                somme=''
                    
        #On vérifie si on clique sur une touche lors de la connexion
        if event.type == KEYDOWN and (tableau=='conn_entrer_uti' or tableau=='conn_entrer_mdp' or tableau=='inscr_entrer_uti' or tableau=='inscr_entrer_mdp'):
            liste_touches=liste_nb+liste_lettres
            for el in liste_touches:
                #On vérifie si on écrit dans le rectangle utilisateur et et réaffiche l'utilisateur
                if tableau=='conn_entrer_uti' or tableau=='inscr_entrer_uti':
                    if el==event.key:
                        if len(str_uti)<12:
                            affichage_image(screen, rectangle, (290, 240))

                            str_uti=str_uti+str(dico_touches[el])
                            afficher = taper_font.render(str_uti, 1, (0, 0, 0))
                            screen.blit(afficher, (300, 250))

                            long_uti=afficher.get_rect().width
                            affichage_image(screen, curseur, (300+long_uti+10,260))
                        
                            pygame.display.flip()
                        #Si l'utilisateur est de 12 caractères, on remplace le dernier par la touche pressée
                        else:
                            str_uti=str_uti[0:11]+dico_touches[el]
                            
                            affichage_image(screen, rectangle, (290, 240))
                            
                            afficher = taper_font.render(str_uti, 1, (0, 0, 0))
                            screen.blit(afficher, (300, 250))

                            long_uti=afficher.get_rect().width
                            affichage_image(screen, curseur, (300+long_uti+10,260))
                            
                            pygame.display.flip()
                #Même principe que pour l'utilisateur
                elif tableau=='conn_entrer_mdp' or tableau=='inscr_entrer_mdp':
                    if el==event.key:
                        if len(str_mdp)<12:
                            affichage_image(screen, rectangle, (290, 640))

                            str_mdp=str_mdp+str(dico_touches[el])
                            str_mdp_cache+='*'
                            
                            afficher_cache = taper_font.render(str_mdp_cache, 1, (0, 0, 0))
                            long_mdp_cache=afficher_cache.get_rect().width
                            afficher = taper_font.render(str_mdp, 1, (0, 0, 0))
                            long_mdp=afficher.get_rect().width
                            
                            if mdp_cache_verification==True:
                                screen.blit(afficher_cache, (300, 650))
                                affichage_image(screen, curseur, (300+long_mdp_cache+10,660))
                            elif mdp_cache_verification==False:
                                screen.blit(afficher, (300, 650))
                                affichage_image(screen, curseur, (300+long_mdp+10,660))

                            long_mdp=afficher.get_rect().width
                        
                            pygame.display.flip()
                        else:
                            str_mdp=str_mdp[0:11]+dico_touches[el]
                            
                            affichage_image(screen, rectangle, (290, 640))

                            afficher_cache = taper_font.render(str_mdp_cache, 1, (0, 0, 0))
                            long_mdp_cache=afficher_cache.get_rect().width
                            afficher = taper_font.render(str_mdp, 1, (0, 0, 0))
                            long_mdp=afficher.get_rect().width
                            
                            if mdp_cache_verification==True:
                                screen.blit(afficher_cache, (300, 650))
                                affichage_image(screen, curseur, (300+long_mdp_cache+10,660))
                            elif mdp_cache_verification==False:
                                screen.blit(afficher, (300, 650))
                                affichage_image(screen, curseur, (300+long_mdp+10,660))

                            long_mdp=afficher.get_rect().width
                            
                            pygame.display.flip()

            #Si on appuie sur retour, on efface le dernier caractère et on réaffiche le mot de passe/utilisateur
            if event.key == K_BACKSPACE:
                if tableau=='conn_entrer_uti' or tableau=='inscr_entrer_uti':
                    affichage_image(screen, rectangle, (290, 240))
                    
                    str_uti=str_uti[0:len(str_uti)-1]
                    afficher = taper_font.render(str_uti, 1, (0, 0, 0))
                    screen.blit(afficher, (300,250))

                    long_uti=afficher.get_rect().width
                    affichage_image(screen, curseur, (300+long_uti+10,260))
                    
                    pygame.display.flip()
                elif tableau=='conn_entrer_mdp' or tableau=='inscr_entrer_mdp':
                    affichage_image(screen, rectangle, (290, 640))
                    
                    str_mdp=str_mdp[0:len(str_mdp)-1]
                    str_mdp_cache=str_mdp_cache[0:len(str_mdp_cache)-1]
                    afficher_cache = taper_font.render(str_mdp_cache, 1, (0, 0, 0))
                    long_mdp_cache=afficher_cache.get_rect().width
                    afficher = taper_font.render(str_mdp, 1, (0, 0, 0))
                    long_mdp=afficher.get_rect().width
                    if mdp_cache_verification==True:
                        screen.blit(afficher_cache, (300, 650))
                        affichage_image(screen, curseur, (300+long_mdp_cache+10,660))
                    elif mdp_cache_verification==False:
                        screen.blit(afficher, (300, 650))
                        affichage_image(screen, curseur, (300+long_mdp+10,660))
                    
                    pygame.display.flip()

            #On vérifie si on appuie sur Entrée
            if event.key == K_RETURN:
                #On vérifie si on se connecte
                if tableau=='conn_entrer_uti' or tableau=='conn_entrer_mdp':
                    sing_id=(str_uti,)
                    sing_mdp=(str_mdp,)
                    #On vérifie que l'identifiant existe et qu'il correspond au mot de passe
                    if check_identifiant_existe(sing_id)==True and check_mdp(str_uti)==str_mdp:
                        cur.execute("SELECT argent FROM membres WHERE identifiant = ?",(str_uti,))
                        argent_sing=cur.fetchone()

                        compte=[str_uti, str_mdp, argent_sing[0]]

                        tableau='menu'

                        #On affiche le menu
                        screen.fill(black)
                        dessine_menu(screen)
                        pygame.display.flip()

                    #Sinon on affiche un message d'alerte
                    else:
                        affichage_image(screen, alerte, (300, 800))
                #On vérifie si on s'inscrit
                elif tableau=='inscr_entrer_uti' or tableau=='inscr_entrer_mdp':
                    sing_id=(str_uti,)
                    sing_mdp=(str_mdp,)

                    #On vérifie que le mot de passe est bien supérieur à 3 caractères
                    if len(str_uti)>3 and check_identifiant_existe(sing_id)==False:
                        var =[(str_uti, str_mdp, 10000)]
                        for i in var:
                            cur.execute("INSERT INTO membres(identifiant, mdp, argent) VALUES(?,?,?)", i)
                        conn.commit()
                        
                        compte=[str_uti,str_mdp,10000]

                        tableau='menu'

                        screen.fill(black)
                        dessine_menu(screen)
                        pygame.display.flip()

                    #Sinon on affiche un message d'alerte
                    else:
                        affichage_image(screen, alerte, (300, 800))
                    
        #On vérifie si on clique sur une touche lors du pari de la machine à sous ou du blackjack
        if event.type == KEYDOWN and (tableau=='mas_entrer_somme' or tableau=='pari_bj' or tableau=='roulette_miser'):
            #On vérifie si la touche cliquée est un nombre
            for el in liste_nb:
                if el==event.key:
                    #On vérifie si la taille du nombre parié est inférieur à 8 (la taille maximum)
                    if len(somme)<8:
                        #Si oui, on affiche le nombre parié avec le nouveau chiffre et on l'ajoute à la variable 'somme'
                        if tableau=='pari_bj':
                            affichage_image(screen, mas_rectangle_somme, (250, 750))
                        else:
                            affichage_image(screen, mas_rectangle_somme, mas_rectangle_somme_pos)
                    
                        somme=somme+dico_nb[el]
                        afficher = taper_font.render(somme, 1, (0, 0, 0))
                        if tableau=='pari_bj':
                            screen.blit(afficher, (250,750))
                        else:
                            screen.blit(afficher, (500,600))

                        long_somme=afficher.get_rect().width
                        
                        if tableau=='pari_bj':
                            affichage_image(screen, curseur_bj, (250+long_somme+10,760))
                        else:
                            affichage_image(screen, curseur_bj, (500+long_somme+10,610))
                        
                        pygame.display.flip()
                    else:
                        #Si elle égale à 8, on supprime le dernier chiffre et on ajoute le nouveau
                        somme=somme[0:7]+dico_nb[el]

                        if tableau=='pari_bj':
                            affichage_image(screen, mas_rectangle_somme, (250, 750))
                        else:
                            affichage_image(screen, mas_rectangle_somme, mas_rectangle_somme_pos)
                        
                        afficher = taper_font.render(somme, 1, (0, 0, 0))
                        if tableau=='pari_bj':
                            screen.blit(afficher, (250,750))
                        else:
                            screen.blit(afficher, (500,600))

                        long_somme=afficher.get_rect().width
                        if tableau=='pari_bj':
                            affichage_image(screen, curseur_bj, (250+long_somme+10,760))
                        else:
                            affichage_image(screen, curseur_bj, (500+long_somme+10,610))
                        
                        pygame.display.flip()

            #On vérifie si la touche cliquée est 'Retour'
            if event.key == K_BACKSPACE:
                #On supprime le dernier chiffre de l'affichage et de la variable 'somme'
                if tableau=='pari_bj':
                    affichage_image(screen, mas_rectangle_somme, (250, 750))
                else:
                    affichage_image(screen, mas_rectangle_somme, mas_rectangle_somme_pos)
                
                somme=somme[0:len(somme)-1]
                afficher = taper_font.render(somme, 1, (0, 0, 0))
                if tableau=='pari_bj':
                    screen.blit(afficher, (250,750))
                else:
                    screen.blit(afficher, (500,600))

                long_somme=afficher.get_rect().width
                if tableau=='pari_bj':
                    affichage_image(screen, curseur_bj, (250+long_somme+10,760))
                else:
                    affichage_image(screen, curseur_bj, (500+long_somme+10,610))

                pygame.display.flip()

            #On vérifie si la touche cliquée est 'Entrée'
            elif event.key == K_RETURN:
                #Sil la somme est nulle, alors elle sera égale à 0 (et invalide)
                if somme=='':
                    somme='0'

                #Si le joueur a assez d'argent pour parier et que 'somme'>0, alors il peut jouer
                if compte[2]>=int(somme) and int(somme)>0:
                    if tableau=='mas_entrer_somme':
                        tableau='mas_gains'

                        affichage_image(screen, mas_fond, (0,0))

                        #On appelle la fonction roulette qui retourne les gains ou 0 si on perd
                        gains=slot_partie(int(somme))
                        animation_machine(screen, gains[1], [bar, bar_2, bar_3, cherry, scatter, symb_7, cloche])
                        time.sleep(0.25)

                        #Si les gains sont supérieurs à 0, le joueur à gagné
                        if gains[0] > 0 :
                            #On met à jour la variable 'compte'
                            compte[2]=compte[2]-int(somme)+gains[0]

                            #On met à jour la base de données
                            cur.execute("UPDATE membres SET argent = ? WHERE identifiant = ?", (compte[2], compte[0]))
                            conn.commit()

                            #On affiche les gains du joueur
                            afficher = font2.render('Vous avez gagné '+str(gains[0])+' dollars', 1, (0, 0, 0))
                            longueur_phrase = afficher.get_rect().width
                            screen.blit(afficher, ((1600-longueur_phrase)/2, 750))
                            affichage_image(screen, rejouer, (500, 800))
                            affichage_image(screen, retour_menu, (900, 800))
                            pygame.display.flip()
                        #Si il a perdu
                        else:
                            #On met à jour la variable 'compte' en faisant la différence de son solde et de sa mise
                            compte[2]=compte[2]-int(somme)

                            #On met à jour la base de données
                            cur.execute("UPDATE membres SET argent = ? WHERE identifiant = ?", (compte[2], compte[0]))
                            conn.commit()

                            #On affiche que le joueur a perdu
                            afficher = font2.render('Vous avez perdu votre mise', 1, (0, 0, 0))
                            longueur_phrase = afficher.get_rect().width
                            screen.blit(afficher, ((1600-longueur_phrase)/2, 750))
                            affichage_image(screen, rejouer, (500, 800))
                            affichage_image(screen, retour_menu, (900, 800))
                            pygame.display.flip()
                    elif tableau=='pari_bj':
                        tableau='affichage_cartes_bj'

                        infos=play_blackjack(int(somme), screen)
                        ct_jr=infos[1]
                        ct_crp=infos[2]

                        #Si le joueur gagne du premier coup (blackjack avec une tête/10 et un as), on affiche ses gains
                        if infos[0]>0:
                            tableau='fin_bj'

                            compte[2]=compte[2]+int(somme)

                            cur.execute("UPDATE membres SET argent = ? WHERE identifiant = ?", (compte[2], compte[0]))
                            conn.commit()

                            affichage_image(screen, rectangle_bj, (310, 610))
                            afficher = font2.render('Blackjack ! Vous avez gagné '+str(somme)+' dollars', 1, (0, 0, 0))
                            longueur_afficher = afficher.get_rect().width
                            screen.blit(afficher, ((1100-longueur_afficher)/2, 750))
                            affichage_image(screen, mas_rejouer, (375, 810))
                            affichage_image(screen, mas_quitter, (775, 810))
                            pygame.display.flip()

                        #Sinon le jeu continue
                        else:
                            tableau='jeu_bj'
                    elif tableau=='roulette_miser':
                        #Si le pari est invalide on affiche un message à l'utilisateur
                        if somme == '':
                            screen.fill(white)
                            phrase = font2.render("La valeur doit être supérieure à 0. Combien voulez vous miser sur "+str(nb_actuel[0])+" ?", 1, (0, 0, 0))
                            longueur_phrase = phrase.get_rect().width
                            screen.blit(phrase, ((1600-longueur_phrase)/2, 420))
                                                
                            affichage_image(screen, mas_rectangle_somme, mas_rectangle_somme_pos)
                            pygame.display.flip()

                        #On appelle la fonction 'pari' pour afficher le prochain pari
                        if len(pari_actuel)>0 and somme!='':
                            compte[2]=compte[2]-int(somme)
                            
                            cur.execute("UPDATE membres SET argent = ? WHERE identifiant = ?", (compte[2], compte[0]))
                            conn.commit()
                            
                            paris[nb_actuel[0]]=int(somme)
                            nb_actuel[0]=pari(pari_actuel[0])

                            somme=''
                        #Si on a fait tous les paris, on appelle la fonction 'roulette' pour jouer à la roulette
                        elif len(pari_actuel)==0 and somme!='':
                            tableau='roulette_gains'
                            
                            paris[nb_actuel[0]]=int(somme)
                            nb_actuel[0]=0
                            
                            compte[2]=compte[2]-int(somme)

                            somme=''

                            cur.execute("UPDATE membres SET argent = ? WHERE identifiant = ?", (compte[2], compte[0]))
                            conn.commit()

                            paris_copie=paris.copy()

                            #L'argent gagné sur la roulette
                            dico_gains=roulette(paris, screen)
                            gains=0
                            mises_perdues=0

                            print(paris)
                            
                            for el in dico_gains.keys():
                                if dico_gains[el]>paris_copie[el]:
                                    gains+=dico_gains[el]
                                else:
                                    mises_perdues-=paris[el]
                            print(gains, mises_perdues)
                                    
                            if gains+mises_perdues>=0:
                                phrase = font2.render('Vous avez gagné '+str(gains)+'$', 1, (255, 255, 255))
                                longueur_phrase = phrase.get_rect().width
                                screen.blit(phrase, ((1600-longueur_phrase)/2, 600))
                                pygame.display.flip()
                                
                            else:
                                phrase = font2.render('Vous avez perdu '+str((mises_perdues-gains)*(-1))+'$', 1, (255, 255, 255))
                                longueur_phrase = phrase.get_rect().width
                                screen.blit(phrase, ((1600-longueur_phrase)/2, 600))
                                pygame.display.flip()
                                
                            compte[2]=compte[2]+gains
                                
                            cur.execute("UPDATE membres SET argent = ? WHERE identifiant = ?", (compte[2], compte[0]))
                            conn.commit()

                            paris=re_paris()
                                
                            affichage_image(screen, mas_rejouer, mas_rejouer_pos)
                            affichage_image(screen, mas_quitter, mas_quitter_pos)
                            pygame.display.flip()
                        
                #Sinon, on affiche que la somme misée est invalide
                else:
                    somme=''

                    if tableau=='pari_bj':
                        affichage_image(screen, rectangle_bj, (310, 610))
                        affichage_image(screen, mas_rectangle_somme, (250, 750))
                        affichage_image(screen, curseur_bj, (260, 760))
                        afficher = font2.render('Pari invalide. Combien voulez-vous parier ?', 1, (0, 0, 0))
                        longueur_afficher = afficher.get_rect().width
                        screen.blit(afficher, ((1100-longueur_afficher)/2, 680))
                    elif tableau=="roulette_miser":
                        affichage_image(screen, fond_roulette, (0, 0))
                        affichage_image(screen, mas_rectangle_somme, mas_rectangle_somme_pos)
                        affichage_image(screen, curseur_bj, (510, 610))
                        
                        afficher = font2.render('Pari invalide. Combien voulez-vous parier ?', 1, (255, 255, 255))
                        longueur_afficher = afficher.get_rect().width
                        screen.blit(afficher, ((1600-longueur_afficher)/2, 420))
                        
                        argent = font2.render(str(compte[2])+'$', 1, (255, 255, 255))
                        screen.blit(argent, (30, 30))
                        pygame.display.flip()
                    elif tableau=='mas_entrer_somme':
                        affichage_image(screen, mas_fond, (0, 0))
                        
                        afficher = font2.render('Pari invalide. Combien voulez-vous parier ?', 1, (0, 0, 0))
                        longueur_afficher = afficher.get_rect().width
                        screen.blit(afficher, ((1600-longueur_afficher)/2, 400))

                        argent = font2.render(str(compte[2])+'$', 1, (0, 0, 0))
                        screen.blit(argent, (30, 30))
                
                        affichage_image(screen, mas_rectangle_somme, mas_rectangle_somme_pos)
                        affichage_image(screen, curseur_bj, (510, 610))
                        pygame.display.flip()
                
                        
        #On vérifie si on clique sur une touche lors du choix des paris sur le tapis de la roulette
        if event.type == KEYDOWN and tableau=='roulette_tapis':
            #Si on clique sur 'Entrée', on met en place la boucle pour les paris
            if event.key == K_RETURN:
                tableau='roulette_miser'
                for el in paris.keys():
                    if paris[el]==1:
                        pari_actuel.append(el)

                nb_actuel[0]=pari(pari_actuel[0])
pygame.quit()
