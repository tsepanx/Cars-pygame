class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_coordinates(self):
        return [self.x, self.y]

    def set_coordinates(self, arr):
        self.x = arr[0]
        self.y = arr[1]

    def get_length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def normalize(self):
        self.div(self.get_length())

    def set_length(self, value):
        self.normalize()
        self.mul(value)

    def get_direction(self):
        length = self.get_length()
        if length != 0:
            return self / length
        else:
            return Vector(0, 0)

    @staticmethod
    def scalar(vector1, vector2):
        return vector1.x * vector2.x + vector1.y * vector2.y

    def add(self, vector):
        self.x += vector.x
        self.y += vector.y

    def sub(self, vector):
        self.x -= vector.x
        self.y -= vector.y

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def mul(self, value):
        self.x *= value
        self.y *= value

    def __mul__(self, value):
        other = Vector(self.x, self.y)
        other.x *= value
        other.y *= value
        return other

    def div(self, value):
        if value > 0:
            self.x /= value
            self.y /= value

    def __truediv__(self, other):
        if other > 0:
            res = Vector(0, 0)
            res.x = self.x / other
            res.y = self.y / other
            return res

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def clear(self):
        self.x = 0
        self.y = 0
