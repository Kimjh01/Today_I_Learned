# 선형 탐색(Linear Search) 개념

Linear Search : 배열의 맨 앞부터 차례대로 값을 비교해가며 target을 찾는 가장 단순한 탐색 기법 

- 장점: 정렬 여부와 무관하게 사용할 수 있고 구현이 매우 간단
- 단점: 최악의 경우 전체 원소를 모두 확인해야 하므로 **시간 복잡도는 O(n)**

---

# 선형 탐색(Linear Search) 구현

## Python Code

```python
def linear_Search(arr, target):
    for i in range(len(arr)):
        if target == arr[i]:
            return i
    return -1

if __name__ == "__main__":
    data = [1, 5, 8, 4, 9, 2, 7, 6]
    print(linear_Search(data, 2))
```

---

## C++ Code

```c++
#include <iostream>

using namespace std;

int linear_search(int arr[], int size, int target){
    for(int i = 0; i < size; i ++){
        if(target == arr[i]) return i;
    }
    return -1;
}

int main(){
    int data[] = {1, 5, 8, 4, 9, 2, 7, 6};
    int n = sizeof(data) / sizeof(data[0]);
    cout << linear_search(data, n, 2);
    return 0;
}

```