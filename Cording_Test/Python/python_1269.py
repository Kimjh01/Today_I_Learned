# https://www.acmicpc.net/problem/1269

N, M = map(int, input().split())

arr_1 = set(map(int, input().split()))
arr_2 = set(map(int, input().split()))
num1 = arr_1 - arr_2
num2 = arr_2 - arr_1
num = len(num1) + len(num2)
print(num)