class Dog:
    def __init__(self):
        self.sound = "멍멍"

class Cat:
    def __init__(self):
        self.sound = "야옹"

class Pet1(Dog, Cat):
    def __init__(self):
        super().__init__()  
    
    def __str__(self):
        return f"애완동물은 {self.sound} 소리를 냅니다."

class Pet2(Cat, Dog):
    def __init__(self):
        super().__init__() 
    
    def __str__(self):
        return f"애완동물은 {self.sound} 소리를 냅니다."

pet1 = Pet1()
print(pet1) 

pet2 = Pet2()
print(pet2) 
