# 백트래킹 · 트리 · BST · 힙 

**백트래킹 개념**

* 상태공간 트리에서 DFS로 탐색, 유망하지 않은 분기 조기 중단(pruning)
* 완전탐색 대비 탐색 공간 축소, 최악의 경우 지수 시간 유지
* 전형 문제: 순열/조합/부분집합, N-Queens, Sudoku, 그래프 색칠, 해밀턴 경로, 부분합/배낭, 단어 퍼즐

**백트래킹 탐색 흐름**

1. 선택 → 후보 중 하나 선택
2. 적용 → 상태 갱신(방문, 자료구조 업데이트)
3. 검사 → 해답 조건/제약 조건 확인, 불만족 시 백트래킹
4. 진행 → 유망 시 더 깊이 탐색, 아니면 다음 후보
5. 되돌리기 → 다음 분기를 위해 상태 원복(undo)

**가지치기(pruning) 유형**

* 제약 기반 가지치기: 유효성 위반 즉시 중단(예: N-Queens의 열/대각충돌)
* 경계 기반 가지치기(bound): 상한/하한으로 더 나은 해 불가능 판단 시 중단(분기 한정)
* 정렬+조기중단: 정렬 후 남은 합/용량으로 불가능 판단(부분합/배낭)
* 대칭성 제거: 중복되는 대칭 해 배제(퀸의 첫 행 반쪽만 시도)
* 후보 축소(도메인 감소): Sudoku에서 셀 후보 집합 동적 축소(MRV)

**백트래킹 템플릿 (Python)**

```python
def backtrack(path, choices):
    if is_solution(path):
        record(path); return
    for c in get_candidates(path, choices):
        apply(c, path)        # 상태 갱신
        if promising(path):   # 가지치기
            backtrack(path, choices)
        undo(c, path)         # 원복
```

**백트래킹 템플릿 (C++)**

```cpp
bool promising(const State& s);
void backtrack(State& s, Answer& ans){
    if (is_solution(s)) { ans.push_back(s); return; }
    for (auto& c : candidates(s)) {
        apply(s, c);
        if (promising(s)) backtrack(s, ans);
        undo(s, c);
    }
}
```

**순열 패턴 (중복 없음, Python)**

```python
def permutations(nums):
    n=len(nums); used=[False]*n; out=[]
    def dfs(path):
        if len(path)==n: out.append(path[:]); return
        for i,v in enumerate(nums):
            if used[i]: continue
            used[i]=True; path.append(v)
            dfs(path)
            path.pop(); used[i]=False
    dfs([]); return out
```

**조합/부분집합 패턴 (사전식, Python)**

```python
def combinations(nums, k):
    out=[]
    def dfs(start, path):
        if len(path)==k: out.append(path[:]); return
        for i in range(start, len(nums)-(k-len(path))+1):
            path.append(nums[i])
            dfs(i+1, path)
            path.pop()
    dfs(0, []); return out

def subsets(nums):
    out=[]
    def dfs(i, path):
        if i==len(nums): out.append(path[:]); return
        path.append(nums[i]); dfs(i+1, path)   # 포함
        path.pop();          dfs(i+1, path)    # 미포함
    dfs(0, []); return out
```

**부분합(Subset Sum) 가지치기 (정렬+prefix, Python)**

```python
def subset_sum(nums, target):
    nums.sort()
    prefix=[0]
    for x in nums: prefix.append(prefix[-1]+x)
    res=[]
    def dfs(i, cur, s):
        if s==target: res.append(cur[:]); return
        if i==len(nums) or s>target: return
        if s + (prefix[-1]-prefix[i]) < target: return
        cur.append(nums[i]); dfs(i+1, cur, s+nums[i]); cur.pop()
        dfs(i+1, cur, s)
    dfs(0, [], 0); return res
```

**N-Queens 핵심 가지치기**

