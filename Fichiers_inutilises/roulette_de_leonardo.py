import random
rouge = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]#chiffre dans la catégorie rouge
noir = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]#chiffre dans la catégorie noir
mise_rouge=50#mise multipliée par 2
mise_noir=50#mise multipliée par 2

mise_0=50#mise multipliée par 36
mise_1=50#mise multipliée par 36
mise_2=50#mise multipliée par 36
mise_3=50#mise multipliée par 36
mise_4=50#mise multipliée par 36
mise_5=50#mise multipliée par 36
mise_6=50#mise multipliée par 36
mise_7=50#mise multipliée par 36
mise_8=50#mise multipliée par 36
mise_9=50#mise multipliée par 36
mise_10=50#mise multipliée par 36
mise_11=50#mise multipliée par 36
mise_12=50#mise multipliée par 36
mise_13=50#mise multipliée par 36
mise_14=50#mise multipliée par 36
mise_15=50#mise multipliée par 36
mise_16=50#mise multipliée par 36
mise_17=50#mise multipliée par 36
mise_18=50#mise multipliée par 36
mise_19=50#mise multipliée par 36
mise_20=50#mise multipliée par 36
mise_21=50#mise multipliée par 36
mise_22=50#mise multipliée par 36
mise_23=50#mise multipliée par 36
mise_24=50#mise multipliée par 36
mise_25=50#mise multipliée par 36
mise_26=50#mise multipliée par 36
mise_27=50#mise multipliée par 36
mise_28=50#mise multipliée par 36
mise_29=50#mise multipliée par 36
mise_30=50#mise multipliée par 36
mise_31=50#mise multipliée par 36
mise_32=50#mise multipliée par 36
mise_33=50#mise multipliée par 36
mise_34=50#mise multipliée par 36
mise_35=50#mise multipliée par 36
mise_36=50#mise multipliée par 36

mise_colone1=50#mise multipliée par 3
mise_colone2=50#mise multipliée par 3
mise_colone3=50#mise multipliée par 3

mise_douzaine1=50#mise multipliée par 3
mise_douzaine2=50#mise multipliée par 3
mise_douzaine3=50#mise multipliée par 3

mise_1_à_18=50#mise multipliée par 2
mise_19_à_36=50#mise multipliée par 2

x=random.randint(0,36)#nombre aléatoire entre 0 et 36
print(x)#affiche le nombre choisi

#Mise par couleur

if x == 1 or x == 3 or x == 5 or x == 7 or x == 9 or x == 12 or x == 14 or x == 16 or x == 18 or x == 19 or x == 21 or x == 23 or x == 25 or x == 27 or x == 30 or x == 32 or x == 34 or x == 36:# demande que x soit egal à un chiffre rouge
    mise_rouge=mise_rouge*2#double la mise
    print(mise_rouge)#affiche le gain+ la mise de départ

if x == 2 or x == 4 or x == 6 or x == 8 or x == 10 or x == 11 or x == 13 or x == 15 or x == 17 or x == 20 or x == 22 or x == 24 or x == 26 or x == 28 or x == 29 or x == 31 or x == 33 or x == 35:# demande que x soit egal à un chiffre noit
    mise_noir=mise_noir*2#double la mise
    print(mise_noir)#affiche le gain+ la mise de départ

#Mise par chiffre

if x == 0:
    mise_0=mise_0*36
    print(mise_0)

if x == 1:
    mise_1=mise_1*36
    print(mise_1)

if x == 2:
    mise_2=mise_2*36
    print(mise_2)

if x == 3:
    mise_3=mise_3*36
    print(mise_3)

if x == 4:
    mise_4=mise_4*36
    print(mise_4)

if x == 5:
    mise_5=mise_5*36
    print(mise_5)

if x == 6:
    mise_6=mise_6*36
    print(mise_6)

if x == 7:
    mise_7=mise_7*36
    print(mise_7)

if x == 8:
    mise_8=mise_8*36
    print(mise_8)

if x == 9:
    mise_9=mise_9*36
    print(mise_9)

if x == 10:
    mise_10=mise_10*36
    print(mise_10)

if x == 11:
    mise_11=mise_11*36
    print(mise_11)

