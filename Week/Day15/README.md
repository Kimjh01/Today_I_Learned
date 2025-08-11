```python
import sys

input = sys.stdin.readline

T = int(input().strip())
for tc in range(1, T + 1):
    V, E, A, B = map(int, input().split())

    # 간선 입력은 줄 바꿈이 섞일 수 있어 안전하게 2*E개를 모을 때까지 읽음
    raw = []
    need = 2 * E
    while len(raw) < need:
        raw += list(map(int, input().split()))

    parent = [0] * (V + 1)
    children = [[] for _ in range(V + 1)]

    for i in range(0, need, 2):
        p, c = raw[i], raw[i + 1]
        parent[c] = p
        children[p].append(c)

    # 1) LCA 구하기: A의 조상들을 집합에 넣고, B를 위로 올리며 처음 만나는 곳
    anc = set()
    x = A
    while x:
        anc.add(x)
        x = parent[x]

    y = B
    while y not in anc:
        y = parent[y]

    lca = y

    # 2) 서브트리 크기 계산 (반복 DFS)
    cnt = 0
    stack = [lca]
    while stack:
        node = stack.pop()
        cnt += 1
        stack.extend(children[node])

    print(f"#{tc} {lca} {cnt}")




```