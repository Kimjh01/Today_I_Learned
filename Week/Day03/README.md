# Day 3: Python Function

## 함수

Function :특정 작업을 수행하기 위한 **재사용 가능한 코드 묶음**

### 함수를 사용하는 이유
- 두 수의 합을 구하는 함수를 정의하고 사용함으로써 코드의 중복을 방지
- **재사용성**이 높아지고, 코드의 **가독성과 유지보수성** 향상 

```python
def get_sum(num1, num2): #함수를 정의
    return num1 + num2

num1 = 5
num2 = 3
sum_result = get_sum(num1, num2) #함수를 호출하여 결과 출력
print(sum_result)
```

### 함수 호출(function call)
- 함수를 실행하기 위해 함수의 이름을 사용하여 해당 함수의 코드 블록을 실행하는 것

---

## 함수 구조

```python 
def make_sum(pram1, pram2): # function 인자는 parameter
    """이것은 두 수를 받아 
    두 수의 합을 반환하는 함수입니다. 
    >>> make_sum(1, 2) 
    3
    """             # function 내부는 Docstring, Docstring + return = function body
    return pram1, pram2 # return value는 output 값
```

### 함수 정의와 호출
- 함수 정의(정의)
    - 함수 정의는 def 키워드로 시작
    - def 키워드 이후 함수 이름 작성
    - 괄호 안에 매개변수를 정의할 수 있음
    - 매개변수(parameter)는 함수에 전달되는 값

- 함수 body
    - 콜론(:) 다음에 들여쓰기 된 코드 블록
    - 함수가 실행 될 때 수행되는 코드를 저으이

- Docstring 
    - 함수 body 앞에 선택적으로 작성 가능한 함수 설명서

- 함수 반환 값
    - 함수는 필요한 경우 결과를 반환할 수 있음
    - return 키워드 이후에 반환할 값을 명시
    - return 문은 함수의 실행을 종료하고, 결과를 호출 부분으로 반환
    - 함수 내에서 return 문이 없다면 None이 반환
    
- 함수 호출
    - 함수를 사용하기 위해서 호출이 필요
    - 함수의 이름과 소괄호를 사용해 호출
    - 필요한 경우 인자(argument)를 전달해야 함
    - 호출 부분에서 전달된 인자는 함수 정의 시 작성한 매개변수에 대입
    
---

## 함수와 반환 값

print() 함수는 반환 값이 없음
- print() 함수는 화면에 값을 출력하기만 할 뿐 반환(return)값이 없음
- 파이썬에서 반환 값이 없는 함수는 기본적으로 None을 반환한다고 간주

```python
return_value = print(1)
print(return_value) # None

def my_func():
    print('hello')

result = my_func()
print(result) # None
```

---

## 매개변수와 인자

매개변수(parameter)
- 함수를 정의할 때, 함수가 받을 값을 나타내는 변수

인자(argument)
- 함수를 호출할 때, 실제로 전달되는 값

```python
def add_numbers(x, y):
    result = x + y
    return result 

a = 2, b = 3
sum_result = add_numbers(a, b)
print(sum_result)
```
---

## 다양한 인자 종류

Positional Arguments(위치 인자)
- 함수 호출 시 이자의 위치에 따라 전달되는 인자
- 위치 인자는 함수 호출 시 반드시 값을 전달해야 함

```python
def greet(name, age):
    print(f'안녕하세요, {name}님! {age}살이시군요.')

greet('Alice', 25) # 안녕하세요, Alice님! 25살이시군요.
greet('Alice') # TypeError: greet() missing 1 required positional argument: 'age'
```

Default Argument Value(기본 인자 값)
- 함수 정의에서 매개변수에 기본 값을 할당하는 것
- 함수 호출 시 인자를 전달하지 않으면, 기본값이 매개변수에 할당됨

```python
def greet(name, age = 30):
    print(f'안녕하세요, {name}님! {age}살이시군요.')

greet('Bob') # 안녕하세요, Bob님! 30살이시군요.
```

Keyword Arguments(키워드 인자)
- 함수 호출 시 인자의 이름과 함께 값을 전달하는 인자
- 매개변수와 인자를 일치시키지 않고, 특정 매개변수에 값을 할당할 수 있음
- 인자의 순서는 중요하지 않으며, 인자의 이름을 명시하여 전달
>> 단, 호출 시 키워드 인자는 위치 인자 뒤에 위치해야 함

