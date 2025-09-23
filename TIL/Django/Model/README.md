# Django 3 _ Model

## Model

데이터베이스와 Python 클래스(객체)로 추상화된 형태로 상호작용

> Django의 강력한 기능: 개발자가 데이터베이스에 대한 깊은 지식 없이도 쉽게 데이터 관리 가능
유지보수 및 확장성 증대: 데이터베이스 변경 시에도 코드 수정 최소화, 재사용 가능한 데이터 모델을 통해 개발 효율성 향상

- urls.py: 사용자 요청의 시작점
- views.py: 요청을 처리하고 models.py를 통헤 데이터를 다룸
- models.py: 데이터베이스를 정의하고, 데이터베이스와 상호작용
- templates: views.py로부터 받은 데이터를 사용자에게 보여줄 화면을 구성

### Model Class

DB의 테이블을 정의하고 데이털ㄹ 조작할 수 있는 기능들을 제공

> Model class는 데이터베이스 테이블의 구조를 설계하는 청사진(blueprint) 역할을 함
어떤 데이터(컬럽)을 저장할지, 그 데이터의 형태는 어떠할지(타입, 길이 등)를 Python 코드로 명확히 정의

**Model 클래스 작성**

- 앱 폴더(`articles/`) 안의 **`models.py`*- 파일에 작성
- 예시 코드:

  ```python
  # articles/models.py
  from django.db import models

  class Article(models.Model):
      title = models.CharField(max_length=10)
      content = models.TextField()
  ```

**Model 클래스 → DB 테이블**

- 작성한 모델 클래스는 DB에 테이블로 변환됨
- Django가 자동으로 `id` 기본 키(primary key) 필드를 추가
- 위 코드 기준 최종 테이블 구조:

  | id | title | content |
  | -- | ----- | ------- |
  | .. | ..    | ..      |

**Model 클래스의 상속**

- `class Article(models.Model):`
- `models.Model` 은 Django에서 제공하는 부모 클래스
- 개발자는 **테이블 구조(컬럼 정의)*- 만 작성하면 되고, 나머지 DB 동작 관련 코드는 이미 구현되어 있음

**클래스 변수명 = 테이블 컬럼명**

- `title` → `title` 컬럼
- `content` → `content` 컬럼

즉, 모델의 속성이 곧 DB 테이블의 필드 이름이 됨

**Model Field**

- **Model Field = DB 컬럼의 정의**
- 데이터 타입과 제약 조건을 설정
- 예시:

  - `CharField(max_length=10)` → 길이 제한 있는 문자열 필드
  - `TextField()` → 긴 문자열 저장 가능

> `CharField`의 `max_length`는 SQLite에서는 강제되지 않지만,
> 유효성 검사 및 데이터 명확성을 위해 명시적으로 지정하는 것을 권장.


**모델 클래스는 DB 테이블의 설계도**
→ `models.py`에 작성 → Django ORM이 SQL로 변환 → DB 테이블 생성

---

## Model Field

DB 테이블의 필드(열)정의 데이터 타입 및 제약 조건 명시

> Django는 이러한 필드 정의를 바탕으로 데이터베이스 컬럼을 자동으로 생성하고, 데이터 입력 시 유효성 검사 등 필요한 기능을 제공 
정확한 필드 정의는 애플리케이션의 안정성을 높이는 데 필수적

1. Field types (필드 유형)
- 데이터베이스에 저장될 "데이터의 종류"를 정의

2. Field options (필드 옵션)
- 필드의 "동작"과 "제약 조건"을 정의

```python
  # articles/models.py
  from django.db import models

  class Article(models.Model):
      title = models.CharField(max_length=10)
      content = models.TextField()
```
### Field typeds

데이터베이스에 저장될 "데이터의 종류"를 정의 
(models 모듈의 클래스로 정의되어 있음)

```python
  # articles/models.py
  from django.db import models

  class Article(models.Model):
      title = models.CharField(max_length=10)
      content = models.TextField()
```

**CharField()**

제한된 길이의 문자열을 저장
(필드의 최대 길이를 결정하는 max_length는 선택 옵션)

**TextField()**

길이 제한이 없는 대용량 텍스트를 저장
(무한대는 아니며 사용하는 시스템에 따라 달라짐)

**주요 필드 유형**

문자열 필드 
- CHarField, TextField

숫자 필드
- IntegerField, FloatField

날짜/시간 필드
- DateField, TimeField, DateTimeField

파일 관련 필드 
- FileField. ImageField

> 다양한 Django 모델 필드 유형을 모두 다루기는 어려움, 필요한 필드 유형은 Django 공싱 문서를 참고하여 찾아 사용

### Field options

