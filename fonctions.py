import sys, time, pygame
from pygame.locals import *

pygame.init()

#VARIABLES IMPORTANTES: IMAGES, POLICES, COULEURS RGB
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
deco = pygame.image.load("Images/Menu_jeu/Profil/deco.png")

rect_blanc = pygame.image.load("Images/Menu_jeu/Profil/rect_blanc.png")
rect_blanc_pos = (550, 370)


#-----------

#Chargement images blackjack

curseur_bj = pygame.image.load("Images/Jeux/Blackjack/curseur_bj.png")

blackjack = pygame.image.load("Images/Jeux/Blackjack/blackjack.png")

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

liste_triple_ligne_vert = [pygame.image.load("Images/Jeux/Roulette/1_12_vert.png"), pygame.image.load("Images/Jeux/Roulette/13_24_vert.png"), pygame.image.load("Images/Jeux/Roulette/25_36_vert.png")]
liste_triple_ligne_bleu = [pygame.image.load("Images/Jeux/Roulette/1_12_bleu.png"), pygame.image.load("Images/Jeux/Roulette/13_24_bleu.png"), pygame.image.load("Images/Jeux/Roulette/25_36_bleu.png")]

liste_sextuple_ligne_vert = [pygame.image.load("Images/Jeux/Roulette/1_18_vert.png"), pygame.image.load("Images/Jeux/Roulette/pair_vert.png"), pygame.image.load("Images/Jeux/Roulette/noir_vert.png"),pygame.image.load("Images/Jeux/Roulette/rouge_vert.png"), pygame.image.load("Images/Jeux/Roulette/impair_vert.png"), pygame.image.load("Images/Jeux/Roulette/19_36_vert.png")]
liste_sextuple_ligne_bleu = [pygame.image.load("Images/Jeux/Roulette/1_18_bleu.png"), pygame.image.load("Images/Jeux/Roulette/pair_bleu.png"), pygame.image.load("Images/Jeux/Roulette/noir_bleu.png"),pygame.image.load("Images/Jeux/Roulette/rouge_bleu.png"), pygame.image.load("Images/Jeux/Roulette/impair_bleu.png"), pygame.image.load("Images/Jeux/Roulette/19_36_bleu.png")]


#Chargement images machine à sous

mas_fond = pygame.image.load("Images/Jeux/Machine_a_sous/fond_mas.png")

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

mas_rejouer = pygame.image.load("Images/Jeux/Machine_a_sous/mas_rejouer.png")
mas_rejouer_pos = (450, 700)
mas_quitter = pygame.image.load("Images/Jeux/Machine_a_sous/mas_quitter.png")
mas_quitter_pos = (840, 700)

rejouer = pygame.image.load("Images/Jeux/Machine_a_sous/mas_rejouer.png")
retour_menu = pygame.image.load("Images/Jeux/Machine_a_sous/mas_quitter.png")


#-----------
#Chargement polices

font = pygame.font.Font("Polices/dejavu_sansbold.ttf", 100)
font2 = pygame.font.Font("Polices/dejavu_sansbold.ttf", 50)

#-----------

#Couleur RGB pour le fond de l'écran

black = 0, 0, 0
white = 255, 255, 255

#Chargement polices

font = pygame.font.Font("Polices/dejavu_sansbold.ttf", 100)
font2 = pygame.font.Font("Polices/dejavu_sansbold.ttf", 50)

#FONCTIONS D'AFFICHAGE

def affichage_image(screen, image, position):
    screen.blit(image, (position[0], position[1]))

def ecran_de_demarrage(screen):
    screen.fill(white)
    phrase = font2.render('Bienvenue dans le casino Umthombo !', 1, (0, 0, 0))
    longueur_phrase = phrase.get_rect().width
    screen.blit(phrase, ((1600-longueur_phrase)/2, 200))
    screen.blit(inscription, inscription_pos)
    screen.blit(connexion, connexion_pos)
    pygame.display.flip()

def conn_inscr(screen, n):
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

