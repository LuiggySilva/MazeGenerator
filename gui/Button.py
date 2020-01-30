import pygame, time
from gui import Text

class Button():
    def __init__(self, position, size, text, color, font_size):
        self.position = position
        self.size = size
        self.text = text
        self.color = color
        self.font_size = font_size
        self.pygame_text = Text.Text((self.position[0] + self.size // 2, self.position[1] + self.size // 8), self.text, self.font_size, (255,255,255))
        self.clicked = False
        self.bnt_rect = pygame.Rect(self.position[0], self.position[1], self.size, self.size//2)
    
    def get_rect(self):
        return self.bnt_rect
    
    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.position[0], self.position[1], self.size, self.size//2))
        pygame.draw.rect(window, (0,0,0), (self.position[0], self.position[1], self.size, self.size//2), 4)
        self.pygame_text.draw(window)

    def click_here(self): 
        if (not self.is_clicked()):
            self.clicked = True
            self.pygame_text = Text.Text((self.position[0] + self.size // 2, self.position[1] + self.size // 8), self.text, self.font_size, (0,0,0))	
        else:
            self.clicked = False
            self.pygame_text = Text.Text((self.position[0] + self.size // 2, self.position[1] + self.size // 8), self.text, self.font_size, (255,255,255))
        pygame.display.update()

    def is_clicked(self):
        return self.clicked
    
    def get_text(self):
        return self.text