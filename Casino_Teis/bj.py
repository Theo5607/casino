import random
import sys, time, pygame
from pygame.locals import *

vert = 0, 255, 0

blackjack = pygame.image.load("Images/Jeux/Blackjack/blackjack.png")

stand = pygame.image.load("Images/Jeux/Blackjack/stand.png")
tirer = pygame.image.load("Images/Jeux/Blackjack/tirer.png")

back = pygame.image.load("Images/Jeux/Blackjack/back.png")

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
    return liste_cartes

liste_cartes=crea_liste_cartes()


def tirer_carte():
    '''Tire une carte aléatoire dans le dictionnaire et retourne la carte tirer'''
    nb_carte = random.randint(1,52)
    return(liste_cartes[nb_carte])

def dessin_carte(nb_carte, x, y, screen):
    screen.blit(dico_images_cartes[nb_carte], (x, y))
    pygame.display.flip()
    time.sleep(1)

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

    screen.fill(vert)
    pygame.display.flip()

    for i in range(0, len(ct_jr)):
        dessin_carte(ct_jr[i][3], 400, 300+i*40, screen)

    dessin_carte(ct_crp[0][3], 800, 300, screen)
    screen.blit(back, (800, 330))

    screen.blit(tirer, (450, 750))
    screen.blit(stand, (850, 750))

    pygame.display.flip()

    #def animation_cartes(liste, x, y):
        #liste_cartes_deja_posees=[]
        #for el in liste:      
            #for i in range(y,0,-2):
                #screen.fill(vert)
                #var=0
                #for carte in liste_cartes_deja_posees:
                        #var+=1
                        #screen.blit(carte, (x, y+40*var))
                        #pygame.display.flip()
                #screen.blit(dico_images_cartes[el[3]], (x, y-i))
                #pygame.display.flip()
                #time.sleep(0.00001)
                
            #y+=40
            #liste_cartes_deja_posees.append(dico_images_cartes[el[3]])
        #pygame.display.flip()

    #animation_cartes(ct_jr, 400, 300)
    #animation_cartes(ct_crp, 800, 300)

    #check si il y a eu blackjack direct
    
    if (ct_jr[0][0]==1 and (ct_jr[1][0]==(10 or 11 or 12 or 13))) or (ct_jr[1][0]==1 and (ct_jr[0][0]==(10 or 11 or 12 or 13))): #vérification s'il ya eu un blackjack
        gains = mise*2

        screen.blit(blackjack, (500, 670))
        pygame.display.flip()

        time.sleep(2)
        return [gains, [], []]
    else:
        return [gains, ct_jr, ct_crp]

def action(act, cartes_joueur, cartes_croupier, screen):
    def calcul_somme(jeu_carte):
        somme=0
        for el in jeu_carte:
            somme+=el[0]
        return somme
        
    ct_jr=cartes_joueur
    ct_crp=cartes_croupier
    gains=0
    if act == 1:
        ct_jr.append(tirer_carte())
        dessin_carte(ct_jr[len(ct_jr)-1][3], 400, 300+(len(ct_jr)-1)*40, screen)
        
    #ajoute des cartes au croupier tant qu'il na pas 17    
    if act==2:
        stand=1
        while int(somme_crp) < 17:
            ct_crp.append(tirer_carte())
            somme_crp+=ct_crp[len(ct_crp)-1][0]
            print(somme_crp)

        #dit que le croupier a perdu s'il a plus de 21 en mains
        if somme_crp>21 and somme_jr<21:
            gains=mise*2
            phrase="Le croupier a dépassé 21, vous gagnez!"
            end_check=True

        #dit que le joueur a perdu s'il a plus de 21 en mains
        elif somme_jr>21:
            gains=0
            phrase="Vous avez plus de 21 en cartes, vous perdez"
            end_check=True

        elif somme_crp>somme_jr and  somme_crp<=21 and stand==1:
            gains=0
            phrase="Le croupier a plus que vous, vous perdez."
            end_check=True

        elif somme_jr>somme_crp and somme_jr<22 and stand==1 and somme_jr!=somme_crp:
            gains=mise*2
            phrase="Vous avez plus que le croupier, vous gagnez!"
            end_check=True

        elif somme_crp==somme_jr and stand==1:
            gains=0
            phrase="Le croupier a autant que vous, vous perdez."
            end_check=True

    if calcul_somme(ct_jr)>21:
        return [gains, ct_jr, ct_crp]
    elif calcul_somme(ct_jr)==21:
        return [gains+1, ct_jr, ct_crp]
    else:
        return [gains-1, ct_jr, ct_crp]

#print(play_blackjack(3))
