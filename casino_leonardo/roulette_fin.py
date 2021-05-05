type_mise = {"mise_rouge" : 100, "mise_noir" : 100,"mise_colone1" : 100,"mise_colone2" : 100,"mise_colone3" : 100,"mise_douzaine1" : 100,"mise_douzaine2" : 100,"mise_douzaine3" : 100,"mise_1_à_18" : 100,"mise_19_à_36" : 100,"mise_impair" : 100,"mise_pair" : 100,"mise_vert": 1000}
for i in range(1,36):
    type_mise[i+1]=0
#un dictionnaire qui a comme clés sur quoi il va parier et la valeur est égale à combien il va parier

import random#fait appel à la biblioth

def roulette(type_mise):
    """prend en argument un dictionnaire qui a comme clés sur quoi il va parier et la valeur est égale à combien il va parier et retourne les gains ainsi que les symboles qui ont gagné"""
    x=random.randint(0,36)#nombre aléatoire entre 0 et 36
    print("Le chiffre qui est sorti :",x)#affiche le nombre choisi
    rouge = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]#chiffre dans la catégorie rouge
    noir = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]#chiffre dans la catégorie noir
    #Mise par couleur

    if x in rouge:# demande que x soit egal à un chiffre rouge
        type_mise["mise_rouge"]=type_mise["mise_rouge"]*2#double la mise
        print("couleur rouge, vous avez gagné :",type_mise["mise_rouge"])#affiche le gain+ la mise de départ

    if x in noir:# demande que x soit egal à un chiffre noit
        type_mise["mise_noir"]=type_mise["mise_noir"]*2#double la mise
        print("couleur noir, vous avez gagné :",type_mise["mise_noir"])#affiche le gain+ la mise de départ

    if x == 0:# demande que x soit egal à 0
        type_mise["mise_vert"]=type_mise["mise_vert"]*36#multiplie ta mise par 36
        print("couleur vert, vous avez gagné :",type_mise["mise_vert"])#affiche le gain+ la mise de départ

    #Mise par chiffre

    for i in range(0,37):# i un chiffre entre 1 et 36
        if x == i+1: #si x est égale a un chiffre entre 1 et 36
            type_mise[i+1]=type_mise[i+1]*36#multiplie la mise par 36
            print(type_mise[i+1])#affiche le gain+ la mise de départ

    #Mise par colonne

    if x%3 == 1 :# demande que x soit egal à un chiffre de la première colonne
        type_mise["mise_colone1"]=type_mise["mise_colone1"]*3#triple la mise
        print("colonne 1, vous avez gagné :",type_mise["mise_colone1"])#affiche le gain+ la mise de départ

    if x%3 == 2 :# demande que x soit egal à  un chiffre de la seconde colonne
        type_mise["mise_colone2"]=type_mise["mise_colone2"]*3#triple la mise
        print("colonne 2, vous avez gagné :",type_mise["mise_colone2"])#affiche le gain+ la mise de départ

    if x%3 == 3:# demande que x soit egal à un chiffre de la troisième colonne
        type_mise["mise_colone3"]=type_mise["mise_colone3"]*3#triple la mise
        print("colonne 3, vous avez gagné :",type_mise["mise_colone3"])#affiche le gain+ la mise de départ

    #Mise par douzaine

    if x > 0 and x <=12:#demande que x soit entre 1 et 12
        type_mise["mise_douzaine1"]=type_mise["mise_douzaine1"]*3#multiplie par 3 la mise
        print("douzaine 1, vous avez gagné :",type_mise["mise_douzaine1"])#affiche le gain+ la mise de départ

    if x > 12 and x <=24:#demande que x soit entre 13 et 24
        type_mise["mise_douzaine2"]=type_mise["mise_douzaine2"]*3#multiplie par 3 la mise
        print("douzaine 2, vous avez gagné :",type_mise["mise_douzaine2"])#affiche le gain+ la mise de départ

    if x > 24 and x <=36:#demande que x soit entre 25 et 36
        type_mise["mise_douzaine3"]=type_mise["mise_douzaine3"]*3#multiplie par 3 la mise
        print("douzaine 3, vous avez gagné :",type_mise["mise_douzaine3"])#affiche le gain+ la mise de départ

    #mise de 1 à 18 ou de 19 à 36

    if x > 0 and x <=18:#demande que x soit entre 1 et 18
        type_mise["mise_1_à_18"]=type_mise["mise_1_à_18"]*2#multiplie par 2 la mise
        print("mise entre 1 à 18, vous avez gagné :",type_mise["mise_1_à_18"])#affiche le gain+ la mise de départ

    if x > 18 and x <=36:#demande que x soit entre 19 et 36
        type_mise["mise_19_à_36"]=type_mise["mise_19_à_36"]*2#multiplie par 2 la mise
        print("mise entre 19 à 36, vous avez gagné :",type_mise["mise_19_à_36"])#affiche le gain+ la mise de départ

    #mise impair

    if x%2 == 1:#demande que le reste de x/2 est égale à 1
        type_mise["mise_impair"]=type_mise["mise_impair"]*2#multiplie par 2 la mise
        print("mise pair, vous avez gagné :",type_mise["mise_impair"])#affiche le gain+ la mise de départ

    #mise pair

    if x%2 == 0:#demande que le reste de x/2 est égale à 0
        type_mise["mise_pair"]=type_mise["mise_pair"]*2#multiplie par 2 la mise
        print("mise impair, vous avez gagné :",type_mise["mise_pair"])#affiche le gain+ la mise de départ
    return(type_mise)#retourne la variale type_mise

#type_mise_new=roulette(type_mise)#type_mise_new est une variable égale à roulette(type_mise)
