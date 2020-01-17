import time
import pygame
import sys
import random
from random import choice

class MazeWall():
	def __init__(self, posX = 0, posY = 0):
		self._posX = posX
		self._posY = posY
		self._borders = {'TOP':True,'LEFT':True,'RIGHT':True,'BOTTOM':True}

	def get_position(self):
		return self._posX, self._posY

	def get_borders(self):
		return self._borders

	def set_border(self, border):
		self._borders[border] = False

	def remove_border(self, border, another_wall):
		if(border in self._borders.keys() and border in another_wall.get_borders().keys()):
			self._borders[border] = False
			if(border == 'TOP'):
				another_wall.set_border('BOTTOM')
			elif(border == 'LEFT'):
				another_wall.set_border('RIGHT')
			elif(border == 'RIGHT'):
				another_wall.set_border('LEFT')
			elif(border == 'BOTTOM'):
				another_wall.set_border('TOP')

	def all_borders(self):
		return self._borders['TOP'] and self._borders['LEFT'] and self._borders['RIGHT'] and self._borders['BOTTOM']

if __name__ == '__main__' : MazeWall()