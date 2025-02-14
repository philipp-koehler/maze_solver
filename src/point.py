
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("Unsupported operand type for +: 'Point' and '{}'".format(type(other).__name__))
        
    def __sub__(self, other):
        if isinstance(other, Point):
            return Point(self.x - other.x, self.y - other.y)
        else:
            raise TypeError("Unsupported operand type for -: 'Point' and '{}'".format(type(other).__name__))

    def __mul__(self, val):
        if isinstance(val, int):
            return Point(self.x * val, self.y * val)
        else:
            raise TypeError("Unsupported operand type for *: 'Point' and '{}'".format(type(val).__name__))
