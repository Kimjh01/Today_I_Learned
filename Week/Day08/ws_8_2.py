class Animal:
    def __init__(self):
        pass

# 아래 클래스를 수정하시오.
class Dog(Animal):
    def __init__(self):
        super().__init__()

    def bark(self):
        print('멍멍!')


dog1 = Dog()
dog1.bark()