**Field options**

필드 "동작"과 "제약 조건"을 정의

```python
  # articles/models.py
  from django.db import models

  class Article(models.Model):
      title = models.CharField(max_length=10)
      content = models.TextField()
```

**제약 조건**

Constraint

특정 규칙을 강제하기 위해 테이블의 열이나 행에 적용되는 규칙이나 제한사항 

> 숫자만 저장되도록 제한을 두거나, 문자가 100자 까지만 저장되도록 하는 등의 제한 조건을 의미 

**주요 필드 옵션**

null
- 데이터베이스에서 NULL 값을 허용할지 여부를 결정 (기본값: False)

blank 
- form에서 빈 값을 허용할지 여부를 결정 (기본값: False)

defailt 
- 필드의 기본값을 설정 

> 다양한 Django 모델 필드 유형만큼이나 필드 옵션 또한 매우 다양, 각 모델 필드가 어떤 옵션을 가질 수 있는지는 Django 공식 문서를 참고하여 필요에 맞게 찾아 사용하시길 권장

---

## Migrations

model 클래스의 변경사항(필드 생성, 수정 삭제 등)을 DB에 최종 반영하는 방법

> 모든 변경 사항이 코드로 관리되어 협업 시 모델 변경 내역에 대한 추적과 공유가 수월함 

**Django 모델 클래스와 Migration 과정**

모델 정의부터 마이그레이션 파일 생성까지

```python
# articles/models.py
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
```

```bash
$ python manage.py makemigrations
```

``` bash
Migrations for 'articles':
  articles/migrations/0001_initial.py
    + Create model Article
```

- 모델 클래스 작성/수정

  - Django에서는 Python 클래스로 정의

    - CharField: 제한된 길이의 문자열 저장
    - TextField: 길이 제한 없는 대용량 텍스트

- 마이그레이션 파일 생성 명령어

  - Python 코드로 된 migration 파일(설계도)을 만드는 방법

> 모델 변경을 감지하고 migration 파일을 생성하는 명령어
  migration 파일 == 최종 설계도

- 생성된 최종 설계도(0001_initial.py) 마이그레이션 파일을 DB에 반영하기

폴더 구조:

```
articles/migrations/0001_initial.py
```

```bash
$ python manage.py migrate
```

- 마이그레이션 파일(0001_initial.py)

  - 마이그레이션 파일은 모델 변경사항을 기록한 Python 코드
  > 마이그레이션 파일은 DB 테이블 변경 내역을 순차적으로 저장하여 추적 관리

- SQL 실행(자동 변환)

  - migrate 명령어는 마이그레이션 파일의 Python 코드를 SQL 문으로 자동 변환
  - 변환 과정: Python 코드 → 번역 → SQL 쿼리문 → 데이터베이스 실행

> SQL: DB를 조작하는데 사용되는 표준 질의 언어

**Migrations 과정 핵심 정리**

- model class (설계도 초안)
  → makemigrations
  → migration 파일(0001_initial.py) (최종 설계도)
  → migrate
  → db.sqlite3 (DB)

**Migrations 핵심 명령어 2가지**

```bash
$ python manage.py makemigrations
```

- 역할: model class를 기반으로 최종 설계도(migration)를 작성

```bash
$ python manage.py migrate
```

- 역할: 최종 설계도를 DB에 전달하여 반영

> 마이그레이션 파일은 되도록이면 직접 건드리면 안됨
  migrations 폴더에 자동으로 생성된 파일들은 직접 수정하거나 삭제하지 않는 것이 원칙

**Migration 경고 메시지**

- Django 서버를 시작할 때 출력되는 migration 관련 경고 메시지

  - 이 메시지는 프로젝트 실행 시 **미적용 마이그레이션 파일**이 있을 때 나타냄

예시:

```bash 
$ python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
```

해결방법

- 경고 메시지에 명시된 대로 `python manage.py migrate` 명령어를 실행

중요한 이유

- 최신 모델 변경 사항이 데이터베이스에 반영되지 않아 프로젝트가 제대로 작동하지 않을 수 있음

### + Migrations

**이미 생성된 테이블에 필드를 추가해야 한다면?**

이미 기존 테이블이 존재하는 경우, 새 필드를 추가할 때 문제가 발생할 수 있음

- 기존에 레코드가 있는 테이블에 새로운 필드를 추가하면 어떤 값으로 채울지 결정해야 함
- Django의 makemigrations 실행 시 기본값 설정을 요구하는 프롬프트가 표시 됨

| id | title | content | created_at | updated_at |
| -- | ----- | ------- | ---------- | ---------- |
| .. | ..    | ..      | ..         | ..         |
| .. | ..    | ..      | ..         | ..         |
| .. | ..    | ..      | ..         | ..         |

