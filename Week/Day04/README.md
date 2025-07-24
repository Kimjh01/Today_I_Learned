# Day 4: Python Module & Control of Flow

## 모듈

Module : **한 파일로 묶인 변수와 함수의 모음** 특정한 기능을 하는 코드가 작성된 파이썬 파일(.py)
> 생산성 증가를 위해 다른 프로그래머들이 작성한 **검증된 코드** 사용
> **만들어 둔 변수나 함수들의 모음**을 "모듈"

### 모듈 예시

Math 내장 모듈
- 파이썬이 미지 작성한 수학 관련 변수와 함수가 작성된 모듈

```python
import math
print(math.pi) # 3.14159265358979
print(math.sqrt(4)) # 2.0
```

---

### 모듈 활용 

**Import문 사용**

같은 이름의 함수가 여러 모듈에 있을 때 충돌을 방지할 수 있음
    - '.(dot)': 연산자를 사용하여 점의 왼쪽 객체에서 점의 오른쪽 이름을 찾아라 의미

```python
import math
print(math.pi) # 모듈명. 변수명
print(math.sqrt(4)) # 모듈명. 함수명
```
> 자칫 코드가 길어질 수 있음

**form절 사용**

코드가 짧고 간결해짐 

```python
from math import pi, sqrt

print(pi)
print(sqrt(4))

from math import sqrt
math_result = sqrt(16)

def sqrtx(x):
    return str(x ** 0.5)
my_result = sqrt(16)
```

> 정의된 모듈의 위치를 알기 어려워 명시적이지 않을 수 있음
> 사용자가 선언한 변수 또는 함수와 겹치게 되어 모듈에서 정의한 값이나 동작이 이뤄지지 않을 수 있음

**form문 사용 시 주의사항**

서로 다른 모듈에서 import된 변수나 함수의 이름이 같은 경우 이름 충돌 발생
    - 마지막 import 된 것이 이전 것을 덮어쓰기 때문에, 나중에 import된 것만 유효함

```python
from math import sqrt # math.sqrt가 먼지 import
from my_math import sqrt # my_math.sqrt가 math.sqrt를 덮어씀

result = sqrt(9) # my_math.sqrt 사용
```

- 모든 요소를 한 번에 import 하는 * 표기는 권장하지 않음
```python
from math import * 
from my_math import sqrt, tangent # 어느 함수가 math.sqrt와 중복되는지 모름

e = 9 # math 모듈의 자연상수 e를 사용 못하게 됨
```

**'as' 키워드**

as 키워드를 사용하여 별칭(alias)을 부여
    - 두 개 이상의 모듈에서 동일한 이름의 변수, 함수 클래스 등을 가져올 때 발생하는 이름 충돌 해결
```python
from math import sqrt # math.sqrt가 먼지 import
from my_math import sqrt as my_sqrt # my_math.sqrt가 math.sqrt를 덮어씀

sqrt(4)
my_sqrt(4)
```

- import 되는 함수나 변수명이 너무 길거나 자주 사용해야 할 경우 'as' 키워드로 별칭을 정의해 쉽게 사용
```python
import pandas as pd
import matplotlib.pyplot as plt

# 'as'를 사용하여서 호출할 때 편리하게 사용

df = pd.DataFrame()
plt.plot(x, y)
```
---

## 사용지 정의 모듈

**직접 정의한 모듈 사용하기**

- my_math.py 생성하여 두 수의 합을 구하는 add 함수를 작성
```python
def add(x, y):
    return x + y
```

- 같은 위치에 sample.py 파일을 생성하고 my_math 모듈의 add 함수 import 후 add 함수 호출 
```python
import my_math
print(my_math.add(10, 20))
```

---

## 파이썬 표준 라이브러리 

**파이썬 표준 라이브러리**

Python Standard Library : 파이썬 언어와 함께 제공되는 다양한 모듈과 패키지의 모음
 
---

## 패키지

Package : 연관된 **모듈**들을 하나의 디렉토리에 **모아 놓은 것**
    - 패키지는 다른 프로그래머들이 잘 만들어둔 **코드 꾸러미**

**직접 패기지 만들기**

- 밑에 코드를 사용하여 디렉토리 구조를 참조하여 제작 

