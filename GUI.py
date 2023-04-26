#gui for sudoku solver
import pygame

def sudoku_gui():
     pygame.init()
     gui_size = (700,700)
     screen = pygame.display.set_mode(gui_size)
     screen.fill("")