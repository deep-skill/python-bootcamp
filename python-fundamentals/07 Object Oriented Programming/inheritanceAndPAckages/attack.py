class Human:
    def attack(self):
        print('Lanza una patada')


class Cyborg(Human):
    def attack(self):
        print('Lanza un láser')


class Ninja(Human):
    def attack(self):
        print('Lanza una estrella')


class C18(Ninja, Cyborg):
    pass


human = Human()
cyborg = Cyborg()
ninja = Ninja()
c18 = C18()

human.attack()
cyborg.attack()
ninja.attack()
print()
c18.attack()
