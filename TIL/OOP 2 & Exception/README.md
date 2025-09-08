# OOP 2 & Exception

## 상속

Inheritanc: 한 큰래스(부모)의 속성과 메서드를 다른 클래스(자식)가 물려받는 것

> 부모 클래스와 자식 클래스 간의 상하 관계가 형성되고, 위쪽에 있는 부모 클래스가 본인의 속성과 메서드를 아래쪽에 있는 자식에게 넘겨주는 것이 상속
> 속성과 메서드를 자식에게 넘겨주는 과정을 상속 과정

**상속이 필요한 이유**

1. 코드 재사용
- 상속을 통해 기존 클래스의 속성과 메서드를 재사용할 수 있음
- 기존 클래스를 수정하지 않고도 기능을 확장할 수 있음

2. 계층 구조
- 상속을 통해 클래스들 간의 계층 구조를 형성할 수 있음
- 부모 클래스와 자식 클래스 간의 관계를 표현하고, 더 구체적인 클래스를 만들 수 있음

3. 유지 보수의 용의성
- 상송을 통해 기존 클래스의 수정이 필요한 경우, 해달 클래스만 수정하면 되므로 유지 보수가 용이해짐
- 코드의 일관성을 유지하고, 수정이 필요한 범위를 최소화할 수 있음 

**상속 예시**

```python 

class Animal:
    def eat(self):
        print('먹는 중')

class Dog(Animal):
    def bark(self):
        print('멍멍')

my_dog = Dog()
my_dog.bark() # 멍멍

# 부모 클래스(Animal) 메서드 사용 가능
my_dog.eat() # 먹는 중

```

> 자식 클래스를 정의할 때 반드시 상송하려는 부모 클래스 이름을 함께 선언해야 함

---

## 클래스 상속

**상속 없이 구현하는 경우**

- 상속이 없이 구현하는 경우 학생/교수 정보를 별돌로 표현하기 어려움
- Person class만을 사용하는 경우 학생과 교수가 가지는 각각의 고유 속성을 표현하기 어려움. 나이와 이름만으로는 직업 정보를 나타낼 수 없음

```python 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def talk(self):
        print(f'반갑습니다. {self.name}입니다.')

s1 = Person('김학생', 23)
s1.talk() # 반갑습니다. 김학생입니다.

p1 = Person('박교수', 59)
p1.talk() # 반갑습니다. 박교수입니다.

```

- 상속 없이 구현하는 경우 교수/학생 클래스로 각각 선언하여 구현함
- 클래스를 각각 분리 했지만 메서드가 중복으로 정의될 수 있음

```python 
class Professor:
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

    def talk(self): #중복
        print(f'반갑습니다. {self.name}입니다.')

class Student:
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa

    def talk(self): #중복
        print(f'반갑습니다. {self.name}입니다.')
```

> 중복되고 있는 공통 속성인 name, age와 메서드 talk를 부모 클래스에서 한 번만 정의하고, 필요한 클래스들이 이 부모 클래스를 물려받아 사용할 수 있음


**상속을 사용한 계층 구조 변경**

```python 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def talk(self): # 메서드 재사용
        print(f'반갑습니다. {self.name}입니다.')

class Professor:
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

class Student:
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa

p1 = Professor('박교수', 49, '컴퓨터공학과')
s1 = Student('김학생', 20, 3.5)

# 부모 Person 클래스의 talk 메서드를 활용
p1.talk() # 반갑습니다. 박교수입니다.

# 부모 Person 클래스의 talk 메서드를 활용
s1.talk() # 반갑습니다. 김학생입니다.

```

---

## 메서드 오버라이딩

Method Overriding: 부모 클래스의 메서드를 같은 이름, 같은 파라미터 구조로 재정의하는 것

> 자식 클래스에서 메서드를 다시 정의하면, 부모 클래스의 메서드 대신 자식 클래스의 메서드가 실행됨
> 오버라이딩은 동일한 이름과 매개변수를 사용하지만, 내부 동작을 원하는 대로 바꿀 수 있게함
> 부모 클래스의 기능을 유지하면서도 일부 동작을 맞춤형으로 바꾸고 싶을 때 유용

- 오버라이딩: 덮어 씌운다, 재정의한다는 뜻으로 부모 클래스의 메서드 동작을 바꾸는 것 

**메서드 오버라이딩 예시**

