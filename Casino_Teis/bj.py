import random
import sys, time, pygame
from pygame.locals import *

#Importation des images

blackjack = pygame.image.load("Images/Jeux/Blackjack/blackjack.png")

stand = pygame.image.load("Images/Jeux/Blackjack/stand.png")
tirer = pygame.image.load("Images/Jeux/Blackjack/tirer.png")
fond_bj = pygame.image.load("Images/Jeux/Blackjack/fond_blackjack.png")

back = pygame.image.load("Images/Jeux/Blackjack/back.png")

#Création d'un dictionnaire de cartes

dico_images_cartes={}

for i in range(1,53):
    dico_images_cartes[i]=pygame.image.load("Images/Jeux/Blackjack/"+str(i)+".png")

def ret_spec(nb):
    '''Retourne le nom de la carte'''
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
    """Crée la liste de cartes"""
    liste_cartes={}

    for i in range(1,53):
        nb=i
        famille_nb=0

        while nb > 13:
            nb=nb-13
            famille_nb=famille_nb+1

        if famille_nb==0:
            liste_cartes[i]=[nb,ret_spec(nb),'coeur',i]
        elif famille_nb==1:
            liste_cartes[i]=[nb,ret_spec(nb),'carreau',i]
        elif famille_nb==2:
            liste_cartes[i]=[nb,ret_spec(nb),'pique',i]
        elif famille_nb==3:
            liste_cartes[i]=[nb,ret_spec(nb),'trèfle',i]
            
        if liste_cartes[i][0]>10:
            liste_cartes[i][0]=10
        elif liste_cartes[i][0]==1:
            liste_cartes[i][0]=11
    return liste_cartes

liste_cartes=crea_liste_cartes()


def tirer_carte():
    '''Tire une carte aléatoire dans le dictionnaire et retourne la carte tirer'''
    nb_carte = random.randint(1,52)
    return(liste_cartes[nb_carte])

def dessin_carte(nb_carte, x, y, screen):
    """Affiche une carte en fonction de son numéro et de ses coordonnées"""
    screen.blit(dico_images_cartes[nb_carte], (x, y))
    pygame.display.flip()
    time.sleep(0.5)

def play_blackjack(mise, screen):
    #phrase qui explique si on a gagner ou pas
    phrase=" "
    gains=0

    '''Tire les différentes cartes aux joueur et au croupier, le joueur gagne directement si la somme de ses cartes est égale à 21, sinon on demande au joueur ce qu'il souhaite faire: 1=tirer une carte'''
    mise #mise()
    gains = 0
    ct_jr = [] #création d'une liste contenant les cartes du joueur
    ct_crp = [] #création d'une liste contenant les cartes du croupier

    #ajoute les deux premières cartes au joueur et au croupier
    ct_jr.append(tirer_carte())
    ct_crp.append(tirer_carte())
    ct_jr.append(tirer_carte())
    ct_crp.append(tirer_carte())

    screen.blit(fond_bj, (0,0))
    pygame.display.flip()

    for i in range(0, len(ct_jr)):
        dessin_carte(ct_jr[i][3], 400, 300+i*40, screen)

    dessin_carte(ct_crp[0][3], 800, 300, screen)
    screen.blit(back, (800, 340))

    screen.blit(tirer, (325, 750))
    screen.blit(stand, (725, 750))

    pygame.display.flip()

    #check si il y a eu blackjack direct
    
    if (ct_jr[0][0]==11 and ct_jr[1][0]==10) or (ct_jr[1][0]==11 and ct_jr[0][0]==10): #vérification s'il ya eu un blackjack
        gains = mise*2

        screen.blit(blackjack, (375, 325))
        pygame.display.flip()
        return [gains, [], []]
    else:
        return [gains, ct_jr, ct_crp]

def action(act, cartes_joueur, cartes_croupier, screen):
    """Fonction qui prend en paramètres les cartes du croupier et du joueru, l'action (tirer ou stand) et qui réagit en fonction des cartes tirées"""
    def calcul_somme(jeu_carte):
        somme=0
        compteur_as=0
        for el in jeu_carte:
            if el[1]=='as':
                compteur_as+=1
        for el in jeu_carte:
            somme+=el[0]
        if somme>21 and compteur_as>0:
            somme-=compteur_as*10
        return somme
        
    ct_jr=cartes_joueur
    ct_crp=cartes_croupier
    gains=0
    if act == 1:
        ct_jr.append(tirer_carte())
        dessin_carte(ct_jr[len(ct_jr)-1][3], 400, 300+(len(ct_jr)-1)*40, screen)
        
    #ajoute des cartes au croupier tant qu'il na pas 17    
    if act==2:
        dessin_carte(ct_crp[1][3], 800, 340, screen)

        if (ct_crp[0][0]==11 and ct_crp[1][0]==10) or (ct_crp[1][0]==11 and ct_crp[0][0]==10): #vérification s'il ya eu un blackjack
            pygame.display.flip()
            return [gains, "Le croupier a fait Blackjack ! Vous perdez votre mise."]
        
        somme_jr = calcul_somme(ct_jr)
        somme_crp = calcul_somme(ct_crp)
        while somme_crp < 17:
            ct_crp.append(tirer_carte())
            somme_crp=calcul_somme(ct_crp)
            
            dessin_carte(ct_crp[len(ct_crp)-1][3], 800, 300+(len(ct_crp)-1)*40, screen)
            time.sleep(0.5)

        #dit que le croupier a perdu s'il a plus de 21 en mains
        if somme_crp>21 and somme_jr<21:
            return gains+1, "Le croupier a dépassé 21! "

        elif somme_jr>somme_crp and somme_jr<22 and somme_jr!=somme_crp:
            return gains+1, "Votre somme est supérieure à celle du croupier! "

        elif somme_crp>somme_jr and  somme_crp<=21:
            return gains, "La somme du croupier est supérieure à la votre! "
            
        elif somme_crp==somme_jr:
            return gains, "Le croupier a autant que vous, vous perdez! "

    if calcul_somme(ct_jr)>21:
        return gains, ct_jr, ct_crp
    elif calcul_somme(ct_jr)==21:
        return gains+1, ct_jr, ct_crp
    else:
        return gains-1, ct_jr, ct_crp
