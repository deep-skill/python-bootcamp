class Calc:

    version = '1.0'  # atributo global

    def __init__(self, name):
        self.name = name

    def model(self):
        return self.name

    @staticmethod
    def sum(x, y):
        return x + y


# Un método estático puede llamarse desde la clase
print(Calc.sum(8, 3))
print()

# Un atributo global es el mismo para todos los objetos
print(Calc.version)
Calc.version = '3.0'
calc = Calc('CasioT60')
print(calc.version)
calc.version = '4.0'
calc2 = Calc('CasioT61')
print(calc2.version)
Calc.version = '5.0'
print(calc2.version)

# Podemos agregar atributos después de creado el objeto
print(dir(calc))
calc.serie = '404'
Calc.series = '200'
print(dir(calc))
print(dir(calc2))

calc.function = lambda x: x ** 2
print(calc.function(5))
