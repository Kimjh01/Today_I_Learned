# 완전 탐색

## 반복과 재귀

**반복(iteration)과 재귀(Recursion)은 유사한 작업을 수행할 수 있음**

반복은 수행하는 작업이 완료될 때 까지 계속 반복
- 루프 (for, while 구조)
- 반복문은 코드를 n 번 반복시킬 수 있음

재귀는 주어진 문제의 해를 구하기 위해 동일하면서 더 작은 문제의 해를 이용하는 방법
- 하나의 큰 문제를 해결할 수 있는(해결하기 쉬운) 다 직은 문제로 쪼개고 결과들을 결합
- 재귀호출은 n 중 반복문과 같은 효과

**재귀호출로 N 중 for문 구현**
- N 입력 후 111... ~ 333 ... 출력하는 문제는 for문으로 구현이 어려움

```python

path = []
N = 3

def run(lev):
    if lev == N:
        print(path)
        return
    for i in range(1,4):
        path.append(i)
        run(lev + 1)
        path.pop()

# N = int(input())
run(0)

```

**재귀를 연습하기 전, 알아야 할 함수의 특징 1**
- KFC 함수 호출할 때, int 타입 객체를 전달하면 값만 복사됨
- min 함수의 x와, KFC함수의 x는 서로 다른 객체
    - 한국에 사는 kim과 미국에 사는 kim이 이름만 같고, 서로 다른 사람인 것과 같음

**재귀를 연습하기 전, 알아야 할 함수의 특징 2**
- 함수가 끝나면, 해당 함수를 호출했던 곳으로 돌아옴

**재귀호출 공부의 시작은, 무한 재귀호추를 막는 것 부터 시작**

아래 if문을 "기저조건 (base case)" 이라고 함

```python

def KFC(x):
    if x == 2:
        return 
    
    print(x)
    KFC(x+1)
    print(x)

KFC(0)
print('end')

```

**재귀호출 코드가 1개**
-

## 순열

**순열이란?**

서로 다른 N 개에서, R개를 중복 없이, 순서를 고려하여 나열하는 것

- 순열을 중복을 취급하지 않음!

**중복 순열이란?**

서로 다른 N 개에서, R개를 **중복을 허용하고**, 순서를 고려하여 나열하는 것

**중복순열 구현 원리**
1) 재귀호출을 할 때 마다, 이동 경로를 흔적으로 남김! 
2) 가장 마지막 레벨에 도착했을 때, 이동 경로를 출력

**Permutation**
- 먼저 path라는 전역 리스트를 준비
- 그리고 Level 2, Breach 3으로 동작하는 재귀 코드 구현

```python

path = []

def KFC(x):
    if x == 2:
        return 
    
    for i in range(3):
        KFC(x+1)

KFC(0)

```

- 재귀호출을 하기 직전에 이동할 곳의 위치를 path 리스트에 기록

```python

path = []

def KFC(x):
    if x == 2:
        return 
    
    for i in range(3):
        path.append(i)
        KFC(x+1)

KFC(0)

```

- 재귀호출 됨. 그리고 코드가 계속 진행되어, path.append(i)를 수행

- 두번 재귀호출 되었고, 이제 바닥에 도착했으니 출력하는 코드를 수행

```python

path = []

def KFC(x):
    if x == 2:
        print(path)
        return 
    
    for i in range(3):
        path.append(i)
        KFC(x+1)

KFC(0)

```

- 함수가 리턴 되고, 함수가 즉시 종료됨
- 이후 path에 적은 마지막 기록이 삭제되어야 함

```python

path = []

def KFC(x):
    if x == 2:
        print(path)
        return 
    
    for i in range(3):
        path.append(i)
        KFC(x+1)
        path.pop()

KFC(0)

```

- 이어서 for문이 진행되고, 변수 i값은 1이 됨
- path 배열 마지막에 1이 삽입됨

- 재귀호출이 된 후, path 리스트를 출력

- 중복 순열 소스코드 완성 -> [0,0]~[2,2] 까지 출력하는 소스코드

```python

path = []

def KFC(x):
    if x == 2:
        print(path)
        return 
    
    for i in range(3):
        path.append(i)
        KFC(x+1)
        path.pop()

KFC(0)

```

**중복을 취급하지 않는 "순열" 구현 방법**
1) 중복순열 코드를 작성
2) 중복을 제거하는 코드를 추가하면 순열 코드가 됨

**중복을 제거하는 원리**
- 전역 리스트를 사용으로 이미 선택했던 숫자인지 아닌지 구분

- 이를 used 배열 또는 visited 배여리라 부름
    - DFS, DFS에 사용되는 것과 같음

**중복을 제거한 순열 생성 예시**
- 0을 선택하고 재귀호출 한 후에는, 또 다시 0을 선택하지 못하도록 막아야 함
- 재귀 호출을 하기 직전, 이미 선택했던 숫자인지 아닌지 검사하는 코드가 필요

**중복을 제거한 순열 생성 예시**
- 이미 사용한 숫자인지 아닌지 구분하는 List 준비
- 전역으로 used 라는 리스트를 준비

```python 

used = [False, False, False]

# 또는

used = [False for _ in range(3)]

```

**중복을 제거한 순열 생성 예시**
1) 이미 사용을 한 숫자인지 아닌지 검사해주는 소스코드 추가
2) 만약 이미 사용한 숫자일 경우, 재귀호출을 생략하는 코드를 추가
3) 처음 사용하는 숫자라면 used에 기록
4) 모든 처리가 끝나고 돌아왔다면 used에서 기록을 지움


