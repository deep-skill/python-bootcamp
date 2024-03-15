class Fraction:

    def __init__(self, num, den):
        self.num = num
        self.den = den

    def to_decimal(self):
        return self.num / self.den

    def to_reduced_shape(self):
        g = self.__gcd(self.num, self.den)
        return '{} / {}'.format(self.num // g, self.den // g)

    def __gcd(self, a, b):
        if b == 0:
            return a
        return self.__gcd(b, a % b)

    def product(self, that):
        res_fraction = Fraction(self.num * that.num, self.den * that.den)
        return res_fraction

    def __mul__(self, that):
        res_fraction = Fraction(self.num * that.num, self.den * that.den)
        return res_fraction

    def addition(self, that):
        num = self.num * that.den + self.den * that.num
        den = self.den * that.den
        res_fraction = Fraction(num, den)
        return res_fraction

    def __add__(self, that):
        num = self.num * that.den + self.den * that.num
        den = self.den * that.den
        res_fraction = Fraction(num, den)
        return res_fraction

    def __lt__(self, that):
        return self.to_decimal() < that.to_decimal()

    def __str__(self):
        return '{} / {}'.format(self.num, self.den)


fraction = Fraction(10, 20)
print(fraction)
print(fraction.to_reduced_shape())
print(fraction.to_decimal())

fraction2 = Fraction(3, 4)
fraction3 = fraction.product(fraction2)
print(fraction3.to_reduced_shape())
fraction4 = fraction.addition(fraction2)
print(fraction4.to_reduced_shape())

print((fraction + fraction2).to_reduced_shape())
print((fraction * fraction2).to_reduced_shape())

fraction_list = [fraction2, fraction3, fraction3, fraction4, fraction2, fraction]
fraction_list.sort()
for f in fraction_list:
    print(f.to_decimal())
