import pygame

class MazeWall():
    def __init__(self, posX, posY, index, size):
        self._posX = posX
        self._posY = posY
        self._index = index
        self._size = size
        self._borders = {'TOP':True,'LEFT':True,'RIGHT':True,'BOTTOM':True}
 
    def get_index(self):
        return self._index

    def set_index(self, new_index):
        self._index = new_index

    def get_position(self):
        return self._posX, self._posY

    def get_size(self):
        return self._size

    def set_position(self, posX, posY):
        self._posX = posX
        self._posY = posY

    def get_borders(self):
        return self._borders

    def set_border(self, border):
        self._borders[border] = False

    def remove_border(self, border, another_wall):
        if(border in self._borders.keys() and border in another_wall.get_borders().keys()):
            self._borders[border] = False
            if(border == 'TOP'):
                another_wall.set_border('BOTTOM')
            elif(border == 'LEFT'):
                another_wall.set_border('RIGHT')
            elif(border == 'RIGHT'):
                another_wall.set_border('LEFT')
            elif(border == 'BOTTOM'):
                another_wall.set_border('TOP')

    def all_borders(self):
        return self._borders['TOP'] and self._borders['LEFT'] and self._borders['RIGHT'] and self._borders['BOTTOM']

    def draw_path(self, direction, window):
        if(direction == 'RIGHT'):
            pygame.draw.line(window, (0,255,0), (self._posX + self._size//2, self._posY + self._size//2), (self._posX + self._size + self._size//2, self._posY + self._size//2), 4)
        elif(direction == 'LEFT'):
            pygame.draw.line(window, (0,255,0), (self._posX + self._size//2, self._posY + self._size//2), (self._posX - self._size//2, self._posY + self._size//2), 4)
        elif(direction == 'TOP'):
            pygame.draw.line(window, (0,255,0), (self._posX + self._size//2, self._posY + self._size//2), (self._posX + self._size//2, self._posY - self._size//2), 4)
        elif(direction == 'BOTTOM'):
            pygame.draw.line(window, (0,255,0), (self._posX + self._size//2, self._posY + self._size//2), (self._posX + self._size//2, self._posY + self._size + self._size//2), 4)

    def draw_wall(self, window):
        if(self._borders['TOP']):
            pygame.draw.line(window, (0,0,0), (self._posX, self._posY), (self._posX + self._size, self._posY), 1)
        if(self._borders['BOTTOM']):
            pygame.draw.line(window, (0,0,0), (self._posX, self._posY + self._size), (self._posX + self._size, self._posY + self._size), 1)
        if(self._borders['LEFT']):
            pygame.draw.line(window, (0,0,0), (self._posX, self._posY), (self._posX, self._posY + self._size), 1)
        if(self._borders['RIGHT']):
            pygame.draw.line(window, (0,0,0), (self._posX + self._size, self._posY), (self._posX + self._size, self._posY + self._size), 1)
            
    def path_is_free(self, another_cell, direction):
        if(direction == 'N'):
            return not self.get_borders()['TOP'] and not another_cell.get_borders()['BOTTOM']
        elif(direction == 'W'):
            return not self.get_borders()['LEFT'] and not another_cell.get_borders()['RIGHT']
        elif(direction == 'E'):
            return not self.get_borders()['RIGHT'] and not another_cell.get_borders()['LEFT']
        elif(direction == 'S'):
            return not self.get_borders()['BOTTOM'] and not another_cell.get_borders()['TOP']
        else:
            print('ih rpz - mazewall - path_is_free')
            return False

    def to_string(self):
        string = ''
        string += '=*=' * 30
        string += f'\n > maze-cell-index : {self.get_index()}'
        string += f'\n > maze-cell-position : {self.get_position()}'
        string += f'\n > maze-cell-size : {self._size}'
        string += f'\n > maze-cell-borders : {self.get_borders()}'
        return string

if __name__ == '__main__' : print('MazeWall')