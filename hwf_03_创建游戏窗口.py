# 开发人员：Lenovo
# 开发时间：2021-07-27 18:05
# 文件名称：hwf_03_创建游戏窗口.py
# 开发工具：PyCharm
import pygame
pygame.init()
# 创建游戏的窗口
screen = pygame.display.set_mode((480, 700))
while True:
    print(screen)

pygame.quit()