```python
def greet(name, age):
    print(f'안녕하세요, {name}님! {age}살이시군요.')

greet(age = 35, name = 'Dave') # 안녕하세요, Dave님! 35살이시군요.
```

Arbitrary Argument Lists(임의의 인자 목록)
- 정해지지 않은 개수의 인자를 처리하는 인자 # 0개 이상을 처리 
- 함수 정의 시 매개변수 앞에 '*'를 붙여 사용
- 여러 개의 인자를 tuple로 처리 # Packing을 tuple(시퀀스, 변경 불가)로 

```python
def calculate_sum(*args):
    print(args) # (1, 100, 5000, 30)
    print(type(args)) # <class 'tuple'>

calculate_sum(1, 100, 5000, 30)
```

Arbitrary Keyword Argument Lists(임의의 키워드 인자 목록)
- 정해지지 않은 개수의 키워드 인자를 처리하는 인자 
- 함수 정의 시 매개변수 앞에 '**'를 붙여 사용
- 여러 개의 인자를 dictionary로 묶어 처리 #Packing을 dict로 

```python
def print_info(**kwargs):
    print(kwargs)
print_info(name='Eve', age=30) # {'name' : 'Eve', 'age' : 30}
```

함수 인자 권장 작성 순서
- 위치 -> 기본 -> 가변 -> 가변 키워드
- 호출 시 인자를 전달하는 과정에서 혼란을 줄일 수 있도록 함
>> 단, 모든 상황에 적용되는 절대적인 규칙은 아니며, 상황에 따라 유연하게 조정될 수 있음

```python
def func(pos1, pos2, default_arg='default', *args, **kwargs):
    ...
```

인자의 모든 종류를 적용한 예시 

```python 
def func(pos1, pos2, default_arg='default', *args, **kwargs):
    print('pos1:', pos1)
    print('pos2:', pos2)
    print('default_arg:', default_arg)
    print('args:', args)
    print('kwargs:', kwargs)

func(1, 2, 3, 4, 5, 6, key1='value1', key2='value2')

# 실행 결과 

"""
pos1: 1
pos2: 2
default_arg: 3
args: (4, 5, 6)
kwargs: {'key1': 'value1', 'key2': 'value2'}
"""
```

---

## 재귀 함수

함수 내부에서 자기 자신을 호출하는 함수

### 팩토리얼

n! -> n*(n-1)! -> n*(n-1)(n-2)! ...
- faxtorial 함수는 자기 자신을 재귀적으로 호출하여 입력된 숫자 n의 팩토리얼을 계산
- 재귀 호출은 n이 0이 될 때까지 반복되며, 종료 조건을 설정하여 재귀 호출이 멈추도록 함 
- 재귀 호출의 결과를 이용하여 문제를 작은 단위의 문제로 분할하고, 분할된 문제들의 결과를 조합하여 최종 결과를 도출

```python
def factorial(n):
    if n == 0:
        return 1
    else: 
        return n * factorial(n-1)

print(factorial(5)) # 120111
```

n! = n*(n-1)! -> n*(n-1)(n-2)* ... * 1
5! = 5*4*3*2*1 = 120

같은 문제를 다른 input을 통해서 해결

```python
def factorial(n):
    if n == 1:
        return 1
    else: 
        return n * factorial(n-1)

print(factorial(5)) # 120
```

재귀 함수 특징
- 특정 알고리즘 식을 표현할 때 변수의 사용이 줄어들며, 코드의 가독성이 높아짐 
- 1개 이상의 base case(종료되는 상황)가 존재하고, 수렴하도록 작성

재귀 함수 활용시 기억해야 할것
- 종료 조건을 명확히 할 것 
- 반복되는 호출이 종료 조건을 향하도록 할 것

>> 재귀 함수는 메모리 사용량이 많고 느릴 수 있음
>> 종료 조건이 잘못되면 **스택 오버플로우** 에러가 발생할 수 있음
>> 복잡한 재귀 함수는 코드의 가독성을 저하시킴

