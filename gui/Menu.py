import pygame
from gui import Button, Text
from maze import Maze

class Menu():
    def __init__(self, window_width, window_height, title):
        self.SCREEM_WIDTH, self.SCREEM_HEIGHT = window_width, window_height
        self.COLORS = {
            "BLACK":(0,0,0),
            "GRAY":(105,105,105),
            "WHITE":(255,255,255),
            "RED":(255,0,0),
            "BLUE":(0,0,255),
            "GREEM":(0,255,0),
            "YELLOW":(255,255,0),
            "BROWN":(100, 50, 0),
            "ORANGE":(255, 150, 50),
            "PINK":(255, 50, 150)
        }
        # Titulo
        self.title = Text.Text((self.SCREEM_WIDTH//2, self.SCREEM_HEIGHT//16), title, 80, self.COLORS['BLACK'])
        # Texto indicando a escolha do tamanho do labirinto
        self.choose_maze_size_text = Text.Text((self.SCREEM_WIDTH // 2,self.SCREEM_HEIGHT // 3), 'Choose size of maze:', 50, self.COLORS['BLACK'])
        # Variaveis base para centralizar os botoes lado a lado na tela
        self.bntX, self.bntY = self.SCREEM_WIDTH//2 - 75, self.SCREEM_HEIGHT//2
        self.bnt_size, self.bnt_color, self.bnt_font_size = 150, self.COLORS["GRAY"], 25
        # Opções do tamanho do labirinto
        self.bnt_1 =Button.Button((self.bntX - 200, self.bntY), self.bnt_size, '10x05', self.bnt_color, self.bnt_font_size)
        self.bnt_2 =Button.Button((self.bntX - 400, self.bntY), self.bnt_size, '05x05', self.bnt_color, self.bnt_font_size)
        self.bnt_3 =Button.Button((self.bntX, self.bntY)      , self.bnt_size, '10x10', self.bnt_color, self.bnt_font_size)
        self.bnt_4 =Button.Button((self.bntX + 200, self.bntY), self.bnt_size, '20x10', self.bnt_color, self.bnt_font_size)
        self.bnt_5 =Button.Button((self.bntX + 400, self.bntY), self.bnt_size, '20x20', self.bnt_color, self.bnt_font_size)
        self.bnt_quit =Button.Button((1020, 500), self.bnt_size, 'QUIT', self.bnt_color, self.bnt_font_size)
        # Listas com os botões e textos do menu principal
        self.main_menu_buttons = [self.bnt_quit,self.bnt_1,self.bnt_2,self.bnt_3,self.bnt_4,self.bnt_5]
        self.main_menu_texts = [self.choose_maze_size_text, self.title]
        # Menu do labirindo
        self.bnt_back = Button.Button((1085, 10), 100, 'BACK', self.bnt_color, self.bnt_font_size)
        self.bnt_new_maze = Button.Button((10, 10), 100, 'NEW', self.bnt_color, self.bnt_font_size)
        self.bnt_solve_maze = Button.Button((130, 10), 100, 'SOLVE', self.bnt_color, self.bnt_font_size)
        self.start_text = Text.Text((1040, 9), '● start', 20, self.COLORS['BLUE'])
        self.end_text = Text.Text((1033, 30), '● end', 20, self.COLORS['RED'])
        # Listas com botoes e textos do menu no labirinto
        self.maze_buttons = [self.bnt_back, self.bnt_new_maze, self.bnt_solve_maze]
        self.maze_texts = [self.start_text, self.end_text]

    def get_colors(self):
        return self.COLORS

    def draw_main_menu(self, window):
        window.fill(self.COLORS['WHITE'])
        pygame.draw.line(window, self.COLORS['BLACK'], (250, 155), (950, 155), 5)
        for bnt in self.main_menu_buttons:
            bnt.draw(window)
        for text in self.main_menu_texts:
            text.draw(window)
        return self.main_menu_buttons
    
    def draw_maze_menu(self, maze_size, window):
        window.fill(self.COLORS['WHITE'])
        self.maze_title = Text.Text((self.SCREEM_WIDTH // 2, 10), f'Maze ({maze_size[1]}x{maze_size[0]})', 40, self.COLORS['BLACK'])
        self.maze_title.draw(window)
        pygame.draw.line(window, self.COLORS['BLACK'], (0, 75), (1200, 75), 5)
        for bnt in self.maze_buttons:
            bnt.draw(window)
        for text in self.maze_texts:
            text.draw(window)
        return self.maze_buttons

if __name__ == "__main__": print('Menu')