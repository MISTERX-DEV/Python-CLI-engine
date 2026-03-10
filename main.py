import os

WIDTH = 120
HEIGHT = 30

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
    SYMBOL = "#"
    def __init__(self, x, y):
        super().__init__(x, y)

class Engine:
    points = []
    def __init__(self, pos: Point):
        Engine.points.append(pos)

    @staticmethod
    def render():
        buffer = []

        for y in range(HEIGHT):
            line = ""
            for x in range(WIDTH):
                draw = False
                for p in Engine.points:
                    if x == p.x and y == p.y:
                        symbol = p.SYMBOL
                        draw = True
                        break
                if draw:
                    line += symbol
                else:
                    line += " "
            buffer.append(line)

        os.system("cls" if os.name == "nt" else "clear")
        print("\n".join(buffer))