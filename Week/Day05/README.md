# Day 5: Data Structure 1

## Data Structure

데이터 구조 : 여러 데이터를 효과적으로 사용 관리하기 위한 구조 **(str, list, dict)**

### 자료구조 

- 각 데이터의 **효율적인 저장, 관리**를 위한 구조를 나눠 놓은 것
- 단순히 데이터를 묶는 것을 넘어, **프로그램의 성능과 효율성, 유지보수성**에 큰 영향을 미치는 핵심적인 개념

### 메서드

- 문자열, 리스트, 딕셔너리 등 각 **데이터 구조**의 **메서드**를 호출하여 다양한 **기능**을 활용하기

> 문자열, 리스트, 딕셔너리 등 파이썬의 다양한 데이터 구조는 저마다 고유한 메서드를 가짐
> 메서드들은 해당 데이터 구조의 데이터를 효율적으로 조작하거나 특정 기능을 수행하기 위해 제공

---

## Method

메서드: **객체에 속한 함수**, 프로그래밍에서 **객체(object)**가 특정 작업을 수행하도록 정의된 함수

- 메서드는 클래스(class) 내부에 정의되는 함수 
- 클래스는 파이썬에서 '타입을 표현하는 방법'이며 이미 은연중에 사용
- help 함수를 통해 str을 호출해보면 class 였다는 것을 알 수 있음

> 메서드는 어딘가(class)에 속해 있는 **함수**이며, 각 테이터 타입별로 다양한 **기능**을 가진 메서드가 존재

### Method 호출 방법

```python 
# 데이터 타입 객체.메서드()

'hello'.capitalize()
```
> 우리가 만든 객체(데이터)에게 원하는 명령(메서드)을 내리는 방법

```python 
# 문자열 메서드 예시
print('hello'.capotalize()) # Hello

# 리스트 메서드 예시
numbers = [1, 2, 3]
numbers.append(4)

print(numbers) # [1, 2, 3, 4]
 ```

---

## 시퀀스 데이터 구조

### 문자열

**문자열 조회 / 탐색 및 검증 메서드**

| 메서드              | 설명                   |
| ---------- | -------------------- |
| s.find(x)  | x의 첫 번째 위치를 반환. 없으면, -1을 반환 |
| s.index(x)  | x의 첫 번째 위치를 반환. 없으면, 오류 발생 |
| s.isupper(x)  | 문자열 내의 모든 문자가 대문자인지 확인    |
| s.islower(x)  | 문자열 내의 모든 문자가 소문자인지 확인 |
| s.isalpha(x)  | 문자열 내의 모든 문자가 알파벳 인지 확인, *단순 알파벳이 아닌 유니코드 상 Letter (한국어도 포함) |

.find(x):  x의 첫 번째 위치를 반환. 없으면, -1을 반환

```python 

print('banana'.find('a')) # 1

print('banana'.find('z')) # -1

```
s.index(x): x의 첫 번째 위치를 반환. 없으면, 오류 발생

```python 

print('banana'.index('a')) # 1

print('banana'.index('z')) # ValueError : substring not found

```

s.isupper(x), s.islower(x):  문자열 내의 모든 문자가 대문자/소문자인지 확인

```python 

string1 = 'HELLO'
string2 = 'Hello'
print(string1.isupper()) # True
print(string2.isupper()) # False
print(string1.islower()) # False
print(string2.islower()) # False

```

s.isalpha(x): 문자열 내의 모든 문자가 알파벳 인지 확인

```python 

string1 = 'Hello'
string2 = '123heis98576ssh'
print(string1.isalpha()) # True
print(string2.isalpha()) # False

```

**문자열 조작 메서드(새로운 문자열 반환)

| 메서드              | 설명                   |
| ---------- | -------------------- |
| s.replace(old, new[, count]) | 바꿀 대상 글자를 새로운 글자로 바꿔서 반환 |
| s.strip([chars])  | 공백이나 특정 문자를 제거 |
| s.split(sep=None, maxsplit = -1) | sep를 구분자 문자열로 사용하여 문자열에 있는 단어들의 리스트를 반환  |
| 'separator'.join(iterable)  | 구분자로 iterable의 문자열을 연결한 문자열을 반환 |
| s.capitalize() | 가장 첫 번째 글자를 대문자로 변경 |
| s.title() | 문자열 내 띄어쓰기 기준으로 각 단어의 첫 글자는 대문자로, 나머지는 소문자로 변환 |
| s.upper() | 모두 대문자로 변경 |
| s.lower() | 모두 소문자로 변경 |
| s.swapcase() | 대 <-> 소문자 서로 변경 |


