# 분할 정복

## 분할 정복 기법

**분할 정복 기법의 개념**

문제를 작은 하위 문제로 나누고(분할) 각각을 해결(정복)한 뒤, 그 결과를 결합(통합)하여 원래 문제를 해결하는 알고리즘 기법

**분할 정복 기법의 설계 전략**
- 분할(Divide): 해결할 문제를 여러 개의 작은 부분으로 나눔
- 정복(Conquer): 나눈 작은 문제를 각각 해결
- 통합(Combine): (필요하다면) 해결된 해답을 모음

**분할 정복 기법의 예시**
- 가짜 동전 찾기

n 개의 동전들 중에 가짜 동전이 하나 포함되어 있음
가짜 동전은 진짜 동전에 비해 아주 조금 가벼움
진짜 동전들의 무게가 동일하다고 할 때 양팔 저울을 이용해서 가짜 동전을 찾자

- 양팔 저울을 최소로 사용해서 가짜 동전을 찾는 방법은 무엇?
- 예를 들어 동전이 24(진짜 23, 가짜 1)개 있다면?

**분할 정복 기법의 예시 - 거듭제곱**

- 반복 알고리즘

* 시간 복잡도 $O(n)
* 원소를 \$n\$번 곱해서 제곱 계산
* 예시

  * \$C^2 = C \times C\$
  * \$C^3 = C \times C \times C\$
  * \$C^n = C \times C \times \cdots \times C\$

* 의사코드

  ```
  Iterative_Power(x, n)
      result ← 1
      FOR i in 1 → n
          result ← result * x
      RETURN result
  ```

- 분할 정복 알고리즘

* 시간 복잡도 O(\log n)
* 지수를 절반으로 줄여가며 계산
* 짝수일 때

  \$C^n = \left(C^{\tfrac{n}{2}}\right) \times \left(C^{\tfrac{n}{2}}\right)\$

* 홀수일 때

  \$C^n = \left(C^{\tfrac{n-1}{2}}\right) \times \left(C^{\tfrac{n-1}{2}}\right) \times C\$

* 예시

  \$C^8 = \left(\left(C^2\right)^2\right)^2\$

* 의사코드

  ```
  Recursive_Power(x, n)
      IF n == 1 : RETURN x
      IF n is even
          y ← Recursive_Power(x, n/2)
          RETURN y * y
      ELSE
          y ← Recursive_Power(x, (n-1)/2)
          RETURN y * y * x
  ```

---

## 병합 정렬 

- Merge Sort: 여러 개의 정렬된 자료의 집합을 병합하여 한 개의 정렬된 집합으로 만드는 방식

* 시간 복잡도 O(n \log n)
* top - down 방식
* 자료를 최소 단위의 문제까지 나눈 후에 차례대로 정렬하여 최종 결과를 얻어냄

**분할 단계**

전체 집합을 반으로 쪼갬 → 최소 크기까지 분할

**병합 단계**

두 집합을 정렬하면서 합침 → 하나의 정렬된 리스트 완성

**예시**

* 입력: {69, 10, 30, 2, 16, 8, 31, 22}
* 결과: {2, 8, 10, 16, 22, 30, 31, 69}

**의사코드**

```
merge_sort(LIST m)
    IF length(m) == 1 : RETURN m

    middle ← length(m) / 2
    left ← merge_sort(m[0:middle])
    right ← merge_sort(m[middle:])

    RETURN merge(left, right)
```

```
merge(LIST left, LIST right)
    result ← []

    WHILE left not empty OR right not empty
        IF left not empty AND right not empty
            IF first(left) <= first(right)
                append popfirst(left) to result
            ELSE
                append popfirst(right) to result
        ELIF left not empty
            append popfirst(left) to result
        ELIF right not empty
            append popfirst(right) to result

    RETURN result
```

---

## 퀵 정렬

Quick Sort: 기준값을 중심으로 주어진 배열을 두 개로 분할하고, 각각을 정렬하여 전체 배열을 정렬하는 방식 

