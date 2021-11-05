# 开发人员：Lenovo
# 开发时间：2021-07-28 16:51
# 文件名称：hwf_06_update方法.py
# 开发工具：PyCharm
import pygame
pygame.init()
# 创建游戏的窗口
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
bg = pygame.image.load("./images/background.png")
screen.blit(bg, (0, 0))

# 绘制英雄的飞机
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (150, 300))

# 可以在所有绘制完成后再统一调用Update方法，可以提高游戏的绘制效率，进而提高游戏的流畅度
pygame.display.update()
while True:
    print(screen)