s.replace(old, new[, count]): 바꿀 대상 글자를 새로운 글자로 바꿔서 반환


```python 

text = 'Hello, world! world world'
new_text1 = text.replace('world', 'Python')
new_text2 = text.replace('world', 'Python', 1)
print(new_text1) # Hello, Python! Python Python
print(new_text2) # Hello, Python! world world

```

s.strip([chars]): 문자열의 시작과 끝에 있는 공백이나 특정 문자를 제거


```python 

text = '   Hello, world!   '
new_text = text.strip()
print(new_text) # 'Hello, world!'

```

s.split(sep=None, maxsplit = -1): sep를 구분자 문자열로 사용하여 문자열에 있는 단어들의 리스트를 반환


```python 

text = 'Hello, world!'
words1 = test.split(',')
words2 = test.split()
print(words1) # ['Hello', ' world!']
print(words2) # ['Hello',', 'world!']

```

'separator'.join(iterable): 구분자로 iterable의 문자열을 연결한 문자열을 반환

```python 

word = ['Hello', 'world!']
text = '-'.join(words)
print(text) # 'Hello-world!'

```

**문자열 조작 메서드**

```python 

text = 'heLLo, woRld!'
new_text1 = text.capitalize()
new_text2 = text.title()
new_text3 = text.upper()
new_text4 = text.lower()
new_text5 = text.swapcase()
print(new_text1) # 'Hello, world!'
print(new_text2) # 'Hello, World!'
print(new_text3) # 'HELLO, WORLD!'
print(new_text4) # 'hello, world!'
print(new_text5) # 'HEllO, WOrLD!'

```

## 리스트 

**리스트 값 추가 및 삭제 메서드**

| 메서드              | 설명                   |
| ---------- | -------------------- |
| L.append(x) | 리스트 마지막에 항목 x를 추가 |
| L.extend(m) | Iterable m의 모든 항목들을 리스트 끝에 추가(+=과 같은 기능) |
| L.insert(i, x) | 리스트 인덱스 i에 항목 x를 삽입 |
| L.remove(x) | 리스트 가장 왼쪽에 있는 항목(첫 번째) x를 제거, 항모기 존재하지 않을 경우, ValueError |
| L.pop() | 리스트 가장 오른쪽에 있는 항목(마지막)을 반환 후 제거 |
| L.pop(i) | 리스트의 인덱스 i에 있는 항목을 반환 후 제거 |
| L.clear() | 리스트의 모든 항목 제거 |


L.append(x): 리스트 마지막에 항목 x를 추가 


```python

my_list = [1, 2, 3]
my_list.append(4)
print(my_list) # [1, 2, 3, 4]

```

L.extend(m): Iterable m의 모든 항목들을 리스트 끝에 추가(+=과 같은 기능) 


```python

my_list = [1, 2, 3]
my_list.extend([4, 5, 6])
print(my_list) # [1, 2, 3, 4, 5, 6]

```

**주의 사항**

```python

#append()와 비교
my_list = [1, 2, 3]
my_list.append([4, 5, 6])
print(my_list) # [1, 2, 3, [4, 5, 6]]

# 반복 가능한 객체가 아니면 추가 불가
my_list.extend(100) # TypeError: 'int' object is not iterable

```

L.insert(i, x): 리스트 인덱스 i에 항목 x를 삽입 


```python

my_list = [1, 2, 3]
my_list.insert(1, 5)
print(my_list) # [1, 5, 2, 3]

```

L.remove(x): 리스트 가장 왼쪽에 있는 항목(첫 번째) x를 제거, 항모기 존재하지 않을 경우, ValueError 


```python

my_list = [1, 2, 3, 2, 2, 2]
my_list.remove(2)
print(my_list) # [1, 3, 2, 2, 2]

```


L.pop(i): 리스트의 인덱스 i에 있는 항목을 반환 후 제거, 작성하지 않을 경우 마지막 항목을 제거


