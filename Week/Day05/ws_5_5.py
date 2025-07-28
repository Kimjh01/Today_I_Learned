# 아래 함수를 수정하시오.
def even_elements(my_list):
    arr = []
    i = 0
    while i < len(my_list):
        if my_list[i] % 2 == 0:
            arr.extend([my_list[i]])  
            i += 1
        else:
            my_list.pop(i) 
    return arr

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)