- 자식 클래스가 부모 클래스의 메서드를 덮어써서 새로운 동작을 구현할 수 있음
- Animal class를 상속받은 Dog 클래스에서 eat 메서드를 다시 정의하는 것

```python 

class Animal:
    def eat(self):
        print('Animal이 먹는 중')

class Dog(Animal):
    # 부모 클래스(Animal)의 eat 메서드를 재정의(오버라이딩)
    def eat(self):
        print('Dog가 먹는 중')

my_dog = Dog()
my_dog.eat() # Dog가 먹는 중

```

**[참고] 오버로딩 (Overloading)**

- 같은 이름, 다른 파라미터를 가진 여러 메서드를 정의하는 것 (파이썬은 미지원)
- 파이썬은 실제로 하나의 메서드만 인식하며, 인자의 형태가 다르다는 이유로 메서드를 여러 개 구분하여 불러주지 않음

> 파이썬은 마지막으로 선언된 메서드만 인식함

```python 

class Example:
    def do_something(self, x):
        print('첫 번째 do_something 메서드:', x)

    def do_something(self, x, y):
        print('두 번째 do_something 메서드:', x, y)

example = Example()

# TypeError: do_something() missing 1 required positional argument: 'y'
example.do_something(10)

```

---

## 다중 상속

- 둘 이상의 상위 클래스로부터 여러 행동이나 특징을 상송받을 수 있음
- 상속받은 모든 클래스의 요소를 활용 가능
- 중복된 속성이나 메서드가 있는 경우 **상속 순서에 의해 결정**

```python 

class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self): 
        print f'안녕, {self.name}'

class Mom(Person):
    gene = 'XX'

    def swim(self):
        return '엄마가 수영'

class Dad(Person):
    gene = 'XY'

    def walk(self):
        return '아빠가 걷기'

class FirstChild(Dad, Mom):
    def swim(self):
        return '첫째가 수영'

    def cry(self):
        return '첫째가 응애'


baby1 = FirstChild('아가')
print(baby1.cry()) # 첫째가 응애
print(baby1.swim()) # 첫째가 수영
print(baby1.walk()) # 아빠가 걷기
print(baby1.gene) # XY

```

**다이아몬드 문제(The diamond problem)**

- 두 클래스 B와 C가 A에서 상속되고 클래스 D가 B와 C 모두에서 상속될 때 발생하는 모호함
- B와 C가 재정의한 메서드가 A에 있고 D가 이를 재정의하지 않은 경우라면?

> D는 B의 메서드 중 어떤 버전을 상속하는가? 아니면 C의 메서드 버전을 상속하는가?

**파이썬에서의 해결책**

- MRO(Method Resolution Order)알고리즘을 사용하여 클래스 목록을 생성
- 부모 클래스로부터 상속된 속성을 정해진 내부 알고리즘에 따라 검색
- 이 순서는 기본적으로 왼쪽에서 오른쪽으로 진행되며, 계층 구조에서 중복되는 클래스는 한 번만 확인 
- 속성이 D에서 발견되지 않으며, B에서 찾고, 거기에서도 발견되지 않으면, C에서 찾고, 이런식으로 진행 됨

```python 

class D(B,C)
    pass

```

Method Resolution Order: 파이썬이 메서드를 찾는 순서에 대한 규칙 메서드 결정 순서

> MRO는 다중 상속에서 어떤 부모 클래스의 메서드를 먼저 사용할지 순서를 정의
> 파이썬은 미리 정해진 MRO를 통해 다중 상속 환경에서도 예측 가능한 방식으로 메서드 탐색이 이루어질 수 있도록 함

---

## super() 메서드

super(): 메서드 해석 순서(MRO)에 따라, 현재 클래스의 부모(상위) 클래스의 메서드나 속성에 접근할 수 있게 해주는 내장 함수

> super()를 사용하면 직접 부모 클래스 이름을 적지 않아도 MRO에 따라 자동으로 올바른 메서드를 찾아 실행할 수 있음
> 다중 상속에서 super()를 호출하면 상속 순서에 맞춰 여러 부모 클래스의 메서드를 순차적으로 실행할 수 있음
> 생성자나 오버라이딩된 메서드에서 super()를 호출하면 부모 클래스의 초기화나 로직을 그대로 활용 가능

**super() 특징**

- 단순히 "부모 클래스의 메서드를 호출"하기 위한 용동 뿐만 아니라, 다중 상속(Multiple Inheritance)이 있을 때도 올바른 순서(MRO)에 따라 상위 클래스의 메서드를 찾아 실행하기 위해 super()를 사용

