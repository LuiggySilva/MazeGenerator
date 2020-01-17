import time
import pygame
import sys
import random
from random import choice

class Button():
	def __init__(self, pos=(00,00), size='small', text='button', window=None, color="GRAY", font_size=35):
		
		self.font = pygame.font.SysFont("comicsansms", font_size)
		self.black_color = (0,0,0)
		self.white_color = (255,255,255)
		self.color = color
		self.pos = pos
		self.text = text
		self.size = size
		self.size_button = self.get_button_size(self.size)

		self.text_button = self.font.render(self.text, True, self.white_color)
		self.text_button_rect = self.text_button.get_rect().center = (self.pos[0] + self.text_button.get_rect()[2]//4, self.pos[1] + self.text_button.get_rect()[3]//4)
		self.is_clicked = False
		self.window = window

		# Rect
		self.button_rect = pygame.Rect(self.pos[0], pos[1], self.get_button_size(size)[0], self.get_button_size(size)[1])
		pygame.draw.rect(self.window, self.color, self.button_rect)
		# Text
		self.window.blit(self.text_button, self.text_button_rect)
		
		# Top border
		pygame.draw.line(self.window, self.black_color, (self.pos[0], self.pos[1]), (self.pos[0] + self.size_button[0], self.pos[1]), 4)
		# Botton border
		pygame.draw.line(self.window, self.black_color, (self.pos[0], self.pos[1] + self.size_button[1]), (self.pos[0] + self.size_button[0], self.pos[1] + self.size_button[1]), 4)
		# Left border
		pygame.draw.line(self.window, self.black_color, (self.pos[0], self.pos[1]), (pos[0], pos[1] + self.size_button[1]), 4)
		# Right border
		pygame.draw.line(self.window, self.black_color, (self.pos[0] + self.size_button[0], self.pos[1]), (self.pos[0] + self.size_button[0], self.pos[1] + self.size_button[1]), 4)

	def Click(self): 
		if (not self.isClicked()):
			self.is_clicked = True
			self.text_button = self.font.render(self.text, True, self.black_color)	
		else:
			self.is_clicked = False
			self.text_button = self.font.render(self.text, True, self.white_color)
		
		self.window.blit(self.text_button, self.text_button_rect)

	def isClicked(self):
		return self.is_clicked

	def get_button_size(self, size):
		if(size == 'small'):
			return (150,75)
		elif(size == 'medium'):
			return (200, 100)
		else:
			return (100,50)

if __name__ == '__main__' : Button(1200, 600)