**병합 정렬과 퀵 정렬의 차이**

|          |              병합 정렬                 |                       퀵 정렬                       |
| -------- | ------------------------------------- | ---------------------------------------------------|
| 분할 기준 |        단순히 배열을 반으로 나눔        | 기준 아이템(pivot item)을 중심으로 기준보다 작은 것을 왼편, 큰 것을 오른 편에 위치 시킴 |
| 병합 처리 | 정렬된 부분을 다시 병합하는 과정이 필요함 | 별도의 병합 과정 불필요 |

* 시간 복잡도: 평균 O(n \log n)
* Partitioning 이라는 과정을 반복하면서, 빠른 속도로 정렬이 되는 알고리즘

### Partitioning

1. **작업 영역 지정**

    * 현재 정렬해야 하는 배열 구간 선택

2. **Pivot 결정**

    * 일반적으로 가장 왼쪽 원소를 pivot으로 선택
    * 중간값이나 오른쪽 값을 pivot으로 선택해도 무방

3. **Pivot을 기준으로 재배치**

    * pivot보다 작은 값은 왼쪽으로 이동
    * pivot보다 큰 값은 오른쪽으로 이동
    * 이때 각각의 구간 내부는 정렬되지 않음

4. **왼쪽 부분 재귀 Partitioning**

    * pivot 고정 후, 왼쪽 부분 배열을 새로운 작업 영역으로 지정
    * 다시 pivot 선택
    * pivot 기준으로 왼쪽/오른쪽 재배치
    * pivot 위치 고정

5. **오른쪽 부분 재귀 Partitioning**

    * pivot 고정 후, 오른쪽 부분 배열을 새로운 작업 영역으로 지정
    * pivot 선택
    * pivot 기준으로 재배치 후 위치 고정

6. **Pivot 위치 확정 (Fix)**

    * partitioning이 끝나면 pivot의 위치는 고정
    * 이후 재귀적으로 왼쪽 구간과 오른쪽 구간에 대해 partitioning 반복
    * 작업 영역이 원소 1개라면 pivot 위치가 자동으로 Fix
    * 더 이상 Partitioning 필요 없음

**의사코드**

```
quick_sort(LIST A, int left, int right)
    IF left < right
        pivot ← partition(A, left, right)
        quick_sort(A, left, pivot - 1)
        quick_sort(A, pivot + 1, right)

partition(LIST A, int left, int right)
    pivot ← A[left]
    low ← left + 1
    high ← right

    WHILE low ≤ high
        WHILE low ≤ right AND A[low] ≤ pivot
            low ← low + 1
        WHILE high ≥ left+1 AND A[high] ≥ pivot
            high ← high - 1
        IF low < high
            swap A[low], A[high]

    swap A[left], A[high]
    RETURN high
```

**List Partitioning 예시**

초기 배열:

```
[6, 9, 5, 1, 3, 13, 10]
```

1. 첫 Pivot = 6

```
[1, 3, 5, 6, 9, 13, 10]
```

→ pivot(6) Fix

2. 왼쪽 \[1, 3, 5] → pivot = 1

```
[1, 3, 5]
```

→ pivot(1) Fix

3. \[3, 5] → pivot = 3

```
[3, 5]
```

→ pivot(3) Fix

4. 오른쪽 \[9, 13, 10] → pivot = 9

```
[9, 10, 13]
```

→ pivot(9) Fix

5. \[10, 13] → pivot = 10 Fix

- 최종 결과:

```
[1, 3, 5, 6, 9, 10, 13]
```

---

**Quick Sort 알고리즘 (의사 코드)**

```pseudo
quickSort(A[], l, r):
    if l < r:
        s ← partition(A[], l, r)
        quickSort(A[], l, s - 1)
        quickSort(A[], s + 1, r)
```

---

**Hoare Partition (의사 코드)**