```python

path = []
used = [False, False, False]

def KFC(x):
    if x == 2:
        print()
        return 

    for i in range(3):
        if used[i] == True:
            continie
        used[i] = True
        path.append(i)
        KFC(x+1)
        path.pop()
        used[i] = False

KFC(0)

```

## 완전탐색

**Brute-Force**
모든 가능한 경우를 모두 시도를 해보고 정답을 찾아내는 알고리즘

**완전 탐색 문제 1**

주사위 눈의 합

- 먼저 합을 출력하는 코드를 작성
- 재귀호출을 할 때마다 선택한 값의 누적합을 구함

- 파라미터에 sum을 추가하여 구현
    - sum: 지금까지 구한 합
    - i: 선택한 주사위 눈금

- 재귀호출 할 때 sum + i 값을 전달 

```python

path = []

def kfc(x, sum):
    if x == 3:
        print(f'{path} = {sum}')
        return 
    
    for i in range(1, 7):
        path.append(i)
        kfc(x + 1, sum + i)
        path.pop()
    
kfc(x: 0, sum: 0)

```

- sum이 <= 10 이하 일 때만 출력
- 실제로는 모두 탐색하지만, 출력만 하지 않는 방법

```python

path = []

def kfc(x, sum):
    if x == 3:
        if sum <= 10:
            print(f'{path} = {sum}')
        return 
    
    for i in range(1, 7):
        path.append(i)
        kfc(x + 1, sum + i)
        path.pop()
    
kfc(x: 0, sum: 0)

```

- 가지치기: 답이 아닌 것에 대해 즉시 되돌아감

- 누적합이 10이 넘어가는 순간 더 탐색할 필요 없음

```python

path = []

def kfc(x, sum):

    if sum > 10:
        return 

    if x == 3:
        print(f'{path} = {sum}')
        return 
    
    for i in range(1, 7):
        path.append(i)
        kfc(x + 1, sum + i)
        path.pop()
    
kfc(x: 0, sum: 0)

```

**완전탐색 문제 2**

연속 3장의 트럼프 카드

- A, J, Q, K 네 종류의 카드들이 충분히 있음
- 이 중, 5장의 카드를 뽑아 나열

    - A A A A A
    - A A A A J
    - ...
    - K K K K K

- 같은 종류의 카드가 세장 연속으로 나오는 경우의 수는?

- 모든 경우에 대해 다 시도하기
1) 순열 코드를 작성 
    - 먼저 [A, J, Q, K] 카드에 대해 [AAAAA ~ KKKKK]까지 출력
    - 같은 종류의 연속 세장이 나왔다면 Counting 

2) 같은 종류의 연속 세장이 나왔다면 Counting

```python

card = ['A', 'J', 'Q', 'K']
path =  []

def permu(lev):
    if lev == 5:
        print(path)
        return 
    
    for i in range(4):
        path.append(card[i])
        permu(lev + 1)
        path.pop()

permu(0)

```

- 같은 카드가 연속 세장인지 검사하는 코드
- cont_three()
    - 연속 세장이 있으면 True를 리턴
    - 아니면 False를 리턴

```python

def cont_three():
    if path[0] == path[1] == path[2]: return True
    if path[1] == path[2] == path[3]: return True
    if path[2] == path[3] == path[4]: return True
    return False

```

전체코드 

```python

card = ['A', 'J', 'Q', 'K']
path =  []
cnt = 0

def cont_three():
    if path[0] == path[1] == path[2]: return True
    if path[1] == path[2] == path[3]: return True
    if path[2] == path[3] == path[4]: return True
    return False

def permu(lev):
    global cnt
    if lev == 5:
        if cont_three():
            cnt += 1
        return 
    
    for i in range(4):
        path.append(card[i])
        permu(lev + 1)
        path.pop()

permu(0)
print(cnt)

```

**완전탐색 문제 3**

Baby - gin 

* 0 이상 9 이하의 숫자가 적힌 **6장의 카드**가 주어짐
* **Run**: 3장의 카드가 연속적인 번호를 갖는 경우 (예: 0-1-2)
* **Triplet**: 3장의 카드가 같은 번호를 갖는 경우 (예: 7-7-7)
* 6장의 카드가 `run`과 `triplet`으로만 구성된 경우를 **Baby-gin**이라고 함

예시)

* 카드 `0 1 2 7 7 7` → (012 run, 777 triplet) → Baby-gin 
* 카드 `6 6 7 7 6 7` → (666 triplet, 777 triplet) → Baby-gin 
* 카드 `1 0 1 1 2 3` → 어떤 조합으로도 Baby-gin 안됨

**풀이 방법**

1. 6장의 카드로 만들 수 있는 **모든 순열**을 생성
2. 각 순열을 두 그룹(앞 3장, 뒤 3장)으로 나누어 검사
3. 두 그룹이 모두 **run 또는 triplet**이면 Baby-gin

```python
from itertools import permutations

def is_run_or_triplet(arr):
    # triplet 검사
    if arr[0] == arr[1] == arr[2]:
        return True
    # run 검사
    if arr[0] + 1 == arr[1] and arr[1] + 1 == arr[2]:
        return True
    return False

def is_baby_gin(cards):
    for perm in permutations(cards, 6):
        if is_run_or_triplet(perm[:3]) and is_run_or_triplet(perm[3:]):
            return True
    return False

cards1 = [0, 1, 2, 7, 7, 7]
cards2 = [6, 6, 7, 7, 6, 7]
cards3 = [1, 0, 1, 1, 2, 3]

print(is_baby_gin(cards1))  
print(is_baby_gin(cards2))  
print(is_baby_gin(cards3))  
```
