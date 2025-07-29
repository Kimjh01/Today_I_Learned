# https://www.acmicpc.net/problem/1157

word = input().upper()  
alphabet = [0] * 26

for ch in word:
    alphabet[ord(ch) - 65] += 1  

max_val = max(alphabet)
if alphabet.count(max_val) > 1:
    print("?")
else:
    print(chr(alphabet.index(max_val) + 65))