재귀 함수를 사용하는 이유
- 문제의 자연스러운 표현
    - 복잡하 문제를 간결하고 직관적으로 표현
- 코드의 간결성
    - 상황에 따라 반복문보다 알고리즘 코드가 더 간결하고 명확해질 수 있음
- 수학적 문제 해결
    - 수학적 정의가 재귀적으로 표현되는 경우, 직접적인 구현 가능

---

## 내장 함수

Bulit-in function: 파이썬이 기본적으로 제공하는 함수 **별도 import 없음**

- 내장 함수는 편리하지만, 다른 언어에서 다르게 동작 할 수 있음
- **내부 동작 원리**를 이해하면 문제 해결에 더 효과적으로 활용 성능 저하 문제를 피할 수 있음

```python
numbers = [1, 2, 3, 4, 5]
print(numbers) # [1, 2, 3, 4, 5]
print(len(numbers)) # 5
print(max(numbers)) # 5
print(min(numbers)) # 1
print(sum(numbers)) # 15
print(sorted(numbers, reverse=True)) # [5, 4, 3, 2, 1]
```

---

## 함수와 Scope

Python의 범위(Scope)
- 함수는 코드 내부에 local Scope를 생성하며, 그 외의 공간인 global scope로 구분

범위와 변수 관계
- scope
    - global scope: 코드 어디에서든 참조할 수 있는 공간
    - local scope: 함수가 만든 scope(함수 내부에서만 참조 가능)

- variable
    - global variable scope: global scope에 정의된 변수
    - local variable scope: local scope에 정의된 변수

scope 예시

num은 local scope에 존재하기 때문에 global scope에서 사용할 수 없음
- 이는 변수의 **수명주기**와 연관이 있음

```python
def func():
    num = 20 
    print('local', num) # local 20

func()

print('global', num) # NameError: name 'num' is not defined
```

변수 수명주기(liecycle)

변수의 수명주기는 변수가 선언되는 위치와 scope에 따라 결정됨

1. built-in scope
    - 파이썬이 실행된 이후부터 영원히 유지
2. global scope
    - 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지
3. local scope
    - 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지

이름 검색 규칙(Name Resolution)

파이썬에서 사요되는 이름(식별자)들은 특정한 이름공간(namespace)에 저장됨
- 아래 순서대로 이름을 찾아 나가며 LEGB Rule라 불림
    1. Local scope: 지역 범위(현재 작업 중인 범위)
    2. Enclosed scope: 지역 범위 한단계 위 범위
    3. Global scope: 최상단에 위치한 범위
    4. Built-in scope: 모든 것을 담고 있는 범위(정의하지 않고 사용하는 모든 것)

>> 함수 내에서는 바깥 Scope의 변수에 접근 가능하나 수정은 할 수 없음

LEGB Rule 예시 

sum이라는 이름을 global scope에서 사용함으로써, 기존 built-in scope에 있던 내장함수 sum을 사용하지 못하게 됨

>> sum을 참조 시 LEGB Rule에 따라 global에서 먼저 찾기 때문

```python
print(sum) # <built-in function sum>
print(sum(range(3))) # 3
sum = 5

print(sum) # 5
print(sum(range(3))) # TypeError: 'int' object is not callable
```

---

## global 키워드

변수의 스코프를 전역 범위로 지정하기 위해 사용
일반적으로 함수 내에서 전역 변수를 수정하려는 경우에 사용

```python
num = 0 # 전역 변수

def increment(): 
    global num # 전역 변수로 선언
    num += 1

print(num) # 0
increment()
print(num) # 1
```

global 키워드 선언 전에 참조 불가

```python
num = 0 

def increment(): 
    # SyntacError: name 'num' is used
    # prior to global declaration
    print(num)
    global num 
    num += 1
```

매개변수에는 global 키워드 사용 불가

```python
num = 0

def increment(num): 
    # "num" is assigned before global
    # declaration
    global num 
    num += 1
```

---

## 함수 스타일 가이드

### 함수 이름 작성 규칙

기본 규칙(Snake_names)
- 소문자와 언더스코어(_) 사용
- 동사로 시작하여 함수의 동작 설명
- 약어 사용 지양
```python
#Good
def calculate_total_price(price, tax):
    return price + (price * tax)

#Bad
def calc_price(p, t):
    return p + (p *t)
```