```python

my_list = [1, 2, 3, 4, 5]
item1 = my_list.pop()
item2 = my_list.pop(0)
print(item1) # 5
print(item2) # 1
print(my_list) #  [2, 3, 4]

```

L.clear(): 리스트의 모든 항목 제거 

```python

my_list = [1, 2, 3]
my_list.clear()
print(my_list) #  []

```

**리스트 탐색 및 정렬 메서드**

| 문법        | 설명                 |
| ---------- | -------------------- |
| L.index(x) | 리스트 첫 번째로 일치하는 항목 x의 인덱스를 반환 |
| L.count(x) | 리스트에서 항목 x의 개수를 반환 |
| L.reverse() | 리스트의 순서를 역순으로 변경 (정렬 x) |
| L.sort() | 리스트를 정렬 (매개변수 이용가능) |

L.index(x): 리스트 첫 번째로 일치하는 항목 x의 인덱스를 반환 


```python

my_list = [1, 2, 3]
index = my_list.index(2)
print(index) # 1

```

L.count(x): 리스트에서 항목 x의 개수를 반환 


```python

my_list = [1, 2, 2, 3, 3, 3]
count = my_list.count(3)
print(count) # 3

```

L.reverse(): 리스트의 순서를 역순으로 변경 (정렬 x) 


```python

my_list = [1, 3, 2, 8, 1, 9]
index = my_list.reverse()
print(my_list.reverse()) # None
print(index) # [9, 1, 8, 2, 3, 1]

```

L.sort(): 리스트를 정렬 (매개변수 이용가능) 


```python

my_list = [3, 2, 100, 1]
my_list.sort()
print(index) # [1, 2, 3, 100]

# 내림차순 정렬
my_list.sort(reverse=True)
print(my_list) # [100, 3, 2, 1]

```

---

## 복사

### 객체와 참조

**가변 / 불변 객체의 개념**

객체 복사의 핵심을 파악하려면, 파이썬 자료구조의 가변과 불변 두 가지 종류를 봐야 함

- Mutable(가변) 객체
    - 생성 후 내용을 변경할 수 있는 객체 # ex: list(리스트), dict(딕셔너리), set(집합)

- Immutable(불변) 객체
    - 생성 후 내용을 변경할 수 없는 객체 # ex: int(정수), float(실수), str(문자열), tuple(튜플)

**변수 할당의 의미**

파이썬에서 변수 할당은 객체에 대한 참조를 생성하는 과정 
- 변수는 객체의 메모리 주소를 가리키는 Label 역할을 함
- '=' 연산자를 사용하여 변수에 값을 할당 
    - 할당 시 **새로운 객체**가 새성되거나 **기존 객체에 대한 참조**가 생성

새로운 객체 생성 후 참조 
> 할당되는 값이 새로운 객체일 경우, 파이썬은 먼저 해당 객체를 메모리에 만들고, 변수가 그 객체를 가리키도록 함

기존 객체에 대한 참조
> 이미 메모리에 존재하는 객체를 변수에 할당하면, 새로운 객체를 만들지 않고 해당 객체에 대한 참조만 생성 

서로 다른 모듈에서 import된 변수나 함수의 이름이 같은 경우 이름 충돌 발생
    - 마지막 import 된 것이 이전 것을 덮어쓰기 때문에, 나중에 import된 것만 유효함


Mutable(가변) 객체: 생성 후 내용을 변경할 수 있는 객체


```python

a = [1, 2, 3, 4]
b = a
b[0] = 100

print(a) # [100, 2, 3, 4]
print(b) # [100, 2, 3, 4]
print(a is b) # True

```

Immutable(불변) 객체: 생성 후 내용을 변경할 수 없는 객체


```python

a = 20
b = a
b = 10

print(a) # 20
print(b) # 10
print(a is b) # False

```

**id() 함수를 사용한 메모리 주소 확인**

- id() 함수를 사용하여 객체의 메모리 주소를 확인 가능
- is 연산자를 통해 두 변수가 같은 객체를 참조하는지 확인 가능 


```python

x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(f'x의 id: {id(x)}') 
print(f'y의 id: {id(y)}') 
print(f'z의 id: {id(z)}') 

print(f'x와 y는 같은 객체인가? {x is y}') 
print(f'x와 z는 같은 객체인가? {x is z}') 

# 결과 
x의 id: 1682231207424
y의 id: 1682231207424
z의 id: 1682231224896

x와 y는 같은 객체인가 ? True
x와 z는 같은 객체인가 ? False

```

