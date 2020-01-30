import random
from random import shuffle
from functools import partial

class MazeSolver():
    def __init__(self, screem_maze, screem_maze_size, screem_maze_start_end, terminal_maze, terminal_maze_size, terminal_maze_start_end):
        self.terminal_maze = terminal_maze
        self.screem_maze_solve = self.solve_maze(terminal_maze_start_end, 'SCREEM', terminal_maze_start_end[0])
        self.terminal_maze_solve = self.solve_maze(terminal_maze_start_end, 'TERMINAL', terminal_maze_start_end[0])
        
    def get_screem_maze_solve(self):
        return self.screem_maze_solve
    
    def get_terminal_maze_solve(self):
        return self.terminal_maze_solve
    
    # Solve algorithms
    
    def exisits_left_wall(self, current_position, current_direction, maze):
        if(current_direction == 'N'):
            if(maze[current_position[0]][current_position[1]-1] == 0):
                return True 
        elif(current_direction == 'W'):
            if(maze[current_position[0]+1][current_position[1]] == 0):
                return True 
        elif(current_direction == 'E'):
            if(maze[current_position[0]-1][current_position[1]] == 0):
                return True  
        elif(current_direction == 'S'):
            if(maze[current_position[0]][current_position[1]+1] == 0):
                return True  
        return False

    def front_cell_is_free(self, current_position, current_direction, maze):
        if(current_direction == 'N'):
            return maze[current_position[0]-1][current_position[1]] == 1
        elif(current_direction == 'W'):
            return maze[current_position[0]][current_position[1]-1] == 1
        elif(current_direction == 'E'):
            return maze[current_position[0]][current_position[1]+1] == 1
        elif(current_direction == 'S'):
            return maze[current_position[0]+1][current_position[1]] == 1
        else:
            return False
    
    def rotate_to_left(self, current_direction):
        if(current_direction == 'N'):
            return 'W'
        elif(current_direction == 'W'):
            return 'S'
        elif(current_direction == 'E'):
            return 'N'
        elif(current_direction == 'S'):
            return 'E'
        else:
            return current_direction

    def rotate_to_right(self, current_direction):
        if(current_direction == 'N'):
            return 'E'
        elif(current_direction == 'W'):
            return 'N'
        elif(current_direction == 'E'):
            return 'S'
        elif(current_direction == 'S'):
            return 'W'
        else:
            return current_direction
    
    def go_to_front_cell(self, current_position, current_direction, pos_increment):
        if(current_direction == 'N'):
            return (current_position[0]-pos_increment, current_position[1])
        elif(current_direction == 'W'):
            return (current_position[0], current_position[1]-pos_increment)
        elif(current_direction == 'E'):
            return (current_position[0], current_position[1]+pos_increment)
        elif(current_direction == 'S'):
            return (current_position[0]+pos_increment, current_position[1])
        else:
            return current_position

    def get_direction(self, start_position, maze):
        # Se for igual a zero tem uma parede
        top_neighbor = maze[start_position[0]-1][start_position[1]] == 1
        left_neighbor = maze[start_position[0]][start_position[1]-1] == 1
        right_neighbor = maze[start_position[0]][start_position[1]+1] == 1
        bottom_neighbor = maze[start_position[0]+1][start_position[1]] == 1
        directions = {'N':top_neighbor,'W':left_neighbor,'E':right_neighbor,'S':bottom_neighbor}
        # Se tiver uma parede eu removo
        if(directions['N']):
            del directions['N']
        if(directions['W']):
            del directions['W']
        if(directions['E']):
            del directions['E']
        if(directions['S']):
            del directions['S']
        # Pego uma direção aleatoria das que sobraram
        keys = list(directions.keys())
        shuffle(keys)
        return keys[0]

    def add_entry_index(self, _list, elem, frist_index, second_index):
        aux = _list[0:frist_index+1]
        aux.append(elem)
        for elem in _list[second_index:len(_list)-1]:
            aux.append(elem)
        return aux

    def clear_solved_maze(self, solve_maze, pos_increment, maze):
        # Remover caminhos duplicados
        return solve_maze

    def append_fst(self, elem, solve_list):
        aux = [elem]
        for e in solve_list:
            aux.append(e)
        return aux

    def solve_maze(self, start_end_position, maze_type, current_position):
        start_pos, end_pos = start_end_position
        maze = self.terminal_maze
        solved_maze_path = [start_pos]
        current_direction = self.get_direction(start_pos, maze)
        
        pos_increment = None
        if(maze_type == 'TERMINAL'):
            pos_increment = 1
        else:
            pos_increment = 3
        
        while(not current_position == end_pos):
            if(self.exisits_left_wall(current_position, current_direction, maze)):
                if(self.front_cell_is_free(current_position, current_direction, maze)):
                    current_position = self.go_to_front_cell(current_position, current_direction, pos_increment)
                    solved_maze_path.append(current_position)
                else:
                    current_direction = self.rotate_to_right(current_direction)
            else:
                current_direction = self.rotate_to_left(current_direction)
                current_position = self.go_to_front_cell(current_position, current_direction, pos_increment)
                solved_maze_path.append(current_position)
        
        maze_solve = self.clear_solved_maze(solved_maze_path, pos_increment, maze)
        if(not start_pos in maze_solve):
            maze_solve = self.append_fst(start_pos, maze_solve)
        if(not end_pos in maze_solve):
            maze_solve.append(end_pos)
        
        return maze_solve

if __name__ == "__main__" : print('MazeSolver')