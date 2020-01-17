import time
import pygame
import sys
import random
from random import choice
from Maze import RenderMaze, MazeWall
from UI import Text, Button

class CreateMaze():
	def __init__(self, size_maze=(10,5), COLORS=['BLACK'], Clock=None, Window=None):
		self.PYGAME_WIDTH = 1188
		self.PYGAME_HEIGHT = 548
		self.COLORS = COLORS
		self.window = Window
		self.Clock = Clock
		self.size_maze = size_maze
		self.maze_matrix = self.make_matrix_maze()

		# Setting the size and position of the elements depending on the size of the matrix
		self.sizes = {
		    (5,5):   {"POSX":self.PYGAME_WIDTH//2 - 252,"POSY":86, "pixelSize":100},
		    (10,5):  {"POSX":self.PYGAME_WIDTH//2 - 504,"POSY":86, "pixelSize":100},
		    (10,10): {"POSX":self.PYGAME_WIDTH//2 - 254,"POSY":86, "pixelSize":50},
		    (20,10): {"POSX":self.PYGAME_WIDTH//2 - 504,"POSY":86, "pixelSize":50},
		    (20,20): {"POSX":self.PYGAME_WIDTH//2 - 254,"POSY":70, "pixelSize":25}
		}
		self.POSX = self.sizes[self.size_maze]["POSX"]
		self.POSY = self.sizes[self.size_maze]["POSY"]
		self.pixelSize = self.sizes[self.size_maze]["pixelSize"]
		self.pixelPOSIncrement = 1

		# Creating matrix with rects
		self.matrix_maze = []
		for i in range(0, self.size_maze[1]):
			self.matrix_maze.append([])
			for j in range(0, self.size_maze[0]):
				self.matrix_maze[i].append(MazeWall.MazeWall((self.POSX,self.POSY), self.pixelSize))
				self.POSX = self.POSX + (self.pixelSize + self.pixelPOSIncrement)
			self.POSY = self.POSY + (self.pixelSize + self.pixelPOSIncrement)
			self.POSX = self.sizes[self.size_maze]["POSX"]

		self.POSX = self.sizes[self.size_maze]["POSX"]
		self.POSY = self.sizes[self.size_maze]["POSY"]
		self.make_maze()
		self.render = RenderMaze.RenderMaze(self.window, self.sizes, self.PYGAME_WIDTH, self.PYGAME_HEIGHT, self.POSX, self.POSY, self.pixelSize, self.maze_matrix, self.size_maze, self.pixelPOSIncrement, self.COLORS, self.Clock)

	def get_matrix_maze(self):
		return self.maze_matrix

	def make_matrix_maze(self):
		maze = []
		height, width  = self.size_maze
		for i in range(0, width):
			maze.append([])
			for j in range(0, height):
				maze[i].append(MazeWall.MazeWall(i,j))
		return maze

	def find_valid_neighbours(self, cell):
	    delta = [('TOP', (-1,0)), ('BOTTOM', (1,0)), ('RIGHT', (0,1)), ('LEFT', (0,-1))]
	    neighbours = []
	    ny, nx = self.size_maze
	    for direction, (dx,dy) in delta:
	        x2, y2 = cell.get_position()
	        x2, y2 = x2 + dx, y2 + dy
	        if (0 <= x2 < nx) and (0 <= y2 < ny):
	            neighbour = self.maze_matrix[x2][y2]
	            if neighbour.all_borders():
	                neighbours.append((direction, neighbour))
	    return neighbours

	def make_maze(self):
		height, width = self.size_maze
		n = width * height
		cell_stack = []
		ix, iy = random.randint(0, width-1), random.randint(0, height-1)
		current_cell = self.maze_matrix[ix][iy]
		nv = 1

		self.window.fill(self.COLORS['WHITE'])
		while nv < n:
			neighbours = self.find_valid_neighbours(current_cell)
			if neighbours == []:
				current_cell = cell_stack.pop()
				continue
			direction, next_cell = random.choice(neighbours)
			current_cell.remove_border(direction, next_cell)
			cell_stack.append(current_cell)
			current_cell = next_cell
			nv += 1

if __name__ == '__main__' : CreateMaze()