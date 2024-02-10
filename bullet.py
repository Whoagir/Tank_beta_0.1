import pygame
import math


# класс, отвечающий за снаряд и все с ним связанное
class Bullet(object):
    def __init__(self, center, app, tank_rotate, tank):
        self.bullet_img = pygame.image.load('assets/secondary objects/bullets/bullet.png').convert_alpha()  # модель снаряда
        self.x, self.y = center
        self.app = app
        self.tank = tank
        self.tank_rotate = tank_rotate

        self.speed = -1  # скорость снаряда

    def fly(self, dt):
        self.x += self.speed * dt
        self.y += self.speed * dt

    def draw(self, screen):
        bullet = self.bullet_img
        rect_bullet = bullet.get_rect(center=self.app.grid_dict[(self.x, self.y)][0])
        screen.blit(bullet, rect_bullet)

    def conflict(self):
        pass