```python
# my_package/math/my_math.py
def add(x, y):
    return x + y

# my_package/statistics/tools.py
def mod(x, y):
    return x % y 
```

**직접 만든 패키지 사용**

- 밑에 코드를 작성하여 결과 확인 
```python
# sample.py
from my_package.math import my_math
from my_package.statistics import tools

print(my_math.add(1,2))
print(tools.mod(1,2))
```
> 비슷한 기능이 한 파일에 몰려 있으면 헷갈릴 수 있음
> 유사기능은 묶고, 관련 없는 것은 나눠 사용
> 폴더/파일 명은 소문자 + 언더스코어(_)를 사용

**패키지의 종류**

PSL(python standard library) 내부 패키지
- 파이썬을 설치하면 자동으로 사용할 수 있는 기본 패키지
- 다양한 기능이 들어 있어 복잡한 작업도 쉽게 처리 가능
- 'math', 'os', 'sys', 'random'등 다양한 패키지가 존재
- 설치 없이 import 해서 사용 가능 

파이썬 외부 패키지
- 필요한 기능을 사용하기 위해 직접 설치해서 쓰는 패키지
- 다양한 패키지들이 존재 ex. 엑셀 파일 불러오기, 데이터를 분석 및 시각화
- 사용할 패키지를 설치 할 때는 'pip' 사용


**pip**

pip : 외부 패키지들을 설치하도록 도와주는 파이썬의 패키지 관리 시스템

**패키지 설치**
- 최신 버전 / 특정 버전 / 최소 버전을 명시하여 설치할 수 있음

```bash
$ pip install SomePackage
$ pip install SomePackage == 1.0.5
$ pip install SomePackage >= 1.0.4
```

> 호환성 이슈가 생기지 않는게 가장 중요
> 설치 패키지는 'pip freeze > requirement.txt' 명령어로 기록
> requirement.txt 중요

**requests 외부 패키지 설치 및 사용 예시**

requests 패키지
- 파이썬에서 웹에 요청을 보내고 응답을 받는 걸 아주 쉽게 만들어주는 외부 패키지

- pip을 통해 requests 패키지를 설치
```bash
$ pip install requests
```

- rwquests를 import 하여 웹에 데이터 요청
```python
import requests

#공휴일 정보 API
url = "https:// data.nager.at/api/v3/publicholidays/2025/KR"
response = requests.get(url).json()
print(response)
```
> .get(url): 주어진 url로 요청하는 requests 패키지 메서드
> .json(): 문자열로 이루어진 json자료형을 dict 자료형으로 변환시키는 requests 패키지 메서드

**패키지 사용 목적**

모듈들의 이름공간을 구분하여 충돌을 방지 
모듈들을 효율적으로 관리하고 할 수 있도록 돕는 역할 

---

## 제어문

Control Statement: 코드의 실행 흐름을 제어하는 데 사용되는 구문, **조건**에 따라 코드 블록을 실행하거나 **반복적**으로 코드를 실행

> 제어문은 **상황에 따라 다른 코드를 실행**하거나 **같은 코드를 여러 번 반복**

**조건문**

- if, elif, else
```python
if score >= 90:
    message = "축하합니다! 최고입니다!"
elif score >= 70:
    print("멋져요! 잘하셨어요!")
else:
    print("조금 더 노력해보세요!")
```

**반복문**

- for
```python
for i in range(N):
    twinkle(message)
```

- while, 반복문 제어 키워드(breal, continue)
```python
while True:
    print("계속할까요? (y/n)")
    answer = input()
    if answer == 'y':
        play()
    else:
        print("게임을 종료합니다.")
        break
```

## 조건문

Conditional Statement : 주어진 조건식을 평가하여 해당 조건이 참(True)인 경우에만 코드 블록을 실행하거나 건너뜀

if / elif / else : 파이썬 조건문에 사용되는 키워드 

> 조건문은 주어진 조건을 평가하여 True인 경우에만 코드를 실행 

## 'if' statement

**if 문**
- 조건문의 기본 형태 
- if 문에 작성된 조건을 만족할 때 내부 코드 실행
- 작성되는 조건은 표현식으로 작성

**elid 문**
- 이전의 조건을 만족하지 못하고 추가로 다른 조건이 필요할 때 사용
- 여러 개의 elif 문을 사용할 수 있음 

