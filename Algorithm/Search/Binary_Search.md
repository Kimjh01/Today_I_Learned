# 이진 탐색(Binary Search) 개념

Binary Search : **정렬된 리스트**에서 검색 범위를 줄여 나가면서 특정 값을 빠르게 찾는 알고리즘

* 매 단계마다 탐색 범위를 절반으로 줄이므로 **시간 복잡도는 O(log n)**

## 탐색 단계

1. `low` 를 배열의 시작 Index (0)으로 `high`를 배열의 마지막 Index (n-1)으로 지정
2. `mid = (low+high)/2` 지정
3. 정렬된 배열 `arr[]`에서 `arr[mid]`와 찾고자 하는 특정 값 `target` 비교
    - `if(arr[mid] == target):`, 탐색 성공
    - `if(arr[mid] > target):`, 오른쪽 절반(`high = mid - 1`)을 버리고 왼쪽 절반 탐색
    - `if(arr[mid] < target):`, 왼쪽 절반(`low = mid + 1`)을 버리고 오른쪽 절반 탐색
4. low > high가 되면 탐색 실패


# 이진 탐색(Binary Search) 구현

**정렬된 배열**을 인지하고 탐색을 진행할 것

##Python Code

```python
def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while(low <= high):
        mid = (low + high)//2
        
        if (arr[mid] < target):
            low = mid + 1
        
        elif (arr[mid] > target):
            high = mid - 1
        
        else:
            return True
    
    return False

if __name__ == "__main__":
    data = [1, 2, 3, 4, 6, 7, 9, 11, 13]
    print(binary_search(data, 4))

```

##C++ Code

```c++
#include <iostream>

using namespace std;

bool binary_search(const int arr[], int size, int target){
    int low = 0, high = size - 1;
    while (low <= high){
        int mid = (low+high)/2;
        if (arr[mid] < target){
            low = mid + 1;
        }        
        else if (arr[mid] > target){
            high = mid - 1;
        }        
        else{
            return true;            
        }
    }
    return false;
}


int main(){
    int data[] = {1, 2, 3, 4, 6, 7, 9, 11, 13};
    int n = sizeof(data)/sizeof(data[0]);
    cout << binary_search(data, n, 7) << endl;
    return 0;
}

```