> 단일 상속 구조, 다중 상속 구조로 사용됨

**super() 사용 예시**

- 명시적으로 부모 클래스 이름을 적지 않아도 부모 메서드를 안전하게 호출할 수 있음
- Student의 생성자에서 super().__init__()를 호출하면, Person의 __init__() 메서드가 호출되어 name, age, number, email 속성을 초기화한 뒤 Student 고유의 student_id 속성을 추가
- 이때 Person 클래스를 직접 명시하지 않고 super()를 사용하므로, 나중에 클래스 이름이 바뀌거나 상속 구조가 변경되어도 super() 호출 부분을 그대로 사용할 수 있어 유지보수성이 향상 

```python 

# 사용 전

class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number =number
        self.email = email
        
class Student:
    def __init__(self, name, age, number, email, student_id):
        self.name = name
        self.age = age
        self.number =number
        self.email = email
        self.student_id = student_id

# 사용 후

class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number =number
        self.email = email
        
class Student:
    def __init__(self, name, age, number, email, student_id):\
        #super()를 통해 Person의 __init__ 메서드 호출
        super().__init__(self, name, age, number, email)
        self.student_id = student_id

```

**단일 상속 구조에서의 super 함수**

- "부모 클래스의 생성자(또는 메서드)를 호출하기 위해 사용" 
- 명시적으로 이름을 지정하지 않고 부모 클래스를 참조할 수 있으므로, 코드를 더 유지 관리하기 쉽게 만들수 있음
- 클래스 이름이 변경되거나 부모 클래스가 교체되어도 super()를 사용하면 코드 수정이 더 적게 필요

> 단일 상속에서는 super()를 사용해 부모 클래스를 직접 지정하지 않고 메서드를 호출
> 이렇게 하면 나중에 부모 클래스 이름이 바뀌거나 계층이 수정돼도 코드 유지 관리가 훨씬 수월해짐

**super() 사용 예시 (다중 상속)**

```python 

class ParentA:
    def __init__(self):
        self.value_a = 'ParentA'
    def show_value(self):
        print(f'Value from ParentA: {self.value_a}')
        
class ParentB:
    def __init__(self):
        self.value_b = 'ParentB'
    def show_value(self):
        print(f'Value from ParentB: {self.value_b}')

class Child(ParentA, ParentB):
    def __init__(self):
        super().__init__() # ParentA 클래스의 __init__ 메서드 호출
        self.value_c = 'Child'
    def show_value(self):
        super().show_value() # ParentA 클래스의 show_value 메서드 호출
        print(f'Value from Child: {self.value_c}')
    

# 출력 결과

child = Child()
child.show_value()

"""
Value from ParentA: ParentA
value from Child: Child 
"""
print(child.value_c) # Child
print(child.value_a) # ParentA

```

1. Child 클래스는 ParentA, ParentB를 순서대로 상속

2. child = Child()를 실행하면 Child의 init 메서드에서 super().__init()를 호출

3. MRO에 의해 Child -> ParentA -> ParentB 순으로 메서드를 찾는데, 이 상황에서 super().__init__()는 바로 다름 순서에 해당하는 ParentAdml init을 호출

4. ParentA의 init 이 실행되어 value_a가 초기화, ParentB의 init은 이 예제에서는 자동으로 호출되지 않음
    - 만약 ParentA의 init 안에서도 super().__init__()를 호출한다면, 그 다음으로 ParentB의 init이 실행되어 value_b도 초기화할 수 있음 이렇게 여러 부모 클래스의 초기화가 순서대로 이루어질 수 있음

```python 

class ParentA:
    def __init__(self):
        super().__init__()
        self.value_a = 'ParentA'
    print(child.value_b) # Parent B
    
```
5. child.show_value()를 호출하면 child의 show_value에서 super().show_value()를 호출

6. show_value() 메서드를 찾기 위해 Child -> ParentA -> ParentB 순서로 탐색하므로, 첫 번째로 ParentA의 show_value()가 실행됨 

**다중 상속 구조에서의 super 함수**

- MRO(메서드 해석 순서)에 따라 각 클래스의 메서드를 찾아가기 때문에, 단순히 직계 부모만이 아니라 다중 상속 관계에서도 적절한 상위 클래스의 메서드를 안전하게 호출할 수 있음

