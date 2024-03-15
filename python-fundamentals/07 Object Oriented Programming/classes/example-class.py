class Example:
    def __init__(self, name, version="1"):
        self.name = name
        self._version = version
        self._private_field = "private"
        self.__really_private = "really private"

    def version(self):
        return self._version
        pass

    def show(self):
        # print(self.name + " " + self.version)
        print("{} {}".format(self.name, self.version))


example1 = Example("Example 1")
example1.show()
print(example1.name)
example1._private_field = "public"
print(example1._private_field)
print(example1.version())
print(example1._Example__really_private)