**else 문**
- 모든 조건을 만족하지 않으면 실행

```python
if 조건1:
    조건 1을 만족할 때 실행
elif 조건2:
    조건 2를 만족할 때 실행
elif 조건3:
    조건 3을 만족할 때 실행
else:
    모든 조건을 만족하지 않을 때 실행
```

**복수 조건문** 
- 조건식을 동시에 검사하는 것이 아니라 **순차적**으로 비교
- 조건식의 순서에 따라 원하는 결과가 나오지 않을 수 있음을 주의 

```python
dust = 155 #결과: 보통

if dust > 30:
    print('보통')
elif dust > 80:
    print('나쁨')
elif dust > 150:
    print('매우 나쁨')
else:
    print('좋음')
```

**중첩 조건문** 
- 조건문(if) 내부에 또 다른 조건문 (if) 작성 가능

```python
dust = 485 #결과: 매우 나쁨
           #     위험해요! 나가지 마세요!

if dust > 150:
    print('보통')
    if dust > 300:
        print('위험해요! 나가지 마세요!')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    print('좋음')
```

## 반복문

Loop Statement: 주어진 코드 블록을 여러 번 반복해서 실행하는 구문

**for문**
- 반복 가능한(iterable) 객체의 요소들을 반복하는데 주로 사용
- 주로 반복 가능한(iterable) 객체 요소의 개수만큼 반복
- 특징: 반복 횟수가 정해져 있음

```python
student_list = ['Alice', 'Bob', 'Charlie',]
for student in student_list:
    print(f"Hello, {student}!")
```
**while문**
- while 조건이 참(True)인 동안 반복
- 반복 횟구가 정해지지 않은 경우 주로 사용

```python
input_value = ''
while input_value != 'exit': # exit 입력하면 반복 종료
    input_value = input("Enter a value: ")
    print(input_value)
```

**반복문 내 사용 가능한 키워드**
반복문 제어 키워드 
- 반복문 내부에서 반복문의 흐름을 제어할 수 있는 키워드를 의미
- break 키워드: 해당 키워드를 만나게 되면 남은 코드를 무시하고 반복문 종료
- continue 키워드: 해당 키워드를 만나게 되면 다음 코드는 무시하고 반복문 처음으로 돌아가 다음 반복을 수행

빈 코드 블록 키워드
- 코드 구조상 문장이 필요하지만 실제로 실행할 코드가 없거나 일시적으로 비워둘 때 사용
- 주로 코드의 틀을 유지하거나 나중에 내용을 채우기 위한 용도
- pas 키워드: 아무 동작도 하지 않음을 명시적으로 표시

## 'for' statement

for 반복문: 반복 가능한(iterable) 객체의 요소들을 반복하는데 사용, 반복 가능한 객체의 요소 개수 만큼 반복이 수행

```python
for 변수 in 반복 가능한 객체:
    코드 블록
```

iterable: 요소를 하나씩 반환할 수 있는 모든 객체(반복문에서 순회할 수 있는 객체)

> 시퀀스 자료형(list, tuple, str)뿐만 아니라 비시퀀스 자료형(dic, set)등도 반복 가능한 객체

**for문 작동원리**
- 리스트 내 첫 항목이 반복 변수(item)에 할당되고 코드블록이 실행
- 다음으로 반복 변수에 리스트의 2번째 항복이 할당되고 코드블록이 다시 실행
- ... 마지막으로 반복 변수에 리스트의 마지막 요소가 할당되고 코드블록이 실행
- 더 이상 반복 변수에 할당할 값이 없으면 반복 종료

```python
item_list = ['apple', 'banana', 'coconut']
for item in item_list: # item: 반복 변수
    print(item)

# 출력
'''
apple
banana
coconut
'''
```

**문자열 순회**
- 문자열은 문자로 구성된 시퀀스 자료형
- 문자열 반복시 문자가 반복 변수에 할당되어 반복 수행

```python
country = 'Korea'

for char in country:
    print(char)

# 출력
'''
K
o
r
e
a
'''   
```

**range 순회**
- 특정 숫자 범위만큼 반복을 하고 싶을 때 range 함수를 사용

