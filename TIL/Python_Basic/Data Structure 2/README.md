# Data Structure 2

## 비시퀀스 데이터 구조

Dictionary: 키(Key)와 값(Value)을 짝지어 저장하는 자료구조
- 딕셔너리는 내부적으로 **해시 테이블**을 사용하여 **키-값** 쌍을 관리
- 키를 통한 값의 **삽입, 삭제, 검색**이 데이터의 크기와 관계없이 **매우 빠름**

**딕셔너리 메서드**

| 메서드              | 설명                                          |
| ------------------ | --------------------------------------------- |
| D.get(k)           | 키 K에 연결된 값을 반환(키가 없으면 None을 반환) |
| D.get(k, v)        | 키 k에 연결된 값을 반환하거나 키가 없으면 기본 값으로 v를 반환 |
| D.Keys()           | 딕셔너리 D의 키를 모은 객체를 반환 |
| D.values()         | 딕셔너리 D의 값을 모은 객체를 반환 |
| D.items()          | 딕셔너리 D의 키/값 쌍을 모은 객체를 반환 |
| D.pop(k)           | 딕셔너리 D에서 키 k를 제거하고 연결됐던 값을 반환 (없으면 오류) |
| D.pop(k, v)        | 딕셔너리 D에서 키 k를 제거하고 연결됐던 값을 반환 (없으면 v를 반환) |
| D.clear()          | 딕셔너리 D의 도든 키/값 쌍을 제거 |
| D.setdefault(k)    | 딕셔너리 D에서 키 K와 연결된 값을 반환 |
| D.setdefault(k, v) | 딕셔너리 D에서 키 k와 연결된 값을 반환, k가 D의 키가 아니면 값 v와 연결한 키 k를 D에 추가하고 v를 반환 |
| D.update(other)    | other 내 각 키에 대해 D에 있는 키면 D에 있는 그 키의 값을 other에 있는 값으로 대체, other에 있는 각 키에 대해 D에 없는 키/값 쌍을 D에 추가 |


.get(key[,default]):  키 연결된 값을 반환하거나 키가 없으면 None 혹은 기본 값을 반환

```python 

person = {'name': 'Alice', 'age': 25}

print(person.get('name')) # Alice
print(person.get('country')) # None
print(person.get('country', 'Unknown')) # Unknown
print(person['country']) # KeyError: 'country'

```
.keys(): 딕셔너리 키를 모은 객체를 반환

```python 

person = {'name': 'Alice', 'age': 25}
print(person.keys()) # dict_keys(['name', 'age'])
for item in person.keys():
    print(item)

"""
name
age
"""

```

.values(): 딕셔너리 값을 모은 객체를 반환

```python 

person = {'name': 'Alice', 'age': 25}
print(person.values()) # dict_keys(['Alice', '25'])
for item in person.values():
    print(item)

"""
name
age
"""

```

.items(): 딕셔너리 키/값 쌍을 모은 객체를 반환

```python 

person = {'name': 'Alice', 'age': 25}
print(person.items()) # dict_keys([('name': 'Alice'), ('age': 25)])
for key, value in person.items():
    print(key, value)

"""
name Alice
age 25
"""

```

.pop(key[,default]): 키를 제거하고 연결됐던 값을 반환 (없으면 에러나 default를 반환)

```python 

person = {'name': 'Alice', 'age': 25}
print(person.pop('age')) # 25
print(person) # {'name': 'Alice'}
print(person.pop('country', None)) # None
print(person.pop('country')) # KeyError

```

.clear(): 딕셔너리의 모든 키/값 쌍을 제거

```python 

person = {'name': 'Alice', 'age': 25}
person.clear()
print(person) # {} 

```

.setdefault(key[,default]): 키와 연결된 값을 반환, 키가 없다면 default와 연결한 키를 딕셔너리에 추가하고 default를 반환 

```python 

person = {'name': 'Alice', 'age': 25}
print(person.setdefault('country', 'KOREA')) # KOREA
print(person) # {'name': 'Alice', 'age': 25, 'country', 'KOREA'} 

```

.update(*[other]*): other가 제공하는 키/값 쌍으로 딕셔너리를 갱신하고 기존 키는 덮어씀

```python 

person = {'name': 'Alice', 'age': 25}
other_person = {'name': 'Jane', 'country': 'KOREA'}

print.update(other_person)
print(person) # {'name': 'Jane', 'age': 25, 'country': 'KOREA'}

print.update(age=100, address='SEOUL')
print(person) # {'name': 'Jane', 'age': 100, 'country': 'KOREA', 'address': 'SEOUL'}

```