구성 요소
- 동사 + 명사: save_user()
- 동사 + 형용사 + 명사: calculate_total_price()
- get/set 접두사: get_username(), set_username()

>> 이름만으로 '무엇을 하는지' 명확히 표현
>> True / False를 반환한다면 시작을 is 또는 has 추천
>> 프로젝트 내에 일관성을 지키는 것이 가독성을 향상시킴

---

## 단일 책임 원칙

단일 책임 원칙(Single Responsibility Principle)
- 모든 객체는 하나의 명확한 목적과 책임만을 가져야 함

함수 설계 원칙
1. 명확한 목적
    - 함수는 한 가지 작업만 수행
    - 함수 이름으로 목적을 명확히 표현
2. 책임 분리
    - 데이터 검증, 처리, 저장 등을 별도 함수로 분리
    - 각 함수는 독립적으로 동작 가능하도록 설계
3. 유지보수성
    - 작은 단위의 함수로 나누어 관리
    - 코드 수정 시 영향 범위를 최소화 

**Bad** (책임이 섞임)
```python
def process_user_data(user_data):
    # 책임 1: 데이터 유효성 검사
    if len(user_data['password']) < 8:
        raise ValueError('비밀번호는 8자 이상이어야 합니다.')

    # 책임 2: 비밀번호 암호화 및 저장
    user_data['password'] = hash_password(user_data['password'])
    db.users.insert(user_data)

    # 책임 3: 이메일 발송
    send_email(user_data['email'], '가입을 환영합니다!')
```

**Good** (책임을 분리)
```python
def validate_password(password):
    # 데이터 유효성 검사
    if len(user_data['password']) < 8:
        raise ValueError('비밀번호는 8자 이상이어야 합니다.')

def save_user(user_data):
    # 비밀번호 암호화 및 저장
    user_data['password'] = hash_password(user_data['password'])
    db.users.insert(user_data)

def send_welcome_email(email):
    # 환영 이메일 발송
    send_email(email, '가입을 환영합니다!')

# 메인 함수에서 순차적으로 실행
def process_user_data(user_data):
    validate_password(user_data['password'])
    save_user(user_data)
    send_welcome_email(user_data['email'])
```

---

## Packing & Unpacking

### Packing

Packing: 여러 개의 데이터를 **하나의 컬렉션**으로 모아 담는 과정

기본원리
- 여러 개의 값을 하나의 튜플로 묶는 파이썬의 기본 동작
- 한 변수에 콤마(,)로 구분된 값을 넣으면 자동으로 튜플로 처리

```python
packed_values = 1, 2, 3, 4, 5
print(packed_values) # (1, 2, 3, 4, 5)
```

'*'을 활용한 패킹 (함수 매개변수 작성 시)
- 남는 위치 인자들을 튜플로 묶기 
- *를 붙인 매개변수가 남는 위치 인자들을 모두 모아 하나의 튜플로 만듦

```python
def my_func(*args):
    print(args) # (1, 2, 3, 4, 5)
    print(type(args)) # <class 'tuple'>

my_func(1, 2, 3, 4, 5)
```

'**'을 활용한 패킹 (함수 매개변수 작성 시)
- 남는 위치 인자들을 딕셔너리로 묶기 
- **를 붙인 매개변수가 남는 키워드 인자들을 모두 모아 하나의 딕셔너리로 만듦

```python
def my_func2(**kwargs):
    print(kwargs) # {'a' : 1, 'b' : 2, 'c' : 3}
    print(type(kwargs)) # <class 'dict'>

my_func2(a=1, b=2, c=3)
```
print 함수의 패킹 예시
- print 함수에서 임의의 가변 인자를 작성할 수 있었던 이유
>> 인자 개수에 상관 없이 튜플 하나로 패킹 되어서 내부에서 처리

```python
def my_func(*objects):
    print(objects) # (1, 2, 3, 4, 5)
    print(type(objects)) # <class 'tuple'>

my_func(1, 2, 3, 4, 5)
```
>> print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
- objects를 텍스트 스트림 file로 인쇄하는데, sep로 구분되고 end를 뒤에 붙임
- 있다면, sep, end, file 및 flush는 반드시 키워드 인자로 제공해야 함
- 모든 비 키워드 인자는 str()이 하듯이 문자열로 변환된 후 스트림에 쓰이는데, sep로 구분되고 end를 뒤에 붙임


