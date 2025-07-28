# 아래 함수를 수정하시오.
def count_character(char, tatget):
    number = char.count(tatget)
    return number


result = count_character("Hello, World!", "o")
print(result)  # 2
