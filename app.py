import pygame
from constant import *
from grid import Grid


# основной класс в котором происходят все события
class App(object):
    def __init__(self):  # метод инициализации
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))  # что бы окошечко было
        self.running = True  # переменная что бы работал главный цикл
        self.grid = Grid()  # переменная класса сетки
        self.objects = []  # набор объектов

        self.objects.append(self.grid)  # добавляем объекты в список

    def update(self):
        for obj in self.objects:
            obj.update()

    def event_handler(self, event):  # обработчик событий
        if event.type == pygame.QUIT:
            self.stop()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.stop()

    def run(self):  # метод, который отвечает за бесконечный цикл программы
        while self.running:
            for event in pygame.event.get():
                self.event_handler()

            self.update()

    def draw(self):  # метод отрисовки
        self.screen.fill(WHITE)

        for obj in self.objects:
            obj.draw(self.screen)

    def stop(self):
        self.running = False

if __name__ == '__main__':
    game = App()
    game.run()
