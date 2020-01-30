import pygame

class MazeRender():
    def __init__(self, screem_maze, terminal_maze, screem_maze_size, sizes, screem_maze_solve, terminal_maze_solve):
        self.screem_maze = screem_maze
        self.terminal_maze = terminal_maze
        self.screem_maze_size = screem_maze_size
        self.sizes = sizes
        self.screem_maze_solve = screem_maze_solve
        self.terminal_maze_solve = terminal_maze_solve
    
    def draw_screem_maze(self, start, end, colors, window):
        for walls in self.screem_maze:
            for wall in walls:
                wall.draw_wall(window)	
                if(wall.get_index() == start):
                    x, y = wall.get_position()
                    pixel_size = self.sizes[self.screem_maze_size]['pixel_size']
                    pygame.draw.circle(window, colors['BLUE'], (x + pixel_size // 2, y + pixel_size // 2), 7)
                if(wall.get_index() == end):
                    x, y = wall.get_position()
                    pixel_size = self.sizes[self.screem_maze_size]['pixel_size']
                    pygame.draw.circle(window, colors['RED'], (x + pixel_size // 2, y + pixel_size // 2), 7)

    def wall_list(self):
        wall_list = []
        for walls in self.screem_maze:
            for wall in walls:
                wall_list.append(wall)
        return wall_list

    def verifiy_direction_path(self, frist_wall_position, second_wall_position, maze):
        if  (second_wall_position[0] == frist_wall_position[0] and second_wall_position[1] >= frist_wall_position[1]): # RIGHT
            return 'RIGHT'
        elif(second_wall_position[0] == frist_wall_position[0] and second_wall_position[1] <= frist_wall_position[1]): # LEFT
            return 'LEFT'
        elif(second_wall_position[0] <= frist_wall_position[0] and second_wall_position[1] == frist_wall_position[1]): # TOP
            return 'TOP'
        elif(second_wall_position[0] >= frist_wall_position[0] and second_wall_position[1] == frist_wall_position[1]): # BOTTOM
            return 'BOTTOM'
        else:
            print(f'>>> verify-direction-error >>> fst:{frist_wall_position} - snd:{second_wall_position}')
            print(maze)
            print('\n')

    def draw_screem_maze_solve(self, start, end, colors, window):
        pixel_size = self.sizes[self.screem_maze_size]['pixel_size']
        for i in range(1, len(self.screem_maze_solve)):
            frist = self.screem_maze_solve[i-1]
            second = self.screem_maze_solve[i]
            frist_wall = None
            second_wall = None
            for wall in self.wall_list():
                wall_pos = wall.get_index()
                if(wall_pos == frist):
                    frist_wall = wall
                elif(wall_pos == second):
                    second_wall = wall
                else:
                    continue
            direction = self.verifiy_direction_path(frist, second, self.screem_maze_solve)
            if(frist_wall is not None):
                frist_wall.draw_path(direction, window)
            if(frist_wall is not None and frist_wall.get_index() == start):
                x, y = frist_wall.get_position()
                pygame.draw.circle(window, colors['BLUE'], (x + pixel_size//2, y + pixel_size//2), 7)
            if(second_wall is not None and second_wall.get_index() == end):
                x, y = second_wall.get_position()
                pygame.draw.circle(window, colors['RED'], (x + pixel_size//2, y + pixel_size//2), 7) 
    
    def draw_terminal_maze(self, show_solve=False, start=None, end=None):
        RED   = "\033[1;31m"  
        BLUE  = "\033[1;34m"
        GREEN = "\033[0;32m"
        RESET = "\033[0;0m"
        REVERSE = "\033[;7m"

        if (not show_solve): 
            print(f'Maze ({self.screem_maze_size[1]}x{self.screem_maze_size[0]})\n')
        else:
            print(f'Maze ({self.screem_maze_size[1]}x{self.screem_maze_size[0]}) - Solve\n')
        
        for i in range(0, len(self.terminal_maze)):
            for j in range(0, len(self.terminal_maze[i])):
                pixel = self.terminal_maze[i][j]
                if((i,j) == start):
                    print(BLUE + '1 ' + RESET, end='')
                elif((i,j) == end):
                    print(GREEN + '1 ' + RESET, end='')
                elif((i,j) in self.terminal_maze_solve and show_solve):
                    print(REVERSE + '1 ' + RESET, end='')
                else:
                    if(not pixel):
                        print(RED + '0 ' + RESET, end='')
                    else:
                        print('1 ' + RESET, end='')
            print('' + RESET)
        print('\n')

if __name__ == "__main__" : print('MazeRender')