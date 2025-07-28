food_list = [
    {
        '종류': '한식',
        '이름': '잡채'
    },
    {
        '종류': '채소',
        '이름': '토마토'
    },
    {
        '종류': '중식',
        '이름': '자장면'
    },
]

# 아래에 코드를 작성하시오.
for food in food_list:
    name = food['이름']
    ty = food['종류']
    if name == '토마토':
        ty = '과일'
    if name == '자장면':
        print('자장면엔 고춧가루지')
    print(f'{name} 은/는 {ty} (이)다.')

print(food_list)