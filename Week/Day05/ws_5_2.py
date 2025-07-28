'''
# 아래 함수를 수정하시오.
def remove_duplicates(arr):
    new_lst = []
    new_lst = list(set(arr))
    return new_lst


result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(result)
'''

# 아래 함수를 수정하시오.
def remove_duplicates(arr):
    new_lst = []
    new_lst = arr
    for idx in range(len(new_lst)):
        if new_lst.count(idx) > 1:
            while new_lst.count(idx) > 1:
                new_lst.pop(idx)

    return new_lst


result = remove_duplicates([1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 4, 4, 5])
print(result)