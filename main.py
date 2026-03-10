import os

WIDTH = 20
HEIGHT = 20
BACKGROUND = " "

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y    
    def __repr__(self):
        return str((self.x, self.y))
    
    # Сложение векторов
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    # Вычитание векторов
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    # Умножение на число
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    # Деление на число
    def __truediv__(self, scalar):
        return Vector(self.x / scalar, self.y / scalar)
    
class Point(Vector):
    def __init__(self, x, y, symbol="#"):
        super().__init__(x, y)
        self.symbol = symbol
    def get_points(self):
        return [self] 

class Engine:
    def __init__(self, width, height, background):
        self.width = width
        self.height = height
        self.background = background
        self.drawables = []

    def add(self, drawable):
        self.drawables.append(drawable)

    def render(self):
        grid = [[self.background for _ in range(self.width)] for _ in range(self.height)]

        for obj in self.drawables:
            for point in obj.get_points():
                x  = int(point.x)
                y = int(point.y)
                if 0 <= x < self.width and 0 <= y < self.height:
                    grid[y][x] = point.symbol

        # Преобразуем в строки
        lines = ["".join(row) for row in grid]

        # Очистка экрана и вывод
        os.system("cls" if os.name == "nt" else "clear")
        print("\n".join(lines))

engine = Engine(WIDTH, HEIGHT, BACKGROUND)



engine.render()