- 복잡한 상속 구조에서도 코드를 유연하고 깔끔하게 유지할 수 있음

**super() 정리**

- super()를 사용할 때는 MRO를 잘 이해하고 있어야 함

- ClassName.__mro__ 또는 ClassName.mro()를 확인해 MRO 순서를 파악한 뒤 적절히 활용하는 연습을 하면, 보다 복잡한 상속 구조에서도 코드를 잘 관리할 수 있음

**mro(), __mro__ 사용 예시**

```python 

class A:
    def __init__(self):
        print("A Constructor")

class B(A):
    def __init__(self):
        super().__init__()
        print("B Constructor")

class C(A):
    def __init__(self):
        super().__init__()
        print("C Constructor")

class D(B, C):
    def __init__(self):
        super().__init__()
        print("D Constructor")

# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
print(D.mro())

# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
print(D.__mro__)
    
```

**MRO가 필요한 이유**

- 부모 클래스들이 여러 번 액세스 되지 않도록, 각 클래스에서 지정된 왼쪽에서 오른쪽으로 가는 순서를 보존하고, 각 부모를 오직 한 번만 호출하고, 부모들의 우선순위에 영향을 주지 않으면서 서브 클래스를 만드는 단조적인 구조 형성

> 프로그래밍 언어에서 신뢰성 있고 확장성 있는 클래스를 설계할 수 있음
> 클래스 간의 메서드 호출 순서가 예측 가능하게 유지되며, 코드의 재사용성과 유지보수성이 향상됨

---

## 에러와 예외 

### 디버깅

Bug: 소프트웨어에서 발생하는 오류 또는 결함, 프로그램의 예상된 동작과 실제 동작 사이의 불일치

Debugging: 소프트웨어에서 발생하는 버그를 찾아내고 수정하는 과정, 프로그램의 오작동 원인을 식별하여 수정하는 작업

> 디버깅은 코드 실행 과정에서 변수 값이나 흐름을 점검하며 문제의 정확한 위치와 원인을 찾아내는 과정
> 효과적인 디버깅을 위해 단계별로 코드를 실행하거나 로그를 출력해 프로그램 상태를 확인

**디버깅 방법**

1. print 함수 활용
    - bisection으로 나눠서 생각 
2. 개발 환경(text editorm IDE)등에서 제공하는 기능 활용
    - breakpoint, 변수 조회 등
3. Python tutor 활용

4. 뇌 컴파일, 눈 디버깅 

---

## 에러 

Error: 프로그램 실행 중에 발생하는 예외 상황

> 프로그램을 실행할 때 예상치 못한 문제가 발생하면 오류
> 예를 들어, 존재하지 않는 파일을 읽으려 하거나 0으로 나누면 오류가 발생, 이러한 상황을 처리하지 않으면 프로그램 중단

- 문법 에러(Syntax Error): 프로그램의 구문이 올바르지 않은 경우 발생 (오타, 괄호 및 콜론 누락 등의 문법 오류)

- 예외(Exception): 프로그램 실행 중에 감지되는 에러

```python 

# Invalid syntax (문법 오류)
while # Syntax Error: invalid syntax 

# assign to literal (잘못된 할당)
5 = 3 # Syntax Error: cannot assign to literal here. Maybe you meant '==' instead of '='?

# Unterminated string literal
# 보통 문자열이나 문장을 제대로 닫지 않은 상태에서 줄 끝에 다다랐을 때 발생
print('hello 
# Syntax Error: unterminated string literal (detected at line 1)

```

> 문법 에러는 **코드 실행 이전**에 발생하므로, 에디터에서 제공하는 **밑줄, 색상, 자동완성** 등을 적극 활용해 미리 감지
> 특히 **괄호, 따옴표, 콜론 누락**은 가장 흔한 실수이므로 한 줄을 끝낼 때 항상 닫힘 여부를 점검하는 습관이 중요
---

## 예외 

Exception: 프로그램 실행 중에 감지되는 에러

> 프로그램이 잘못된 동작을 시도할 때 자동으로 감지됨
> 리스트에 없는 값을 꺼내려 하면 예외가 발생
> 이런 상황을 처리하지 않으면 프로그램은 즉시 종료

Built-in Exceptions: 예외 상황을 나타내는 예외 클래스들

