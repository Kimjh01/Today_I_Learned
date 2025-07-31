class Person:
    count = 0  

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count += 1 

    def introduce(self):
        return f"제 이름은 {self.name} 이고, 저는 {self.age}살 입니다."

    @classmethod
    def number_of_people(cls):
        return cls.count


person1 = Person("Alice", 25)
print(person1.introduce())
print(Person.number_of_people())
