#!/bin/env python3
# 引入——初始化和设置——响应与刷新

# 引入
import os, sys, time, pygame
from pygame.locals import *
from pygame.font import *

def show_text(surface_handle, pos, text, color, font_bold = False, font_size = 13, font_italic = False):
    '''
    文字处理函数
    input:
        surface_handle:surface句柄
        pox:文字显示位置
        color:文字颜色
        font_bold:是否加粗
        font_size:字体大小
        font_italic:是否斜体
    oupput:
        none
    author:
        zps
    '''
    # 获取系统字体，并设置文字大小
    cur_font = pygame.font.SysFont("宋体", font_size)

    # 设置是否加粗
    cur_font.set_bold(font_bold)

    # 设置是否斜体
    cur_font.set_italic(font_italic)

    #设置文字内容
    text_fmt = cur_font.render(text,1,color)

    # 绘制文字
    surface_handle.blit(text_fmt, pos)

pygame.init()
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("显示文字")
# 填充白色
#screen.fill((255.255.255))

timer = 10
show_text(screen, (250,150),str(timer) ,(255,255,255),font_size = 221)
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
    show_text(screen, (250,150),str(timer) ,(255,255,255),font_size = 221)
    # 刷新
    pygame.display.update()
































