def restructure_word(word, arr):
    for check in word:
        if check.isdecimal(): 
            for _ in range(int(check)):
                if arr:    
                    arr.pop()
        else:             
            if check in arr:
                arr.remove(check)
    return arr

original_word = '코딩 공부는ㄴ 1일ㄹ 1커ㅓ밋ㅅ @@@#^()#_+!&~:"'
word = '1ㄴ2ㄹ3ㅓ4ㅅ5'
arr = list(original_word)

print(arr)

result = restructure_word(word, arr)

print(result)

print("".join(result))
