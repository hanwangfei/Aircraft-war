# 开发人员：Lenovo
# 开发时间：2021-07-28 21:14
# 文件名称：hwf_12_演练精灵.py
# 开发工具：PyCharm
import pygame
from plane_sprites import *
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

# 创建时钟对象
clock = pygame.time.Clock()

# 1.定义rect记录飞机初始位置
hero_rect = pygame.Rect(150, 500, 102, 126)


# 创建敌机的精灵
enemy = GameSprite("./images/enemy1.png")
enemy1 = GameSprite("./images/enemy1.png", 2)
# 创建敌机的精灵组
enemy_group = pygame.sprite.Group(enemy,enemy1)


# 游戏循环-->意味着游戏的正式开始
while True:
    # 可以指定循环内部代码执行的频率
    clock.tick(60)

    # 监听事件
    for event in pygame.event.get():
        # 判断事件类型是否是退出事件
        if event.type == pygame.QUIT:
            print("游戏退出...")
            # quit卸载所有模块
            pygame.quit()
            exit()
    # 2.修改飞机位置
    hero_rect.y -= 1
    # 判断飞机的位置
    if hero_rect.y <= -126:
        hero_rect.y = 700
    # 3.调用blit方法绘制图像
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    # 让精灵组调用两个方法
    # update----让组中的所有对象更新位置
    enemy_group.update()
    # draw------在screen上绘制所有的精灵
    enemy_group.draw(screen)
    # 4.调用update方法更新现实
    pygame.display.update()
    # print(screen)
