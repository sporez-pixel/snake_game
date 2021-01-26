import pygame as p
from pygame import *
import time
import random

class Apple:
    x = random.randint(1,79)*10
    y = random.randint(1,59)*10

    def draw(self,surface,colour):
        p.draw.rect(surface,colour,[self.x,self.y,10,10])

    def colision(self,applex,appley):
        if (self.x==applex and self.y==appley):
            return True
        return False

    def newcoord(self):
        self.x = random.randint(0,79)*10
        self.y = random.randint(0,59)*10

class Player:
    x = []
    y = []
    step = 10
    length = 3
    direction = 0
    WHITE = (255,255,255)

    updateCountMax = 2
    updateCount = 0

    def __init__(self, length):
        self.length = length
        for i in range(0,2000):
            self.x.append(400)
            self.y.append(300)

    def update(self):
        self.updateCount += 1

        if (self.updateCount > self.updateCountMax):

            for i in range(self.length-1,0,-1):
                print ("self.x[" + str(i) + "] = self.x[" + str(i-1) + "]")
                self.x[i] = self.x[i-1]
                self.y[i] = self.y[i-1]

            # update position of head of snake
            if self.direction == 0:
                self.x[0] = self.x[0] + self.step
            if self.direction == 1:
                self.x[0] = self.x[0] - self.step
            if self.direction == 2:
                self.y[0] = self.y[0] - self.step
            if self.direction == 3:
                self.y[0] = self.y[0] + self.step

            self.updateCount = 0

    def moveRight(self):
        self.direction = 0

    def moveLeft(self):
        self.direction = 1

    def moveUp(self):
        self.direction = 2

    def moveDown(self):
        self.direction = 3

class Game:
    def isCollision(self,x1,y1,x2,y2,bsize):
        if x1 >= x2 and x1 <= x2 + bsize:
            if y1 >= y2 and y1 <= y2 + bsize:
                return True
        return False

    def outside(self,x1,y1,x2,y2):
        if x1 < 0 or x1 > x2:
            return True
        if y1 < 0 or y1 > y2:
            return True
        return False

    def message(self,msg,color,dis):
        mesg = p.font.SysFont(None, 50).render(msg, True, color)
        dis.blit(mesg, [800/2, 600/2])

class App:
    WIDTH = 800
    HEIGHT = 600
    player = 0
    blue = (0,0,255)
    red = (255,0,0)
    white = (255,255,255)

    def __init__(self):
        self.running = True
        self.displaySurface = None
        self.player = Player(2)
        self.apple = Apple()
        self.game = Game()

    def on_init(self):
        p.init()
        self.displaySurface = p.display.set_mode((self.WIDTH, self.HEIGHT))
        p.display.set_caption("My first game in pygame!")
        self.running = True

    def draw(self):
        for i in range(0,self.player.length):
            x = self.player.x[i]
            y = self.player.y[i]
            p.draw.rect(self.displaySurface,self.white,[x,y,10,10])

    def onEvent(self):
        if (p.event.type == p.QUIT):
            self.running = False

    def onLoop(self):
        self.player.update()
        if (self.apple.colision(self.player.x[0],self.player.y[0])):
            self.apple.newcoord()
            self.player.length += 1
            self.player.update()

        for i in range(2,self.player.length):
            if self.game.isCollision(self.player.x[0],self.player.y[0],self.player.x[i], self.player.y[i],0):
                print("You lose! Collision: ")
                print("x[0] (" + str(self.player.x[0]) + "," + str(self.player.y[0]) + ")")
                print("x[" + str(i) + "] (" + str(self.player.x[i]) + "," + str(self.player.y[i]) + ")")
                exit(0)

        if self.game.outside(self.player.x[0],self.player.y[0],self.WIDTH,self.HEIGHT):
            print("You lose!")
            exit(0)
        pass

    def onRender(self):
        self.displaySurface.fill(self.blue)
        self.draw()
        self.apple.draw(self.displaySurface,self.red)
        p.display.flip()

    def onCleanup(self):
        p.quit()

    def onExecute(self):
        if self.on_init() == False:
            self.running = False
 
        while(self.running):
            p.event.pump()
            keys = p.key.get_pressed() 
            
            if (keys[p.K_RIGHT]):
                self.player.moveRight()

            if (keys[p.K_LEFT]):
                self.player.moveLeft()

            if (keys[p.K_UP]):
                self.player.moveUp()

            if (keys[p.K_DOWN]):
                self.player.moveDown()

            if (keys[p.K_ESCAPE]):
                self.running = False

            self.onLoop()
            self.onRender()
            time.sleep (50.0 / 1000.0);

        self.onCleanup()

if __name__ == "__main__":
    game = App()
    game.onExecute()