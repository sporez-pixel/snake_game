import pygame

# JUST DEFINING COLOURS
white=(255,255,255)
red=(255,0,0)
blue=(0,0,255)
black=(0,0,0)

# SIZE
block=10

# PYGAME WINDOW SETTINGS
pygame.init()
game=pygame.display.set_mode((800,600))
pygame.display.set_caption('My first pygame game')
game_over=False

class snake:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.length = 1
    
    def draw(self):
        game.fill(blue)
        pygame.draw.rect(game,white,[self.x,self.y,block,block])

    def update(self,x,y): # X Y COORDINATES UPDATE
        self.x+=x
        self.y+=y 

def update():
    pygame.display.update()

def border(x,y):# CHECKING IF HE IS OUT OF RANGE OF THE BOARD
    if x>=800 or y>=600:
        return True
    if x<0 or y<0:
        return True

font_style = pygame.font.SysFont(None,50)
def msg(writing,colour):
    message = font_style.render(writing, True, colour)
    game.blit(message,[400,300])

# COORDINATES
x=0
y=0

s=snake(400,300) # DEFAULT POSITION OF SNAKE IN THE MIDDLE OF THE BOARD
s.draw()
update()

clock = pygame.time.Clock() # SETTING UP TIME FOR SNAKE SPEED

while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                x=-10
                y=0
            elif event.key==pygame.K_RIGHT:
                x=10
                y=0
            elif event.key==pygame.K_DOWN:
                x=0
                y=10
            elif event.key==pygame.K_UP:
                x=0
                y=-10
        
    s.update(x,y)
    s.draw()
    update()
    game_over=border(s.x,s.y)

    clock.tick(10) # SNAKE SPEED

while True:
    msg('You lost', red)  
    update()   
       
pygame.quit()
quit()