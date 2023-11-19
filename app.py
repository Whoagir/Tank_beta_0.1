import pygame
import config
from grid import Grid
from tank import Tank


# основной класс в котором происходят все события
class App(object):
    def __init__(self):  # метод инициализации
        self.screen = pygame.display.set_mode((config.WIN_WIDTH, config.WIN_HEIGHT))  # что бы окошечко было
        self.running = True  # переменная что бы работал главный цикл
        self.clock = pygame.time.Clock()

        self.objects = []  # набор объектов

        self.grid = Grid()  # переменная класса сетки
        self.objects.append(self.grid)  # добавляет объект сетка в список
        self.grid.create_perlin_map()

        self.tank = Tank(self, (100, 100))  # экземпляр танка
        self.objects.append(self.tank)  # добавляет объект танк в список

    def update(self, dt):
        for obj in self.objects:
            obj.update(dt)

    def event_handler(self, event):  # обработчик событий
        if event.type == pygame.QUIT:
            self.stop()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.stop()

    def input(self):
        for obj in self.objects:
            obj.input(pygame.key.get_pressed())

    def run(self):  # метод, который отвечает за бесконечный цикл программы
        while self.running:
            for event in pygame.event.get():
                self.event_handler(event)

            dt = self.clock.tick(config.FPS)/1000

            self.input()
            self.update(dt)
            self.draw()

    def draw(self):  # метод отрисовки
        self.screen.fill(config.WHITE)

        for obj in self.objects:
            obj.draw(self.screen)
        pygame.display.update()

    def stop(self):
        self.running = False


if __name__ == '__main__':
    game = App()
    game.run()
