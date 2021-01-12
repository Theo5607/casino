import random
type_mise = {"mise_rouge" : 0, "mise_noir" : 0,"mise_colone1" : 0               ,"mise_colone2" : 0,"mise_colone3" : 0,"mise_douzaine1" : 0,"mise_douzaine2" : 0,"mise_douzaine3" : 0,"mise_1_à_18" : 0,"mise_19_à_36" : 0,"mise_impair" : 0,"mise_pair" : 0}
for i in range(0,36):
    type_mise[i+1]=0
    print(type_mise)

x=random.randint(0,36)#nombre aléatoire entre 0 et 36
print(x)#affiche le nombre choisi

#Mise par couleur

if x == 1 or x == 3 or x == 5 or x == 7 or x == 9 or x == 12 or x == 14 or x ==16 or x == 18 or x == 19 or x == 21 or x == 23 or x == 25 or x == 27 or x == 30 or x == 32 or x == 34 or x == 36:# demande que x soit egal à un chiffre rouge
    type_mise["mise_rouge"]=type_mise["mise_rouge"]*2#double la mise
    print(type_mise["mise_rouge"])#affiche le gain+ la mise de départ

if x == 2 or x == 4 or x == 6 or x == 8 or x == 10 or x == 11 or x == 13 or x == 15 or x == 17 or x == 20 or x == 22 or x == 24 or x == 26 or x == 28 or x == 29 or x == 31 or x == 33 or x == 35:# demande que x soit egal à un chiffre noit    
    type_mise["mise_noir"]=type_mise["mise_noir"]*2#double la mise
    print(type_mise["mise_noir"])#affiche le gain+ la mise de départ

#Mise par chiffre

for i in range(0,36):
    if x == i+1:
        type_mise[i+1]=type_mise[i+1]*36
        print(type_mise[i+1])

#Mise par colonne

if x == 1 or x == 4 or x == 7 or x == 10 or x == 13 or x == 16 or x == 19 or x == 22 or x == 25 or x == 28 or x == 31 or x == 34:# demande que x soit egal à un chiffre de la première colonne
    type_mise["mise_colone1"]=type_mise["mise_colone1"]*3#triple la mise
    print(type_mise["mise_colone1"])#affiche le gain+ la mise de départ

if x == 2 or x == 5 or x == 8 or x == 11 or x == 14 or x == 17 or x == 20 or x  == 23 or x == 26 or x == 29 or x == 32 or x == 35:# demande que x soit egal à  un chiffre de la seconde colonne
    type_mise["mise_colone2"]=type_mise["mise_colone2"]*3#triple la mise
    print(type_mise["mise_colone2"])#affiche le gain+ la mise de départ

if x == 3 or x == 6 or x == 9 or x == 12 or x == 15 or x == 18 or x == 21 or x == 24 or x == 27 or x == 30 or x == 33 or x == 36:# demande que x soit egal à un chiffre de la troisième colonne
    type_mise["mise_colone3"]=type_mise["mise_colone3"]*3#triple la mise
    print(type_mise["mise_colone3"])#affiche le gain+ la mise de départ

#Mise par douzaine

if x > 0 and x <=12:#demande que x soit entre 1 et 12
    type_mise["mise_douzaine1"]=type_mise["mise_douzaine1"]*3#multiplie par 3 la mise
    print(type_mise["mise_douzaine1"])#affiche le gain+ la mise de départ

if x > 12 and x <=24:#demande que x soit entre 13 et 24
    type_mise["mise_douzaine2"]=type_mise["mise_douzaine2"]*3#multiplie par 3 la mise
    print(type_mise["mise_douzaine2"])#affiche le gain+ la mise de départ

if x > 24 and x <=36:#demande que x soit entre 25 et 36
    type_mise["mise_douzaine3"]=type_mise["mise_douzaine3"]*3#multiplie par 3 la mise
    print(type_mise["mise_douzaine3"])#affiche le gain+ la mise de départ

#mise de 1 à 18 ou de 19 à 36

if x > 0 and x <=18:#demande que x soit entre 1 et 18
    type_mise["mise_1_à_18"]=type_mise["mise_1_à_18"]*2#multiplie par 2 la mise
    print(type_mise["mise_1_à_18"])#affiche le gain+ la mise de départ

if x > 18 and x <=36:#demande que x soit entre 19 et 36
    type_mise["mise_19_à_36"]=type_mise["mise_19_à_36"]*2#multiplie par 2 la mise
    print(type_mise["mise_19_à_36"])#affiche le gain+ la mise de départ

#mise impair

if x%2 == 1:#demande que le reste de x/2 est égale à 1
    type_mise["mise_impair"]=type_mise["mise_impair"]*2#multiplie par 2 la mise
    print(type_mise["mise_impair"])#affiche le gain+ la mise de départ

#mise pair

if x%2 == 0:#demande que le reste de x/2 est égale à 0
    type_mise["mise_pair"]=type_mise["mise_pair"]*2#multiplie par 2 la mise
    print(type_mise["mise_pair"])#affiche le gain+ la mise de départ