def dessine_menu(screen):
    """Fonction qui dessine le menu"""
    screen.blit(fond, (0,0))
    screen.blit(banderole, (0, 0))
    screen.blit(profil, profil_pos)
    screen.blit(blackjack_icone, blackjack_icone_pos)
    screen.blit(slot_icone, slot_icone_pos)
    screen.blit(roulette_icone, roulette_icone_pos)
    screen.blit(quitter, quitter_pos)

def check_tapis(screen, clic, paris, tableau):
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

    ligne_triple=['mise_douzaine1','mise_douzaine2','mise_douzaine3']
    coordonnees_triple=[187, 415]
    for i in range(0,3):
        if(clic[0]>=coordonnees_triple[0]+i*422 and clic[0]<=coordonnees_triple[0]+416+i*422) and (clic[1]>=coordonnees_triple[1] and clic[1]<=coordonnees_triple[1]+179) and tableau=='roulette_tapis':
            if paris[ligne_triple[i]]==0:
                screen.blit(liste_triple_ligne_bleu[i], (coordonnees_triple[0]+i*422, coordonnees_triple[1]))
                pygame.display.flip()
                return [ligne_triple[i], 1]
            elif paris[ligne_triple[i]]==1:
                screen.blit(liste_triple_ligne_vert[i], (coordonnees_triple[0]+i*422, coordonnees_triple[1]))
                pygame.display.flip()
                return [ligne_triple[i], 0]

    ligne_sextuple=['mise_1_à_18','mise_pair','mise_noir','mise_rouge','mise_impair','mise_19_à_36']
    coordonnees_sextuple=[187, 599]
    for i in range(0,6):
        if(clic[0]>=coordonnees_sextuple[0]+i*213 and clic[0]<=coordonnees_sextuple[0]+209+i*213) and (clic[1]>=coordonnees_sextuple[1] and clic[1]<=coordonnees_sextuple[1]+179) and tableau=='roulette_tapis':
            if paris[ligne_sextuple[i]]==0:
                screen.blit(liste_sextuple_ligne_bleu[i], (coordonnees_sextuple[0]+i*213, coordonnees_sextuple[1]))
                pygame.display.flip()
                return [ligne_sextuple[i], 1]
            elif paris[ligne_sextuple[i]]==1:
                screen.blit(liste_sextuple_ligne_vert[i], (coordonnees_sextuple[0]+i*213, coordonnees_sextuple[1]))
                pygame.display.flip()
                return [ligne_sextuple[i], 0]

    #On retourne une liste vide si les vérifications de clic n'ont pas été concluantes.
    return []

def affichage_tapis(screen):
    screen.fill(white)
    affichage_image(screen, roulette_tapis, (0, 0))
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

    coordonnees_triple_ligne=[187, 414]
    for i in range(0,3):
        screen.blit(liste_triple_ligne_vert[i], (coordonnees_triple_ligne[0]+i*(426), coordonnees_triple_ligne[1]))
                    
    pygame.display.flip()

def affichage_curseur(screen, str_uti, str_mdp):
    screen.blit(rectangle, (300, 250))
    screen.blit(rectangle, (300, 650))
    uti = font.render(str_uti, 1, (0, 0, 0))
    screen.blit(uti, (300, 250))
    mdp = font.render(str_mdp, 1, (0, 0, 0))
    screen.blit(mdp, (300, 650))
    pygame.display.flip()

def affichage_menu_jeu(screen):
    screen.fill(white)
    screen.blit(mas_jouer, mas_jouer_pos)
    screen.blit(mas_retour, mas_retour_pos)
    pygame.display.flip()

def affichage_paris(screen):
    screen.blit(mas_somme, (0, 0))
    screen.blit(mas_rectangle_somme, mas_rectangle_somme_pos)
    screen.blit(curseur_bj, (510, 610))

def affichage_rejouer(screen):
    screen.blit(mas_rejouer, mas_rejouer_pos)
    screen.blit(mas_quitter, mas_quitter_pos)

#FONCTIONS DE FONCTIONNEMENT