> 내장 예외는 파이썬에서 이미 정의되어 있으며, 특정 예외 상황에 대한 처리를 위해 사용
> ZeroDivisionError는 0으로 나눌 때, FileNotFoundError는 없는 파일을 열 때 발생
> 이러한 예외를 사용하면 오류에 맞는 적절한 처리 방법을 적용할 수 있음

```python 
# ZeroDivisionError: 나누기 또는 모듈로 연산의 두 번째 인자가 0일 때 발생
10/0 # ZeroDivisionError: division by zero

# NameError: 지역 또는 전역 이름을 찾을 수 없을 때 발생
print(name1) # NameError: name 'name1' is not defined

# TypeError: 타입 불일치, 인자 누락, 인자 초과, 인자 타입 불일치
'2' + 2 # TypeError: can only concatenate str (not "int: to str)

sum() # TypeError: sum() takes at least 1 positional argument (0 givien)

sum(1, 2, 3) # TypeError: sum() takes at most 2 arguments (3 given)

import random
random.sample(1,2) # TypeError: Population must be a sequence. For dicts or sets, use sorted(d)

# ValueError: 연산이나 함수에 문제가 없지만 부적절한 값을 가진 인자를 받았고, 상황이 IndexError처럼 더 구체적인 예외로 설명되지 않는 경우 발생
int('1.5') # ValueError: invalid literal for int() with base 10: '1.5'
range(3).index(6) # ValueError: 6 is not in range
range

# IndexError: 시퀀스 인덱스가 범위를 벗어남
empty_list = []
empty_list = [2] # IndexError: list index out of range

# KeyError: 딕셔너리에 해당 키가 존재하지 않는 경우
person = {'name', 'Alice'}
person['age'] # KeyError: 'age'

# ImportError: import 하려는 이름을 찾을 수 없을 때
from random import hahaha # ImportError: cannot impoer name 'hahaha' from 'random'

# ModuleNotFoundError: 모듈을 찾을 수 없을 때
import hahaha # ModuleNotFoundError: No module named 'hahaha'

# KeyboardInterrupt: 사용자가 Control-c 또는 Delete를 누를 때 발생
while True:
    continue
'''
Traceback (most recent call last):
    File "...". Line 20, in <module>
        continue
KeyboardInterrupt
'''

# IndentationError: 잘못된 들여쓰기와 관련된 문법 오류
for i in range(10):
print(i) # IndentationError: expected an indented block after 'for' statement on line 19

```

---

## 예외 처리

Exception Handling: 예외가 발생했을 때 프로그램이 비정상적으로 종료되지 않고, 적절하게 처리할 수 있도록 하는 방법

> 예외 처리를 통해 오류가 발생해도 프로그램의 흐름을 안전하게 이어갈 수 있음
> Python에서는 try, except 구문을 사용해 특정 예외를 잡아내고 원하는 동작을 수행
> 예외 처리를 구현하면 프로그램 사용자에게 오류 메시지를 보여주거나 대체 로직을 실행할 수 있음 

**예외처리 사용 구문**

- try: 예외가 발생할 수 있는 코드 작성
- except: 예외가 발생했을 때 실행할 코드 작성
- else: 예외가 발생하지 않았을 때 실행할 코드 작성
- finally: 예외 발생 여부와 상관없이 항상 실행할 코드 작성 

```python 

try:
    x = int(input('숫자를 입력하세요:'))
    y = 10 / x
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except ValueError:
    print('유효한 숫자가 아닙니다.')
else:
    print(f'결과: {y}')
finally:
    print('프로그램이 종료되었습니다.')

```

---

## try & except

try & except 구조

```python 
try:
    # 예외가 발생할 수 있는 코드

except:
    # 예외 처리 코드

```

> try 블록 안에는 예외가 발생할 수 있는 코드를 작성
> except 블록 안에는 예외가 발생했을 때 처리할 코드를 작성
> 예외가 발생하면 프로그램 흐름은 try 블록을 빠져나와 해당 예외에 대응하는 except 블록으로 이동

```python 
try:
    result = 10 / 0

except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')

try:
    num = int(input('숫자입력 : '))
except ValueError:
    print('숫자가 아닙니다.')

"""
숫자입력 :  a
숫자가 아닙니다.
"""

```

---

## 복수 예외 처리

**예외 처리 연습**

- 100을 사용자가 입력한 값으로 나누고 출력하는 코드
    - 먼저, 발생한 에러가 무엇인지 예상해보기

