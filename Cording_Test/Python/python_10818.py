# https://www.acmicpc.net/problem/10818

N = int(input())
arr = []
arr = list(map(int, input().split()))
print(min(arr), max(arr))