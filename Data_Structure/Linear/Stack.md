# 스택(Stack) 개념 

Stack : **후입선출(Last-In-Front-Out)** 방식의 자료구조, 즉 가장 마지막에 스택에 추가된 항목이 먼저 제거 됨

* push(x) : 스택의 맨 위(top)에 x를 추가
* pop() : 스택의 맨 위 요소 제거 및 반환
* top()/peek() : 스택의 맨 위 요소 조회(제거하지 않음)
* empty() : 스택이 비어 있는지 확인

> 모든 연산이 평균적으로 O(1) 시간에 처리
> 주로 **함수 호출, 괄호 검사, 그래프 탐색(DFS), 표현식 계산, 되돌리기 기능**등에 활용

## 구현 방식

1. 배열 기반(Array-based)
* 배열과 인덱스(top 포인터)를 사용
* 장점: 메모리 연속 할당으로 캐시 효율이 좋음
* 단점: 크기를 미리 정해야 하거나, 재할당(resize)이 필요

2. 링크드 리스트 기반(Linked-list‑based)
* 노드(Node)와 포인터로 연결
* 장점: 크기 제한이 없고, 삽입/삭제 시 메모리 이동 불필요
* 단점: 포인터 관리 오버헤드 및 캐시 효율 저하

# 스택(Stack) 구현

## Python Code

```python
class Stack:
    def __init__:
        self.data() = []
    
    def push(self, x):
        self._data.append(x)

    def pop():
        if self.empty():
            raise IndexError("Pop from empty stack")
        return self._data.pop()

    def top(self):
        if self.empty():
            raise IndexError("top from empty stack")
        return self._data[-1]

    def empty(self):
        return len(self._data) == 0


if __name__ == "__main__":
    st = stack()
    st.push(10)
    st.push(20)
    print(st.top()) #20
    print(st.pop()) #20
    print(st.empty()) #False

```

## C++ Code

```c++
#include <iostream>
#include <stack>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    stack<char> st;
    st.push('A');
    st.push('B');
    st.push('C');

    cout << st.top() << '\n';   // C
    char popped = st.top();
    st.pop();
    cout << popped << '\n';     // C
    cout << (st.empty() ? "Empty\n" : "Not Empty\n");

    return 0;
}

```