```pseudo
partition(A[], l, r):
    p ← A[l]        //p: pivot
    i ← l, j ← r
    while i ≤ j:
        while i ≤ j and A[i] ≤ p: i++
        while i ≤ j and A[j] ≥ p: j--
        if i < j: swap(A[i], A[j])
    swap(A[l], A[j])
    return j
```

**Hoare Partition 아이디어**

* **Pivot 값보다 작은 원소** → 왼쪽
* **Pivot 값보다 큰 원소** → 오른쪽
* Pivot은 항상 **좌/우 그룹 사이의 올바른 위치**에 자리 잡게 됨

**Hoare Partition 과정**

1. Pivot을 맨 왼쪽 원소로 설정
2. `i`는 pivot 다음 인덱스, `j`는 배열의 끝에서 시작
3. `i`는 Pivot보다 큰 값을 찾을 때까지 증가, `j`는 Pivot보다 작은 값을 찾을 때까지 감소
4. `i < j`면 두 원소를 교환
5. 교차되면 Pivot과 `j`를 교환하여 Pivot을 제 위치에 둠

결과: Pivot 기준으로 작은 값과 큰 값이 나뉘며, Pivot은 고정(Fix)

**Hoare Partition 예시**

초기 배열:

```
[6, 9, 5, 1, 3, 13, 10]
```

1. **첫 Pivot = 6 (왼쪽 첫 원소)**

   * i → 오른쪽으로 이동하며 pivot보다 큰 값 찾음
   * j → 왼쪽으로 이동하며 pivot보다 작은 값 찾음
   * 교환 반복

```
[6, 9, 5, 1, 3, 13, 10]
 i                 j
```

2. i=9(>6), j=10(>6), j 더 왼쪽 → j=3(<6) 발견

   * swap i=9과 j=3

```
[6, 3, 5, 1, 9, 13, 10]
```

3. 다시 i=5(<6), i=9(>6), j=1(<6) swap

```
[6, 3, 1, 5, 9, 13, 10]
```

4. i ≥ j 교차 → pivot(6)과 j=5 교환

```
[5, 3, 1, 6, 9, 13, 10]
```

→ pivot(6) Fix

**이후 재귀 과정**

* 왼쪽 `[5, 3, 1]` → 정렬 후 `[1, 3, 5]`
* 오른쪽 `[9, 13, 10]` → 정렬 후 `[9, 10, 13]`

**최종 결과:**

```
[1, 3, 5, 6, 9, 10, 13]
```

## Lomuto Partition 과정

1. Pivot을 배열의 마지막 원소로 설정
2. `i`를 `p-1`에서 시작
3. `j`를 `p`부터 `r-1`까지 순회하며,

   * `A[j] ≤ Pivot`이면 `i++` 후 `A[i]`와 `A[j]`를 교환
4. 최종적으로 `A[i+1]`과 Pivot을 교환

결과: Pivot 기준으로 배열이 나뉘며, Pivot은 고정

**Lomuto Partition 예시**

초기 배열:

```
[6, 9, 5, 1, 3, 13, 10]
```

1. **첫 Pivot = 마지막 원소(10)**

   * i=-1, j=0부터 n-2까지 순회
   * pivot보다 작거나 같으면 i 증가 후 swap

```
Pivot = 10
```

2. j=0 → 6 ≤ 10 → i=0 → swap(6,6)

```
[6, 9, 5, 1, 3, 13, 10]
```

3. j=1 → 9 ≤ 10 → i=1 → swap(9,9)

```
[6, 9, 5, 1, 3, 13, 10]
```

4. j=2 → 5 ≤ 10 → i=2 → swap(5,5)

```
[6, 9, 5, 1, 3, 13, 10]
```

5. j=3 → 1 ≤ 10 → i=3 → swap(1,1)

```
[6, 9, 5, 1, 3, 13, 10]
```

6. j=4 → 3 ≤ 10 → i=4 → swap(3,3)

```
[6, 9, 5, 1, 3, 13, 10]
```

7. j=5 → 13 ≤ 10? ❌ pass

