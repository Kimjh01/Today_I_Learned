# 큐(Queue) 개념 

Stack : **선입선출(Front-In-Front-Out)** 방식의 자료구조, 즉 가장 처음에 큐에 추가된 항목이 먼저 제거 됨

- enqueue(x): 큐의 뒤쪽에 x 삽입
- dequeue(): 큐의 앞쪽에서 요소 제거 후 반환
- front(): 맨 앞 요소 조회(제거하지 않음)
- empty(): 비어 있는지 확인

> 모든 연산이 평균적으로 O(1) 시간에 처리
> 주로 **BFS 탐색, 프로세스 스케줄링, 너비 우선 탐색** 등에 사용

# 큐(Queue) 구현

## Python Code

```python
from collections import deque

class Queue:
    def __init__(self):
        self._data = deque()

    def enqueue(self, x):
        self._data.append(x)

    def dequeue(self):
        if self.empty():
            raise IndexError("dequeue from empty queue")
        return self._data.popleft()

    def front(self):
        if self.empty():
            raise IndexError("front from empty queue")
        return self._data[0]

    def empty(self):
        return not self._data

if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    print(q.front())    # 1
    print(q.dequeue())  # 1
    print(q.empty())    # False

```

## C++ Code

```c++
#include <bits/stdc++.h>
using namespace std;

class Queue {
private:
    deque<int> data;  // 내부 저장소로 deque 사용

public:
    void enqueue(int x) {
        data.push_back(x);
    }
    int dequeue() {
        if (empty()) {
            throw out_of_range("dequeue from empty queue");
        }
        int frontElem = data.front();
        data.pop_front();
        return frontElem;
    }
    int front() const {
        if (empty()) {
            throw out_of_range("front from empty queue");
        }
        return data.front();
    }
    bool empty() const {
        return data.empty();
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    Queue q;
    q.enqueue(1);
    q.enqueue(2);
    cout << q.front() << "\n";   // 1
    cout << q.dequeue() << "\n"; // 1
    cout << (q.empty() ? "Empty\n" : "Not Empty\n"); // Not Empty
    return 0;
}

```
