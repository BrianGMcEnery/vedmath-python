class Triple:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_values(self):
        return (self.a, self.b, self.c)

    def is_valid(self):
        (a, b, c) = (self.a, self.b, self.c)
        return a ** 2 + b ** 2 == c ** 2