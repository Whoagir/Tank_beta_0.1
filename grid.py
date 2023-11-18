import random
from constant import *
from numpy import floor
from perlin_noise import PerlinNoise


# класс сетки
class Grid(object):
    ''' ВАЖНО ПОНИМАТЬ, ЧТО СЕТКА ИМЕЕТ ВИД dict[(local_x, local_y)] = ((global_x, global_y), heights)
    key = (local_x, local_y) values = ((global_x, global_y), heights) '''
    def __init__(self):  # создаем переменную "сетки", указываем её тип (словарь)
        self.grid = dict()

        self.heights = []

    def update(self):
        pass

    def completion(self, heights: list):  # генерируем сетку, где ключ у нас локальные координаты, а значения это глобальные координаты и высота
        for i in range(numbers_width_grid + 1):
            for j in range(numbers_height_grid + 1):
                self.grid[(i, j)] = (x_global_coord_grid + width * i / numbers_width_grid - width / (numbers_width_grid * 2),
                                     y_global_coord_grid + height * j / numbers_height_grid - height / (numbers_height_grid * 2)), \
                                    heights[i][j]

    def generate_perlin_noise(self, seed):  # метод генерации высот
        # генерация основного шума и параметризация
        noise = PerlinNoise(octaves=2, seed=seed)  # 4522
        elevation = 1  # высота
        chunk_size = 24  # размер чанка
        terrain_width = max(numbers_width_grid, numbers_height_grid) + 1  # размер карты

        # генерация матрицы для представления ландшафта
        landscale = [[0 for i in range(terrain_width)] for i in range(terrain_width)]

        for position in range(terrain_width ** 2):
            # вычисление высоты y в координатах (x, z)
            x = floor(position / terrain_width)
            z = floor(position % terrain_width)
            y = floor(noise([x / chunk_size, z / chunk_size]) * elevation)
            landscale[int(x)][int(z)] = int(y)

        altitude_L = list(landscale)  # высота

        return altitude_L

    def create_perlin_map(self):
        seed = random.randint(1000, 3000)
        self.heights = self.generate_perlin_noise(seed)

    def get(self):  # получаем сетку по запросу
        return self.grid
