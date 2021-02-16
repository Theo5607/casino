import sys, time, pygame
from tkinter import *
from sqlite3 import *
from pygame.locals import *
#from Casino_Matvei.test import slot_partie

pygame.init()

screen = pygame.display.set_mode((1600, 900))

#image fond machine

fond_slot= pygame.image.load("images/fond_slot_machine.png")


screen.blit(fond_slot, (0, 0))
pygame.display.flip()

#importation de toutes les images

bar= pygame.image.load("images/bar.png")
bar_2= pygame.image.load("images/2_bar.png")
bar_3= pygame.image.load("images/3_bar.png")
symb_7= pygame.image.load("images/7.png")
bar= pygame.image.load("images/bar.png")
cherry= pygame.image.load("images/cherry.png")
cloche=pygame.image.load("images/cloche.png")
