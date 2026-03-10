import os

WIDTH = 120
HEIGHT = 30
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

class Engine:
    def __init__(self, width, height, background):
        self.width = width
        self.height = height
        self.background = background
        self.points = []

    def add_point(self, point):
        self.points.append(point)

    def render(self):
        grid = [[self.background for _ in range(self.width)] for _ in range(self.height)]

        for p in self.points:
            if 0 <= p.x < self.width and 0 <= p.y < self.height:
                grid[p.y][p.x] = p.symbol

        # Преобразуем в строки
        lines = ["".join(row) for row in grid]

        # Очистка экрана и вывод
        os.system("cls" if os.name == "nt" else "clear")
        print("\n".join(lines))

engine = Engine(WIDTH, HEIGHT, BACKGROUND)



engine.render()