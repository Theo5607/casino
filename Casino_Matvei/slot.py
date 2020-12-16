import random

def slot_jeu(): #appeller cette fonction pour jouer au slot
    mise=''
    while mise!='10' and mise!='25' and mise!='50' and mise!='100' and mise!='500' and mise!='1000' and mise!='777': #demande à combien s'élevra la mise 
        
        mise = input('Combien voulez vous miser? (10, 25, 50, 100, 500 ou 1000) ou sortir de la machine à sous (777)? ')
        if mise == '777':
            slot_machine()
        else: #à partir d'ici programme du jeu de la machine à sous
            def slot_partie(mise): #fonction prenant en argument lamise sur laquelle l'utlisateur va jouer
                symboles=['7','cloche','bar3','bar2','bar1','lemon','scatter']
                #définition des symboles tirés
                p1=symboles[random.randint(0,6)] 
                p2=symboles[random.randint(0,6)]
                p3=symboles[random.randint(0,6)]
                p4=symboles[random.randint(0,6)]
                p5=symboles[random.randint(0,6)]
                p6=symboles[random.randint(0,6)]
                p7=symboles[random.randint(0,6)]
                p8=symboles[random.randint(0,6)]
                p9=symboles[random.randint(0,6)]
                



def slot_machine(): #decider si on veut jouer ou sortir
    print("Vous voici donc dans la machine à sous de notre casino")

    rep_slot=''
    while rep_slot!='1' and rep_slot!='0': #permet de décider si l'on veut jouer au slot ou reveni au hall
        rep_slot = input('Voulez vous vous jouer (0) ou revenir au hall (1)? ')
        print(rep_slot)

    if rep_slot=='1': #fait revenir au hall
        pass
        #hall()
    
    if rep_slot=='0': #nous laisse jouer au jeu
        slot_jeu()
    return
    
slot_machine()