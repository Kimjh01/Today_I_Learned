# Day 2: Python 기초

## 리스트

List: 여러 개의 값을 순서대로 저장하는, 변경 가능한(mutalbe) 시퀀스 자료형

### 리스트 표현
- 대괄호 `[]` 안에 값들을 쉼표 `,`로 구분하여 만듦
- 숫자, 문자열, 심지어 다른 리스트까지 모든 종류의 데이터를 담을 수 있음
- 값을 추가, 수정, 삭제하는 등 자유롭게 변경 가능

```python
my_list_1 = []
my_list_2 = [1, 'a', 3, 'b', 5]
my_list_3 = [1, 2, 3, 'Python', ['hello', 'world', '!!!']]
````

### 시퀀스로서의 리스트

리스트는 시퀀스이므로, 문자열처럼 인덱싱, 슬라이싱, 길이 확인, 반복 등 공통 기능을 모두 사용 가능

```python
my_list = [1, 'a', 3, 'b', 5]

# 인덱싱
print(my_list[1])  # a

# 슬라이싱
print(my_list[::-1])  # [5, 'b', 3, 'a', 1]

# 길이
print(len(my_list))  # 5
```

## 중첩리스트 (Nested List)

다른 리스트를 값으로 가진 리스트

### 중첩리스트 접근하기
* 인덱스를 연달아 사용하여 안쪽 리스트의 값에 접근할 수 있음
* 먼저 바깥 리스트의 인덱스로 안쪽 리스트를 선택
* 선택된 안쪽 리스트에 다시 한번 인덱스를 사용

```python
my_list = [1, 2, 3, 'Python', ['hello', 'world', '!!!']]
print(my_list[-1][1][0])  # w
print(my_list[4][-1])     # !!!
print(len(my_list))       # 5
```

## 리스트의 가변성

한 번 생성된 리스트는 그 내용을 자유롭게 수정, 추가, 삭제할 수 있음 (문자열의 불변성과 반대)

```python
my_list = [1, 2, 3, 4, 5]
my_list[1] = 'two'
print(my_list)  # [1, 'two', 3, 4, 5]

my_list[2:4] = ['three', 'four']
print(my_list)  # [1, 'two', 'three', 'four', 5]
```

---

## 튜플 (Tuple)

여러 개의 값을 순서대로 저장하는 **변경 불가능한(Immutable)** 시퀀스 자료형

### 튜플 표현

```python
my_tuple_1 = ()
my_tuple_2 = (1,)
my_tuple_3 = (1, 'a', 3, 'b', 5)
my_tuple_4 = 1, 'hello', 3.14, True
```

* 소괄호 없이도 생성 가능
* 단일 요소일 경우 반드시 후행 쉼표 필요 (`(1,)`)

### 시퀀스로서의 튜플

```python
my_tuple = (1, 'a', 3, 'b', 5)

# 인덱싱
print(my_tuple[1])  # a

# 슬라이싱
print(my_tuple[::-1])  # (5, 'b', 3, 'a', 1)

# 길이
print(len(my_tuple))  # 5
```

### 튜플의 불변성

```python
my_tuple = (1, 'a', 3, 'b', 5)
my_tuple[1] = 'z'  # TypeError 발생
```

* 함수 다중 반환, 값 교환 등에서 주로 간접적으로 사용됨
* 데이터의 안정성과 무결성을 보장

---

## 레인지 (Range)

연속된 정수 시퀀스를 생성하는, **변경 불가능한(Immutable)** 자료형

```python
range(n)         # 0 ~ n-1
range(start, stop)
range(start, stop, step)
```

```python
my_range_1 = range(5)
my_range_2 = range(1, 10)
my_range_3 = range(5, 0, -1)

print(list(my_range_1))  # [0, 1, 2, 3, 4]
print(list(my_range_2))  # [1, ..., 9]
print(list(my_range_3))  # [5, 4, 3, 2, 1]
```

---

## 딕셔너리 (Dictionary)

Key - Value 쌍으로 이루어진 **순서 없고 중복 없는 변경 가능한(Mutable)** 자료형

```python
my_dict = {'name': '홍길동', 'age': 25}
print(my_dict['name'])  # 홍길동

