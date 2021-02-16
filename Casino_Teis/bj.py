import random

def play_blackjack(mise):
    #phrase qui explique si on a gagner ou pas
    phrase=" "
    gains=0

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
  
        
    '''Tire les différentes cartes aux joueur et au croupier, le joueur gagne directement si la somme de ses cartes est égale à 21, sinon on demande au joueur ce qu'il souhaite faire: 1=tirer une carte'''
    mise #mise()
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
        gains = mise*2
        print("Blackjack")


    else:
        print("cartes du joueur: un", ct_jr[0][1],"et un",ct_jr[1][1])
        print()
        print("cartes du croupier: un", ct_crp[0][1])
        print()
        action=''
        somme_jr=ct_jr[0][0] + ct_jr[1][0]
        somme_crp=ct_crp[0][0] + ct_crp[1][0]
        end_check=False

        #boucle qui se répéte tant que la partie n'est pas terminée
        while end_check!=True:

            while action !=('1' and '2' and '3' and '4'): #demande au joueur ce qu'il souhaite faire 1= tirer une carte, 2= double la mise et tire une seul carte, 3=si jamais un double tombe on peut diviser les cartes 4= le joueur ne fait rien
                action=input("Voulez vous ajouter une carte (1), double (2), spilt (3) ou stand (4)")

                if action == '1':
                    ct_jr.append(tirer_carte())
                    somme_jr+=ct_jr[len(ct_jr)-1][0]
                    print("vous avez cette somme de cartes:",somme_jr)
                    

                #ajoute des cartes au croupier tant qu'il na pas 17    
                if action=='4':
                    while int(somme_crp) < 17:
                        ct_crp.append(tirer_carte())
                        somme_crp+=ct_crp[len(ct_crp)-1][0]
                        print(somme_crp)

                #dit que le croupier a perdu s'il a plus de 21 en mains
                if somme_crp>21 and somme_jr<21:
                    gains=mise*2
                    phrase="Le croupier a dépassé 21 vous gagnez"
                    end_check=True
                    break
                #dit que le joueur a perdu s'il a plus de 21 en mains
                elif somme_jr>21:
                    gains=0
                    phrase="Vous avez plus de 21 en cartes, vous perdez"
                    end_check=True
                    break
                elif somme_crp>somme_jr and  somme_crp<=21:
                    gains=0
                    phrase="le croupier a plus que vous"
                    end_check=True
                    break



    return gains,phrase


print(play_blackjack(3))