---

## 세트

set: **고유한** 항목들의 정렬되지 않은 컬렉션
- 내부적으로 **해시 테이블**을 사용하여 데아터를 저장
- 항목의 **고유성**을 효과적으로 보장하며, 항목의 추가, 삭제, 존재 여부 확인(in 연산)이 데이터의 크기에 관계없이 **매우 빠름**
- 또한, 합집합(Union), 교집합(Intersection), 차집합(Difference) 등 수학적인 집합 연산을 간편하게 수행할 수 있는 것이 가장 큰 특징

> # {1, 3, 'a', 'c', 'b'} 와 같은 예시는 순서가 없으니 유의바람 


| 메서드              | 설명                                          |
| ------------------ | --------------------------------------------- |
| s.add(x)           | 세트 s에 항목 x를 추가, 이미 x가 있다면 변화 없음 |
| s.update(iterable) | 세트 s에 다른 iterable 요소를 추가 |
| s.clear       | 세트 s의 모든 항목을 제거 |
| s.remove(x)   | 세트 s에서 항목 x를 제거, 항목 x가 없을 경우 Key error |
| s.pop()       | 세트 s에서 임의의 항목을 반환하고, 해당 항목을 제거 |
| s.discard(x)  | 세트 s에서 항목 x를 제거 |


.add(x): 세트에 x를 추가

```python 

my_set = {'a', 'b', 'c', 1, 2, 3}

my_set.add(4)
print(my_set) # {1, 2, 3, 'a', 'b', 'c', 'd'}

```

.update(iterable): 세트에 다른 iterable 요소를 추가

```python 

my_set = {'a', 'b', 'c', 1, 2, 3}

my_set.update([1, 4, 5])
print(my_set) # {'a', 'b', 'c', 1, 2, 3, 4, 5}

```

.clear(): 세트에 모든 항목을 제거

```python 

my_set = {'a', 'b', 'c', 1, 2, 3}

my_set.clear()
print(my_set) # set()

```

.remove(x): 세트에 항목 **x를 제거**, 항목 **x가 없을 경우 KetError**

```python 

my_set = {'a', 'b', 'c', 1, 2, 3}

my_set.remove(2)
print(my_set) # {'a', 'b', 'c', 1, 3}

my_set.remove(10)
print(my_set) # KeyError

```

.pop(): 세트에 **임의의** 요소를 제거하고 **반환**

```python 

my_set = {'a', 'b', 'c', 1, 2, 3}

element = my_set.pop()
print(element) # 1
print(my_set) # {'a', 'b', 'c', 2, 3}

```

.discard(x): 세트에서 항목x를 제거 .remove와 달리 에러 없음

```python 

my_set = {'a', 'b', 'c', 1, 2, 3}

my_set.discard(2)
print(my_set) # {1, 3, 'a', 'c', 'b'}
my_set.discard(10)

```

**세트의 집합 메서드**

```python 

set1 = {0, 1, 2, 3, 4}
set2 = {1, 3, 5, 7 ,9}
set3 = {0, 1}

print(set1.difference(set2)) # {0, 2, 4}
print(set1.intersection(set2)) # {1, 3}
print(set1.issubset(set2)) # False
print(set3.issubset(set1)) # True
print(set1.issuperset(set2)) # False
print(set1.union(set2)) # {0, 1, 2, 3, 4, 5, 7, 9}

```

---

## 해시 테이블

Hash table: 해시 테이블은 **'키(Key)'와 '값(value)'**을 짝지어 저장하는 자료구죠 

> 키와 해시함수를 사용해 인덱스를 알아내면 배열에서 값을 꺼내는 것보다 빠름

**해시 테이블 원리**
- 키를 해시 함수를 통해 해시 값으로 변환
- 변환된 해시 값을 인덱스로 삼아 데이터를 저장하거나 찾음
- 검색, 삽입, 삭제를 빠르게 수행

**해시** 

Hash: **임의의 크기**를 가진 데이터를 고정된 크기의 **고유한 값**으로 변환
- 생성된 해시 값(고유한 정수)은 해당 데이터를 식별하는 '지문' 역할을 함
- 파이썬에서는 이 해시 값을 이용해 해시 테이블에 데이터를 저장
- 이 변환을 수행하는 것이 **해시 함수**

**해시 함수** 

Hash function: 임의 길이 데이터를 입력 받아 고정 길이(정수)로 변환해 주는 함수 **정수가 해시 값**

