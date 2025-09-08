# Stack 2

## Stack 계산기 

### 후위 표기법 변환

**문자열로 된 계산기**

Stack을 이용하여 값을 계산할 수 있음

문자열 수식 계산의 일반적인 방법

- Step1. 중위 표기법의 수식을 후위 표기법으로 변경 (stack 이용) 
- Step2. 후위 표기법의 수식을 stack을 이용하여 계산

> 중위 표기법(infix notation): 연산자를 피연산자의 가운데 표기하는 방법
> 후위 표기법(postfix notation): 연산자를 피연산자 뒤에 표기하는 방법 

**Step1. 중위 표기법의 후위 표기법 변환 방법 1**

1. 수식의 각 연산자에 대해서 우선 순위에 따라 괄호를 사용하여 다시 표현

2. 각 연산자를 그에 대응하는 오른쪽 괄호의 뒤로 이동

3. 괄호를 제거

> A*B-C/D라는 중위 표기법에서 후위 표기법으로 변환하는 방법
> 1단계: ((A*B)-(C/D))
> 2단계: ((A B)*(C D)/)-
> 3단계: AB*CD/-

**Step1. 중위 표기법의 후위 표기법 변환 방법 2 _ (알고리즘 - Stack 이용)**

1. 입력 받는 중위 표기법에서 토큰을 읽음

2. 토큰이 피연산자면 토큰을 출력

3. 토큰이 연산자(괄호포함)일 때,
    - 이 토큰이 스택의 top에 저장되어 있는 연산자보다 우선순위가 높으면 스택에 push하고,
    - 그렇지 않다면 스택 top의 연산자의 우선순위가 토큰의 우선순위보다 작을 때까지 스택에서 pop한 후 토큰의 연산자를 push 만약 top에 연산자가 없다면 push함

4. 토큰이 오른쪽 괄호 ')'이면 스택 top에 왼쪽 괄호 '('가 올 때까지 스택에 pop연산을 수행하고 pop한 연산자를 출력, 왼쪽 괄호를 만나면 pop만 하고 출력하지 않음

5. 주우이 표기법에 더 읽을 것이 없다면 중지하고, 더 읽을 것이 있다면 1부터 다시 반복

6. 스택에 남아 있는 연산자를 모두 pop하여 출력
    - 스택 밖의 왼쪽 괄호는 우선 순위가 가장 높으며, 스택 안의 왼쪽 괄호는 우선 순위가 가장 낮음

**표기법 변환 설명 개요**

토큰
중위 표기법으로 입력되는 수식
스택의 상태 변화
top -> 스택
후위 표기법으로 출력될 수식

**후위 표기법 변환 1**

1) 토큰 하나 가져오기

2) 스택이 비어 있거나 토큰 우선순위가 top 보다 높으면 push  

3) top 변경: 스택에 쌓여 있는 마지막 값을 가리킴

```python

icp(in-coming priority)
isp(in-stack priority)

if (icp > isp) push()
else pop()

```

| 토큰 | isp | icp |
| --- | --- | --- |
|  )  |  -  |  -  |
| *,/ |  2  |  2  |
| +,- |  1  |  1  |
|  (  |  0  |  0  |

**후위 표기법 변환 2**

1) 토큰 하나 가져오기

2) 피연산자면 출력


**후위 표기법 변환 3**

1) +의 우선 순위가 스택안의 ( 보다 높음, push()

2) top 변경

**후위 표기법 변환 4**

**후위 표기법 변환 5**

1) *가 +보다 높음

**후위 표기법 변환 6**

1) (가 *보다 높음

**후위 표기법 변환 7**

**후위 표기법 변환 8**

1) -가 (보다 높음

**후위 표기법 변환 9**

**후위 표기법 변환 10**

1) 여는 괄호를 만날 때까지 모두 pop()

2) 버림

3) pop() 

4) top 변경 

5) 여는 괄호 버림

6) top 변경

**후위 표기법 변환 11**

1) /보다 낮은 연산자를 만날 때까지 pop() /보다 낮은 연산자일 경우 push()

2) /보다 낮지 않으므로 pop()

3) ->

4) /보다 낮으므로 push() 

**후위 표기법 변환 12**

