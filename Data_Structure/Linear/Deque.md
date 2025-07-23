# 덱(Deque) 개념 

Deque : **양쪽 끝에서 삽입과 삭제**가 가능한 자료구조

- push_front(x): 앞쪽에 x 삽입
- push_back(x): 뒤쪽에 x 삽입
- pop_front(): 앞쪽에서 요소 제거 후 반환
- pop_back(): 뒤쪽에서 요소 제거 후 반환
- front(): 앞쪽 요소 조회
- back(): 뒤쪽 요소 조회
- empty(): 비어 있는지 확인
- size(): 요소 개수 반환

> 모든 연산이 평균적으로 O(1) 시간에 처리
> **큐와 스택을 모두 구현할 수 있고, 슬라이딩 윈도우, 캐시 구현(LRU), 양방향 BFS** 등에 활용

# 큐(Queue) 구현

## Python Code

```python
ffrom collections import deque

class Deque:
    def __init__(self):
        self._data = deque()

    def push_front(self, x):
        self._data.appendleft(x)

    def push_back(self, x):
        self._data.append(x)

    def pop_front(self):
        if self.empty():
            raise IndexError("pop_front from empty deque")
        return self._data.popleft()

    def pop_back(self):
        if self.empty():
            raise IndexError("pop_back from empty deque")
        return self._data.pop()

    def front(self):
        if self.empty():
            raise IndexError("front from empty deque")
        return self._data[0]

    def back(self):
        if self.empty():
            raise IndexError("back from empty deque")
        return self._data[-1]

    def empty(self):
        return not self._data

    def size(self):
        return len(self._data)

if __name__ == "__main__":
    dq = Deque()
    dq.push_back(1)
    dq.push_front(2)
    print(dq.front(), dq.back())  # 2 1
    print(dq.pop_front())         # 2
    print(dq.pop_back())          # 1
    print(dq.empty())             # True

```

## C++ Code

```c++
#include <bits/stdc++.h>
using namespace std;

class Deque {
private:
    deque<int> data; 

public:
    void push_front(int x) {
        data.push_front(x);
    }

    void push_back(int x) {
        data.push_back(x);
    }

    int pop_front() {
        if (empty()) {
            throw out_of_range("pop_front from empty deque");
        }
        int val = data.front();
        data.pop_front();
        return val;
    }

    int pop_back() {
        if (empty()) {
            throw out_of_range("pop_back from empty deque");
        }
        int val = data.back();
        data.pop_back();
        return val;
    }

    int front() const {
        if (empty()) {
            throw out_of_range("front from empty deque");
        }
        return data.front();
    }

    int back() const {
        if (empty()) {
            throw out_of_range("back from empty deque");
        }
        return data.back();
    }

    bool empty() const {
        return data.empty();
    }

    int size() const {
        return data.size();
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    Deque dq;
    dq.push_back(1);
    dq.push_front(2);
    cout << dq.front() << " " << dq.back() << "\n"; // 2 1
    cout << dq.pop_front() << "\n";                 // 2
    cout << dq.pop_back() << "\n";                  // 1
    cout << (dq.empty() ? "Empty\n" : "Not Empty\n"); // Empty
    return 0;
}


```