### Unpacking

Unpacking: 컬렉션에 담겨있는 데이터들을 개별 요소로 펼쳐 놓은 과정

기본원리
- 튜플이나 리스트 등의 객체의 요소들을 개별 변수에 할당
- '시퀀스 언패킹(Sequence Unpacking)' 또는 '다중 할당(Multiple Assignment)'이라고 부름

```python
packed_values = 1, 2, 3, 4, 5 
# (1, 2, 3, 4, 5) 각 요소들이 
# a, b, c, d, e 변수에 순서대로 '언패킹' 되어 할당
a, b, c, d, e = packed_values
print(a, b, c, d, e) # 1, 2, 3, 4, 5
```

'*'을 활용한 패킹 (함수 인자 전달)
- 리스트나 튜플 앞에 *를 붙여 각 요소를 함수의 개별 위치 인자로 전달 

```python
def my_function(x, y, z):
    print(x, y, z)

names = ['alice', 'jane', 'peter']
my_function(*name) # alice jane peter
```

'**'을 활용한 언패킹 (딕셔너리 -> 함수 키워드 인자)
- 딕셔너리 앞에 **를 붙여 {키:값}쌍을 키 = 값 형태의 키워드 인자로 전달

```python
def my_function(x, y, z):
    print(x, y, z)

my_dict = {'x': 1, 'y': 2, 'z': 3}
my_function(**my_dict) # 1 2 3
```

### Packing & Unpacking, * & ** 정리

| 구분  | 상황 | * 연산자 | ** 연산자  |
| ----- | ---- | ------- | --------- |
| 패킹   | 함수 **정의**시| 여러 위치 인자를 하나의 튜플로 받음 | 여러 키워드 인자를 하나의 딕셔너리로 받음 |
| 언패킹 | 함수 **호출**시| 리스트/튜플을 개별 위치 인자로 전달 | 딕셔너리를 개별 키워드 인자로 전달 |

---

## 함수와 반환

함수의 return, 반환의 원칙
- 파이썬 함수는 언제나 단 하나의 값(객체)만 반환할 수 있음
- 여러 값을 반환하는 경우에도 하나의 튜플로 패킹하여 반환

```python
def get_user_info():
    name = 'Alice'
    age = 30
    return name, age #콤마(,)로 여러 값을 반환하는 것처럼 보임

user_data = get_user_info()
print(user_data) # ('Alice', 30) 단 하나의 튜플로 반환 
```

파이썬 함수의 반환 핵심
- 파이썬 함수는 오직 **하나의 값(객체)**만 return 할 수 있음
- return a, b, c 처럼 콤마를 사용하면, 파이썬 값들을 하나의 튜플로 자동 패킹하여 반환
- 반환된 튜플은 각 변수에 언패킹하여 사용할 수 있음

---

## 람다 표현식

Lambda expressions: 익명 함수를 만드는 데 사용되는 표현식, 한 줄로 간단한 함수로 정의

람다 표현식 구조
- lambda 키워드: 람다 함수를 선언하기 위해 사용되는 키워드
- 매개변수: 함수에 전달되는 매개변수들, 여러 개의 매개변수는 쉼표로 구분
- 표현식: 함수의 실행되는 코드 블록으로, 결과값을 반환하는 표현식으로 작성

람다 표현식 예시 
- 간단한 연산이나 함수를 만들 때, 함수를 매개변수로 전달할 때 유용

**Pre**
```python
def addition(x, y):
    return x + y 

def addition(x, y):
    return x + y 
result = addition(3, 5)
print(result) # 8
```

**Lambda**
```python
lambda x, y: x + y

addition = lambda x, y: x + y
result = addition(3, 5)
print(result) # 8
```

람다 표현식 활용(with map 함수)

```python
numbers = [1, 2, 3, 4, 5]
def square(x):
    return x**2

#Lambda 미사용
squared1 = list(map(square, numbers))
print(squared1)

#Lambda 사용
squared2 = list(map(lambda x: x**2, numbers))
print(squared2)
```