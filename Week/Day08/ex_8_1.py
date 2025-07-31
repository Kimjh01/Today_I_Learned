data = {'name': '홍길동'}
try:
    if not data['age']:
        print(data['age'])
except KeyError:
    print('data에는 age라는 키가 없습니다.') 
    data['age'] = 30
    print(data)
# 아래에 코드를 작성하시오.

arr = ['반갑', '하세요', '안녕']
try:
    for i in range(4):
        print(arr.pop())
    print(arr)
    # 아래에 코드를 작성하시오.
except IndexError:
    print(arr)
    print('더 이상 pop 할 수 없습니다.')

try:
    word = '3.15'
    print(int(word))
    # 아래에 코드를 작성하시오.
except ValueError:
    print('정수로 변환 가능한 값을 입력해 주세요.')


