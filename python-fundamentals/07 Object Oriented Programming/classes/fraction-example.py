class Fraction:

    def __init__(self, num, den):
        self.num = num
        self.den = den

    def to_decimal(self):
        return "{:.3}".format(self.num / self.den)

    def get_reduced_shape(self):
        gcd = self._gcd(self.num, self.den)
        new_num = self.num // gcd
        new_den = self.den // gcd
        #return "{} / {}".format(new_num, new_den)
        return Fraction(new_num, new_den)

    @classmethod
    def _gcd(cls, a, b):
        if b == 0:
            return a
        return cls._gcd(b, a % b)

    def __mul__(self, other):
        if type(other) != type(self):
            raise "El argumento debe ser de tipo {}".format(type(self))
        new_num = self.num * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __add__(self, other):
        new_num = self.num * other.den + self.den * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __str__(self):
        if self.den == 1:
            return "{}".format(self.num)
        return "{} / {}".format(self.num, self.den)


fraction = Fraction(3, 9)
other_fraction = Fraction(2, 3)
print(fraction)
print(fraction.to_decimal())
print(fraction.get_reduced_shape())
print(fraction * other_fraction)
add_fraction = fraction + other_fraction
print(add_fraction)
print(add_fraction.get_reduced_shape())

print(fraction * 50)