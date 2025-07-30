# Day 7: OOP 1

## 절차 지향과 객체 지향 

Procedural Programming: 함수와 로직 중심 작성 데이터를 **순차적으로 처리**

- 변수와 함수를 별개로 다룸

```python 

name = "Alice"
age = 25

def introduce(name, age):
    print(f"안녕하세요, {name}입니다. 나이는 {age}살입니다.")

introduce(name, age)

```

**절차 지향 프로그래밍 특징**

- 입력을 받고, 처리하고, 결과를 내는 과정이 위에ㅐ서 아래로 순차적으로 흐르는 형태 
- 순차적인 명령어 실행
- 데이터와 함수(절차)의 분리
- 함수 호출의 흐름이 중요
 
> 데이터를 다시 재사용하기보다는 처음부터 끝까지 실행되는 결과물이 중요

**절차 지향적 프로그래밍의 한계**

1. 복잡성 증가
- 프로그램 규모가 커질수록 데이터와 함수의 관리가 어려움
- 전역 변수의 증가로 인한 관리의 어려움

2. 유지보수 문제
- 코드 수정 시 영향 범위 파악이 어려움


Object Oriented Programming: 클래스는 **설계도**, 인스턴스는 **실제 물건**

- 사람(객체) 안에 name, age와 이와 관련된 기능(메서드) 포함

```python 

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"안녕하세요, {self.name}입니다. 나이는 {self.age}살입니다.")

alice = Person("Alice", 25)
alice.introduce() # 객체가 자신의 정보를 출력

```

**객체 지향 프로그래밍 특징**

- 프로그램을 데이터(변수)와 그 데이터를 처리하는 함수(메서드)를 하나의 단위(객체)로 묶어서 조직적으로 관리

- 데이터와 메서드의 결합
 


|     **절차 지향**      |     **객체 지향**      |
| ------------------ | -------------------------- |
| - 데이터와 해당 데이터를 처리하는 함수(절차)가 중요 | - 데이터와 해당 데이터를 처리하는 메서드를 하나의 객체로 묶음 |
| - 데이터와 해당 데이터를 처리하는 메서드를 하나의 객체로 묶음 | 객체 간 상호작용과 메시지 전달이 중요 |


|     **절차 지향**      |     **객체 지향**      |
| ------------------ | -------------------------- |
| "어떤 순서로 처리할까?"| "어떤 객체가 이 문제를 해결할까?", "이 객체는 어떤 속성과 기능을 가질까?" |

**객체지향 - "데이터가 살아나다**
- 객체 지향은 수동적인 데이터가 능동적인 객체로 변화한 것
- 절차 지향에서는 데이터가 함수의 매개변수로 전달되어 처리되는 수동적 존재였지만, 객체 지향에서는 데이터와 해당 데이터를 처리하는 메서드가 하나의 객체로 통합되어 **스스로 기능을 수행하는 능동적 존재가 됨**
- 이는 코드의 구조화와 재사용성을 높이는 동시에, 실제 세계의 모델링 방식과 더 유사한 프포그래밍을 가능하게 함


**주의 사항**

절차 지향과 객체 지향은 대조되는 개념이 아니다

> 객체 지향은 기존 절차 지향을 기반으로 두고 보완하기 위해 객체라는 개념을 도입
> 상속, 코드 재사용성, 유지보수성 등의 이점을 가지는 패러다임

---

## 객체와 클래스 

Object: 실제 존재하는 사물을 추상화한 것 "속성"과 "동작"을 가짐

Class: 객체를 만들기 위한 설계도, 데이터와 기능을 함께 묶는 방법을 제공, 파이썬에서 타입을 표현하는 방법

> 클래스로부터 여러 개의 객체를 쉽게 만들어 낼 수 있음

**객체 특성**

- 속성(Attribute): 객체의 상태/데이터

- 메서드(Method): 객체의 행동/기능

