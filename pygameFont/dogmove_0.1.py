#!/bin/env python3
# 引入——初始化和设置——响应与刷新

# 引入
import os, sys, time, pygame
from pygame.locals import *
from pygame.font import *

pygame.init()
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("显示文字")
# 填充白色
#screen.fill((255.255.255))

timer = 20
# main loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit
            sys.exit
    
    if (timer>0):
        timer -= 1
        time.sleep(1)
    screen.fill([0,0,0])
#    show_text(screen, (10,10),str(timer) ,(255,255,255),font_size = 21)
    cur_font = pygame.font.SysFont("宋体",23)
    text_fmt = cur_font.render(str(timer),1,[255,255,255])
    screen.blit(text_fmt, (20,20))
    # 刷新
    pygame.display.update()
































