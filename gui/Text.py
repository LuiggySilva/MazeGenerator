import pygame

class Text():
    def __init__(self, position, text, font_size, color):
        self.pygame_font = pygame.font.SysFont("comicsansms", font_size)
        self.text = text
        self.color = color
        self.font_size = font_size
        self.position = position
        self.pygame_text = self.pygame_font.render(self.text, True, self.color)
        self.rect = self.pygame_text.get_rect()

    def get_rect(self):
        return self.rect

    def draw(self, screem):
        screem.blit(self.pygame_text, (self.position[0] - self.rect[2] // 2, self.position[1]))

if __name__ == "__main__": print('Text')