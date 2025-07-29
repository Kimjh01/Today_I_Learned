# https://www.acmicpc.net/problem/1152

arr = input().strip()
if arr == "":
    print(0)
else:
    print(arr.count(" ") + 1)
