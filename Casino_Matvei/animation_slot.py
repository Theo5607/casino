def animation_machine(liste_de_symboles):
    list_symbole=liste_de_symboles
    screen = pygame.display.set_mode((1600, 900))

#image fond machine

    fond_slot= pygame.image.load("images/fond_slot_machine.png")


    screen.blit(fond_slot, (0, 0))


#importation de toutes les images

    bar= pygame.image.load("images/bar.png")
    watermelon= pygame.image.load("images/watermelon.png")
    cherry= pygame.image.load("images/cherry.png")
    symb_7= pygame.image.load("images/symb_7.png")
    diamond= pygame.image.load("images/diamond.png")
    cloche=pygame.image.load("images/cloche.png")
    lemon = pygame.image.load("images/lemon.png")

    pos_1=(495, 95)
    pos_2=(700, 95)
    pos_3=(905, 95)
    pos_4=(495, 300)
    pos_5=(700, 300)
    pos_6=(905, 300)
    pos_7=(495, 505)
    pos_8=(700, 505)
    pos_9=(905, 505)
    list_pos=[pos_1,pos_2,pos_3,pos_4,pos_5,pos_6,pos_7,pos_8,pos_9]

    #symboles=['7','cloche','cherry','watermelon','bar','lemon','scatter']

    list_symbole = slot_partie(13)[0]


    for i in range (9):
        if list_symbole[i-1]==0:
            screen.blit(symb_7,list_pos[i-1])
        elif list_symbole[i-1]==1:
            screen.blit(cloche,list_pos[i-1])
        elif list_symbole[i-1]==2:
            screen.blit(bar_3,list_pos[i-1])
        elif list_symbole[i-1]==3:
            screen.blit(bar_2,list_pos[i-1])
        elif list_symbole[i-1]==4:
            screen.blit(bar,list_pos[i-1])
        elif list_symbole[i-1]==5:
            screen.blit(lemon,list_pos[i-1])
        elif list_symbole[i-1]==6:
            screen.blit(scatter,list_pos[i-1])
    pygame.display.flip()
