import pygame, random
from random import choice
from maze import MazeWall

class MazeCreate():
    def __init__(self, maze_size, window_width, window_height):
        self.SCREEM_WIDTH, self.SCREEM_HEIGHT = window_width - 12, window_height - 52
        
        self.screem_maze = None
        self.screem_maze_size = maze_size
        self.screem_maze_start, self.screem_maze_end = (0, 0), (self.screem_maze_size[0] - 1, self.screem_maze_size[1] - 1) # Deixar isso aleatorio depois
        #print(str(self.screem_maze_start) + ' --- ' + str(self.screem_maze_end))
        
        self.terminal_maze = None
        self.terminal_maze_size = (maze_size[0] * 3, maze_size[1] * 3)
        self.terminal_maze_start, self.terminal_maze_end = (1, 1), (self.terminal_maze_size[0] - 2, self.terminal_maze_size[1] - 2) # Deixar isso aleatorio depois
        #print(str(self.terminal_maze_start) + ' --- ' + str(self.terminal_maze_end))
        
        # Setting the size and position of the maze cells depending on the size of the matrix
        self.sizes = {
            (5,5):   {"pos_x":self.SCREEM_WIDTH//2 - 252,"pos_y":86, "pixel_size":100},
            (5,10):  {"pos_x":self.SCREEM_WIDTH//2 - 504,"pos_y":86, "pixel_size":100},
            (10,10): {"pos_x":self.SCREEM_WIDTH//2 - 254,"pos_y":86, "pixel_size":50},
            (10,20): {"pos_x":self.SCREEM_WIDTH//2 - 504,"pos_y":86, "pixel_size":50},
            (20,20): {"pos_x":self.SCREEM_WIDTH//2 - 254,"pos_y":86, "pixel_size":25}
        }
        
        # Size and start x and y frist cell position in screem 
        self.pos_x = self.sizes[self.screem_maze_size]["pos_x"]
        self.pos_y = self.sizes[self.screem_maze_size]["pos_y"]
        self.pixel_size = self.sizes[self.screem_maze_size]["pixel_size"]
        
        self.make_screem_maze()
        self.screem_maze_borders = self.get_screem_maze_borders()
        self.make_terminal_maze()
    
    def make_screem_maze(self):
        self.screem_maze = []
        for i in range(0, self.screem_maze_size[0]):
            self.screem_maze.append([])
            for j in range(0, self.screem_maze_size[1]):
                self.screem_maze[i].append(MazeWall.MazeWall(-1,-1, (i, j), self.pixel_size))
        self.setting_screem_maze_cell_positions()
        self.create_maze()
    
    def get_screem_maze_borders(self):
        aux_maze = []
        for i in range(0, self.screem_maze_size[0]):
            aux_maze.append([])
            for j in range(0, self.screem_maze_size[1]):
                aux_maze[i].append(self.screem_maze[i][j].get_borders())
        return aux_maze

    def setting_screem_maze_cell_positions(self):
        for i in range(0, self.screem_maze_size[0]):
            for j in range(0, self.screem_maze_size[1]):
                self.screem_maze[i][j].set_position(self.pos_x, self.pos_y)
                self.pos_x = self.pos_x + (self.pixel_size)
            self.pos_y = self.pos_y + (self.pixel_size)
            self.pos_x = self.sizes[self.screem_maze_size]["pos_x"]

        self.pos_x = self.sizes[self.screem_maze_size]["pos_x"]
        self.pos_y = self.sizes[self.screem_maze_size]["pos_y"]
    
    def make_terminal_maze(self):
        width = self.terminal_maze_size[0]
        height = self.terminal_maze_size[1]
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
                self.screem_maze[contX][contY].set_index((i,j))
                if(not self.screem_maze_borders[contX][contY]['TOP']):
                    aux_maze[i-1][j] = 1
                if(not self.screem_maze_borders[contX][contY]['LEFT']):
                    aux_maze[i][j-1] = 1
                if(not self.screem_maze_borders[contX][contY]['RIGHT']):
                    aux_maze[i][j+1] = 1
                if(not self.screem_maze_borders[contX][contY]['BOTTOM']):
                    aux_maze[i+1][j] = 1
                contY += 1
            if(contY >= self.screem_maze_size[1]):
                contY = 0
            contX += 1
        
        self.terminal_maze = aux_maze 
    
    def get_screem_maze(self):
        return self.screem_maze

    def get_terminal_maze(self):
        return self.terminal_maze

    def get_screem_maze_size(self):
        return self.screem_maze_size

    def get_terminal_maze_size(self):
        return self.terminal_maze_size
    
    def get_sizes(self):
        return self.sizes
    
    def find_valid_neighbours(self, cell):
        delta = [('TOP', (-1,0)), ('BOTTOM', (1,0)), ('RIGHT', (0,1)), ('LEFT', (0,-1))]
        neighbours = []
        nx, ny = self.screem_maze_size
        for direction, (dx,dy) in delta:
            x2, y2 = cell.get_index()
            x2, y2 = x2 + dx, y2 + dy
            if (0 <= x2 < nx) and (0 <= y2 < ny):
                neighbour = self.screem_maze[x2][y2]
                if neighbour.all_borders():
                    neighbours.append((direction, neighbour))
        return neighbours

    def create_maze(self):
        width, height = self.screem_maze_size
        total_cells = width * height
        cell_stack = []
        ix, iy = random.randint(0, width-1), random.randint(0, height-1)
        current_cell = self.screem_maze[ix][iy]
        visited_cells = 1

        while visited_cells < total_cells:
            neighbours = self.find_valid_neighbours(current_cell)
            if neighbours == []:
                current_cell = cell_stack.pop()
                continue
            direction, next_cell = random.choice(neighbours)
            current_cell.remove_border(direction, next_cell)
            cell_stack.append(current_cell)
            current_cell = next_cell
            visited_cells += 1
    
    def get_screem_maze_start_end(self):
        return self.screem_maze_start, self.screem_maze_end
    
    def get_terminal_maze_start_end(self):
        return self.terminal_maze_start, self.terminal_maze_end

if __name__ == "__main__" : print('MazeCreate')