# 아래 함수를 수정하시오.
def get_keys_from_dict(dictionary):
    result = list(dictionary.keys())
    return result

def get_all_keys_from_dict(dictionary):
    result = []
    for key in dictionary.keys():
        result.append(key)
        value = dictionary[key]
        if isinstance(value, dict):
            result.extend(get_all_keys_from_dict(value)) 
    return result


my_dict = {'name': 'Alice', 'age': 25}
result = get_keys_from_dict(my_dict)
print(result)  # ['name', 'age']

my_dict = {'person': {'name': 'Alice', 'age': 25}, 'location': 'NY'}
result = get_all_keys_from_dict(my_dict)
print(result)  # ['person', 'name', 'age', 'location']


