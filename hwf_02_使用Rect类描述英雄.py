# 开发人员：Lenovo
# 开发时间：2021-07-27 17:55
# 文件名称：hwf_02_使用Rect类描述英雄.py
# 开发工具：PyCharm
import pygame

hero_rect = pygame.Rect(100, 500, 120, 125)
print("英雄的原点%d %d" % (hero_rect.x, hero_rect.y))
print("英雄的尺寸%d %d" % (hero_rect.width, hero_rect.height))
print("英雄的尺寸 %d %d" % hero_rect.size)
print(hero_rect)