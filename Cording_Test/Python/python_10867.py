# https://www.acmicpc.net/problem/10867

S = input()
N = list(map(int, input().split()))

print(*sorted(set(N)))