- 고유성: 각 객체는 고유한 특성을 가짐 # 독립적

---

## 클래스 기초

Class: 클래스는 하나의 구조 안에 **데이터(변수)**와 **기능(함수)**을 함께 정의하는 도구

ex. Class: 소나x 설계도

Instance 
-소나x 1
-소나x 2

Type(variance)
- 색깔, 가죽 종류, 지역, 차량번호

function(method)
- 직전하기, 후진하기, 우회전하기, 자율주행

**클래스 정의**

class 키워드 
- 클래스 이름은 파스칼 케이스 (Pascal Case) 방식으로 작성

``` python 

class MyClass:
    pass

```

__init__ 메서드
- '생성자 메서드'로 불림
- 새로운 객체를 만들 때 필요한 초기값을 설정 (메서드 챕터에서 진행)

``` python 

class Person:
    #생성자 매서드
    def __ init__(self, name, age):
        self.name = name # 인스턴스 속성
        self.age = age # 인스턴스 속성
    
    def introduce(self):
        print(f"안녕하세요, 저는 {self.name}, 나이는 {self.age}살입니다.")
    
```

---

## 인스턴스

Instance: 클래스를 통해 생성된 객체

- 인스턴스는 클래스를 사용해 실제로 만들어진 객체
- 같은 클래스로 여러 인스턴스를 만들 수 있으며,
- 각 인스턴스는 클래스 구조를 따라 동작하지만 서로 독립된 데이터를 가질 수 있음

**인스턴스 예시**

 - 클래스가 설계도라면, 인스턴스는 그 설계도로부터 실제로 만든 '개별 물건'
 - Person("Alice", 25)라고 하면 Person이라는 설계도로부터 이름이 Alice이고 나이가 25dls '사람 객체'가 탄생 

 ``` python

    p1 = Person("Alice", 25)
    p1.introduce() # "안녕하세요. 저는 Alice, 나이는 25살입니다."
    p2 =Person("Bella", 30)
    p2.introduce() # "안녕하세요. 저는 Bella, 나이는 30살입니다."

 ```

--- 

## 클래스와 인스턴스

**클래스와 인스턴스**

- 클래스를 정의한다는 것은 **공통된 특성과 기능을 가진 틀**을 만드는 것
- 실제 활동하는 개별 객체들은 이 틀에서 생성된 **인스턴스(instance)**
- 공통된 특성과 기능을 가진 틀을 만드는 것은 곧 **새로운 타입을 만드는 행위**

> "아이유는 인스턴스다." 라는 표현이 모호한 이유 역시 마찬가지
> "무슨 타입의 인스턴스"인지를 알 수 없기 때문

```python

class Singer:
    pass

iu = Singer()
print(type(iu)) # <class '__main__.Singer'>

```

> type(iu)를 출력하면 Singer가 출력 됨. 즉, Python은 iu가 어떤 타입에 속하는지 알고 있어야함 

- 변수 name의 타입은 str 클래스
> 변수 name은 str 클래스의 인스턴스

```python

name = "Alice"

print(type(name)) # <class 'str'>

```

- 결국 문자열 타입의 변수는 str 클래스로 생성된 인스턴스

```python

print(help(str))

"""
class str(object)
| str(object='') -> str
| str(bytes_or_buffer[, encoding[, errors]]) -> str
|
| Create a new string object from the given object. If encoding or
| errors is specified, then the object must expose a data buffer
| that will be decoded using the given encoding and error handler.
| Otherwise, ...
"""

```

**","'hello','파이썬'** : 문자열 타입(클래스)의 객체(인스턴스)

**[1,2,3], [1], [], ['hi']** : 리스트 타입(클래스)의 객체(인스턴스)

**"hello".upper()"**: 문자열.대문자로(), 객체.행동(), 인스턴스.메서드()

**[1,2,3].sort()**: 리스트.정렬해(), 객체.행동(), 인스턴스.메서드()

