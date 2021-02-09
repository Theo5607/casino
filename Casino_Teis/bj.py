import random 

  
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
        if liste_cartes[i][0]>10:
            liste_cartes[i][0]=10
    return liste_cartes
    
liste_cartes=crea_liste_cartes()

    
    
def tirer_carte():
    nb_carte = random.randint(1,52) 
    return(liste_cartes[nb_carte])

def mise():
    arg_mise=int(input("Combien voulez vous miser?"))
    return arg_mise
    
def hit(ct_crp,ct_jr,somme_crp,somme_jr,gains,mise_finale):
    ct_jr.append(tirer_carte())
    somme_jr+=ct_jr[len(ct_jr)-1][0]
    if somme_jr > 21:
        return gains*0
    else:
        return ct_jr,somme_jr
    
    
def stand(ct_crp,ct_jr,somme_crp,somme_jr,gains,mise_finale):
    print(ct_crp[1][1])
    while int(somme_crp) < 17:
        ct_crp.append(tirer_carte())
        somme_crp+=ct_crp[len(ct_crp)-1][0]
    print(somme_jr,somme_crp)
    if int(somme_jr) < int(somme_crp):
        gains=mise_finale*0
    elif int(somme_jr) > int(somme_crp):
        gains=mise_finale*2
    return gains
        
            
    
def blackjack():
    mise_1=3 #mise()
    gains = 0
    ct_jr = []
    ct_crp = []
    ct_jr.append(tirer_carte())
    ct_crp.append(tirer_carte())
    ct_jr.append(tirer_carte())
    ct_crp.append(tirer_carte())
    print(ct_jr,ct_crp)
    if (ct_jr[0][0]==1 and (ct_jr[1][0]==(10 or 11 or 12 or 13))) or (ct_jr[1][0]==1 and (ct_jr[0][0]==(10 or 11 or 12 or 13))): #vérification s'il ya eu un blackjack
        gains = mise_1*2
        print("Blackjack")
    else:
        print(ct_jr[0][1],ct_jr[1][1])
        print(ct_crp[0][1])
        action=''
        somme_jr=ct_jr[0][0] + ct_jr[1][0]
        somme_crp=ct_crp[0][0] + ct_crp[1][0]
        while action !=('1' and '2' and '3' and '4'):          
            action=input("Voulez vous ajouter une carte (1), double (2), spilt (3) ou stand (4)")
        mise_finale=mise_1
        if action == '1':
            hit(ct_crp,ct_jr,somme_crp,somme_jr,gains,mise_finale)
        if action=='4':
            stand(ct_crp,ct_jr,somme_crp,somme_jr,gains,mise_finale)
    
        
    
    
    print(gains)
    return gains


blackjack()