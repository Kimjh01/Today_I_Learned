# 파라메트릭 탐색(Parametric Search) 개념

Parametric Search : "최적화 문제의 답을 결정 문제(Yes/No)로 바꿔 이분 탐색을 적용" 하는 기법

**전체 시간 복잡도는 O(N · log L)**

**장점**
간결한 구현: “가능/불가능 결정 문제”로 바꾸고 이분 탐색을 적용하기만 하면 돼서 비교적 코드가 단순

일반화 가능: 랜선 자르기 외에도 떡 자르기, 배 공유, 와이파이 신호 세기 등 다양한 최적화 문제에 그대로 응용 가능

정확한 해: 정수 범위에서는 오차 없이 최적의 값을 찾을 수 있음

**단점**
반복 비용: 결정 함수를 매번 O(N)으로 돌려야 하므로, N이나 L이 매우 크면 상수 계수(특히 Python)에서 느려질 수 있음
실수 범위의 오차 처리: 길이가 실수여야 할 경우, 종료 조건과 오차 허용치를 따로 설계해야 해 구현이 복잡


---

## 탐색 단계

1. 결정 문제 정의: “답이 x 이하인가?” 같은 형태로 전환
2. 이분 탐색: 가능한 x의 범위(low, high)를 잡고 중간값 mid에 대해 결정 문제를 확인
3. 범위 축소: 결정 문제의 답이 “가능”이면 high = mid, “불가능”이면 low = mid + 1
4. 종료: low == high일 때 최적값을 찾는다.

> 주요 활용 예: 랜선 자르기, 떡볶이 떡 나누기, 배 공유 문제 등.

---

# 파라메트릭 탐색(Parametric Search) 구현

## Python Code

```python
k, n = map(int, input().split())
data = [int(input()) for _ in range(k)]

left, right = 1, max(data)  
result = 0
while left <= right:
    mid = (left + right) // 2
    total = 0
    for i in data:
        total += i // mid

    if total >= n:
        left = mid + 1
        result = mid
    else:
        right = mid - 1

print(result)
```

---

## C++ Code

```c++
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main(){
    int k, n;
    cin >> k >> n;
    vector<int> data(k);
    for(int i = 0; i < k; i ++){
        cin >> data[i];
    }

    int left = 1, right = *max_element(data.begin(), data.end()),result=0; 
    while(left <= right){
        int mid = (left + right) /2;
        long long total = 0;
        for(int i = 0; i < k; i++) total += data[i] / mid;

        if(total >= n) {
            left = mid + 1;
            result = mid;
        }else right = mid -1;
    }
    cout << result;
    return 0;
}

```
