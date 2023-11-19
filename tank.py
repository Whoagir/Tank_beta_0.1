import math
import pygame


# класс, отвечающий за все, что связано с танком (анимации, движение, коллизия и т.п.)
class Tank:
    def __init__(self, app, pos):
        self.x, self.y = pos

        self.angle = 0  # угол поворота
        self.vel = 0  # текущая скорость
        self.rotation_vel = 0  # направление поворота

        self.rotation_speed = 25  # скорость поворота
        self.speed = 100  # максимальная скорость
        self.acceleration = 1  # ускорение

        self.base_image = pygame.image.load('assets/tank/Straight/Sprite-0001.png').convert_alpha()
        self.base_image = pygame.transform.rotate(self.base_image, -90)

    def update(self, dt):
        self.angle += self.rotation_vel * dt
        rad = math.radians(-self.angle)
        dy = math.sin(rad) * self.vel * dt
        dx = math.cos(rad) * self.vel * dt

        self.x += dx
        self.y += dy

    def draw(self, screen):
        rotated_img = pygame.transform.rotate(self.base_image, self.angle)
        rect = rotated_img.get_rect(center=(self.x, self.y))
        screen.blit(rotated_img, rect)

    def input(self, key_pressed):
        moved = False
        rotated = False
        if key_pressed[pygame.K_a]:
            rotated = True
            self.rotate(left=True)
        if key_pressed[pygame.K_d]:
            rotated = True
            self.rotate(right=True)
        if key_pressed[pygame.K_w]:
            moved = True
            self.move_forward()
        if not moved:
            self.reduce_speed()
        if not rotated:
            self.rotate(stop=True)

    def move_forward(self):
        self.vel = min(self.vel + self.acceleration, self.speed)

    def rotate(self, left=None, right=None, stop=None):
        if left:
            self.rotation_vel = self.rotation_speed
        if right:
            self.rotation_vel = -self.rotation_speed
        if stop:
            self.rotation_vel = 0

    def reduce_speed(self):
        self.vel = max(self.vel - self.acceleration * 2, 0)
