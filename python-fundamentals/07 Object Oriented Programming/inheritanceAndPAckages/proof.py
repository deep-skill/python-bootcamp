class Proof:

    def __init__(self, attr1, attr2):
        self.attr_public = attr2
        self._attr_private = attr1
        self.__attr_super_private = attr1 + attr2

    def _method_private(self):
        self.__method_private()
        print(self.attr_public)

    def __method_private(self):
        print(self._attr_private)


proof = Proof(2, 3)

proof._method_private()  # No deberías
print()

# Lanza error, se ocultan método y atributo
# proof.__method_private()
# print(proof.__attr_super_private)

# Pero hay manera de acceder
proof._Proof__method_private()
print(proof._Proof__attr_super_private)

# Accedemos a un atributo público
print(proof.attr_public)
proof.attr_public = 4
print(proof.attr_public)

# Python no evita que puedas acceder al atributo privado, pero no debes hacerlo
print(proof._attr_private)
proof._attr_private = 4
print(proof._attr_private)