```python
def nqueens(n):
    cols=set(); d1=set(); d2=set(); board=[['.']*n for _ in range(n)]; ans=[]
    def dfs(r):
        if r==n: ans.append([''.join(row) for row in board]); return
        for c in range(n):
            if c in cols or (r-c) in d1 or (r+c) in d2: continue
            cols.add(c); d1.add(r-c); d2.add(r+c); board[r][c]='Q'
            dfs(r+1)
            board[r][c]='.'; cols.remove(c); d1.remove(r-c); d2.remove(r+c)
    dfs(0); return ans
```

* 해의 수 예시: 4→2, 5→10, 6→4, 7→40, 8→92

**Sudoku 백트래킹 + 비트마스크 (Python)**

```python
def solve_sudoku(board):
    rows=[0]*9; cols=[0]*9; box=[0]*9; empties=[]
    def bit(d): return 1<<(d-1)
    for r in range(9):
        for c in range(9):
            ch=board[r][c]
            if ch=='.': empties.append((r,c))
            else:
                d=int(ch); b=(r//3)*3+(c//3)
                m=bit(d); rows[r]|=m; cols[c]|=m; box[b]|=m
    def cand(r,c):
        b=(r//3)*3+(c//3); used=rows[r]|cols[c]|box[b]
        return [d for d in range(1,10) if not (used&(1<<(d-1)))]
    empties.sort(key=lambda rc: len(cand(*rc)))  # MRV
    def dfs(i=0):
        if i==len(empties): return True
        r,c=empties[i]; b=(r//3)*3+(c//3)
        for d in cand(r,c):
            m=1<<(d-1)
            rows[r]|=m; cols[c]|=m; box[b]|=m; board[r][c]=str(d)
            if dfs(i+1): return True
            rows[r]^=m; cols[c]^=m; box[b]^=m; board[r][c]='.'
        return False
    dfs(); return board
```

**상태공간 트리(예: ABC 순열)**

```
           []
       /     |     \
      A      B      C
     / \    / \    / \
   AB  AC BA  BC  CA  CB
    |   |  |   |   |   |
   ABC ACB BAC BCA CAB CBA
```

**트리 기본 용어**

* 노드, 간선, 루트, 부모/자식, 형제, 조상/후손, 차수, 레벨, 높이, 리프
* 트리의 차수 = 노드 차수 최대값
* 간선 수 = 노드 수 - 1

**이진 트리 종류**

* 포화(perfect) 이진 트리: 모든 내부 노드 자식=2, 모든 리프 동일 깊이, 노드=2^(h+1)-1
* 완전(complete) 이진 트리: 레벨 순서로 왼쪽부터 빈 자리 없이 채움
* 편향(skewed) 이진 트리: 한쪽으로만 이어짐

**이진 트리 성질**

* 레벨 i 최대 노드 수 = 2^i
* 높이 h 최대 노드 수 = 2^(h+1)-1
* 포화 이진 트리 내부노드 I, 리프 L 관계: L = I + 1

**배열 기반 표현(1-based)**

* 루트=1, 부모=i//2, 왼쪽=2i, 오른쪽=2i+1

```
인덱스: 1  2  3  4  5  6  7  8  9 ...
노드  : A  B  C  D  E  F  G  H  I ...
```

**연결 리스트 기반 표현**

```cpp
struct Node{
    int key;
    Node *left, *right;
    Node(int k): key(k), left(nullptr), right(nullptr) {}
};
```

**트리 순회 정의**

* 전위(VLR), 중위(LVR), 후위(LRV), 레벨(BFS)

**트리 순회 코드 (Python)**

```python
def preorder(t, out): 
    if t: out.append(t.key); preorder(t.left,out); preorder(t.right,out)

def inorder(t, out): 
    if t: inorder(t.left,out); out.append(t.key); inorder(t.right,out)

def postorder(t, out): 
    if t: postorder(t.left,out); postorder(t.right,out); out.append(t.key)
```

**레벨 순회(BFS) (Python)**

```python
from collections import deque
def levelorder(t):
    if not t: return []
    q=deque([t]); out=[]
    while q:
        x=q.popleft(); out.append(x.key)
        if x.left: q.append(x.left)
        if x.right: q.append(x.right)
    return out
```

