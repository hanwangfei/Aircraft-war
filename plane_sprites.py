# 开发人员：Lenovo
# 开发时间：2021-07-28 21:02
# 文件名称：plane_sprites.py
# 开发工具：PyCharm
import random   # 建议模块导入顺序:官方模块-第三方模块-自定义文件模块
import pygame
# 定义屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 定义刷新帧率
FRAME_PER_SER = 60
# 定义创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 英雄发射子弹事件
HERO_FTRE_EVENT = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""
    def __init__(self, image_name, speed=1):
        # 调用父类的初始化方法
        super().__init__()
        # 定义对象的属性
        self.image = pygame.image.load(image_name)
        # get_rect默认返回的是（0，0，长，宽）
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        # 在屏幕的垂直方向上移动

        self.rect.y += self.speed


class Background(GameSprite):
    """游戏背景精灵"""
    def __init__(self, is_alt=False):
        # 1.调用父类方法实现精灵的创建
        super().__init__("./images/background.png")
        # 2.判断是否是交替图像，如果是，需要设置初始位置
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        # 1.调用父类的方法实现
        super().update()

        # 2.判断背景图是否移除屏幕，如果移出屏幕，将图像设置到屏幕的上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height

        pass


class Enemy(GameSprite):
    """敌机精灵"""
    def __init__(self):
        # 1.调用父类方法，创建敌机精灵，同时指定敌机图片
        super().__init__("./images/enemy1.png")
        # 2.指定敌机的初始随机速度
        self.speed = random.randint(1, 3)
        # 3.指定敌机的初始随机位置
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)
        pass

    def update(self):
        # 1.调用父类方法，保持垂直方向的飞行
        super().update()
        # 2.判断是否飞出屏幕，如果是，需要从精灵组中删除敌机
        if self.rect.y >= SCREEN_RECT.height:
            # print("飞出屏幕 ，需要从精灵组删除.....")
            # kill方法可以将精灵从精灵组中移出，一旦移出，精灵自动销毁
            self.kill()
        pass

    def __del__(self):
        # print("敌机挂了 %s " % self.rect)
        pass


class Hero(GameSprite):
    """英雄精灵"""
    def __init__(self):
        # 1.调用父类方法，设置image && speed
        super().__init__("./images/me1.png", 0)
        # 2.设置英雄的初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        self.speed_y = 0
        # 3.创建子弹的精灵组
        self.bullets = pygame.sprite.Group()

    def update(self):
        # 英雄在水平方向移动
        self.rect.x += self.speed
        # 英雄在竖直方向移动
        self.rect.y += self.speed_y
        # 控制英雄不能离开屏幕
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right
        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.top == SCREEN_RECT.top:
            self.rect.top = SCREEN_RECT.top

    def fire(self):
        for i in (0, 1, 2):

            # 1.创建子弹精灵
            bullet = Bullet()
            # 2.设置精灵位置
            bullet.rect.bottom = self.rect.y - i * 20
            bullet.rect.centerx = self.rect.centerx
            # 3.将精灵添加到精灵组
            self.bullets.add(bullet)

        # print("发射子弹")

class Bullet(GameSprite):
    """游戏精灵类"""
    def __init__(self):
        # 调用父类方法，设置子弹图片，设置初始速度
        super().__init__("./images/bullet1.png", -2)
        pass

    def update(self):
        # 调用父类方法，让子弹沿垂直方向飞行
        super().update()
        # 判断子弹是否飞出屏幕
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        # print("子弹被销毁")
        self.kill()