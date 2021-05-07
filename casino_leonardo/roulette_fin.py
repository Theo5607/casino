import pygame, time

type_mise = {"le rouge" : 100, "le noir" : 100,"la première colonne" : 100,"la deuxième colonne" : 100,"la troisième colonne" : 100,"la première douzaine" : 100,"la deuxième douzaine" : 100,"la troisième douzaine" : 100,"la première moitié" : 100,"la deuxième moitié" : 100,"les nombres impairs" : 100,"les nombres pairs" : 100}
for i in range(0,37):
    type_mise[i]=0
#un dictionnaire qui a comme clés sur quoi il va parier et la valeur est égale à combien il va parier

import random#fait appel à la bibliothèque

def animation_roulette(screen, x):
    """Fonction qui anime la roulette en fonction de x qui est la valeur voulue entre 0 et 36"""
    white = 255, 255, 255

    bandeau = pygame.image.load("Images/Jeux/Roulette/Animation/bandeau_roulette.png")
    triangle = pygame.image.load("Images/Jeux/Roulette/Animation/triangle.png")
    fond_roulette = pygame.image.load("Images/Jeux/Roulette/fond_roulette.png")
    screen.blit(fond_roulette, (0,0))
    #Cette liste correspond aux itérations nécessaires en fonction de l'indice. Ex;: list_machine[0] correspond aux nombres d'itérations nécessaires pour afficher le nombre 0
    list_machine=[3230,3790,2990,3310,3070,3950,2830,3470,4070,3630,3990,4150,3390,4230,3710,4630,3870,4390,3550,4590,3750,4510,3590,4030,3910,4430,3270,4270,3430,3510,4110,3670,4670,3830,4350,3350,4190]

    #On affiche la roulette qui défile qui accélerre puis décelerre à l'aide d'un polynôme du second degré
    for i in range(list_machine[x]):
        screen.blit(bandeau, (-17795+3*i,430))
        screen.blit(triangle, (780,340))
        pygame.display.flip()
        time.sleep(((7/1053405)*i**2-(14/459)*i+50)/10000)
    return


def roulette(type_mise, screen):
    """prend en argument un dictionnaire qui a comme clés sur quoi il va parier et la valeur est égale à combien il va parier et retourne les gains ainsi que les symboles qui ont gagné"""
    x=random.randint(0,36)#nombre aléatoire entre 0 et 36
    print(x)
    animation_roulette(screen, x)
    time.sleep(0.5)
    print("Le chiffre qui est sorti :",x)#affiche le nombre choisi
    rouge = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]#chiffre dans la catégorie rouge
    noir = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]#chiffre dans la catégorie noir
    #Mise par couleur

    if x in rouge:# demande que x soit egal à un chiffre rouge
        type_mise["le rouge"]=type_mise["le rouge"]*2#double la mise

    if x in noir:# demande que x soit egal à un chiffre noit
        type_mise["le noir"]=type_mise["le noir"]*2#double la mise

    if x == 0:# demande que x soit egal à 0
        type_mise[0]=type_mise[0]*36#multiplie ta mise par 36

    #Mise par chiffre

    for i in range(0,37):# i un chiffre entre 1 et 36
        if x == i+1: #si x est égale a un chiffre entre 1 et 36
            type_mise[i+1]=type_mise[i+1]*36#multiplie la mise par 36
            print(type_mise[i+1])#affiche le gain+ la mise de départ

    #Mise par colonne

    if x%3 == 1 :# demande que x soit egal à un chiffre de la première colonne
        type_mise["la première colonne"]=type_mise["la première colonne"]*3#triple la mise

    if x%3 == 2 :# demande que x soit egal à  un chiffre de la seconde colonne
        type_mise["la deuxième colonne"]=type_mise["la deuxième colonne"]*3#triple la mise

    if x%3 == 3:# demande que x soit egal à un chiffre de la troisième colonne
        type_mise["la troisième colonne"]=type_mise["la troisième colonne"]*3#triple la mise

    #Mise par douzaine

    if x > 0 and x <=12:#demande que x soit entre 1 et 12
        type_mise["la première douzaine"]=type_mise["la première douzaine"]*3#multiplie par 3 la mise

    if x > 12 and x <=24:#demande que x soit entre 13 et 24
        type_mise["la deuxième douzaine"]=type_mise["la deuxième douzaine"]*3#multiplie par 3 la mise

    if x > 24 and x <=36:#demande que x soit entre 25 et 36
        type_mise["la troisième douzaine"]=type_mise["la troisième douzaine"]*3#multiplie par 3 la mise

    #mise de 1 à 18 ou de 19 à 36

    if x > 0 and x <=18:#demande que x soit entre 1 et 18
        type_mise["la première moitié"]=type_mise["la première moitié"]*2#multiplie par 2 la mise

    if x > 18 and x <=36:#demande que x soit entre 19 et 36
        type_mise["la deuxième moitié"]=type_mise["la deuxième moitié"]*2#multiplie par 2 la mise

    #mise impair

    if x%2 == 1:#demande que le reste de x/2 est égale à 1
        type_mise["les nombres impairs"]=type_mise["les nombres impairs"]*2#multiplie par 2 la mise

    #mise pair

    if x%2 == 0:#demande que le reste de x/2 est égale à 0
        type_mise["les nombres pairs"]=type_mise["les nombres pairs"]*2#multiplie par 2 la mise
    return(type_mise)#retourne la variale type_mise