**가변 / 불변 메모리 관리 방식**

가변 객체
    - 생성 후에도 그 내용을 수정할 수 있음
    - 객체의 내용이 변경되어도 같은 메모리 주소를 유지

불변 객체
    - 생성 후 그 값을 변경할 수 없음
    - 새로운 값을 할당하면 새로운 객체가 생성되고, 변수는 새 객체를 참조하게 됨

**가변 / 불변 메모리 관리 방식의 이유**

성능 최적화 
    - 불변 객체: 변경이 불가능하므로, 여러 변수가 동일한 객체를 안정하게 공유할 수 있음
    - 가변 객체: 내용 수정이 빈번할 때, 새로운 객체를 생성하는 대신 기존 객체를 직접 수정할 수 있음, 이로 인해 객체 생성 및 삭제에 드는 비용을 절감하여 성능을 향상시킴

메모리 효율성
    - 불변 객체: 동일한 값을 가진 여러 변수가 같은 객체를 참조할 수 있어 메모리 사용을 최소화할 수 있음
    - 가변 객체: 크기가 큰 데이터를 효율적으로 수정할 수 있음
    
---

### 얕은 복사

Shallow Copy: 객체의 최상위 요소만 새로운 메모리에 복사하는 방법, 내부에 중첩된 객체가 있다면 그 객체의 참조만 복사됨

> 얕은 복사의 함정, **가변 객체**
> 얕은 복사 후 **중첩된 리스트**나 딕셔너리 같은 **가변 객체**를 수정하면, 원본 객체와 복사본 객체가 함께 변경됨
> 이는 복사본의 중첩 객체가 여전히 원복 객체의 **중첩 객체를 참조**하고 있기 때문

**얕은 복사 예시**

1차원 리스트에서의 얕은 복사: list()함수

```python
a = [1, 2, 3]
d = list(a) # list() 함수를 사용하여 a의 얕은 복사본 생성

# 원본 리스트 a의 첫 번째 요소 변경
a[0] = 100

print(a) = [100, 2, 3]
print(d) = [1, 2, 3]
```

**얕은 복사의 한계**

2차원 리스트와 같이 변경 가능한 객체 안에 변경 가능한 객체가 있는 경우

```python
a = [1, 2, [3, 4, 5]]
b = a[:]

b[0] = 999
print(a) # [1, 2, [3, 4, 5]]
print(b) # [999, 2, [3, 4, 5]]

b[2][1] = 100
print(a) # [1, 2, [3, 100, 5]]
print(b) # [999, 2, [3, 100, 5]]

print(f'a[2]와 b[2]가 같은 객체인가? {a[2] is b[2]}') # True

```

> a와 b의 주소는 다르지만 내부 객체의 주소는 같기 때문에 함께 변경


**1차원 리스트와 다차원 리스트에서의 차이점**

1차원 리스트 
    - 얓은 복사로 충분히 독립적인 복사본을 만들 수 있음

다차원 리스트
    - 최상위 리스트만 복사되고, 내부 리스트는 여전히 원본과 같은 객체를 참조

---

### 깊은 복사

Deep Copy: 객체의 모든 수준의 요소를 새로운 메모리에 복사하는 방법, **중첩된 객체까지** 모두 새로운 객체로 생성

> 완전한 독립성 보장
> 깊은 복사는 원본 객체와 복사본이 **완전히 독립적임**을 보장
> 복사본의 어떤 수준에 있는 중첩된 내용을 변경하더라도 **원본 객체**에는 **절대 영향을 주지 않음**

**깊은 복사**

copy 모듈에서 제공하는 deepcopy() 함수를 사용

```python
import copy

new_object = copy.deepcopy(original_object)

```

**깊은 복사 예시**


```python
import copy

a = [1, 2, [3, 4, 5]]
b = copy.deepcopy(a)

b[2][1] = 100
print(a) # [1, 2, [3, 4, 5]]
print(b) # [999, 2, [3, 100, 5]]
print(f'a[2]와 b[2]가 같은 객체인가? {a[2] is b[2]}') # False

```

- 중첩된 객체에서의 깊은 복사 

