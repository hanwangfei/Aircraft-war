# 开发人员：Lenovo
# 开发时间：2021-07-27 17:30
# 文件名称：hwf_01_pygame入门.py
# 开发工具：PyCharm
import pygame
# 在调用pygame的其他方法前，必须先调用初始化方法
pygame.init()
# 编写游戏代码
print("游戏的代码...")
# 找到pygame的文件位置，进而做出一些修改，hwf已于2021年7月27日对该代码进行了修改，注释掉了代码最底部的欢迎信息
# print(pygame.__file__)
# 最后游戏结束时要调用quit方法卸载pygame的所有模块进而释放内存
pygame.quit()