**후위 표기법 변환 13**

1) 여는 괄호를 만날 때까지 모두 pop()

2) 버림

3) pop() 

4) -> 

5) pop()

6) ->

**후위 표기법 변환 14**

1) 여는 괄호 버림

2) 수식이 끝났고

3) 스택이 비었으면 정상 종료

4) 결과 값(후위표기법 수식)

### 후위 표기법 연산

**Step2.후위 표기법 식을 Stack을 이용하여 계산**

1) 피연산자를 만나면 스택에 push함

2) 연산자를 만나면 필요한 만큼의 피연산자를 스택에서 pop하여 연산하고, 연산결과를 다시 스택에 push함

3) 수식이 끝나면, 마지막으로 스택을 pop하여 출력

**연산과정 1**

후위표기법으로 표현된 수식
스택
피연사자는 스택에 push()

**연산과정 2**

연산자이면 스택에서 피연산자를 두 번 pop() 하여 두개 꺼냄
pop()
pop()
계산결과 스택에 push()

**연산과정 3**
**연산과정 4**
**연산과정 5**
**연산과정 6**
**연산과정 7**
수식에 더 이상 토큰이 없으면 

## Stack 응용

### Backtracking

**Backtracking**

후보해를 구성해 나가다가, 더 이상 해가 될 수 없다고 판단되면 되돌아가서(backtrack) 다른 경로를 시도하는 방법

- 문제 해결을 위한 탐색 알고리즘의 하나
- 가능성이 없는 경로는 더 이상 탐색하지 않고 되돌아가면 해결책을 찾는 방식
- 최적화(Optimization) 문제와 결정(decision) 문제에 적용

적용 예
- N - Queens 문제
- 미로 찾기
- 순열/조합 생성
- 부분집합 탐색
- 스도쿠 풀이

> 결정 문제: 문제의 조건을 만족하는 해가 존재하는지의 여부를 'yes' 또는 'no'가 답하는 문제 

**Backtracking과 DFS와의 차이**

- Prunning(가지치기) 유무: Backtracking은 어떤 node에서 출발하는경로가 해결책으로 이어질 것 같지 않으면 더 이상 그 경로를 따라가지 않고 시도를 줄임

- 조기 경로 차단: DFS는 모든 경로를 추적하지만, Backtracking은 불필요한 경로를 조기에 차단

- 경우의 수가 많은 경우: N!인 경우의 수를 가진 문제에 대해 DFS를 가하면 처리가 불가능, Backtracking을 적용하면 일반적으로 경우의 수가 줄어들지만 최악의 경우 지수함수 시간(Exponential Time)을 요하므로 처리가 불가능

**모든 후보를 검사?**

No !!

**Baxktracking 기법**

- 어떤 노드의 유망성을 점검한 후에 유망(promising)하지 않다고 결정되면 그 노드의 부모로 되돌아가(backtracking) 다음 자식 노드로 이동

- 어떤 노드를 방문하였을 때 그 노드를 포함한 경로가 해답이 될 수 없으면 그 노드는 유망하지않다고 하며, 반대로 해답의 가능성이 있으면 유망하다고 함

- 가지치기(pruning): 유망하지 않는 노드가 포함되는 경로는 더 이상 고려하지 않음

**Baxktracking 진행 절차**

상태 공간 트리의 DFS 실시 -> 각 node가 유망한가 점검 -> 만일 그 node가 유망하지 않으면, 해당 node의 부모 node로 돌아감 -> 돌아간 node에서 검색을 계속함

**일반 Backtracking 알고리즘**

```python 

def checknode(v): # node
    if promising(v):
        if there is a solution at v:
            write the solution
        else:
            for u in each child of v:
                checknode(u)

```

**DFS vs Backtracking**
 
 순수한 DFS
 155 node

VS

 Backtracking
 27 node

### 부분집합

**Powerset**

어떤 집합의 공집합과 자기자신을 포함한 모든 부분

> 구하고자 하는 어떤 집합의 원소 개수가 n일 경우 부분집합의 수는 2^n개

**Backtracking 기법으로 Powerset 만들기**

