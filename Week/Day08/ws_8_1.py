class Animal:
    def __init__(self):
        pass

class Dog(Animal):
    def __init__(self):
        super().__init__()

class Cat(Animal):
    def __init__(self):
        super().__init__()

class Pet(Dog, Cat):
    count = 0

    def __init__(self):
        super().__init__() 
        Pet.count += 1

    @classmethod
    def access_num_of_animal(cls):
        return f'동물의 수는 {cls.count}마리 입니다.'

# 인스턴스 생성
dog = Pet()
print(Pet.access_num_of_animal())

# print(f'동물의 수는 {Pet.access_num_of_animal()}마리 입니다.')

cat = Pet()
print(Pet.access_num_of_animal())

# print(f'동물의 수는 {Pet.access_num_of_animal()}마리 입니다.')
