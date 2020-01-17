import time
import pygame
import sys
import random
from random import choice
from UI import Button, Text

class Menu():
	def __init__(self, PYGAME_HEIGHT=600, PYGAME_WIDTH=1200, WINDOW_TITLE='Maze', COLORS=['BLACK'], Clock=None, Window=None):
		
		Window.fill(COLORS["WHITE"])
		pygame.display.set_caption(WINDOW_TITLE)

		# Titulo do app
		self.title = Text.Text(pos=(PYGAME_WIDTH//2,PYGAME_HEIGHT//16), pure_text=WINDOW_TITLE, font_size=100, color=COLORS["BLACK"], window=Window)
		# Underline do titulo
		pygame.draw.line(Window, (0,0,0), (PYGAME_WIDTH//2 - 377, PYGAME_HEIGHT//3 - 20), (980,PYGAME_HEIGHT//3 - 20), 5)
		# Texto indicando a escolha do tamanho do labirinto
		self.sub_title = Text.Text(pos=(PYGAME_WIDTH//2,PYGAME_HEIGHT//3), pure_text='Choose size of maze:', font_size=50, color=COLORS["BLACK"], window=Window)

		# Variaveis base para centralizar os botoes lado a lado na tela
		self.bntX, self.bntY = PYGAME_WIDTH//2 - 75, PYGAME_HEIGHT//2
		# Opções do tamanho do labirinto
		self.button1 = Button.Button(pos=(self.bntX - 400, self.bntY), text='05x05', window=Window, color=COLORS["GRAY"])
		self.button2 = Button.Button(pos=(self.bntX - 200, self.bntY), text='10x05', window=Window, color=COLORS["GRAY"])
		self.button3 = Button.Button(pos=(self.bntX, self.bntY),       text='10x10', window=Window, color=COLORS["GRAY"])
		self.button4 = Button.Button(pos=(self.bntX + 200, self.bntY), text='20x10', window=Window, color=COLORS["GRAY"])
		self.button5 = Button.Button(pos=(self.bntX + 400, self.bntY), text='20x20', window=Window, color=COLORS["GRAY"])

		# Lista com os botões
		self.buttons = [self.button1, self.button2, self.button3, self.button4, self.button5]
		self.mazeSize = None
		self.selectMazeSize = False

		# Loop até o tamanho do labirinto ser escolhido
		while(not self.selectMazeSize):
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
					mouse_pos = pygame.mouse.get_pos()
					for button in self.buttons:
						if(button.button_rect.collidepoint(mouse_pos)):
							button.Click()
							self.mazeSize = button.text
							self.selectMazeSize = True

			Clock.tick(30)
			pygame.display.flip()
			pygame.display.update()

		# Texto temporario
		time.sleep(0.5)

	def getMazeSize(self):
		return self.mazeSize

if __name__ == '__main__' : Menu()