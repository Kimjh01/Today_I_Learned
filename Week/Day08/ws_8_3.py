class Animal:
    def __init__(self):
        pass

class Cat(Animal):
    def __init__(self, sound):
        super().__init__()
        self.sound = sound

    def meow(self):
        print("야옹!")

cat1 = Cat("야옹")
cat1.meow()