- 주로 해시 테이블을 구현할 때, 매우 빠른 검색 및 데이터 저장 위치 결정을 위해 사용
- **해시 알고리즘**이라 부름

>**해시 테이블이 빠른 이유**
> 해시 함수는 키(Key)를 입력받아 데이터를 저장하거나 찾을 배열의 **정확한 인덱스**를 즉시 계산
> 마치 책의 제목(키)을 알면 색인(해시 함수)을 통해 페이지 번호(인덱스)를 바로 알아내고, 해당 페이지(배열 위치)로 **곧바로 이동**하여 찾는 것과 같음


**set의 요소 & dict의 키와 해시 테이블 관계**
1. set
- 각 요소를 해시 함수로 변환해 나온 해시 값에 맞춰 해시 테이블 내부 버킷(bucket)에 위치
- "순서"라기보다 "버킷 위치(인덱스)"가 요소의 위치를 결정
- set은 **순서를 버장 안함**

2. dict
- 키(key) -> 해시 함수 -> 해시 값 -> 해시 테이블에 저장
- 단 set과 달리 "삽입 순서"는 유지한다는 것이 언어 사양에 따라 다름 (version issue)
    - 즉, 키를 추가한 순서대로 반복문 순회할 때 나옴
     - 사용자에게 보여지는 키 순서는 삽입 순서가 유지되도록 설계

**set의 pop 메서드 예시 - 정수**
정수(숫자) 값은 해시 값이 숫자 자기 자신과 동일하거나 단순 계산으로 고정

```python

my_set = {3, 2, 1, 9, 100, 4, 87, 39, 10, 52}

print(my_set.pop()) # 1
print(my_set.pop()) # 2
print(my_set.pop()) # 3
print(my_set.pop()) # 100
print(my_set.pop()) # 4
print(my_set.pop()) # 39
print(my_set.pop()) # 9
print(my_set.pop()) # 10
print(my_set.pop()) # 52
print(my_set.pop()) # 87
print(my_set) # set()
```

**set의 pop 메서드 예시 - 문자열**
문자열은 해시 계산 시 파이썬의 해시 난수화(Hash Randomization)가 적용되므로, 실행마다 순서가 달라질 수 있음

```python

my_set = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'}

print(my_set.pop()) # a
print(my_set.pop()) # f
print(my_set.pop()) # h
print(my_set.pop()) # e
print(my_set.pop()) # d

...

```

**Python에서 해시 함수**

1. 정수
    - 같은 정수는 항상 같은 해시 값을 가짐
    - hash(1)은 여러 번 호출해도 결과가 동일

2. 문자열
    - 문자열 해시 시, 파이썬 인터프리터 시작 때 설정되는 난수 시드(seed)가 달라질 수 있음
    - 보안상 이류로 해시 난수화 도입
    - 각 실행마다 달라질 수 있어 'a'의 해시 값도 매번 바뀔 수 있음

```python

print(hash(1)) # 1
print(hash(1)) # 1
print(hash('a')) # 실행시마다 다름 
print(hash('a')) # 실행시마다 다름

```

**해시 난수화와 난수 시드**

- 파이썬 프로세스가 새로 시작될 때마다 해시를 계산할 때 사용하는 난수 시드가 달라짐
    - 해시 함수가 매번 바뀌는 것이 아니라, 해시 계산에 쓰이는 시드 값이 실행마다 달라짐
- 이로 인해 동일한 데이터라도 매번 해시 값이 달라져 결과적으로 버킷 배치가 달라짐