```python 

num = int(input('100으로 나눌 값을 입력하시오 : '))
print(100 / num) 
# 문자 a를 입력했을 때 문자열을 int로 형변환 -> ValueError
# 숫자 0을 입력했을 때 0으로 나눔 -> ZeroDivisionError

# 1
try:
    num = int(input('100으로 나눌 값을 입력하시오 : '))
    print(100 / num) 

except(ValueError, ZeroDivisionError):
    print('제대로 입력해주세요')

# 2
try:
    num = int(input('100으로 나눌 값을 입력하시오 : '))
    print(100 / num) 

except ValueError:
    print('숫자를 넣어주세요.')

except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')

except:
    print('에러가 발생하였습니다.')

```

---

## else & finally

- else 블록은 예외가 발생하지 않았을 때 추가 작업을 진행

- finally 블록은 예외 발생 여부와 상관없이 항상 실행할 코드를 작성

```python 

try:
    x = int(input('숫자를 입력하세요: '))
    y = 10 / x

except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')

except ValueError:
    print('유효한 숫자가 아닙니다.')

else:
    print(f'결과: {y}')

finally:
    print('프로그램이 종료되었습니다')

```

---

## 예외 처리 주의사항

- except Exception이 모든 예외를 먼저 가로채기 때문에 이후 코드는 절대 실행되지 않음
- 내장 예외 클래스는 상속 계층구조를 가지기 때문
- 항상 범용적인 예외 처리(Exception)는 마지막에 두어야 함 

```python 

try:
    num = int(input('100으로 나눌 값을 입력하시오 : '))
    print(100 / num) 

except Exception:
    print('숫자를 넣어주세요.')

# 밑에 코드로 도달을 못함
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')

except:
    print('에러가 발생하였습니다.')

# 개선

try:
    num = int(input('100으로 나눌 값을 입력하시오 : '))
    print(100 / num) 

# 구체적인 예외부터
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')

except ValueError:
    print('숫자를 넣어주세요.')

# 마지막에 광범위한 예외(Exception)
except Exception:
    print('에러가 발생하였습니다.')

```

---

## 예외 객체 다루기 

as 키워드
- 예외객체: 예외가 발생했을 때 예외에 대한 정보를 담고 있는 객체
- except 블록에서 예외 객체를 받아 상세한 예외 정보를 활용 가능

```python 

my_list = []
try:
    number = my_list[1] 

except IndecError as error:
    print(f'{error}가 발생했습니다.')

# list index put of range가 발생했습니다.

```

> 빈 리스트에서 잘못된 인덱스를 참조할 때 IndexError 예외가 발생하는 예시
> error 변수에 담긴 예외 메세지를 출력하면 구체적인 오류 내용을 쉽게 확인할 수 있음

try-except와 if-else
- try-except와 if-else를 함께 사용할 수 있음

```python 

try:
    x = int(input('숫자를 입력하세요: '))
    if x < 0:
    print('음수는 허용되지 않습니다'.)
    else: 
        print('입력한 숫자:', x)
except ValueError:
    print('유효 발생')

```

---

## EAFP & LBYL

EAFP("Easier to Ask for Forgiveness than Permission")
- 예외처리를 중심으로 코드를 작성하는 접근 방식 # try-except

LBYL("Look Before You Leap")
- 값 검사를 중심으로 코드를 작성하는 접근 방식 # if-else

```python 

# EAFP

try:
    result = my_dict['key']
    print(result)
except KeyError:
    print('Key가 존재하지 않습니다.')

# LBYL

if 'key' in my_dict:
    result = my_dict['key']
    print(result)
else:
    print('Key가 존재하지 않습니다.')
    
```

|        **EAFP**           |         **LBYL**          |
| ------------------------  | ------------------------- |
| "일단 실행하고 예외를 처리" | "실행하기 전에 조건을 검사" |
| 코드를 실행하고 예외가 발생하면 예외처리를 수행 | 코드 실행 전에 조건문 등을 사용하여 예외 상황을 미리 검사하고, 예외 상항을 피하는 방식 |
| 코드에서 예외가 발생할 수 있는 부분을 미리 예측하여 대비하는 것이 아니라, 예외가 발생한 후에 예외를 처리 | 코드가 좀 더 예측 가능한 동작을 하지만, 코드가 더 길고 복잡해질 수 있음 |
| 예외 상황을 예측하기 어려운 경우에 유용 | 예외 상황을 미리 방지하고 싶을 때 유용 |

---
