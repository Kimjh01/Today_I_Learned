class BaseModel:
    PK = 1
    TYPE = 'Basic Model'

    def __init__(self, data_type, title, content, created_at, updated_at):
        self.PK = BaseModel.PK
        self.data_type = data_type 
        self.title = title 
        self.content = content 
        self.created_at = created_at 
        self.updated_at = updated_at
        BaseModel.PK += 1

    def save(self):
        print("데이터를 저장합니다.")

class Novel(BaseModel):
    TYPE = 'Novel'

    def __init__(self, data_type, title, content, created_at, updated_at, author):
        super().__init__(data_type, title, content, created_at, updated_at)
        self.author = author

class Other(BaseModel):
    TYPE = 'Other Model'

class ExtendedModel(Novel, Other):
    def __init__(self, data_type, title, content, created_at, updated_at, author, extended_type):
        super().__init__(data_type, title, content, created_at, updated_at, author)
        self.extended_type = extended_type

    def display_info(self):
        print("ExtendedModel 인스턴스의 정보 출력 및 저장 메서드 호출")
        print(f"PK: {self.PK}, TYPE: {Other.TYPE}, Extended Type: {self.extended_type}")

    def save(self):
        print("데이터를 확장해서 저장합니다.")

extended_instance = ExtendedModel('혼합', '확장 모델', '다중 상속 테스트', 2024, 2025, '확장자', 'Extended Type')

extended_instance.display_info()
extended_instance.save()
