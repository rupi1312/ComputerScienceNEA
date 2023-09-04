
#import modules
import pygame #we will be using pygame in order to present the maze
from random import choice

#Global Constants
RESOLUTION = WIDTH, HEIGHT = 1202, 902
TILE = 100
columns = WIDTH // TILE 
rows = HEIGHT // TILE

#Initialise pygame variables
pygame.init()
sc = pygame.display.set_mode(RESOLUTION)
clock = pygame.time.Clock()

#CELL
class Cell: # we will use a class for Cell in order to interact with indivdual elements of the maze 
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.walls = {'north': True, 'east': True, 'south': True, 'west': True}
        self.visited = False
    
    def draw_current_cell(self):
        x = self.x * TILE
        y = self.y * TILE
        pygame.draw.rect(sc, pygame.Color("black"), (x + 2, y + 2, TILE - 2, TILE - 2))

    def draw(self):
        x = self.x * TILE
        y = self.y * TILE
        
        if self.visited:
            pygame.draw.rect(sc, pygame.Color('grey'), (x, y, TILE, TILE))

        if self.walls['north']:
            pygame.draw.line(sc, pygame.Color('black'), (x, y), (x + TILE, y), 2)
        
        if self.walls['east']:
            pygame.draw.line(sc, pygame.Color('black'), (x + TILE, y), (x + TILE, y + TILE), 2)

        if self.walls['south']:
            pygame.draw.line(sc, pygame.Color('black'), (x + TILE, y + TILE), (x, y + TILE), 2)

        if self.walls['west']:
            pygame.draw.line(sc, pygame.Color('black'), (x, y + TILE), (x, y), 2)
    
    def check_cell(self, x, y):
        find_index = lambda x,y: x + y * columns # describe the LAMBDA FUNCTION AND WHY I USED IT!!!
        if x < 0 or x > columns - 1 or y < 0 or y > rows -1:
            return False
        return grid_cells[find_index(x,y)]
   
    def check_neighbours(self):
        neighbours = []
        north = self.check_cell(self.x, self.y - 1)
        east = self.check_cell(self.x + 1, self.y)
        south = self.check_cell(self.x, self.y + 1)
        west = self.check_cell(self.x - 1, self.y)

        if north and not north.visited:
            neighbours.append(north)
        if east and not east.visited:
            neighbours.append(east)
        if south and not south.visited:
            neighbours.append(south)
        if west and not west.visited:
            neighbours.append(west)
        return choice(neighbours) if neighbours else False
     


def remove_walls(current, next):
        dx = current.x - next.x
        if dx == 1:
            current.walls['west'] = False
            next.walls['east'] = False
        elif dx == -1:
            current.walls['east'] = False
            next.walls['west'] = False

        dy = current.y - next.y
        if dy == 1:
            current.walls['north'] = False
            next.walls['south'] = False
        elif dy == -1:
            current.walls['south'] = False
            next.walls['north'] = False    


grid_cells = [Cell(column, row) for row in range(rows) for column in range (columns)]
current_cell = grid_cells[0]
stack = []



while True:
    sc.fill(pygame.Color('gray'))

    for event in pygame.event.get():
        # print(event) # this command will be used to debug inputs from user
        if event.type == pygame.QUIT:
            exit()

    [cell.draw() for cell in grid_cells]
    current_cell.visited = True
    current_cell.draw_current_cell()

    next_cell = current_cell.check_neighbours() 

    if next_cell:
        next_cell.visited = True    
        stack.append(current_cell)
        remove_walls(current_cell, next_cell)
        current_cell = next_cell
    elif stack:
        current_cell = stack.pop()

    pygame.display.flip()
    clock.tick(30) 
    

# Maze generation using DPS