**하나의 객체(object)는 특정 클래스의 인스턴스(instance)이다**
> 123, 900, 5는 클래스 int의 인스턴스
> 'hello', 'bye'는 클래스 str의 인스턴스
> [232, 89, 1], []은 클래스 list의 인스턴스

---

## 클래스 구성요소

**클래스 구조**

생성자 메서드 
- 인스턴스 생성 시 자동 호출되는 특별한 메서드
- __init__ 이라는 이름의 메서드로 정의
- 인스턴스 변수의 초기화 담당

```python

class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

# 인스턴스 생성
c1 = Circle(1)
c2 = Circle(2)

```

인스턴스 변수(속성)
- 각 인스턴스별 고유한 속성
- self. 변수명 형태로 정의
- 인스턴스마다 독립적인 값 유지 

```python

class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

# 인스턴스 변수(속성)
print(c1.radius) # 1
print(c2.radius) # 2

```

클래스 변수(속성)
- 모든 인스턴스가 공유하는 속성
- 클래스 내부에서 직접 정의 

```python

class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

# 클래스 변수(속성)
print(c1.pi) # 3.14
print(c2.pi) # 3.14

```

---

## 클래스 변수와 인스턴스 변수

**클래스 변수와 인스턴스 변수**

- 클래스 변수와 동일한 이름으로 인스턴스 변수 생성 시 클래스 변수가 아닌 인스턴스 변수에 먼저 참조하게 됨

- class.class_variable 로 클래스 변수 참조 가능

```python

class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

c1 = Circle(5)
c2 = Circle(10)
print(c1.radius) # 5
print(c2.radius) # 10

c1.pi = 100

print(c1.pi) # 100
print(Circle.pi) # 3.14
# c2는 인스턴스 변수 pi가 없으므로 클래스 변수 pi를 참조
print(c2.pi) # 3.14

```

---

## 메서드

Method: 클래스 내부에 정의된 함수로, 해당 객체가 어떻게 동작할지를 정의

**인스턴스 메서드**

Instance method: 인스턴스의 **상태를 조작**하거나 **동작을 수행**

**인스턴스 메서드 구조**
- 클래스 내부에 정의되는 메서드의 기본 
- 반드시 첫 번째 인자로 **인스턴스 자신(self)**을 받음
- 인스턴스의 속성에 접근하거나 변경 가능

```python

class MyClass:

    def instance_method(self, arg1, ...):
        pass

```
> self는 매개변수 이름일 뿐이며 다른 이름으로 설정 가능, 하지만 다름 이름을 사용하지 않을 것을 강력히 권장 


**Self 동작 원리**
- upper 메서드를 사용해 문자열 'hello'를 대문자로 변경
```python

'hello'.upper()

```

- 실제 파이썬 내부 동작은 다음과 같음
```python

str.uppper('hello')

```

- str 클래스가 uppper 메서드를 호출했고, 그 첫번째 인자로 문자열 인스턴스가 들어간 것

> 인스턴스 메서드의 첫번째 인자가 반드시 인스턴스 자기 자신인 이유


'hello'.upper()은 str.uppper('hello')를 객체 지향 방식의 메서드로 호출하는 표현 (단축형 호출)

> 'hello'라는 문자열 객체가 단순히 어딘가의 함수로 들어가는 인자로 활용되는 것이 아닌 객체 스스로 메서드를 호출하여 코드를 동작하는 **객체 지향적인 표현인 것**

```python

class Counter:
    def __init__(self):
        self.count = 0 
    
    def increment(self):
        self.count += 1

c = Counter()
c.increment()
print(c.count) # 1

```

constructor method: 인스턴스 객체가 생성될 때 자동으로 호출되는 메서드
> 인스턴스 변수들의 초기값을 설정

