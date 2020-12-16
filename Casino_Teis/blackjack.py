from random import *

def blackjack():
    nb_j = 0
    somme_joueurs = {}
    somme_croupier = 0

    while nb_j < 2:
        nb_j = int(input('Entrez un nombre de joueurs: '))
    for i in range(1,nb_j+1):
        somme = 0
        carte1 = randint(1,13)
        carte2 = randint(1,13)
        carte_croupier = randint(1,13)
        print('Le croupier tire les cartes du joueurs',i,'...')
        if carte1 == 1:
            print('La première carte est un as')
            somme = 11
        elif carte1 == 11:
            print('La première carte est un valet')
            somme = 10
        elif carte1 == 12:
            print('La première carte est une dame')
            somme = 10
        elif carte1 == 13:
            print('La première carte est un roi')
            somme = 10
        else:
            print('La première carte est un',carte1)
            somme = carte1
        if carte2 == 1:
            print('La deuxième carte est un as')
            somme = somme+11
        elif carte2 == 11:
            print('La deuxième carte est un valet')
            somme = somme+10
        elif carte2 == 12:
            print('La deuxième carte est une dame')
            somme = somme+10
        elif carte2 == 13:
            print('La deuxième carte est un roi')
            somme = somme+10
        else:
            print('La deuxième carte est un',carte2)
            somme = somme+carte2
        print('Vous êtes à',somme)
        somme_joueurs[i] = somme
    print('Le croupier tire sa carte')
    if carte_croupier == 1:
        print('La carte du croupier est un as')
        somme_croupier = somme_croupier+11
    elif carte_croupier == 11:
        print('La carte du croupier est un valet')
        somme_croupier = somme_croupier+10
    elif carte_croupier == 12:
        print('La carte du croupier est une dame')
        somme_croupier = somme_croupier+10
    elif carte_croupier == 13:
        print('La carte du croupier est un roi')
        somme_croupier = somme_croupier+10
    else:
        print('La carte du croupier est un',carte_croupier)
        somme_croupier = somme_croupier+carte2
    print('___________')
    print('La somme du croupier est',somme_croupier)
