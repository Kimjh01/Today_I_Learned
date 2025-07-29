# https://www.acmicpc.net/problem/9086

N = int(input())

for _ in range(N):
    ch = input()
    if len(ch) == 1:
        print(ch*2)
    else: 
        print(ch[0]+ch[-1])