```python
for i in range(5):
    print(i)

# 출력
'''
0
1
2
3
4
'''   
```

**dictionary 순회**
- dict 자료형은 비시퀀스 자료형으로 반복 순서가 보장되지 않음을 유의

```python
my_dict ={
    'x': 10,
    'y': 20,
    'z': 30,
}
for key in my_dict:
    print(key)
    print(my_dict[key])

# 출력
'''
x
10
y
20
z
30
'''   
```

**인덱스로 리스트 순회**
- 리스트의 요소가 아닌 인덱스로 접근하여 해당 요소들을 변경하기
- 인덱스를 사용하면 리스트의 원하는 위치에 있는 값을 읽거나 변경할 수 있음

```python
numbers = [4, 6, 10, -8, 5]

for i in range(len(numbers)):
    numbers[i] = numbers[i]*2

print(numbers) #[8, 12, 20, -16, 10]
```

**중첩된 반복문**
- 중첩된 반복문에서의 출력 예상해보기

```python
outers = ['A','B']
inners = ['c','d']

for outer in outers:
    for inner in inners:
        print(outer, inner)

# 출력은?
"""
???
"""
```

**중첩 리스트 순회**
- 안쪽 리스트 요소에 접근하려면 바깥 리스트를 순회하면서 중첩 반복을 사용해 각 안쪽 반복을 순회

```python
elements = [['A','B'], ['c', 'd']]

for elem in elements:
    print(elem)

# 출력
"""
['A','B']
['c','d']

"""

for elem in elements:
    for item in elem:
        print(item)

# 출력
"""
A
B
c
d
"""
```

## 'while' statement

while: 조건식이 True인 동안 코드를 반복해서 실행 == 조건식이 False이 될 때 까지 반복해서 실행

```python
while 조건식:
    코드 블록
```

**while문의 반복 원리**
while의 조건식 확인
- 조건식이 True면 코드 블록 실행
- 조건식이 False면 반복 종료

```python
a = 0

while a < 3:
    print(a)
    a += 1
print('끝')

# 출력 
"""
0
1
2
끝
"""
```

> 코드 블록 실행이 마무리되면 다시 while 조건식 확인

**사용자 입력에 따른 반복**
while문을 사용한 특정 입력 값에 대한 종료 조건 활용

```python
number = int(input('양의 정수: '))

while number <= 0:
    if number < 0:
        print("음수를 입력함")
    else: 
        print("0은 양의 정수 아님")

    number = int(input('양의 정수: '))

print("잘했음")

# 출력 
"""
양의 정수: 0
0은 양의 정수 아님
양의 정수: -1
음수를 입력함
양의 정수: 1
잘했음
"""
```

**while문의 특징**
반드시 **종료 조건**이 필요
- 종료조건이 없는 경우 무한 반복에 빠지게 되어 원하는 동작을 하지 않게 되므로 반드시 종료 조건을 설정해야 함

> 조건은 언젠가 반드시 False가 되로고 반복문 내부에서 변수 값 변화를 시켜야 됨
> while문을 시작하기 전에 조건에서 사요할 변수를 반드시 초기화해야 오류를 방지할 수 있음
> 예상치 못한 상황에 대비해 break 문을 사용하여 종료 가능

**for 반복문**
- iterable 요소를 하나씩 순회하며 반복
- 반복 횟수가 명확하게 정해져 있는 경우 유용
    - 리스트, 튜플, 문자열 등과 같은 시퀀스 형식 처리할 경우
    - range() 함수를 사용해 일정 횟수 만큼 반복 작업을 수행할 경우

**while 반복문**
- 주어진 조건식 True인 동안 반복
- 반복 횟수가 불명확하거나 조건에 따라 반복을 종료해야 할 때 유용
    - 사용자의 입력을 받아서 특정 조건이 충족될 때까지 반복하는 경우
    - 반복 횟수가 미리 정해져 있지 않고, 특정 조건이 만족될 때까지 반복해야 하는 경우

> 문제의 반복 조건과 목적에 따라 더 적합한 반복문 선택
> 필요 시 두 반복문을 중첩해서 사용 가능
> 문제 상황에 따라 융통성 있게 활용

## 반복 제어

