# https://www.acmicpc.net/problem/10809

S = input()

for i in range(26):
    ch = chr(97 + i)  
    print(S.find(ch), end=' ')