**순회 반복(스택) — 중위**

```python
def inorder_iter(t):
    out=[]; st=[]; cur=t
    while cur or st:
        while cur: st.append(cur); cur=cur.left
        cur=st.pop(); out.append(cur.key); cur=cur.right
    return out
```

**Morris 순회(중위, O(1) 메모리)**

```python
def morris_inorder(root):
    cur=root; out=[]
    while cur:
        if not cur.left:
            out.append(cur.key); cur=cur.right
        else:
            pre=cur.left
            while pre.right and pre.right is not cur:
                pre=pre.right
            if not pre.right:
                pre.right=cur; cur=cur.left
            else:
                pre.right=None; out.append(cur.key); cur=cur.right
    return out
```

**순회 예시 트리**

```
        A
      /   \
     B     C
   /  \   / \
  D    E F   G
 / \    \
H   I    J
```

* 전위: A B D H I E J C F G
* 중위: H D I B J E A F C G
* 후위: H I D J E B F G C A
* 레벨: A B C D E F G H I J

**순회로 트리 재구성(Pre+In) (Python)**

```python
def build_tree_pre_in(pre, ino):
    idx={v:i for i,v in enumerate(ino)}
    it=[0]
    def build(l,r):
        if l>r: return None
        root_val=pre[it[0]]; it[0]+=1
        m=idx[root_val]; node=Node(root_val)
        node.left = build(l, m-1)
        node.right= build(m+1, r)
        return node
    return build(0, len(ino)-1)
```

**BST 정의/성질**

* 왼쪽 서브트리 < 루트 < 오른쪽 서브트리
* 중위 순회 = 오름차순
* 평균 O(log n), 편향 시 O(n)

**BST 연산 — Python**

```python
class BST:
    class N:
        __slots__=("k","l","r")
        def __init__(self,k): self.k=k; self.l=self.r=None
    def __init__(self): self.root=None

    def search(self, k):
        t=self.root
        while t and t.k!=k: t=t.l if k<t.k else t.r
        return t

    def insert(self, k):
        if not self.root: self.root=self.N(k); return
        p=None; t=self.root
        while t:
            p=t
            if k==t.k: return
            t = t.l if k<t.k else t.r
        if k<p.k: p.l=self.N(k)
        else: p.r=self.N(k)

    def _min(self, t):
        while t.l: t=t.l
        return t

    def delete(self, k):
        def _del(t,k):
            if not t: return None
            if k<t.k: t.l=_del(t.l,k)
            elif k>t.k: t.r=_del(t.r,k)
            else:
                if not t.l: return t.r
                if not t.r: return t.l
                s=self._min(t.r)   # 후계자
                t.k=s.k
                t.r=_del(t.r, s.k)
            return t
        self.root=_del(self.root,k)
```

**BST 삭제 그림**

```
case1 리프 삭제(13):
    9               9
   / \             / \
  4  12   →       4  12
     /  \            \
    6   15           15

case2 자식1개(12 삭제 → 15로 대체):
    9               9
   / \             / \
  4  12   →       4  15
    /  \            /
   6   15          6

case3 자식2개(9 삭제 → 후계자 15로 교체):
    9                15
   / \      →       /  \
  4  15            4    17
    /  \               /
   6   17             6
```

**BST 검증(유효성 체크)**

```python
def is_bst(t, lo=float("-inf"), hi=float("inf")):
    if not t: return True
    if not (lo < t.key < hi): return False
    return is_bst(t.left, lo, t.key) and is_bst(t.right, t.key, hi)
```

**정렬 배열 → 높이 균형 BST**

```python
def sorted_to_bst(a):
    def build(l,r):
        if l>r: return None
        m=(l+r)//2; node=Node(a[m])
        node.left=build(l,m-1); node.right=build(m+1,r)
        return node
    return build(0, len(a)-1)
```

**LCA(최소 공통 조상, BST)**