**Migration 과정 – 추가 모델 필드 작성**

새로운 필드 작성

- 모델 클래스 수정
  Django 기존 모델을 수정

```python
# articles/models.py
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    # --------------------------
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # --------------------------
```

> Model Field: `models.필드유형(필드 옵션)`

**DateTimeField의 필드 옵션 (optional)**

auto_now

- 데이터가 저장될 때마다 자동으로 현재 날짜시간을 저장

auto_now_add

- 데이터가 **처음 생성될 때만*- 자동으로 현재 날짜시간을 저장

새로운 필드 추가 후 `makemigrations` 명령어 입력

```bash
$ python manage.py makemigrations
```
- 이미 기존 테이블이 존재하기 때문에 필드를 추가할 때 필드의 기본값 설정이 필요
- 선택지:
  1. 현재 대화를 유지하면서 직접 기본 값을 입력하는 방법
  2. 대화를 나가 models.py에 기본 값 관련 설정을 하는 방법

출력 예시:

``` bash 
It is impossible to add the field 'created_at' with 'auto_now_add=True' to article without providing a default.
This is because the database needs something to populate existing rows.
1) Provide a one-off default now which will be set on all existing rows
2) Quit and manually define a default value in models.py.
Select an option:
```

옵션 1: 일회성 기본값 제공 
  - 현재 대화형 프롬프트에서 기본값을 직접 입력
  - 입력한 기본값은 기존의 모든 데이터 행에 적용

- 추가하는 필드의 기본 값을 입력해야 하는 상황
- 날짜 데이터이기 때문에 직접 입력하기보다 Django가 제안하는 기본 값을 사용하는 것을 권장
- 아무것도 입력하지 않고 Enter → Django 제안 기본값으로 설정됨

출력 예시:

```bash 
Please enter the default value as valid Python.
Accept the default 'timezone.now' by pressing 'Enter' or provide another value.
The datetime and django.utils.timezone modules are available, so it is possible to provide e.g. timezone.now as a value.
Type 'exit' to exit this prompt
[default: timezone.now] >>>
```

- migrations 과정 종료 후 두 번째 migration 파일이 생성됨 확인
- Django는 설계도를 쌓아가며 추후 문제 발생 시 복구하거나 되돌릴 수 있도록 함
  (마치 `git commit`과 유사)

출력 예시:

```bash 
Migrations for 'articles':
  articles/migrations/0002_article_created_at_article_updated_at.py
    + Add field created_at to article
    + Add field updated_at to article
```

폴더 구조:

```bash 
migrations/
 ├─ __pycache__/
 ├─ __init__.py
 ├─ 0001_initial.py
 └─ 0002_article_created_at_article_updated_at.py
```

migrate 후 테이블 확인

```bash
$ python manage.py migrate
```

DB 테이블 `articles_article`에 새로운 컬럼 추가됨:

```bash 
articles_article/
 └─ Columns/
    ├─ id (INTEGER)
    ├─ title (varchar(10))
    ├─ content (TEXT)
    ├─ created_at (datetime)
    └─ updated_at (datetime)
```

**언제 Migration이 필요한가?**

- model class에 변경사항(1) 이 생겼다면,
- 반드시 새로운 설계도를(makemigrations)(2) 생성하고,
- 이를 DB에 반영(migrate)(3) 해야 한다.

정리:

```bash
(1) model class 생성/수정 → (2) makemigrations → (3) migrate
```

---

## Admin site

### 관리자 인터페이스

Automatic admin interface
- Django가 추가 설치 및 설정 없이 자동으로 제공하는 관리자 인터페이스 

> Django 관리자 인터페이스는 추가 설정 없이 자동 생성되는 웹 기반 관리 도구

> 주요 기능: 데이터베이스 모델의 CRUD(생성, 읽기, 업데이트, 삭제) 작업을 간편하게 수행할 수 있음

> 활용: 빠른 프로토타이핑, 비개발자 데이터 관리, 내부 시스템 구축에 이상적

**Django admin 계정 생성**
1. 터미널 열기 
- Django 프로젝트 폴더로 이동해서 터미널을 엶 (manage.py 파일이 있는 위치에서 진행하면 됨)

2. 관리자 계정 생성 명령어 입력
```bash
$ python manage.py createsuperuser 
```

3. 정보 입력
- 사용자 이름 (username): 관리자 페이지에 로그인할 때 사용할 아이디를 입력
- 이메일 (email address): 선택 사항이라 입력하지 않고 엔터를 눌러 넘어가도 됨
- 비밀번호 (password): 로그인할 때 사용할 비빌번호 입력(비빌번호 입력 시 콘솔 창에 아무것도 나타나지 않음)
- 비밀번호 확인 (password(again)): 비밀번호를 한 번 더 입력해서 확인 ㄴ