마지막 → pivot과 `i+1=5` swap → swap(13,10)

```
[6, 9, 5, 1, 3, 10, 13]
```

→ pivot(10) Fix


**이후 재귀 과정**

* 왼쪽 `[6, 9, 5, 1, 3]` → 정렬 후 `[1, 3, 5, 6, 9]`
* 오른쪽 `[13]` → 이미 Fix

**최종 결과:**

```
[1, 3, 5, 6, 9, 10, 13]
```

* **Hoare Partition**

  * 교환 횟수가 적음 → 평균적으로 빠름.
  * 하지만 구현이 조금 더 까다롭다.

* **Lomuto Partition**

  * 코드가 간단하고 직관적임.
  * 교환이 많아질 수 있어 성능이 조금 떨어질 수 있음.

**차이 요약**

* **Hoare**: pivot을 양쪽에서 좁혀오며 교환, pivot이 중간에 고정됨
* **Lomuto**: pivot을 마지막 원소로 두고 작은 값들을 앞으로 모은 후 마지막에 pivot 교환

둘 다 최종 결과는 같지만,

* Hoare → 교환 횟수 적고 성능 우수
* Lomuto → 구현 간단, 직관적

---

## 이진 검색 

Binary Search

* 자료의 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법
* 시간 복잡도: 평균/최악 모두 O(\log n)

> 목적 키를 찾을 때까지 이진 검색을 순환적으로 반복 수행함으로써 검색 범위를 반으로 줄여가면서 보다 빠르게 검색을 수행


**이진 검색 과정**

1. 배열의 중앙 원소 선택
2. 중앙값과 찾고자 하는 값 비교

   * 같으면 탐색 성공
   * 찾고자 하는 값이 더 작으면 **왼쪽 반 구간**에서 탐색
   * 더 크면 **오른쪽 반 구간**에서 탐색

3. 찾을 때까지 1~2 과정을 반복

※ 전제 조건: **데이터는 반드시 정렬된 상태여야 한다**

**예시 1 (성공 사례)**

* 배열: `[2, 4, 7, 9, 11, 19, 23]`
* 목표 값: `7`

탐색 과정:

1. 중앙 = 9 → `7 < 9` → 왼쪽 탐색
2. 중앙 = 4 → `7 > 4` → 오른쪽 탐색
3. 중앙 = 7 → 찾음 

**예시 2 (실패 사례)**

* 배열: `[2, 4, 7, 9, 11, 19, 23]`
* 목표 값: `20`

탐색 과정:

1. 중앙 = 9 → `20 > 9` → 오른쪽 탐색
2. 중앙 = 19 → `20 > 19` → 오른쪽 탐색
3. 중앙 = 23 → `20 ≠ 23` → 탐색 실패

**반복 구조 (Iterative)**

```python
def binary_search(arr, key):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
    return -1
```

**재귀 구조 (Recursive)**

```python
def binary_search_recursive(arr, low, high, key):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == key:
        return mid
    elif key < arr[mid]:
        return binary_search_recursive(arr, low, mid - 1, key)
    else:
        return binary_search_recursive(arr, mid + 1, high, key)
```

**분할 정복 알고리즘 정리**

- 병합 정렬
    - 외부 정렬(External Sort)의 기본이 되는 정렬 알고리즘
    - 멀티코어(Multi-Core) Cpu나 다수의 프로세서에서 정렬 알고리즘을 병렬화하기 위해 병합 정렬 알고리즘이 활용

- 퀵 정렬
    - 매우 큰 입력 데이터에 대해서 좋은 성능을 보이는 알고리즘

- 이진 정렬
    - 정렬된 데이터를 기준으로 특정 값이나 범위를 검색하는 데 사용
    - [이진 검색을 활용한 심화 학습 키워드] Lower Bound, Upper Bound
        - 정렬된 배열에서 특정 값 이상(이하)가 처음으로 나타나는 위치를 찾는 알고리즘
        - 특정 데이터의 범위 검색 등에서 활용


