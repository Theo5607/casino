import random

def ret_spec(nb): #Retourne le nom de la carte
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

def crea_liste_cartes(): #Renvoie un dictionnaire qui renvoie pour une clé qui va de 1 à 52 pour le numéro cartes une liste qui contient la valeur de la carte, son nom et sa couleur
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
    
    return liste_cartes
    
liste_cartes=crea_liste_cartes()
    
    
def tirer_carte(cartes):
    nb_carte = random.randint(1,54)
        
    return(liste_cartes[nb_carte])
    

def blackjack(mise, somme_cartes_croupier, somme_cartes_joueur):
    gains = 0
    if somme_cartes_joueur >= somme_cartes_croupier:
        gains = mise*2
    
    return gains
