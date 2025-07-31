class Myth:
    myth = 0  

    def __init__(self, name):
        self.name = name
        Myth.myth += 1  

    @staticmethod
    def description():
        print("신화는 한 나라 혹은 한 민족으로부터 전승되어 오는 예로부터 섬기는 신을 둘러싼 이야기를 뜻한다.")

m1 = Myth("dangun")
m2 = Myth("green & rome")

print(m1.name)
print(m2.name)
print(f"현재까지 생성된 신화 수 : {Myth.myth}")
m1.description()
