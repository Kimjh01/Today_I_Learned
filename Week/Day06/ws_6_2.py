# 아래 함수를 수정하시오.
def get_value_from_dict(arr, key):
    if arr.keys()!=None:
        result = arr.get(key)
    else: 
        result = 'Unknown'
    return result


my_dict = {'name': 'Alice', 'age': 25}
result = get_value_from_dict(my_dict, 'name')
print(result)  # Alice

result = get_value_from_dict(my_dict, 'gender')
print(result)  # Unknown