**DB에 생성된 admin 계정 확인**

```sql
SELECT - FROM auth_user;
```
- id, username, password 해시, is_superuser, is_staff, is_active 등이 기록됨
- 예시: `username=admin`, `is_superuser=1`, `is_staff=1`

**관리자 페이지 접속**

- 브라우저에서 `http://127.0.0.1:8000/admin` 접속
- `createsuperuser`에서 만든 계정으로 로그인

 
**관리자 페이지 초기 화면**

- 로그인 직후에는 **기본 User, Group 모델**만 보임
- 우리가 만든 `Article` 모델은 **추가 설정 필요**

**Admin에 모델 등록**

- `articles/admin.py` 수정

```python
# articles/admin.py
from django.contrib import admin
from .models import Article

admin.site.register(Article)
```

- `Article` 모델이 admin site에 표시되도록 등록

**Admin 사이트에서 모델 확인**

- 다시 admin 페이지 접속
- `ARTICLES` 섹션에 `Article` 모델이 표시됨
- `Add`, `Change` 버튼을 통해 CRUD 가능

**CRUD 테스트**
1. 생성(Create)

- `Add Article` 버튼 클릭
- `title`, `content` 입력 후 저장

2. 조회(Read)

- 목록 화면에서 등록된 Article 확인
- DB(`articles_article` 테이블)에서도 데이터 확인 가능

3. 수정(Update)

- 등록된 Article 클릭 → 내용 수정 → 저장

4. 삭제(Delete)

- Article 상세 페이지에서 **Delete*- 버튼 클릭 → 삭제 확인

> **admin 계정 생성 → admin 접속 → 모델 등록 → CRUD 확인**까지 연결

- 모델이 잘못 등록되지 않았다면 admin 페이지에 보이지 않음
- DB에서도 실시간으로 반영 여부 확인 가능

---

## 데이터베이스 초기화

**Django 데이터베이스 초기화**

1. Migration 파일 삭제

- `articles/migrations/` 폴더 안에서 자동 생성된 마이그레이션 파일 삭제

  - `0001_initial.py`
  - `0002_article_created_at_article_updated_at.py`

- 삭제 금지:

  - `__init__.py`
  - `migrations` 폴더 자체

2. db.sqlite3 파일 삭제

- SQLite DB 자체를 삭제하여 완전 초기화

---

## Migrations 관련

**Migrations 기타 명령어**

1. showmigrations

  ```bash
  $ python manage.py showmigrations
  ```
  - 현재 마이그레이션 파일들이 적용되었는지 여부 확인
  - `[X]` 표시 → migrate 완료됨

2. sqlmigrate

```bash
$ python manage.py sqlmigrate articles 0001
```

- 지정한 migration 파일이 실제 **SQL문**으로 어떻게 변환되는지 확인 가능
- ORM → SQL 변환 과정을 직접 살펴볼 수 있음
- python manage.py sqlmigrate <앱 이름> <마이그레이션 이름>

**최초 migrate 시 출력 내용이 많은 이유**

- Django에는 이미 여러 **내장 app**이 포함되어 있음
  (`admin`, `auth`, `contenttypes`, `sessions`, `messages`, `staticfiles` 등)
- 이 앱들의 기본 migration 파일도 함께 `migrate` 되기 때문에 로그가 길게 출력됨

예시:

```bash
$ python manage.py migrate
Applying contenttypes.0001_initial... OK
Applying admin.0001_initial... OK
Applying auth.0001_initial... OK
...

```

---

## SQLite 

Django 기본 데이터베이스 (DB 관리 시스템)

특징
  - 파일 기반: `db.sqlite3` 하나의 파일로 데이터 저장, 설치/설정 없이 간편하게 복사/이동/백업
  - 가볍고 빠름: 별도 서버 불필요, 소규모 프로젝트에 최적화
  - 높은 호환성: 다양한 운영체제 및 언어에서 사용 가능

**SQLite 주의사항**

- `db.sqlite3`는 Git 등 버전 관리에 포함시키지 않는 것이 원칙
  - 데이터 변경 시마다 **파일 전체**가 변경되기 때문

- SQLite 파일은 로컬 컴퓨터에 저장된 데이터 기록 
- `.gitignore` 파일에 반드시 `db.sqlite3` 추가하여 Git 버전 관리에서 제외해야 함

> .gitignore: git 버전 관리 시스템에서 특정 파일이나 폴더를 추적하지 않도록 설정하는 파일

 



