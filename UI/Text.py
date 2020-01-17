import time
import pygame
import sys
import random
from random import choice

class Text():
	def __init__(self, pos=(0,0), pure_text='text', font_size=25, color=(0,0,0), window=None):
		
		self.font = pygame.font.SysFont("comicsansms", font_size)
		self.window = window
		self.text = self.font.render(pure_text, True, color)
		self.window.blit(self.text, (pos[0] - self.text.get_rect()[2]//2, pos[1]))

if __name__ == '__main__' : Text()