```python

class Person:
    def __init__(self, name):
        # 왼쪽 name : 인스턴스 변수 name
        # 오른쪽 name : 생성자 메서드의 매개변수 이름
        self.name = name
        print("인스턴스가 생성되었습니다.")
    
    def greeting(self):
        print(f"안녕하세요 {self.name}입니다.")

person1 = Person("지민") # 인스턴스가 생성되었습니다.
person1.greeting() # 안녕하세요. 지민입니다.
#Person.greeting(person)

```

**클래스 메서드**

class method: **클래스 변수를 조작**하거나 클래스 레벨의 **동작을 수행**

> @classmethod를 사용하면 클래스 자체가 호출할 수 있고, 그 안에서 클래스 변수를 변경하거나 전체 동작을 정의할 수 있음

**클래스 메서드 구조**
- @classmethod 데코레이터를 사용하여 정의
- 호출 시, 첫번째 인자로 해당 메서드를 호출하는 클래스(cls)가 전달됨
- 클래스를 인자로 받아 클래스 속성을 변경하거나 읽는데 사용

```python

class MyClass:
    @ classmethod
    def class_method(cls, arg1, ...):
        pass

```

> cls는 매개변수 이름일 뿐이며 다른 이름으로 설정 가능
> 하지만 다른 이름을 사용하지 않을 것을 강력히 권장

**클래스 메서드 활용**

```python

class Person:
    population = 0 

    def __init__(self, name):
        self.name = name
        Person.increase_population()
    
    @classmethod
    def increase_population(cls):
        cls.population += 1

person1 = Person("Alice")
person2 = Person("Bella")
print(Person.population) # 2

```

**스태틱 메서드**

static method: 클래스, 인스턴스와 상관없이 **독립적으로 동작하는 메서드**

> @staticmethod를 사용하여 클래스 내부에 있지만 어떤 객체와도 관계없이 동작하는 메서드를 만듬 

**스태틱 메서드 구조**
- @staticmethod 데코레이터를 사용하여 정의
- 호출 시 자동으로 전달 받는 인자가 없음 (self, cls를 받지 않음)
- 인스턴스나 클래스 속성에 직접 접근하지 않는, '도우미 함수'와 비슷한 역할

```python

class MyClass:

    @staticmethod
    def static_method(arg1, ...):
        pass

```

**스태틱 메서드 예시**

- 수학에 관련 기능을 담은 MathUtils 클래스에서 덧셈 기능을 제공하는 예시

```python

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

print(MathUtils.add(3, 5)) # 8 

```

---

## 메서드 활용 

입출금이 가능한 은행 계좌 클래스 만들기

1. __init__(self, owner, balance=0)
    - 종류: 생성자
    - 역할: 새로운 계좌 인스턴스를 생성할 때, 소유자 이름과 초기 잔액 설정
    - 호출방식: BackAccount("Alice", 100)처럼 클래스 호출 시 자동 실행

2. interest_rate = 0.02
    - 종류: 클래스 변수
    - 역할: **모든 BankAccount 인스턴스가 공유**하는 기본 이자율을 저장
    - 특징: 클래스 이름으로 접근, 모든 인스턴스가 같은 값을 참조

```python

class BankAccount:
    interest_rate = 0.02 # 이자율

    def __init__(self, owner, balance=0):
        self.owner = owner # 계좌 소유자
        self.balance = balance # 초기 잔액

```

3. deposit(self, amount)
    - 종류: 인스턴스 메서드
    - 역할: 계좌에 amount만큼의 금액을 입금
    - 특징: self.balance를 직접 조작하여 잔액을 변경
    - 호출방식: alice_acc.deposit(500)처럼 인스턴스를 통해 호출

4. withdraw(self, amount)
    - 종류: 인스턴스 메서드
    - 역할: 계좌에서 amount만큼의 금액을 출금
    - 특징: 출금 가능 여부(잔액>=출금액)를 조건문으로 검사
    - 호출방식: alice_acc.withdraw(200)

