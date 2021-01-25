import pygame as p
from pygame import *
import time
import random

class Apple:
    x = random.randint(0,80)*10
    y = random.randint(0,60)*10

    def draw(self,surface,colour):
        p.draw.rect(surface,colour,[self.x,self.y,10,10])

    def colision(self,applex,appley):
        if (self.x==applex and self.y==appley):
            return True
        return False

    def newcoord(self):
        self.x = random.randint(0,80)*10
        self.y = random.randint(0,60)*10

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
            self.x.append(0)
            self.y.append(0)

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
        self.player = Player(1)
        self.apple = Apple()

    def on_init(self):
        p.init()
        self.displaySurface = p.display.set_mode((self.WIDTH, self.HEIGHT))
        p.display.set_caption("My first game in p!")
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