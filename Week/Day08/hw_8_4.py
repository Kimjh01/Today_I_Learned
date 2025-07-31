class UserInfo:
    def __init__(self):
        self.user_data = {}

    def get_user_info(self):
        name = input('이름을 입력하세요: ').strip()
        age_input = input('나이를 입력하세요: ').strip()

        if name == '':
            print("사용자 정보가 입력되지 않았습니다.")
            return

        if age_input == '' or not age_input.isdigit():
            print("나이는 숫자로 입력해야 합니다.")
            return

        # 둘 다 정상일 때만 저장
        self.user_data['name'] = name
        self.user_data['age'] = int(age_input)

    def display_user_info(self):
        name = self.user_data.get('name')
        age = self.user_data.get('age')

        if name and age is not None:
            print("사용자 정보:")
            print('이름 :', name)
            print('나이 :', age)
        else:
            print("사용자 정보가 입력되지 않았습니다.")


# 실행
user = UserInfo()
user.get_user_info()
user.display_user_info()
