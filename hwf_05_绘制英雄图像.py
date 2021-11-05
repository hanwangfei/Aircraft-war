# 开发人员：Lenovo
# 开发时间：2021-07-28 16:40
# 文件名称：hwf_05_绘制英雄图像.py
# 开发工具：PyCharm
import pygame
pygame.init()
# 创建游戏的窗口
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
# 1>加载游戏数据
bg = pygame.image.load("./images/background.png")
# 2>blit绘制图像
screen.blit(bg, (0, 0))
# 3>update更新屏幕显示
pygame.display.update()

# 绘制英雄的飞机
# 注意pang格式的图像是支持透明的，在绘制图象时，透明区域不会显示任何内容
# 但如果下方已经有内容，会透过透明区域显示出来
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (150, 300))
pygame.display.update()
while True:
    print(screen)