- 앞에서 설명한 일반적인 Backtracking 접근 방법을 이용
- N개의 원소가 들어있는 집합의 2^n개의 부분집합을 
    - True 또는 False값을 가지는 항목들로 구성된 n개의 배열을 만드는 방법을 이용
- 여기서 배열의 i번째 항목은 i번째의 원소가 부분집합의 값인지 아닌지를 나타내는 값

arr[1, 2, 3] 1 2 3

| arr[1, 2, 3] | [1 2 3] | 
| ------------ | ------- | 
|   부분집합    |   bit   |   
|   [       ]  | [0 0 0] | 
|   [     3 ]  | [0 0 1] | 
|   [   2   ]  | [0 1 0] | 
|   [   2 3 ]  | [0 1 1] | 
|   [ 1     ]  | [1 0 0] | 
|   [ 1   3 ]  | [1 0 1] | 
|   [ 1 2   ]  | [1 1 0] | 
|   [ 1 2 3 ]  | [1 1 1] | 

> arr[i] 원소가 부분집합에 포함되지 않으면 bit[i] == 0
> arr[i] 원소가 부분집합에 포함되면 bit[i] == 1

**각 원소가 부분집합에 포함되었는지를 loop를 이용하여 확인하고 부분집합을 생성하는 방법**

```python

bit = [0, 0, 0, 0]
for i in range(2):
    bit[0] = i                  # 0번째 원소
    for j in range(2):
        bit[1] = j              # 1번째 원소
        for k in range(2):
            bit[2] = k          # 2번째 원소
            for l in range(2):
                bit[3] = l      # 3번째 원소
                print(bit)      # 생성된 부분집합 출력

```

**Powerset을 구하는 Backtracking 알고리즘 1**

```python 

def backtrack(a, k, n): # a 주어진 배열, k 결정할 원소, n 원소 개수
    c = [0] * MAXCANDIDATES

    if k == n: 
        process_solution(a, k) # 답이면 원하는 작업을 함
    else 
        ncandidates = construct_candidates(a, k, n, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k + 1, n)

```

**Powerset을 구하는 Backtracking 알고리즘 2**

```python 

def construct_candidates(a, k, n, c): 
    c[0] = True
    c[1] = False
    return 2

def process_solution(a, k):
    for i in range(k):
        if a[i]:
            print(num[i], end = ' ')
    peint()

```

**Powerset을 구하는 Backtracking 알고리즘 3**

```python 

MAXCANDIDATES = 2
NMAX = 4
a = [0] * NMAX
num = [1, 2, 3, 4]
backtrack(a, 0, 3)

```

### 순열1

**단순하게 순열을 생성하는 방법**

```python

for i1 in range(1, 4):
    for i2 in range(1, 4):
        if i2 != i1:
            for i3 in range(1, 4):
                if i3 != i1 and i3 != i2:
                    print(i1, i2, i3)

```

> 동일한 숫자가 포함되지 않을 때, 각 자리 수 별로 loop을 이용해 표현할 수 있음

**Backtracking을 이용하여 {1, 2, 3, ..., NMAX}에 대한 순열 구하기 1**

- 접근 방법은 부분집합을 구하는 방법과 유사

```python
def backtrack(a, k, n): # a 주어진 배열, k 결정할 원소, n 원소 개수
    c = [0] * MAXCANDIDATES

    if k == n: 
        process_solution(a, k) # 답이면 원하는 작업을 함
    else 
        ncandidates = construct_candidates(a, k, n, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k + 1, n)

```

**Backtracking을 이용하여 {1, 2, 3, ..., NMAX}에 대한 순열 구하기 2**

```python 

def construct_candidates(a, k, n, c): 
    in_perm = [False] * (NMAX + 1)

    for i in range(k):
        in_perm[a[i]] = True

    ncandidates = 0
    for i in range(1, NMAX + 1):
        if in_perm[i] == False:
            c[ncandidates] = i
            ncandidates += 1
    return ncandidates

```

**Backtracking을 이용하여 {1, 2, 3, ..., NMAX}에 대한 순열 구하기 3**

```python 

MAXCANDIDATES = 3
NMAX = 3
a = [0] * NMAX
backtrack(a, 0, 3)

```

### 가지치기

**부분집합의 합**

