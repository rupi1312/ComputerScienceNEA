#import modules
import pygame #we will be using pygame in order to present the maze
from random import choice

#Global Constants
RESOLUTION = WIDTH, HEIGHT = 800, 600
TILE = 80
columns = WIDTH // TILE 
rows = HEIGHT // TILE

#Initialise pygame variables
pygame.init()
sc = pygame.display.set_mode(RESOLUTION)
pygame.display.set_caption("DPS")
clock = pygame.time.Clock()

pos = ""
font = pygame.font.SysFont("Arial", 5)
#txt = font.render(pos, True)

# "cell class"
class Cell: # we will use a class for Cell in order to interact with indivdual elements of the maze 
    
    def __init__(self, x, y): # initialisation of the cell class
        
        #the x and y attributes of a cell (it's position)
        self.x = x   # 9 columns
        self.y = y   # 7 rows

        #This attribute initialises that every wall surrounding "this cell" are present.
        self.walls = {'west': True, 'east': True, 'south': True, 'north': True}
        
        # This attribute changes when a cell is traversed or generated, allowing us to keep track of it.
        self.visited = False
    

# This method is where we draw the runtime cell (given it is coloured black), this allows us to track the cell while the maze is generated      
    def draw_current_cell(self): 

        x = self.x * TILE # this is the x coordinate of the lines 
        y = self.y * TILE # this is the y coordinate of the lines
        
        # the cell that is actively moving around the map, it is black and has a larger width and length so it is shown with prominence
        pygame.draw.rect(sc, pygame.Color("black"), (x + 2, y + 2, TILE - 2, TILE - 2))

    
    def draw(self): # This method is where it draws every cell individually given the if statements (meaning it will be grey, have walls that are north east south west, and the lines will be black)

        x = self.x * TILE # this is the x coordinate of the lines 
        y = self.y * TILE # this is the y coordinate of the lines
        
        if self.visited:
            pygame.draw.rect(sc, pygame.Color('grey'), (x, y, TILE, TILE)) # x,y are the top left hand corner of the rectange (rect), the TILE parameters refer to the height and width given to this rectangle

        if self.walls['north']:
            pygame.draw.line(sc, pygame.Color('black'), (x, y), (x + TILE, y), 2) # the (x,y) refers to the start POS of the line, the (x + TILE, y) refers to the end POS of the line
        
        if self.walls['east']:
            pygame.draw.line(sc, pygame.Color('black'), (x + TILE, y), (x + TILE, y + TILE), 2) # ^

        if self.walls['south']:
            pygame.draw.line(sc, pygame.Color('black'), (x + TILE, y + TILE), (x, y + TILE), 2) # ^

        if self.walls['west']:
            pygame.draw.line(sc, pygame.Color('black'), (x, y + TILE), (x, y), 2) # ^
    
    def check_cell(self, x, y):
        find_index = lambda x,y: x + y * columns  # using lambda as enclosed function to return the position of the index

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


# Main Program
grid_cells = [Cell(column, row) for row in range(rows) for column in range (columns)]

current_cell = grid_cells[0]

def find_pos(x,y):
    for current_cell in grid_cells():
        find_index = lambda x,y: x + y * columns

stack = []

while True:
    sc.fill(pygame.Color('gray')) # fill the surface screen with the color gray

    for event in pygame.event.get(): # for every event that occurs, it w
        #() print(event)  this command will be used to debug inputs from user) - ONLY USED FOR DEBUGGING

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

        ''' 
        Subsequently this piece of code is what runs the whole maze generation
        firstly, the if next_cell: code is what 
        '''

    pygame.display.flip() # updates the screen (since im using the while True statement this is for every clock tick)
    clock.tick(10) #tick the clock for the given time