```python
import copy 

original = {'a': [1, 2, 3], 'b': {'c': 4, 'd': [5, 6]}}
copied = copy.deepcopy(original)

print(f'원본: {original}')
print(f'복사본: {copied}')
print(f"original['b']와 copied['b']가 같은 객체인가? {original['b'] is copied['b']}") # False

```

--- 

## List Comprehension 

List Comprehension: 간결하고 효율적인 리스트 생성 방법

> "Pythonic"한 코드 
> 파이썬 개발자들이 선호하는 스타일로, 코드를 더 **"파이썬답게"** 작성하는 방법 중 하나

```python
[expression for 변수 in iterable]
list(expression for 변수 in iterable)

[expression for 변수 in iterable if 조건식]
list(expression for 변수 in iterable if 조건식)

```

**표현식 for 변수 in 순회 가능한 객체 if 조건** # if 조건식 부분은 선택 사항

> 표현식은 결과 리스트에 추가될 값, 변수는 순회 중인 현재 요소, 순회 가능한 객체는 반복할 데이터, 조건식은 필터링 조건
> if 조건식 부분은 선택 사항이며, 조건을 명시하지 않으면 모든 요소에 대해 표현식이 적용

**List Comprehension structure**

```python

# 사용 전 
numbers = [1, 2, 3, 4, 5]
squared_numbers = []
for num in numbers:
    sqaured_numbers.append(num**2)
print(squared_numbers) # [1, 4, 9, 16, 25]

# 사용 후 
numbers = [1, 2, 3, 4, 5]
squared_numbers = [num**2 for num in numbers]
print(squared_numbers) # [1, 4, 9, 16, 25]

```

**List Comprehension 활용 예시**

```python

# 2차원 배열 생성시(인접행렬 생성)

data1 = [[0]*5 for _ in range(5)]

# 또는

data2 = [[0 for _ in range(5)] for _ in range(5)]

# 결과
[[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0]]

```

> Comprehension 너무 남용하면 안됨

---

## 메서드 체이닝

Method Chaining: 여러 메서드를 연속해서 호출하는 방식

**문자열에서의 메서드 체이닝 예시**

코드 순서
1. text.swapcase(): 대소문자를 반전시킴
    - 'heLLO, woRld!' -> 'HEllO. WOrLD!'

2. replace('l', 'z'): 소문자 'ㅣ'을 'z'로 교체
    - 'HEllO. WOrLD!' -> 'HEzzO, WOrLD!'

```python

# 단계별로 실행
text = 'heLLO, woRld!'
step1 = text.swapcase()
print('1단계 결과:', step1) # HEllO. WOrLD!

srep2 = step1.replace('l', 'z')
print('2단계 결과:', step2) # HEzzO, WOrLD!

# 위와 동일한 결과
new_text = text.swapcase().replace('l', 'z')
print(new_text) # HEzzO, WOrLD!

```

**리스트에서의 메서드 체이닝 예시**

copy()로 리스트를 복사한 후, sorted() 함수로 정렬

```python
numbers = [3, 1, 4, 1, 5, 9, 2]
result = numbers.copy().sort()
print(numbers) # [3, 1, 4, 1, 5, 9, 2] (원본은 변경되지 않음)
print(result) # None (sort() 메서드는 None을 반환하기 때문)

# 올바른 체이닝 예시
sorted_numbers = sorted(numbers.copy())
print(sorted_numbers) # [1, 1, 2, 3, 4, 5, 9]

```

**메서드 체이닝 주의사항** 

- 모든 메서드가 체이닝을 지원하는 것은 아님
    - 메서드가 객체를 반환할 때 체이닝이 가능

- None을 반환하는 메서드는 메서드 체이닝이 불가능
    - ex. 리스트의 append(), sort()

> 메서드 체이닝을 사용할 때는 각 메서드의 반환 값을 잘 이해하고 있어야 함

---

## 문자 유형 판별 메서드

문자들의 유형을 판단하는 메서드

isdecimal(): 문자열이 모두 숫자 문자(0~9)로만 이루어져 있어야 True

isdigit(): isdecimal()과 비슷하지만, 유니코드 숫자도 인식('(1)'도 숫자로 인식)

isnumeric(): isdigit()과 유사하지만, 몇가지 추가적인 유니코드 문자를 인식(분수, 지수, 루트 기호도 숫자로 인식)

---