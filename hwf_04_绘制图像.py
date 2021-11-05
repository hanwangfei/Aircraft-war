# 开发人员：Lenovo
# 开发时间：2021-07-28 16:07
# 文件名称：hwf_04_绘制图像.py
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
while True:
    print(screen)

