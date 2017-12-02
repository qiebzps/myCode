#!/bin/env python3
# 引入——初始化和设置——响应与刷新

# 引入
import os, sys, time, pygame
from pygame.locals import *
from pygame.font import *

pygame.init()
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("显示文字")
# 填充红色
screen.fill((255,0,0))

timer = 10 
cur_font = pygame.font.SysFont("宋体",200)  # 设置字体及大小
    
pygame.display.update()
# main loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    if (timer>0):
        timer -= 1
        time.sleep(1)
    screen.fill([0,0,0])
    #show_text(screen, (250,150),str(timer) ,(255,255,255),font_size = 221)
    text = cur_font.render(str(timer),1,[255,255,255])  # 内容，，颜色
    screen.fill((255,0,0))  # 填充红色
    screen.blit(text, (20,20)) # 
    if timer == 0:
        pygame.mixer.music.load("dog.wav")
        pygame.mixer.music.play(1) 
        timer = 10
    # 刷新
    pygame.display.update()
