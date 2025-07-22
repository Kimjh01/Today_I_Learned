## 1. 기본 자료구조

* **배열(Array)**
   – 인덱스로 직접 접근 가능, 연속 메모리
* **문자열(String)**
   – 문자 배열, 슬라이싱·검색·패턴 매칭

## 2. 선형(Linear) 자료구조

* **스택(Stack)**
   – LIFO, 재귀 호출, 괄호 검사, 되돌리기 기능
* **큐(Queue)**
   – FIFO, BFS, 작업 스케줄링
* **덱(Deque)**
   – 양쪽 끝 삽입/삭제, 슬라이딩 윈도우

## 3. 연결(Linked) 자료구조

* **단일 연결 리스트(Singly Linked List)**
* **이중 연결 리스트(Doubly Linked List)**
* **원형 연결 리스트(Circular Linked List)**
    – 삽입·삭제가 빈번한 경우

## 4. 해시(Hash) 기반

* **해시 테이블(Hash Table) / 맵(Map), 언오더드 셋(Unordered Set)**
    – 키-값 저장, 평균 O(1) 조회/삽입/삭제
* **LRU 캐시** (해시 + 덱)

## 5. 트리(Tree)

* **이진 트리(Binary Tree)**
* **이진 탐색 트리(BST)**
* **힙(Heap) / 우선순위 큐(Priority Queue)**
* **세그먼트 트리(Segment Tree)**
    – 구간 합·최댓값 쿼리, 점 업데이트
* **펜윅 트리(Fenwick / BIT)**
    – 부분 합 쿼리, 업데이트
* **트라이(Trie)**
    – 문자열 검색, 사전 문제
* **균형 이진 탐색 트리** (AVL, Red‑Black Tree) — 라이브러리 활용

## 6. 그래프(Graph)

* **인접 리스트/인접 행렬** 표현
* **BFS / DFS**
* **다익스트라, 벨만–포드, 플로이드–워셜**
* **최소 신장 트리(MST)**: 크루스칼, 프림
* **위상 정렬(Topological Sort)**
* **Union‑Find / Disjoint Set Union**
    – 사이클 검출, 집합 합치기

## 7. 기타 응용 구조

* **무지개 테이블 / Bloom Filter** (확률적 집합 검사)
* **스킵 리스트(Skip List)**
* **구간 트리 / 세그먼트 트리 변형** (Lazy Propagation)
* **다항 해시, 롤링 해시** (문자열 패턴 매칭)

---

