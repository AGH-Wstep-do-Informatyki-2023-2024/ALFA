import pygame as pg
import sys, random
from pygame.math import Vector2
import Snake, Apple

pg.init()
width = 800
height = 800
screen = pg.display.set_mode((width, height))
FPS = 60
clock = pg.time.Clock()


        
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