**set의 요소 & dict의 키와 해시 테이블 관계**
- set의 pop()은 "임의의 요소"를 제거하고 반환
    - 실행할 때마다 다른 요소를 얻는다는 의미에서 **"무작위"**가 아니라 **"임의"**라는 의미에서의 **"무작위"** (By "arbitrary" the docs don't mean "random")

**내부적으로 해시 테이블(버킷)을 참조하기 때문에, 실행 때마다 다른 요소가 먼저 나올 수 있음**
- 해시 난수화로 인해 문자열 같은 해시 값이 실행마다 달라질 수 있고, 따라서 set 내부 요소의 배치가 달라질 수 있음
- 정수는 해시 값이 항상 동일하기 때문에, 파이썬을 동일 프로세스에서 연속 실행할 때는 결과가 어느정도 일정해 보이기도 할지만, 여전히 set은 순서가 없으므로 pop되는 순서는 예측 불가능

**Hashable**
- hash() 함수에 넣어 해시 값을 구할 수 있는 객체를 의미 
- 대부분의 **불변 타입**은 해시 가능
    - int, float, str, tuple (단, 내부에 불변만 있을 경우)
- 가변형 객체(list, dict, set)는 기본적으로 해시 불가능
    - 이유: 값이 변하면 해시 값도 달라질 수 있어 해시 테이블 무결성이 깨짐

> Hashable: 해시 함수를 통해 고유한 해시 값을 만들 수 있고, 값이 변하지 않는 객체

```python

print(hash(1))
print(hash(1.0)) 
print(hash('1')) 
print(hash((1, 2, 3))) 

#TypeError: unhashable type: 'list'
print(hash((1, 2, [3, 4])))

```

**Hashable과 불변성 간의 관계**
- 해시 테이블 (ex. set, dict의 KEY)에는 hashable(해시가 가능한 객체)만 저장 가능
- 불변 객체는 생성 후 값 변경이 불가능하므로, 항상 같은 해시 값을 유지
    -> 해시 테이블이 안정적으로 동작
- 다만, "hash 가능하다 != 불변이다"가 절대적이지는 않지만, 일반적으로 내장 자료형 기준에서는 불변이어야 해시 가능

> **가변 객체가 hashable 하지 않는 이유**
> **해시 값의 불변성**: 해시 테이블은 객체의 해시 값을 이용해 데이터를 저장하고 **검색할 위치(인덱스)**를 결정
> **문제 발생**: 만약 list와 같은 가변 객체를 키로 사용하고, 그 리스트의 내용을 변경하면 해시 값도 함께 변하게 됨
> **데이터 손실**: 이 경우, 데이터를 **저장했던 인덱스**와 **변경 후 찾으려는 인덱스**가 달라져 해당 데이터를 영원히 찾을 수 없게 됨
> 따라서, 해시 테이블의 안정적인 동작을 보장하기 위해, 파이썬은 가변 객체의 해시 값 계산을 허용하지 않음 


**Hashable**
- 값이 변경될 수 있으므로, 같은 객체라도 값이 바뀌면 해시 값도 달라질 수 있음
- 해시 테이블에서는 "동일 키 -> 동일 위치"로 가정하고 빠른 검색을 수행하는데, 이 가정이 깨짐
- ex. 리스트, 집합, 딕셔너리 자체를 set이나 dict의 키로 쓸 수 없음

```python

#TypeError: unhashable type: 'list' 
print(hash((1, 2, 3))) 

#TypeError: unhashable type: 'list'
my_set = {[1, 2, 3], 1, 2, 3, 4, 5}

#TypeError: unhashable type: 'set'
my_dict = {{3, 2}: 'a'}

```

**Hashable 객체가 필요한 이유**
1. 해시 테이블 기반 자료 구조 사용
    - set의 요소, dict의 키
    - 중복 방지 & 빠른 검색, 조회

2. 불변성을 통한 일관된 해시 값
    - 한 번 해시 값이 정해지면 바뀌지 않ㅇ야 해시 테이블 무결성이 유지

3. 안정성과 예측 가능성 유지
    - 동일한 데이터는 항상 동일한 해시 값을 반환 -> 로직을 단순화 


## 파이썬 문법 규격

**BNF**
Backus-Naur Form: 프로그래밍 언어의 문법을 표현하기 위한 표기법

**EBNF**
Extended Backus-Naur Form: BNF를 확장한 표기법, 메타 기호를 추가하여 더 간결하고 표현력이 강해진 형태


**EBNF 메타기호**

| 메타 기호 | 의미         |
| -------- | ------------ |
|    []    |  서택적 요소  |
|    {}    | 0번 이상 반복 |
|    ()    |    그룹화    | 

**EBNF 메타기호 [] 사용 예시**
- ex. pop(*key*,*[, default]*)

**BNF와 같은 표기법을 사용하는 이유**
- 서로 다른 프로그래밍 언어, 데이터 형식, 프로토콜 등의 문법을 통일하여 정의하기 위함

>**EBNF 메타 기호의 실용적 활용**
>[]와 같은 EBNF 기호는 파이썬 공식 문서에서 **함수나 메서드의 파라미터**를 설명할 때도 널리 사용됨
>ex. pop(*key*,*[, default]*)처럼 **대괄호([])안에 있는 파라미터는 선택 사항**임을 의미
> 이 기호를 알면 문서만 보고도 어떤 파라미터를 **필수로** 넣어야 하고, 어떤 파라미터를 **생략**할 수 있는지 **한눈에 파악**할 수 있음