# 값 추가 및 변경
my_dict['banana'] = 50
my_dict['apple'] = 100
```

* Key는 고유하고 immutable 자료형이어야 함
* Value는 어떤 자료형이든 가능

---

## 세트 (Set)

순서와 중복이 없는 **변경 가능한(Mutable)** 자료형

```python
my_set = {1, 2, 3}
empty_set = set()
```

### 집합 연산

```python
a = {1, 2, 3}
b = {3, 6, 9}

print(a | b)  # 합집합
print(a - b)  # 차집합
print(a & b)  # 교집합
```

---

## 이외 주요 타입

* **None**: 값이 없음
* **Boolean**: True / False
* **Collection**: str, list, tuple, dict, set, range 등

---

## 컬렉션 정리

| 컬렉션명  | 변경 가능 | 순서 있음 | 비고   |
| ----- | ----- | ----- | ---- |
| str   | X     | O     | 시퀀스  |
| list  | O     | O     | 시퀀스  |
| tuple | X     | O     | 시퀀스  |
| dict  | O     | X     | 비시퀀스 |
| set   | O     | X     | 비시퀀스 |

---

## 불변 vs 가변

| 구분 | 불변 (Immutable)    | 가변 (Mutable)    |
| -- | ----------------- | --------------- |
| 특징 | 변경 불가             | 변경 가능           |
| 예시 | str, tuple, range | list, dict, set |

---

## 형변환

### 암시적 형변환

```python
print(3 + 5.0)        # 8.0
print(True + 3)       # 4
print(True + False)   # 1
```

### 명시적 형변환

| 함수      | 예시            | 결과             |
| ------- | ------------- | -------------- |
| int()   | int("123")    | 123            |
| float() | float("3.14") | 3.14           |
| str()   | str(100)      | "100"          |
| list()  | list("abc")   | \['a','b','c'] |
| tuple() | tuple(\[1,2]) | (1,2)          |
| set()   | set(\[1,2,2]) | {1,2}          |

---

## 연산자

### 산술 연산자

| 연산자  | 설명     |
| ---- | ------ |
| +    | 덧셈     |
| -    | 뺄셈     |
| \*   | 곱셈     |
| /    | 나눗셈    |
| //   | 정수 나눗셈 |
| %    | 나머지    |
| \*\* | 거듭제곱   |

---

### 복합 연산자

| 연산자       | 의미           |
| --------- | ------------ |
| a += b    | a = a + b    |
| a -= b    | a = a - b    |
| a \*= b   | a = a \* b   |
| a /= b    | a = a / b    |
| a //= b   | a = a // b   |
| a %= b    | a = a % b    |
| a \*\*= b | a = a \*\* b |

---

### 비교 연산자

| 연산자          | 의미     |
| ------------ | ------ |
| <, <=, >, >= | 비교     |
| ==           | 동등성(값) |
| !=           | 불일치    |
| is           | 객체 동일성 |
| is not       | 객체 불일치 |

---

## == vs is

```python
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True
print(a is b)  # False

b = a
print(a is b)  # True
```

* `==`: 값 비교 (Equality)
* `is`: 객체 비교 (Identity)

---

## 싱글턴 객체

* 전역에서 하나만 존재하는 객체: `None`, `True`, `False`
* 비교 시 `is` 사용 권장

---

## 논리 연산자

| 연산자 | 의미   |
| --- | ---- |
| and | 논리곱  |
| or  | 논리합  |
| not | 논리부정 |

---

## 단축 평가 (Short-circuit)

* `and`: 하나라도 False면 즉시 False
* `or`: 하나라도 True면 즉시 True

---

## 멤버십 연산자

| 연산자    | 설명     |
| ------ | ------ |
| in     | 포함 여부  |
| not in | 미포함 여부 |

---

## 시퀀스 연산자

| 연산자 | 설명 |
| --- | -- |
| +   | 연결 |
| \*  | 반복 |

---

## 연산자 우선순위

1. `()`, `[]`, 슬라이싱
2. `**`
3. `+`, `-` (단항)
4. `*`, `/`, `//`, `%`
5. `+`, `-`
6. 비교 연산자 (`<`, `==`, `is`, 등)
7. `not`
8. `and`
9. `or`

---

## Trailing Comma

```python
items = [
    'item1',
    'item2',
]
```

* 마지막 요소 뒤에 쉼표 추가
* 가독성 향상
* 단일 요소 튜플 `(1,)`에는 필수


