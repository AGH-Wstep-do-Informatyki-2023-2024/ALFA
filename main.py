import pygame as pg
import sys, random
import Apple
from pygame.math import Vector2

pg.init()
width = 800
height = 800
screen = pg.display.set_mode((width, height))
FPS = 60
clock = pg.time.Clock()



class Snake:
    def __init__(self):
        self.x = width // 2
        self.y = height // 2
        self.body = [Vector2(self.x, self.y), Vector2(self.x - 40, self.y)]
        self.direction = Vector2(40,0)
    
    def draw(self):
        for part in self.body:
            sprite = pg.Rect(part.x, part.y, 40, 40)
            pg.draw.rect(screen, (100, 126, 100), sprite)
    
    def move(self):
        next_body = self.body[:-1]
        next_body.insert(0, next_body[0] + self.direction)
        self.body = next_body[:]

        
apple = Apple() 
snake = Snake()

SCREEN_UPDATE = pg.USEREVENT
pg.time.set_timer(SCREEN_UPDATE, 150)


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            snake.move()
        if event.type == pg.KEYDOWN:
            if event.type == pg.K_UP:
                snake.direction = Vector2(0, -40)
            elif event.type == pg.K_DOWN:
                snake.direction= Vector2(0, 40)
            elif event.type == pg.K_RIGHT:
                snake.direction= Vector2(40, 0)
            elif event.type == pg.K_LEFT:
                snake.direction= Vector2(-40, 0)
        
            
    ##
    screen.fill((0,0,0))
    apple.draw()
    snake.draw()
    ##
            
    pg.display.update()
    clock.tick(FPS)