for문과 while은 매 반복만다 본문 내 모든 코드를 실행하지만 때때로 일부만 실행하는 것이 필요할 때가 있음

**반복 제어 키워드**
break 키워드
- 해당 키워드를 만나게 되면 남은 코드를 무시하고 반복 즉시 종료
- 반복을 끝내야 할 명확한 조건이 있을 때

```python 
for i in range(10):
    if i == 5:
        break
    print(i) # 0 1 2 3 4
```
- ex. 짝수만 찾기, 프로그램 종료 조건 만들기 등

continue 키워드
- 해당 키워드를 만나게 되면 다음 코드는 무시하고 다음 반복을 시행

```python
for i in range(10):
    if i % 2 == 0:
        continue
    print(i) # 1 3 5 7 9
```

- ex. 리스트 홀수만 출력 등

> 반복 제어문은 반드시 반복문 내에서 사용
> 중첩 반복문인 경우 해당 키워드가 작성된 코드 블록의 반복 흐름만 제어한다는 것
> 과도하게 사용하면 가독성이 떨어지므로 필요 상황에만 사용

pass 키워드
- **'아무 동작도 하지 않음'**을 명시적으로 나타내는 키워드
- 반복 제어가 아닌 **코드의 틀을 유지하거나 나중에 내용을 채우기 위한 용도**로 사용
- 코드를 비워두면 오류가 발생하기 때문에 pass 키워드를 사용
- 반복문  뿐만 아니라 함수, 조건문에서도 사용 가능

```python
# Case 1
while True:
    if condition1:
        break
    elif contion2:
        pass # 빈 코드를 의미
    else:
        print('출력')

# Case 2
if condition:
    pass # 아무런 동작도 수행하지 않음
else:
    pass # 구조를 잡을 뿐

# Case 3
def my_function():
    pass # 없으면 오류 발생
```

## 유용한 내장 함수 map & zip

**map**
map(function, iterable): **반복 가능한 데이터구조(iterable)**의 모든 요소에 **function**을 적용하고, 그 결과 값들을 map object로 묶어서 변환

```python
numbers = [1, 2, 3]
result = map(str, numbers)

print(result) # <map object at 0x00000239C915D760>
print(list(result)) ['1', '2', '3']
```

> **map object** 결과를 하나씩 꺼내 쓸 수 있는 반복 가능한 객체 자료형, 전체 값을 확인하려면 list나 tuple로 형변환 필요

**코테에서 활용**

```python
numbers1 = input().split()
print(numbers1) # ['1', '2', '3']

numbers2 = list(map(int, input().split()))
print(numbers2) # [1, 2, 3]
```

> 문자열이 공백으로 구분이면 split을 사용, 연속된 문자 형태면 split 사용 안함

**zip**
zip(* iterable): zip 함수는 여러 개의 반복 가능한 데이터 구조를 묶어서, 같은 위치에 있는 값들을 하나의 tuple로 만든 뒤 그것들을 모아 zip object로 반환하는 함수

```python
girls = ['jane', 'ashley']
boys = ['peter', 'jay']
pair = zip(girls, boys)

print(pair) <zip object at 0x000001c76DE58700>
print(list(pair)) # [('jane', 'ashley'),('peter', 'jay')]
```

> **zip pbject** 짝지어진 결과(tuple)를 하나씩 꺼내 쓸 수 있는 반복 가능한 객체 자료형, 전체 값을 확인하려면 list나 tuple로 형변환을 해줘야 함

**여러 리스트 동시 조회**

```python
kr_scores = [10, 20, 30, 50]
math_scores = [20, 40, 50, 70]
en_scores = [40, 20, 30, 50]

for student_scores in zip(kr_scores, math_scores, en_scores):
    print(student_scores)

#출력
"""
(10, 20, 40)
(20, 40, 20)
(30, 50, 30)
(50, 70, 50)
"""
```

> 반복 가능한 자료형의 길이가 다른 경우 가장 짧은 길이를 기준으로 묶어 반환
> 반드시 반복 가능한 자료형만 인자로 사용
> zip object는 언패킹을 활용하여 변수에 바로 tuple 요소를 할당

**(i,j)의 값을 (j,i) 위치로 옮긴 행렬**
- 2차원 리스트의 같은 컬럼(열) 요소를 동시에 조회
- 실행 결과가 전치 행렬과 동일

