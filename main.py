import pygame, sys, time
from gui import Menu
from maze import Maze

class Main():
    def __init__(self, window_width, window_height):
        pygame.init()
        print('\nMazeGenerator\n')
        self.SCREEM_WIDTH, self.SCREEM_HEIGHT = window_width, window_height
        self.SCREEM_TITLE = 'Maze Generator'
        self.SCREEM_ICON = pygame.image.load('maze_icon.png')
        self.CLOCK = pygame.time.Clock()
        self.SCREEM = pygame.display.set_mode((self.SCREEM_WIDTH, self.SCREEM_HEIGHT))
        
        pygame.display.set_icon(self.SCREEM_ICON)
        pygame.display.set_caption(self.SCREEM_TITLE)
        
        self.menu = Menu.Menu(self.SCREEM_WIDTH, self.SCREEM_HEIGHT, self.SCREEM_TITLE)
        self.main_menu_buttons = self.menu.draw_main_menu(self.SCREEM)
        self.maze_buttons = None
        self.maze_size = None
        self.selected_maze_size = False
        self.back_to_menu = False
        
        self.colors = self.menu.get_colors()
        self.maze = None
        self.draw_maze = False
        self.draw_maze_solve = False
        
        while(True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            if(self.back_to_menu):
                self.menu.draw_main_menu(self.SCREEM)
                self.back_to_menu = False

            while (not self.selected_maze_size):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        mouse_pos = pygame.mouse.get_pos()
                        for button in self.main_menu_buttons:
                            if(button.get_rect().collidepoint(mouse_pos)) and button.get_text() == 'QUIT':
                                sys.exit()
                            if(button.get_rect().collidepoint(mouse_pos)):
                                button.click_here()
                                button.draw(self.SCREEM)
                                self.selected_maze_size = True
                                self.set_tuple_maze_size(button.get_text())         
                pygame.display.update()
            
            self.maze = Maze.Maze(self.maze_size, self.SCREEM_WIDTH, self.SCREEM_HEIGHT)
            self.maze_buttons = self.menu.draw_maze_menu(self.maze_size, self.SCREEM)
            
            while(not self.back_to_menu):
                if(not self.draw_maze and not self.draw_maze_solve):
                    self.maze.draw_screem_maze(self.colors, self.SCREEM)
                    self.maze.draw_terminal_maze()
                    self.draw_maze = True
                
                if(self.draw_maze_solve):
                    self.maze.draw_terminal_maze_solve()
                    self.maze.draw_screem_maze_solve(self.colors, self.SCREEM)
                    self.draw_maze_solve = False
                    self.draw_maze = True
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        mouse_pos = pygame.mouse.get_pos()
                        for button in self.maze_buttons:
                            if(button.get_rect().collidepoint(mouse_pos)) and button.get_text() == 'BACK':
                                self.back_to_menu = True
                                self.selected_maze_size = False
                                self.draw_maze = False
                                button.click_here()
                                button.draw(self.SCREEM)
                                time.sleep(0.5)
                            if(button.get_rect().collidepoint(mouse_pos) and button.get_text() == 'NEW'):
                                self.back_to_menu = True
                                self.draw_maze = False
                                button.click_here()
                                button.draw(self.SCREEM)
                            if(button.get_rect().collidepoint(mouse_pos) and button.get_text() == 'SOLVE'):
                                self.draw_maze_solve = True
                                self.draw_maze = False
                                button.click_here()
                                button.draw(self.SCREEM)
                pygame.display.update()
    
        pygame.display.update()
    
    def set_tuple_maze_size(self, maze_size):
        maze_size = maze_size.split('x')
        x = y = None
        if(int(maze_size[0]) <= int(maze_size[1])):
            x, y = int(maze_size[0]), int(maze_size[1])
        else:
            x, y = int(maze_size[1]), int(maze_size[0])
        self.maze_size = (x, y)
        
            
if __name__ == "__main__" : Main(1200, 600)