집합 {1, 2, 3}의 원소에 대해 각 부분집합에서의 포함 여부를 트리로 표현 

I 원소의 포함 여부를 결정하면 i까지의 부분집합의 합 S_{i}를 결정할 수 있음

S_{i-1}이 찾고자 하는 부분집합의 합보다 크면 남은 원소를 고려할 필요가 없음

> f(i, N, s, t), i-1 원소까지의 합 s

A[i] 원소를 부분집합의 원소로 고려하는 재귀 함수(A는 서로 다른 자연수의 집합)

```python

# i-1 원소까지 고려한 합 s, 찾으려는 합 t

f(i, N, s, t)
    if s == t:                  # i - 1 원소까지의 합이 찾는 값인 경우
            ...
    elif i == N:                # 모든 원소에 대한 고려가 끝난 경우
            ...
    elif s > t:                 # 남은 원소를 고려할 필요가 없는 경우
            ...
    else:                       # 남은 원소가 있고 s < t인 경우
        subset[i] = 1
        f(i+1, N, s + A[i], t)  # i 원소 포함
        subset[i] = 0
        f(i+1, N, s, t)         # i 원소 미포함

```

- 추가 고려 사항

고려한 구간 | 
1  2  3  4 | 5  6  7  8  9  10 
고려한 구간의 합 s | 남은 구간의 합 Rs
s > T이면 중단     | S + RS < # T 남은 원소의 합을 다 더해도 찾는 값 T 미만인경우 중단

### 순열2

**A[1, 2, 3]의 모든 원소를 사용한 순열**

3개의 칸에 넣을 수 있는 수를 나열
123, 132, 213, 231, 312, 321
총 6가지의 경우 

**자리 교환으로 순열 생성 1**

1) P[0] 결정
2) P[1] 결정
3) P[2]
4) 완성

```python

f(i, N)
    if i == N # 순열 완성

    else 
        # 가능한 모든 원소에 대해
        P[i] # 결정
        f(i+1, N)
        p[i] # 복구

```

**자리 교환으로 순열 생성 2**

1) P[0] 결정
2) P[1] 결정
3) P[2]
4) 완성

```python

f(i, N)
    if i == N # 순열 완성

    else 
        for j : i -> N - 1
            P[i] <-> P[j]
            f(i+1, N)
            P[i] <-> P[j]
        
```

### 분할정복

**분할정복 알고리즘 유래**

- 1805년 12월 2일 아우스터리츠 전투에서 나폴레옹이 사용한 전략
- 전력이 우세한 연합군을 공격하기 위해 나폴레옹은 연합국의 중앙부로 쳐들어가 연합군을 둘로 나눔
- 둘로 나뉜 연합군을 한 부분씩 격파함

**설계 전략**

- 분할(Divide): 해결할 문제를 여러 개의 작은 부분으로 나눔
- 정복(Conquer): 나눈 작은 문제를 각각 해결
- 통합(Combine): (필요하다면) 해결된 해답을 모음

**거듭 제곱(Exponentiation)**

O(n)

    C^2 = C x C
    C^3 = C x C x C
    ... 
    C^n = C x C x ... x C

```python

def Power(Base,Exponent):
    if Base == 0:
        return 1
    result = 1 # Base^0 은 1 이므로
    for i in range(Exponent)
        result *= Base
    return result 

```

**분할 정복 기반의 알고리즘**

C^8 = C x C x C x C x C x C x C x C
C^8 = C^4 x C^4 = (C^4)^2 = ((C^2)^2)^2
C^9 = C^4 x C^4 x C = (C^4)^2 x C = ((C^2)^2)^2 x C
C^n = C^n/2 x C^n/2     # n이 짝수
    = C^n/2 x C^n/2 x C # n이 홀수

O(log_{2}n)

C^n = C^n/2 x C^n/2     # n이 짝수
    = C^n/2 x C^n/2 x C # n이 홀수

```python

def power(base, exponent):
    if exponent == 0 or base == 0:
        return 1
    
    if exponent % 2 == 0:
        new_base = power(base, exponent/2)
        return new_base * new_base
    else:
        new_base = power(base, (exponent-1)/2)
        return (new_base * new_base) * base

```