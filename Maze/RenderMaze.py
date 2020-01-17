import time
import pygame
import sys
import random
from random import choice
from UI import Text, Button
import main

class RenderMaze():
	def __init__(self, window=None, sizes=None, PYGAME_WIDTH=1200, PYGAME_HEIGHT=600, POSX=0, POSY=0, pixelSize=25, maze_matrix=None, size_maze=(10,5), pixelPOSIncrement=1, COLORS=['BLACK'], Clock=None):
		# Rendering rects of matrix
		self.POSX = POSX
		self.POSY = POSY
		self.sizes = sizes
		self.POSX = POSX
		self.POSY = POSY
		self.COLORS = COLORS
		self.pixelSize = pixelSize
		self.pixelPOSIncrement = pixelPOSIncrement
		self.PYGAME_WIDTH = PYGAME_WIDTH
		self.PYGAME_HEIGHT = PYGAME_HEIGHT
		self.size_maze = size_maze
		self.maze_matrix = maze_matrix
		self.window = window
		self.Clock = Clock
		self.window.fill(self.COLORS['WHITE'])

		self.title = Text.Text(pos=(self.PYGAME_WIDTH//2, 10), pure_text=f'Maze ({self.size_maze[0]},{self.size_maze[1]}):', font_size=40, color=COLORS["BLACK"], window=self.window)
		self.back = Button.Button(pos=(1085, 10), text='BACK', size='smaller', window=self.window, color=self.COLORS["GRAY"], font_size=25)
		self.buttons = [self.back]
		self.Draw = False
		self.simple_maze = self.maze_borders()
		self.create_simple_maze()

		while(True):
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
					mouse_pos = pygame.mouse.get_pos()
					for button in self.buttons:
						if(button.button_rect.collidepoint(mouse_pos)):
							self.back_to_main()
							break
			
			if(not self.Draw):
				for i in range(0, self.size_maze[1]):
					self.POSX = self.sizes[self.size_maze]["POSX"]
					for j in range(0, self.size_maze[0]):
						x = self.maze_matrix[i][j].get_borders()
						if(x['TOP']):
							pygame.draw.line(self.window, (0,0,0), (self.POSX, self.POSY), (self.POSX + self.pixelSize, self.POSY), 1)
						if(x['BOTTOM']):
							pygame.draw.line(self.window, (0,0,0), (self.POSX, self.POSY + self.pixelSize), (self.POSX + self.pixelSize, self.POSY + self.pixelSize), 1)
						if(x['LEFT']):
							pygame.draw.line(self.window, (0,0,0), (self.POSX, self.POSY), (self.POSX, self.POSY + self.pixelSize), 1)
						if(x['RIGHT']):
							pygame.draw.line(self.window, (0,0,0), (self.POSX + self.pixelSize, self.POSY), (self.POSX + self.pixelSize, self.POSY + self.pixelSize), 1)
						self.POSX += self.pixelSize
					self.POSY += self.pixelSize
				self.POSX = self.sizes[self.size_maze]["POSX"]
				self.POSY = self.sizes[self.size_maze]["POSY"]
			
			self.Draw = True
			self.Clock.tick(5)
			pygame.display.flip()
			pygame.display.update()

	def back_to_main(self):
		time.sleep(0.5)
		self.window.fill(self.COLORS['WHITE'])
		main.Main(1200,600)

	def maze_borders(self):
		aux_maze = []
		for i in range(0, self.size_maze[1]):
			aux_maze.append([])
			for j in range(0, self.size_maze[0]):
				aux_maze[i].append(self.maze_matrix[i][j].get_borders())
		return aux_maze

	def create_simple_maze(self):
		RED   = "\033[1;31m"  
		BLUE  = "\033[1;34m"
		CYAN  = "\033[1;36m"
		GREEN = "\033[0;32m"
		RESET = "\033[0;0m"
		BOLD    = "\033[;1m"
		REVERSE = "\033[;7m"

		width = self.size_maze[1] * 3
		height = self.size_maze[0] * 3
		aux_maze = []

		for i in range(0, width):
			aux_maze.append([])
			for j in range(0, height):
				aux_maze[i].append(0)

		for i in range(1, width, 3):
			for j in range(1, height, 3):
				aux_maze[i][j] = 1

		contX = contY = 0

		for i in range(1, width, 3):
			for j in range(1, height, 3):
				if(not self.simple_maze[contX][contY]['TOP']):
					aux_maze[i-1][j] = 1
				if(not self.simple_maze[contX][contY]['LEFT']):
					aux_maze[i][j-1] = 1
				if(not self.simple_maze[contX][contY]['RIGHT']):
					aux_maze[i][j+1] = 1
				if(not self.simple_maze[contX][contY]['BOTTOM']):
					aux_maze[i+1][j] = 1
				contY += 1
			if(contY >= 5):
				contY = 0
			contX += 1

		for line in aux_maze:
			for pixel in line:
				if(not pixel):
					print(RED + '0 ' + RESET, end='')
				else:
					print('1 ' + RESET, end='')
			print('' + RESET)
		print('\n\n\n\n')
		return aux_maze

if __name__ == '__main__' : RenderMaze()