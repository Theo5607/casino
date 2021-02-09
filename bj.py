import random


import random

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
'''Renvoie un dictionnaire qui renvoie pour une clé qui va de 1 à 52 pour le numéro cartes une liste qui contient la valeur de la carte, son nom et sa couleur'''
    liste_cartes={}

    for i in range(1,53):
        nb=i
        famille_nb=0

        while nb > 13:
            nb=nb-13
            famille_nb=famille_nb+1

        if famille_nb==0:
            liste_cartes[i]=[nb,ret_spec(nb),'coeur']
        elif famille_nb==1:
            liste_cartes[i]=[nb,ret_spec(nb),'carreau']
        elif famille_nb==2:
            liste_cartes[i]=[nb,ret_spec(nb),'pique']
        elif famille_nb==3:
            liste_cartes[i]=[nb,ret_spec(nb),'trèfle']
        if liste_cartes[i][0]>10:
            liste_cartes[i][0]=10
    return liste_cartes

liste_cartes=crea_liste_cartes()



def tirer_carte():
    '''Tire une carte aléatoire dans le dictionnaire et retourne la carte tirer'''
    nb_carte = random.randint(1,52)
    return(liste_cartes[nb_carte])

def mise():
     '''Demande au joueur le mise qu'il souhaite miser et la retourne'''
    arg_mise=int(input("Combien voulez vous miser?"))
    return arg_mise

def hit(ct_jr):
    ct_jr_hit=ct_jr
    ct_jr_hit.append(tirer_carte())
    return ct_jr


def stand(ct_crp,ct_jr,somme_crp,somme_jr,gains,mise_finale):
    '''Le joueur ne tire pas de nouvelle carte, le croupier peut tirer une carte que si la somme des ses deux cartes est inferieur à 17'''
    print(ct_crp[1][1])

    #ajoute des cartes au croupier tant qu'il n'a pas plus de 17
    while int(somme_crp) < 17:
        ct_crp.append(tirer_carte())
        somme_crp+=ct_crp[len(ct_crp)-1][0]
    print("les cartes du croupiers sont:",ct_crp)
    print("la somme des cartes du croupier est:", somme_crp)
    print("la somme des cartes du joueur est:", somme_jr)


    if int(somme_jr) < int(somme_crp) and int(somme_crp)<21:
        gains=mise_finale*0
        print("here loose")
    elif int(somme_jr) > int(somme_crp) or int(somme_crp)>21:
        gains=mise_finale*2
        print("here win")
    return gains



def blackjack():
    '''Tire les différentes cartes aux joueur et au croupier, le joueur gagne directement si la somme de ses cartes est égale à 21, sinon on demande au joueur ce qu'il souhaite faire: 1=tirer une carte'''
    mise_1=3 #mise()
    gains = 0
    ct_jr = [] #création d'une liste contenant les cartes du joueur
    ct_crp = [] #création d'une liste contenant les cartes du croupier

    #ajoute les deux premières cartes au joueur et au croupier
    ct_jr.append(tirer_carte())
    ct_crp.append(tirer_carte())
    ct_jr.append(tirer_carte())
    ct_crp.append(tirer_carte())

    #check si il y a eu blackjack direct
    if (ct_jr[0][0]==1 and (ct_jr[1][0]==(10 or 11 or 12 or 13))) or (ct_jr[1][0]==1 and (ct_jr[0][0]==(10 or 11 or 12 or 13))): #vérification s'il ya eu un blackjack
        gains = mise_1*2
        print("Blackjack")


    else:
        print("cartes du joueur: un", ct_jr[0][1],"et un",ct_jr[1][1])
        print()
        print("cartes du croupier: un", ct_crp[0][1])
        print()
        action=''
        somme_jr=ct_jr[0][0] + ct_jr[1][0]
        somme_crp=ct_crp[0][0] + ct_crp[1][0]
        stand_check=False

        #boucle qui se répéte tant que la partie n'est pas terminée
        while stand_check!=True:

            while action !=('1' and '2' and '3' and '4'): #demande au joueur ce qu'il souhaite faire 1= tirer une carte, 2= double la mise et tire une seul carte, 3=si jamais un double tombe on peut diviser les cartes 4= le joueur ne fait rien
                action=input("Voulez vous ajouter une carte (1), double (2), spilt (3) ou stand (4)")
                mise_finale=mise_1
                if action == '1':
                    ct_jr=hit(ct_jr)
                    somme_jr+=ct_jr[len(ct_jr)-1][0]
                    print("vous avez cette somme de cartes:",somme_jr)
                if action=='4':
                    gains=stand(ct_crp,ct_jr,somme_crp,somme_jr,gains,mise_finale)
                    stand_check=True

                #dit que le joueur a perdu s'il a plus de 21 en mains
                if somme_jr>21:
                    gains=0
                    print("vous avez plus de 21 en valeurs de cartes vous perdez")







    print("vous avez gagner:", gains)
    return gains


blackjack()