```python

class BankAccount:
   ...

   #입금
    def deposit(self, amount):
        self.balance += amount

   #출금

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount 
        else:
            print("잔액 부족!")

    ...
```

5. set_interest_rate(cls, rate)
    - 종류: 클래스 메서드(@classmethod 사용)
    - 역할: 전체 BankAccount 클래스의 이자율을 설정
    - 특징: cls.interest_rate를 변경함으로써 **모든 인스턴스에 영향**
    - 호출 방식: BankAccount.set_interest_rate(0.03)

6. is_positive(amount)
    - 종류: 스태틱 메서드 (@staticmethod 사용)
    - 역할: 전달된 금액이 양수인지 단독으로 판단
    - 특징: 클래스나 인스턴스의 상태에 전혀 의존하지 않음
    - 호출 방식: BankAccount.is_positive(금액) 형태로 **독립 호출**
    

```python

class BankAccount:
    ...

    # 이자율 설정
    @classmethod
    def set_interest_rate(cls, rate):
        cls.interest_rate = rate

    # 금액이 양수인지 검증
    @staticmethod
    def is_positive(amount):
        return amount > 0 

    ...

```

**입출금이 가능한 은행 계좌 클래스 활용**

```python

# 계좌 개설 (인스턴스 생성)
alice_acc = BankAccount("Alice", 1000)

# 입금 및 출금 (인스턴스 메서드 호출)
alice_acc.deposit(500)
alice_acc.withdraw(200)

# 잔액 확인 (인스턴스 변수 참조)
print(alice_acc.balance) # 1300

# 이자율 변경 (클래스 메서드 호출)
BankAccount.set_interest_rate(0.03)
print(BankAccount.interest_rate) # 0.03

# 잔액이 양수인지 확인 (정적 메서드 호출)
print(BankAccount.is_positive(alice_acc.balance)) # True

```

---

## 메서드 정리  

- 인스턴스 메서드: 인스턴스의 상태를 변경하거나, 해당 인스턴스의 특정 동작을 수행

- 클래스 메서드: 클래스 변수를 조작하거나 클래스 레벨의 동작을 수행

- 스태틱 메서드: 클래스 및 인스턴스와 관련이 없는 일반적인 기능을 수행

- 클래스가 사용해야 할 것: 클래스 메서드, 스태틱 메서드

- 인스턴스가 사용해야 할 것: 인스턴스 메서드 

> 공통 설정값을 바꾸거나 유틸리티 성 처리를 할 땐 클래스/스태틱 메서드,
> 개별 객체의 상태를 다룰 땐 반드시 인스턴스 메서드를 사용
> "무엇을 바꾸는가?"가 메서드 선택의 기준

**어떤 메서드를 사용해야 하나?**

```python

class MyClass:
    def instance_method(self):
        return "instance method", self

    @ classmethod
    def class_method(cls):
        return "class method", cls

    @ staticmethod
    def static_method():
        return "static_method"

```

**클래스가 할 수 있는 것** 

- 클래스는 모든 메서드를 호출 할 수 있음
> 하지만 클래스는 클래스 메서드와 스태틱 메서드만 사용

```python

instance = MyClass()
print(MyClass.instance_method(instance)) # ('instance method', <__main__.MyClass object at0x...028F10'>)
print(MyClass.class_method) # ('class method', <class '__main__.MyClass'>)
print(MyClass.static_method) # static method

```

**인스턴스가 할 수 있는 것** 

- 인스턴스는 모든 메서드를 호출 할 수 있음
> 하지만 인스턴스는 인스턴스는 메서드만 사용

```python

instance = MyClass()
print(instance.instance_method()) # ('instance method', <__main__.MyClass object at0x0000...84EAF10'>)
print(instance.class_method) # ('class method', <class '__main__.MyClass'>)
print(instance.static_method) # static method

```

**할 수 있다 != 써도 된다**

