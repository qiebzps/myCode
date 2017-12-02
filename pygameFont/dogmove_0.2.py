#!/bin/env python3 

# 引入
import pygame, sys
from pygame.locals import *
from pygame.font import *

# 初始化与设置
pygame.init()

screen_size = 600,400
screen = pygame.display.set_mode(screen_size)

# main loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    # refresh
    pygame.display.update()