if x == 12:
    mise_12=mise_12*36
    print(mise_12)

if x == 13:
    mise_13=mise_13*36
    print(mise_13)

if x == 14:
    mise_14=mise_14*36
    print(mise_14)

if x == 15:
    mise_15=mise_15*36
    print(mise_15)

if x == 16:
    mise_16=mise_16*36
    print(mise_16)

if x == 17:
    mise_17=mise_17*36
    print(mise_17)

if x == 18:
    mise_18=mise_18*36
    print(mise_18)

if x == 19:
    mise_19=mise_19*36
    print(mise_19)

if x == 20:
    mise_20=mise_20*36
    print(mise_20)

if x == 21:
    mise_21=mise_21*36
    print(mise_21)

if x == 22:
    mise_22=mise_22*36
    print(mise_22)

if x == 23:
    mise_23=mise_23*36
    print(mise_23)

if x == 24:
    mise_24=mise_24*36
    print(mise_24)

if x == 25:
    mise_25=mise_25*36
    print(mise_25)

if x == 26:
    mise_26=mise_26*36
    print(mise_26)

if x == 27:
    mise_27=mise_27*36
    print(mise_27)

if x == 28:
    mise_28=mise_28*36
    print(mise_28)

if x == 29:
    mise_29=mise_29*36
    print(mise_29)

if x == 30:
    mise_30=mise_30*36
    print(mise_30)

if x == 31:
    mise_31=mise_31*36
    print(mise_31)

if x == 32:
    mise_32=mise_32*36
    print(mise_32)

if x == 33:
    mise_33=mise_33*36
    print(mise_33)

if x == 34:
    mise_34=mise_34*36
    print(mise_34)

if x == 35:
    mise_35=mise_35*36
    print(mise_35)

if x == 36:
    mise_36=mise_36*36
    print(mise_36)

#Mise par colonne

if x == 1 or x == 4 or x == 7 or x == 10 or x == 13 or x == 16 or x == 19 or x == 22 or x == 25 or x == 28 or x == 31 or x == 34:# demande que x soit egal à un chiffre de la première colonne
    mise_colone1=mise_colone1*3#triple la mise
    print(mise_colone1)#affiche le gain+ la mise de départ

if x == 2 or x == 5 or x == 8 or x == 11 or x == 14 or x == 17 or x == 20 or x == 23 or x == 26 or x == 29 or x == 32 or x == 35:# demande que x soit egal à un chiffre de la seconde colonne
    mise_colone2=mise_colone2*3#triple la mise
    print(mise_colone2)#affiche le gain+ la mise de départ

if x == 3 or x == 6 or x == 9 or x == 12 or x == 15 or x == 18 or x == 21 or x == 24 or x == 27 or x == 30 or x == 33 or x == 36:# demande que x soit egal à un chiffre de la troisième colonne
    mise_colone3=mise_colone3*3#triple la mise
    print(mise_colone3)#affiche le gain+ la mise de départ

#Mise par douzaine

if x > 0 and x <=12:#demande que x soit entre 1 et 12
    mise_douzaine1=mise_douzaine1*3#multiplie par 3 la mise
    print(mise_douzaine1)#affiche le gain+ la mise de départ

if x > 12 and x <=24:#demande que x soit entre 13 et 24
    mise_douzaine2=mise_douzaine2*3#multiplie par 3 la mise
    print(mise_douzaine2)#affiche le gain+ la mise de départ

if x > 24 and x <=36:#demande que x soit entre 25 et 36
    mise_douzaine3=mise_douzaine3*3#multiplie par 3 la mise
    print(mise_douzaine3)#affiche le gain+ la mise de départ

#mise de 1 à 18 ou de 19 à 36

if x > 0 and x <=18:#demande que x soit entre 1 et 18
    mise_1_à_18=mise_1_à_18*2#multiplie par 2 la mise
    print(mise_1_à_18)#affiche le gain+ la mise de départ

if x > 18 and x <=36:#demande que x soit entre 19 et 36
    mise_19_à_36=mise_19_à_36*2#multiplie par 2 la mise
    print(mise_19_à_36)#affiche le gain+ la mise de départ