```python
scores = [
    [10, 20, 30],
    [40, 50, 39],
    [20, 40, 50],
]

for score in zip(*scores):
    print(score)

#출력
"""
(10, 40, 20)
(20, 50, 40)
(30, 39, 50)
"""
```

## 모듈 내부 살펴보기

내장 함수 **help**를 사용해 모듈에 무엇이 들었는지 확인 가능

## for - else

**파이썬의 조금 특별한 문법**
- for 루프가 break를 만나 중단되지 않고, 끝까지 정상적으로 완료될 때만 else 실행
    - break 문을 만나 반복문이 종료되면 else의 코드 블록은 실행 안됨

```python
for i in range(5):
    print(i)
    if i == 3:
        #break 문이 실행되면 else 블록은 실행 안됨
        print('반복이 중단되었습니다.')
        break
    else:
        print('이 메세지는 출려고디지 않습니다.')

#출력
"""
0
1
2
3
반복이 중단되었습니다.
"""
```

> for-else 문의 경우 if-else 문과 혼동되지 않도록
> 모든 반복을 정상적으로 수행해야 else가 되므로, 검증로직 필요
> while-else문도 존재, 동작 규칙 for-else와 동일, break로 반복이 종료되는 경우 else 실행 안됨

**for-else 예시**
case 1. 중복 아이디를 찾았을 경우
- 중복 아이디를 찾았을 경우(break 실행 -> else 실행 안됨)
    - id_to_check와 동일한 'guset'를 목록에서 발견되는 순간 break가 실행되어 for 루프가 중간에 멈춤

```python
registered_ids = ['admin', 'user01', 'guset', 'user02']
id_to_check = 'guest' # 이미 리스트에 존재하는 아이디

for existing_id in registered_ids:
    if existing_id == id_to_check:
        print('이미 사용 중인 아이디입니다.')
        break # 중복 아이디를 찾았으므로 확인 절차 중단
else:
    #for 루프가 break로 중단되었기에 이 부분은 실행 안됨
    print('사용 가능한 아이디입니다.')

print('아이디 확인 절차를 종료합니다.')

#출력
"""
이미 사용 중인 아이디입니다.
아이디 확인 절차를 종료합니다.
"""
```

case 2. 중복 아이디를 찾았을 경우
- 중복 아이디를 찾지 못한 경우 (break 실행 안됨 -> else 실행됨)
    - new_user는 registered_ids 목록 끝까지 확인해도 존재하지 않음
    - for 루프가 모든 항목을 확인한 뒤 정상적으로 종료되었으므로, else 블록이 실행

```python
registered_ids = ['admin', 'user01', 'guset', 'user02']
id_to_check = 'new_user' #  리스트에 없는 아이디

for existing_id in registered_ids:
    if existing_id == id_to_check:
        print('이미 사용 중인 아이디입니다.')
        break 
else:
    #for 루프가 break로 없이 마무리 되어 else 블록 실행
    print('사용 가능한 아이디입니다.')

#출력
"""
사용 가능한 아이디입니다.
"""
```

## enumerate

enumerate(iterable, start=0): iterable 객체의 각 요소에 대해 **인덱스와 값을 함께 반환**하는 내장함수

```python
fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
    print(index, fruit)

#출력
"""
0 apple
1 banana
2 cherry
"""
```

**enumerate 함수 활용**
enumerate의 index 정보를 이용해 넘버링으로 사용
- start에 시작 값을 설정 가능, 인덱스 정보를 이용해 요소의 위치를 확인할 수 있음

```python

# case 1

movies = ['인터스텔라', '기생충', '인사이드 아웃', '라라랜드']
for idx, title in enumerate(movies, statr=1):
    print(f'{idx}위, {tilte}')

#출력
"""
1위: 인터스텔라
2위: 기생충
3위: 인사이드 아웃
4위: 라라랜드
"""

# case 2

respondents = ['은지', '정우', '소민', '태호']
answers = ['', '좋아요', '', '괜찮아요']

for i, response in enumerate(answers):
    if response == '':
        print(f"{respondents[i]} 미제출")

#출력
"""
은지 미제출
소민 미제출 
"""
```