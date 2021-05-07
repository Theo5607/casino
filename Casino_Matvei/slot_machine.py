import random

def slot_partie(mise): #fonction prenant en argument lamise sur laquelle l'utlisateur va jouer
    gains_slot=0 #création de la variable gains_slot qui définit combien ont été gagné sur cette session

    symboles=['7','cloche','cherry','watermelon','bar','lemon','scatter'] #liste des symboles tirables

    #définition des symboles tirés
    p1=random.randint(0,6)
    p2=random.randint(0,6)
    p3=random.randint(0,6)
    p4=random.randint(0,6)
    p5=random.randint(0,6)
    p6=random.randint(0,6)
    p7=random.randint(0,6)
    p8=random.randint(0,6)
    p9=random.randint(0,6)

    tirage=[p1,p2,p3,p4,p5,p6,p7,p8,p9] #création d'une liste des valeurs utiliées pour définir les gains

    #vérification des tirages des 7
    if tirage.count(0)==3:
        gains_slot=gains_slot+(mise*2)
    elif tirage.count(0)==4:
        gains_slot=gains_slot+(mise*5)
    elif tirage.count(0)==5:
        gains_slot=gains_slot+(mise*20)
    elif tirage.count(0)==6:
        gains_slot=gains_slot+(mise*50)
    elif tirage.count(0)==7:
        gains_slot=gains_slot+(mise*200)
    elif tirage.count(0)==8:
        gains_slot=gains_slot+(mise*1000)
    elif tirage.count(0)==9:
        gains_slot=gains_slot+(mise*9000)

    #vérification des tirages des scatters
    dice1=0
    dice2=0
    if tirage.count(6)==3 or tirage.count(6)>3:
        dice1=random.randint(1,6)
        dice2=random.randint(1,6)
        if dice1==dice2:
            gains_slot=gains_slot+mise*10
        else:
            gains_slot=gains_slot+mise*2

    #vérification de toutes les autres combinaisons
    def multi(pos): #définition d'une fonction à laquelle faire appel pour les mutiplicateurs
        gains_temp=0
        if pos==1:
            gains_temp=gains_temp+mise*8
        elif pos==2:
            gains_temp=gains_temp+mise*6
        elif pos==3:
            gains_temp=gains_temp+mise*4
        elif pos==4:
            gains_temp=gains_temp+mise*3
        elif pos==5:
            gains_temp=gains_temp+mise*1
        return gains_temp

    #p1-p2-p3 (horizontale haut)
    if p1==p2 and p1==p3 and p1!=0 and p1!=6:
        gains_slot=gains_slot+multi(p1)

    #p1-p5-p9 (diagonale haut-gauche to bas-droite)
    if p1==p5 and p1==p9 and p1!=0 and p1!=6:
        gains_slot=gains_slot+multi(p1)

    #p1-p4-p7 (verticale gauche)
    if p1==p4 and p1==p7 and p1!=0 and p1!=6:
        gains_slot=gains_slot+multi(p1)

    #p2-p5-p8 (verticale milieu)
    if p2==p5 and p2==p8 and p2!=0 and p2!=6:
        gains_slot=gains_slot+multi(p2)

    #p3-p6-p9 (verticale droite)
    if p3==p6 and p3==p9 and p3!=0 and p3!=6:
        gains_slot=gains_slot+multi(p3)

    #p3-p5-p7 (diagonale haut-droite to bas-gauche)
    if p3==p5 and p3==p7 and p3!=0 and p3!=6:
        gains_slot=gains_slot+multi(p3)

    #p4-p5-p6 (horizontale milieu)
    if p4==p5 and p4==p6 and p4!=0 and p4!=6:
        gains_slot=gains_slot+multi(p4)

    #p7-p8-p9 (horizontale bas)
    if p7==p8 and p7==p9 and p7!=0 and p7!=6:
        gains_slot=gains_slot+multi(p7)

    return gains_slot, tirage
