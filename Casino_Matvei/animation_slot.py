import pygame, time

def animation_machine(screen, liste_de_symboles, liste_images):
    list_symbole=liste_de_symboles

#importation de toutes les images

    bar= liste_images[0]
    bar_2= liste_images[1]
    bar_3= liste_images[2]
    symb_7= liste_images[5]
    scatter= liste_images[4]
    cloche=liste_images[6]
    lemon = liste_images[3]
    
    #defintion des postions possibles pour les symboles, allant de gauche a droite et du haut vers le bas

    pos_1=(495, 120)
    pos_2=(700, 120)
    pos_3=(905, 120)
    pos_4=(495, 325)
    pos_5=(700, 325)
    pos_6=(905, 325)
    pos_7=(495, 530)
    pos_8=(700, 530)
    pos_9=(905, 530)
    list_pos=[pos_1,pos_2,pos_3,pos_4,pos_5,pos_6,pos_7,pos_8,pos_9]
    
    #recupere les positions pour les symboles sortant de slot_partie

    for i in range (9):
        if list_symbole[i]==0:
            screen.blit(symb_7,list_pos[i])
        elif list_symbole[i]==1:
            screen.blit(cloche,list_pos[i])
        elif list_symbole[i]==2:
            screen.blit(bar_3,list_pos[i])
        elif list_symbole[i]==3:
            screen.blit(bar_2,list_pos[i])
        elif list_symbole[i]==4:
            screen.blit(bar,list_pos[i])
        elif list_symbole[i]==5:
            screen.blit(lemon,list_pos[i])
        elif list_symbole[i]==6:
            screen.blit(scatter,list_pos[i])
        time.sleep(0.3)
        pygame.display.flip()
