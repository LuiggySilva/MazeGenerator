import pygame
from maze import MazeCreate, MazeSolver, MazeRender

class Maze():
    def __init__(self, maze_size, window_width, window_heigth):
        self.maze = MazeCreate.MazeCreate(maze_size, window_width, window_heigth)
        self.solve = MazeSolver.MazeSolver(self.maze.get_screem_maze(), self.maze.get_screem_maze_size(), self.maze.get_screem_maze_start_end(), self.maze.get_terminal_maze(), self.maze.get_terminal_maze_size(), self.maze.get_terminal_maze_start_end())
        self.render = MazeRender.MazeRender(self.maze.get_screem_maze(), self.maze.get_terminal_maze(), maze_size, self.maze.get_sizes(), self.solve.get_screem_maze_solve(), self.solve.get_terminal_maze_solve())
        
    def draw_screem_maze(self, colors, window):
        start_pos, end_pos = self.maze.get_terminal_maze_start_end()
        self.render.draw_screem_maze(start_pos, end_pos, colors, window) 
    
    def draw_screem_maze_solve(self, colors, window):
        start_pos, end_pos = self.maze.get_terminal_maze_start_end()
        self.render.draw_screem_maze_solve(start_pos, end_pos, colors, window)

    def draw_terminal_maze(self):
        start_pos, end_pos = self.maze.get_terminal_maze_start_end()
        self.render.draw_terminal_maze(start=start_pos, end=end_pos)
    
    def draw_terminal_maze_solve(self):
        start_pos, end_pos = self.maze.get_terminal_maze_start_end()
        self.render.draw_terminal_maze(show_solve=True, start=start_pos, end=end_pos)

if __name__ == "__main__" : print('Maze')