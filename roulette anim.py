import pygame, time, random
def animation_roulette(x):
    white = 255, 255, 255
    print("x")
    pygame.init()
    screen = pygame.display.set_mode((1600,900))

    bandeau = pygame.image.load("bandeau_roulette.png")
    triangle = pygame.image.load("triangle.png")
    screen.fill(white)
    list_machine=[323,379,299,331,307,395,283,347,407,363,399,415,339,423,371,463,387,439,355,459,375,451,359,403,391,443,327,427,343,351,411,367,467,383,435,335,419]

    for i in range(list_machine[x]):
        screen.blit(bandeau, (-17760+30*i,430))
        screen.blit(triangle, (780,340))
        pygame.display.flip()
        time.sleep(0.025)
    return



