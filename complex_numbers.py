class Complex:

    def __init__(self, real=None, imaginary=None):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imaginary - other.imaginary)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imaginary * other.imaginary,
                       self.imaginary * other.real + self.real * other.imaginary)

    def __truediv__(self, other):
        return Complex(
            (self.real * other.real + self.imaginary * other.imaginary) / (other.real ** 2 + other.imaginary ** 2),
            (other.real * self.imaginary - self.real * other.imaginary) / (other.real ** 2 + other.imaginary ** 2))

    def __abs__(self):
        return (self.real ** 2 + self.imaginary ** 2) ** (1 / 2)

    def __eq__(self, other):
        return str(self) == str(other)

    def __str__(self):
        if self.real == 0:
            return str(self.imaginary) + 'i'
        if self.imaginary == 0:
            return str(self.real)
        if self.imaginary == 1:
            return str(self.real) + '+' + 'i'
        if self.imaginary == -1:
            return str(self.real) + '-' + 'i'
        if self.imaginary > 0:
            return str(self.real) + '+' + str(self.imaginary) + 'i'
        if self.imaginary < 0:
            return str(self.real) + str(self.imaginary) + 'i'