> 각자의 메서드는 OOP 패러다임에 따라 명확한 목적에 따라 설계된 것이기 때문에
> 클래스와 인스턴스 각각 올바른 메서드만 사용함

---

## 클래스와 인스턴스 간 이름 공간 

- 클래스를 정의하면, 클래스와 해당하는 이름 공간 생성
- 인스턴스를 만들면, 인스턴스 객체가 생성되고 **독립적인** 이름 공간 생성
- 인스턴스에서 특정 속성에 접근하면, 인스턴스 -> 클래스 순으로 탐색

> 같은 클래스로 만든 인스턴스라도 **서로 다른 이름 공간**을 가지므로, 인스턴스 간 변수 값이 영향을 주고 받지 않음
> 속성 접근 시에는 **인스턴스 -> 클래스** 순서로 탐색되니, 같은 이름의 속성이 중복될 경우 **인스턴스 값이 우선**됨

```python

class Person:
    name = "unknown"

    def talk(self):
        print(self.name)

p1 = Person()
p1.talk() # unknown

#p1은 인스턴스 변수가 정의되어 있지 않아 클래스 변수(unknown)가 출력됨

# p2 인스턴스 변수 설정 전/후

p2 = Person()
p2.talk() # unknown
p2.name = "Kim"
p2.talk() # Kim

#p2은 인스턴스 변수가 정의되어 인스턴스 변수(kim)가 출력됨

print(Person.name) # unknown
print(p1.name) # unknown
print(p2.name) # Kim

# 클래스 변수 name 값이 Kim으로 변경된 것이 아닌 p2 인스턴스의 인스턴스 변수 name이 Kim으로 저장됨

```

**독립적인 이름공간을 가지는 이점**

- 각 인스턴스는 독립적인 메모리 공간을 가지며, 클래스와 다른 인스턴스 간에는 서로의 데이터나 상태에 직접적인 접근이 불가능

- 객체 지향 프로그래밍의 중요한 특성 중 하나로, 클래스와 인스턴스를 모듈화하고 각각의 객체가 독립적으로 동작하도록 보장

- 이를 통해 클래스와 인스턴스는 다른 객체들과의 상호작용에서 서로 충돌이나 영향을 주지 않으면서 독립적으로 동작할 수 있음

- 코드의 가독성, 유지보수성, 재사용성을 높이는데 도움을 줌

---

## 매직 메서드

magic method: Double underscore('__')가 있는 메서드는 특수한 동작을 위해 만들어진 메서드

- 인스턴트 메서드
- 특정 상황에 자동으로 호출됨
- 스페셜 메서드 혹은 매직 메서드라 불림

ex. __str__(self), __len__(self)__, __lt__(self, other), __le__(self, other), __eq__(self, other), __gt__(self, other), __ge__(self, other), __ne__(self, other)

- __str__(self): 내장함수 print에 의해 호출되어 객체 출력을 문자열 표현으로 변경

```python

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return f"원의 반지름: {self.radius}"

c1 = Circle(10)
c2 = Circle(1)
print(c1) # 원의 반지름: 10
print(c2) # 원의 반지름: 1

```

> __str__을 정의하면 print(객체) 사용 시 의미 있는 문자열로 출력할 수 있음
> 객체의 정보를 사용자 친화적으로 보여주고 싶다면 사용

---

## 데코레이터

Decorator: 다른 함수의 코드를 유지한 채로 수정하거나 확장하기 위해 사용되는 함수

```python

# 데코레이터 정의
def my_decorator(func):
    def wrapper();
        # 함수 실행 전에 수행할 작업
        print("함수 실행 전")

        # 원본 함수 호출
        result = func()

        # 함수 실행 후에 수행할 작업
        print("함수 실행 후")
        return result

    return wrapper

# 데코레이터 사용
@my_decorator
def my_function():
    print("원본 함수 실행")

my_function()
"""
함수 실행 전
원본 함수 실행
함수 실행 후
"""

```