```python
def lca_bst(t, a, b):
    while t:
        if a<t.key and b<t.key: t=t.left
        elif a>t.key and b>t.key: t=t.right
        else: return t
```

**힙(Heap) 정의**

* 완전 이진 트리 기반
* 최대 힙: 부모 ≥ 자식, 최소 힙: 부모 ≤ 자식
* BST 아님(형제/사촌 간 순서 보장 X)

**힙 인덱싱(0-based)**

* parent=(i-1)//2, left=2i+1, right=2i+2

**최대 힙 구현 (Python)**

```python
class MaxHeap:
    def __init__(self): self.a=[]
    def _up(self,i):
        while i>0:
            p=(i-1)//2
            if self.a[p] >= self.a[i]: break
            self.a[p], self.a[i] = self.a[i], self.a[p]; i=p
    def _down(self,i):
        n=len(self.a)
        while True:
            l=2*i+1; r=2*i+2; m=i
            if l<n and self.a[l]>self.a[m]: m=l
            if r<n and self.a[r]>self.a[m]: m=r
            if m==i: break
            self.a[i], self.a[m] = self.a[m], self.a[i]; i=m
    def push(self,x):
        self.a.append(x); self._up(len(self.a)-1)
    def pop(self):
        if not self.a: raise IndexError
        top=self.a[0]; self.a[0]=self.a[-1]; self.a.pop()
        if self.a: self._down(0)
        return top
```

**힙 삽입 그림 (23 삽입, 상향 교환)**

```
      20                 20                 23
     /  \               /  \               /  \
   15    19     →     15    23     →     20    19
  / \   /  \         / \   /  \         / \   /  \
 4  13 11  17       4  13 11  17      4  13 11  17
                 (23 ↔ 19 교환)     (23 ↔ 20 교환)
```

**힙 삭제 그림 (루트 삭제 후 하향 교환)**

```
삭제 전                     루트 제거 후 재배치             재정렬 진행
    20                           10                         19
   /  \            →            /  \           →          /  \
 15   19                       15  19                    15  10
 ...                           ...                       ...
```

**배열을 힙으로 만들기(빌드힙, Floyd, O(n))**

```python
def build_max_heap(a):
    n=len(a)
    def down(i):
        while True:
            l=2*i+1; r=2*i+2; m=i
            if l<n and a[l]>a[m]: m=l
            if r<n and a[r]>a[m]: m=r
            if m==i: break
            a[i],a[m]=a[m],a[i]; i=m
    for i in range((n-2)//2, -1, -1):
        down(i)
```

**힙 정렬(in-place, 오름차순: 최대 힙)**

```python
def heap_sort_inplace(a):
    build_max_heap(a)
    n=len(a)
    for end in range(n-1, 0, -1):
        a[0], a[end] = a[end], a[0]
        i=0; last=end-1
        while True:
            l=2*i+1; r=2*i+2; m=i
            if l<=last and a[l]>a[m]: m=l
            if r<=last and a[r]>a[m]: m=r
            if m==i: break
            a[i],a[m]=a[m],a[i]; i=m
    return a
```

* 불안정 정렬, 추가 메모리 O(1)

**우선순위 큐 활용**

* 삽입/삭제 O(log n), 최대/최소 O(1)
* 작업 스케줄링, 네트워크 이벤트, 다익스트라/프림, K번째 원소

**시간 복잡도 요약**

* 트리 순회 O(n)
* BST 탐색/삽입/삭제 평균 O(log n), 최악 O(n)
* 힙 삽입/삭제 O(log n), 빌드힙 O(n)
* 힙 정렬 O(n log n)

**실수 방지 체크리스트**

* 백트래킹: 방문표시/원복 순서 정확, 후보 중복 제거
* N-Queens: 대각 인덱스 (r-c), (r+c) 혼동 방지
* 트리 배열표현: 0-based/1-based 혼용 금지
* BST 삭제: 두 자식 케이스 후계자 교체 후 원위치 삭제 잊지 않기
* 힙: down() 자식 둘 비교, 경계 인덱스 주의

---

