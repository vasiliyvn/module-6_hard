class Figure:
    sides_count = 0


    # filled = False  # изначально незакрашена

    def __init__(self, rgb, *side):  # палитра и стороны
        self.__color = list(rgb)
        self.__sides = side[0]  # берём только первое значение
        self.filled = True  # принята палитра (rgb), фигура закрашена

    def get_color(self):

        self.filled = True
        return self.__color

    def _is_valid_color(self, r, g, b):
        self.r, self.g, self.b = r, g, b
        if 0 <= self.r <= 255 and 0 <= self.g <= 255 and 0 <= self.b <= 255:
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self._is_valid_color(r, g, b):
            self.__color = [self.r, self.g, self.b]

    def __is_valid_sides(self, *args):
        for i in args:
            if isinstance(i, int) == self.sides_count and i > 0 and type(i) == int:
                return True
            else:
                return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        massive = []
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
        else:
            for i in range(self.sides_count):
                massive.append(self.__sides)
            self.__sides = massive
            return self.__sides


class Circle(Figure):
    sides_count = 1
    __radius = None

    def set_radius(self):
        self.__radius = self.__len__() / (2 * 3.141569)
        return self.__radius

    def get_square(self):
        self.set_radius()
        return (self.__radius ** 2) * 3.141569

class Triangle(Figure):
    sides_count = 3
    __height = None

    def get_square(self):
        return (self.__sides ** 2) * (3 ** 0.5) / 4

    def set_height(self):
        self.__height = self.__sides * (3 ** 0.5) / 2
        return self.__height

class Cube(Figure):
    sides_count = 12
    # def __init__(self,*side):
    #     super().__init__()
    def get_volume(self):
        return self.get_sides()[0]** 3

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
