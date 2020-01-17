import time
import pygame
import sys
import random
from random import choice
from UI import Menu
from Maze import CreateMaze

class Main():
	def __init__(self, win_width, win_height):
		
		pygame.init()

		self.WINDOW_TITLE = 'Maze Generator'
		self.PYGAME_HEIGHT = win_height
		self.PYGAME_WIDTH = win_width
		self.Clock = pygame.time.Clock()
		self.COLORS = {
			"BLACK":(0,0,0),
			"GRAY":(105,105,105),
			"WHITE":(255,255,255),
			"RED":(255,0,0),
			"BLUE":(0,0,255),
			"GREEM":(0,0,255),
			"YELLOW":(255,255,0),
			"BROWN":(102, 51, 0),
			"ORANGE":(255, 153, 51),
			"PINK":(255, 51, 153)
		}
		self.Window = pygame.display.set_mode((self.PYGAME_WIDTH, self.PYGAME_HEIGHT))
		# Menu de seleção do tamanho do labirinto
		self.menu = Menu.Menu(self.PYGAME_HEIGHT, self.PYGAME_WIDTH, self.WINDOW_TITLE, self.COLORS, self.Clock, self.Window)
		# Construção do labirinto e renderização do labirinto
		self.maze = CreateMaze.CreateMaze(self.get_tuple_maze_size(), self.COLORS, self.Clock, self.Window)

	def get_tuple_maze_size(self):
		maze_size = self.menu.getMazeSize().split('x') 
		return (int(maze_size[0]), int(maze_size[1]))


if __name__ == '__main__' : Main(1200, 600)
