# Django 4 _ ORM

## ORM

object-Relational-Mapping

객체 지향 프로그래밍 언어의 객체(Object)와 데이터베이스의 데이터를 매핑(Mapping)하는 기술

> 개발자 친화적인 데이터베이스 인터페이스

**문제 상황: 언어 차이로 인한 소통 불가**

Django는 Python 언어를 사용하지만 데이터베이스는 SQL 언어를 사용

```bash

    -> python object -> 
django               Database
        <-  SQL  <-

```

**ORM의 역할: 번역자 역할**

ORM은 Django와 데이터베이스 사이에서 언어 번역자 역할을 수행

```bash

    -> python object -> 
django      ORM       Database
        <-  SQL  <-

```

> '통역사'가 중간에서 언어를 번역해 주는 것과 같음, 데이터베이스 구조를 잘 몰라도 파이썬 코드로 쉽게 데이터를 다룰 수 있음

**Django의 데이터 상호작용: ORM이 일하는 방법**

ORM은 Django 개발자를 위해 'QuerySet API'라는 특별한 도구를 제공

  - QuerySet API는 ORM의 기능을 개발자가 Python 코드 안에서 객체 지향적이고 직관적인 방식으로 데이터베이스를 조작할 수 있도록 제공하는 인터페이스 

## QuerySet API

데이터베이스의 복잡한 SQL 쿼리문을, 직관적인 Python 코드로 다룰 수 있게 해주는 강력한 번역기

> 개발자는 SQL을 직접 작성하지 않고도, .filter(), .exclude(), .order_by() 등 파이썬다운 메서드를 사용하여 원하는 데이터를 손쉽게 생성, 조회, 수정, 삭제할 수 있음

**QuerySet API와 ORM의 동작 방식**

1. Django -> DB: Django(QuerySet API)에서 ORM을 통해 데이터베이스로 정보를 요청할 때

  - SQL 쿼리로 변환되어 데이터베이스로 전달됨 

2. DB -> Django: 데이터베이스가 요청에 대한 응답을 보낼 때

  - ORM은 이 SQL 결과를 다시 파이썬이 이해할 수 있는 Python Object 
  - QuerySet 또는 Instance 형태로 변환하여 Django로 변환 

```bash

      ->              QuerySet API           ->    
django  (python object)     (ORM)     (SQL)    Database
      <-         'QuerySet' or 'Instance'     <-

```

**QuerySet API 구문 기본 구조**

```python 
Article.objects.all()
```

Article(모델 클래스)

- 역할: 데이터베이스 테이블에 대한 Python 클래스 표현
- articles_article 테이블의 스키마(필드, 데이터 타입 등)를 정의하며, Django ORM이 데이터베이스와 상호작용할 때 사용하는 기본적인 구조체 

objects(매니저, manager)

- 역할: 데이터베이스 조회(Query) 작업을 위한 기본 인터페이스
- 모델 클래스가 데이터베이스 쿼리 작업을 수행 할 수 있도록 하는 진입점
- Django는 모든 모댈에 Objects라는 이름의 맨저를 자동으로 추가하며, 이 매니저를 통해 .all(), .filter() 등의 쿼리 메서드를 호출

all(QuerySet API 메서드)

- 역할: 특정 데이터베이스 작업을 수행하는 명령
- 매니저를 통해 호출되는 메서드로, 해당 모델과 연결된 테이블의 모든 레코드(rows)를 조회하라는 SQL 쿼리를 생성하고 실행 

**QuerySet API와 ORM의 동작 방식 예시**

```bash

      -> 1) QuerySet API           -> 2) 전체 게시글 줘   
django  (python object)     (ORM)     (SQL)    Database
      <- 4) 'QuerySet' or 'Instance' <- 3) 전체 게시글 받아 

```

**Query란?**

- 데이터베이스에 특정한 데이터를 보여 달라는 요청

- "쿼리문을 작성한다."

  - "원하는 데이터를 얻기 위해 데이터베이스에 요청을 보낼 코드를 작성"

- Django에서 Query가 처리되는 과정 정리

  1. 파이썬 코드 -> ORM: 개발자의 QuerySet API(파이썬 코드)가 ORM으로 전달
  2. ORM -> SQL 변환: ORM이 이를 데이터베이스용 SQL 쿼리로 변환하여 데이터베이스에 전달
  3. DB 응답 -> ORM: 데이터베이스가 SQL 쿼리를 처리하고 결과 데이터를 ORM에 반환 
  4. ORM -> QuerySet 변환: ORM이 데이텁이스의 결과를 QuerySet(파이썬 객체) 형태로 변환하여 우리에게 전달 

**QuerySet이란?**

- 데이터베이스에서 전달받은 객체 목록(데이터 모음)
- **순회*- 가능한 데이터로 1개 이상 데이터를 불러와 사용 가능함 
- Django ORM을 통해 만들어진 자료형
- 단, 데이터베이스가 단일 객체를 반환할 때는 QuerySet이 아닌 모델(Class)의 인스턴스로 반환됨

## QuerySet API 실습

**CRUD란?**
대부분의 소프트웨어가 가지는 기본적인 데이터 처리 기능인 생성, 조회, 수정, 삭제를 묶어 이르는 말

> Django에서는 QuerySet API를 통해, 복잡한 SQL문 없이 Python코드로 이러한 CRUD 작업을 직관적으로 수행할 수 있음 
> Create(저장), Read(조회), Update(갱신), Delete(삭제)

### Create 

**QuerySet API 실습 사전 준비**

외부 라이브러리 설치 및 의존성 기록
  - IPython은 일반 파이썬 셸(명령창)보다 자동 완성 등 편리한 파이썬 작업 환경을 만들어주는 도구 

```bash 
$ pip install ipython 

$ pip freeze > requirements.txt
```

Django Shell 접속하기: Django Shell이란?

- Django 프로젝트의 코드를 명령창에서 바로 실행하고 테스트하는 특별한 파이썬 환경 
- Django 환경 내에서 실행되기 때무에 입력하는 QuerySet API 구문이 Django 프로젝트에 영향을 미침

Django Shell 접속하기 

```bash
$ python manage.py shell
```

Shell "-v" 옵션 (기본값: 1)

- 출력 상세도(verbosity level) 설정: 일반적인 정보 외에 더 많은 디버깅 정보나 진행 상황 메시지를 보여달라는 요청 
- 아래 예시는 shell 시작 시 Django 프로젝트에 등록된 model이 자동으로 import 된 내용이 출력된 것 

```bash
$ python manage.py shell -v 2
```

**데이터 객체를 만드는(생성하는) 3가지 방법**

1. 빈 객체 생성 후 값 할당 및 저장
2. 초기 값과 함께 객체 생성 및 저장
3. create() 메서드로 한 번에 생성 및 저장

**첫번째 방법: 빈 객체 생성 후 값 할당 및 저장**

```python
# 특정 테이블에 새로운 행을 추가하여 데이터 추가
>>> article = Article()   # Article(class)로부터 article(instance) 생성
>>> article
<Article: Article object (None)>

>>> article.title = 'first'      # 인스턴스 변수(title)에 값 할당
>>> article.content = 'django!'  # 인스턴스 변수(content)에 값 할당
```

```python
# save를 하지 않으면 아직 DB에 값이 저장되지 않음
>>> article
<Article: Article object (None)>
>>> Article.objects.all()
<QuerySet []>
```

```python
# save를 호출하고 확인하면 저장된 것을 확인
>>> article.save()
>>> article
<Article: Article object (1)>

>>> article.id
1
>>> article.pk
1

>>> Article.objects.all()
<QuerySet [Article: Article object (1)]>
```

```python
>>> article.title
'first'

>>> article.content
'django!'

>>> article.created_at
datetime.datetime(2023, 6, 30, 6, 55, 42, 322526, tzinfo=datetime.timezone.utc)
```

**두번째 방법: 초기 값과 함께 객체 생성 및 저장**

```python
>>> article = Article(title='second', content='django!')
# 아직 저장 되어있지 않음
>>> article
<Article: Article object (None)>

# save를 호출해야 저장됨
>>> article.save()

>>> article
<Article: Article object (2)>

>>> Article.objects.all()
<QuerySet [<Article: Article object (1)>, <Article: Article object (2)>]>
```

```python
# 값 확인
>>> article.pk
2
>>> article.title
'second'
>>> article.content
'django!'
```

- 첫번째 방법 두번째 방법 모두 결국 Save 메서드를 호출해야 비로소 DB에 데이터가 저장됨
- 테이블에 한 행(레코드)이 쓰여진 것 

**save() 메서드란?**

객체를 데이터베이스에 저장하는 인스턴스 메서드 

> save()가 필요한 경우 -> 객체를 먼저 생성한 후, 데이터베이스에 저장하기 전에 추가적인 처리 
> ex. (다른 데이터와 관계 설정, 유효성 검사)가 필요할 때 호출

**세번째 방법: create() 메서드로 한 번에 생성 및 저장**

```python
# 위 2가지 방법과 달리 바로 저장 이후 바로 생성된 데이터가 반환된다.
>>> Article.objects.create(title='third', content='django!')
<Article: Article object (3)>
```

> save()를 명시적으로 호출하지 않는 것처럼 보이는 이유는 create() 메서드 자체가 객체 생성과 데이터베이스 저장을 한 번에 처리하는 단축 메서드이기 때문 

### Read

**대표적인 조회 메서드**

QuerySet 반환 메서드 
- all()
- filter()

QuerySet을 반환하지 않은 메서드 
- get()

> QuerySet: 데이터베이스에서 전달받은 객체 목록 

**QuerySet 반환 메서드: all()**

전체 데이터 조회 

```python
>>> Article.objects.all()
<QuerySet [<Article: Article object (1)>, <Article: Article object (2)>, <Article: Article object (3)>]>
```

**QuerySet 반환 메서드: filter()**

주어진 매개변수와 일치하는 객체를 포함하는 QuerySet 반환 

```python
>>> Article.objects.filter(content='django!')
<QuerySet [<Article: Article object (1)>, <Article: Article object (2)>, <Article: Article object (3)>]>

>>> Article.objects.filter(title='abc')
<QuerySet []>

>>> Article.objects.filter(title='first')
<QuerySet [<Article: Article object (1)>]>
```

**QuerySet 반환하지 않는 메서드: get()**

주어진 매개변수와 일치하는 객체를 반환 

```python
>>> Article.objects.get(pk=1)
<Article: Article object (1)>

>>> Article.objects.get(pk=100)
DoesNotExist: Article matching query does not exist.

>>> Article.objects.get(content='django!')
MultipleObjectsReturned: get() returned more than one Article -- it returned 2!
```

**get()의 특징**

- 객체를 찾을 수 없으면 DoseNotExist 예외를 발생시키고, 둘 이상의 객체를 찾으면 MultipleObjectReturned 예외를 발생시킴 
- 위와 같은 특징을 가지고 있기 때문에 primary key와 같이 고유성(uniqueness)을 보장하는 조회에서 사용

> Primary key(pk): DB 테이블에서 각 행을 고유하게 식별할 수 있는 속성 

```python
>>> Article.objects.get(pk=1)
<Article: Article object (1)>

>>> Article.objects.get(pk=100)
# DoesNotExist: Article matching query does not exist.

>>> Article.objects.get(content='django!')
# MultipleObjectsReturned: get() returned more than one Article -- it returned 2!
```

### Update

**데이터 수정 방법**

인스턴스 변수를 변경 후 save 메서드 호출

```python
# 수정할 인스턴스 조회
>>> article = Article.objects.get(pk=1)

# 인스턴스 변수를 변경
>>> article.title = 'byebye'

# 저장
>>> article.save()
```

### Delete

**데이터 삭제 방법**

삭제하려는 데이터 조회 후 delete 메서드 호출 

```python
# 삭제할 인스턴스 조회
>>> article = Article.objects.get(pk=1)

# delete 메서드 호출 (삭제된 객체가 반환)
>>> article.delete()
(1, {'articles.Article': 1})

# 삭제한 데이터는 더 이상 조회할 수 없음
>>> Article.objects.get(pk=1)
DoesNotExist: Article matching query does not exist.
```

## ORM with view

### 전체 게시글 조회 

**ORM with View**

View 함수에서 QuerySet API 활용하기

- View에서의 QuerySet API:

  - 웹 페이지에 보여줄 데이터를 DB에서 가져올 때 사용
  - 사용자가 입력한 새로운 데이터를 DB에 저장할 때 사용

2가지 Read(조회)

1. 전체 게시글 조회 
2. 단일 게시글 조회

**전체 게시글 조회**

- 최종 결과화면 미리보기

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="utf-8" />
  <title>Articles</title>
</head>
<body>
  <h1>Articles</h1>
  <hr />
  <p>글 번호: 2</p>
  <p>글 제목: second</p>
  <p>글 내용: django!</p>

  <br />

  <p>글 번호: 3</p>
  <p>글 제목: third</p>
  <p>글 내용: django!</p>
</body>
</html>

```

- 요청 정의**

```
(requests)
http://127.0.0.1:8000/articles/ → urls(Django Project) → urls(articles) → views → models → DB 
                                                                                → templates
```

**요청 정의**

```python
# crud/urls.py
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
]
```

```python
# articles/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

> 앱 URL에서 빈 문자열('')의 의미?
  - `crud/urls.py`에서 `include("articles.urls")`는 `articles/`로 시작하는 모든 요청을 `articles` 앱의 `urls.py`로 넘겨줌
  - 이때 `articles/` 부분은 잘려나가고 나머지 URL만 앱의 `urls.py`로 전달됨
  - 따라서 `path('', views.index)`는 `articles/` 바로 뒤에 아무것도 없는 경우(= `articles/` 자체)를 의미 → 해당 view 함수 실행


```python
# articles/views.py
from .models import Article

def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)
```

```html
<!-- articles/index.html -->
<h1>Articles</h1>
<hr>
{% for article in articles %}
  <p>글 번호: {{ article.pk }}</p>
  <p>글 제목: {{ article.title }}</p>
  <p>글 내용: {{ article.content }}</p>
  <hr>
{% endfor %}
```

## Field lookups

**Field lookups: 데이터 필터링의 마법**

단순 동치 비교(=)를 넘어 더 상세한 조건으로 데이터를 조회할 수 있도록 Django ORM이 제공하는 기능 

> '특정 단어가 포함'된 제목, '특정 날짜 이후'에 작성된 글 등을 찾을 수 있게 해줌 

**Field lookups의 간단한 예시**

Title 필드가 `second`으로 시작하는 Article 데이터(레코드)를 모두 찾고 싶다면?

```python 
Article.objects.filter(title__startswith='second')
```

- Field Lookups은 모델의 필드 이름 뒤에 이중 밑줄(double underscore, __)을 붙이고, 원하는 조회 유형을 명시하는 방식으로 사용 
- filter(), exclude() 및 get()에 대한 키워드 인자로 지정, 손쉽게 필터링 로직을 구성 

```python
# Field lookups 예시 
# "내용에 'dja'가 포함된 모든 게시글 조회"
Article.objects.filter(content__contains='dja')

# "제목이 he로 시작하는 모든 게시글 조회"
Article.objects.filter(title__startswith='he')

```

**다양한 조건의 Field lookups 조회 조건**

exact/iexact
  - exact: 대소문자를 구분하여 정확히 일치하는 값을 찾음 
  - iexact: 대소문자 구분 없이(대소문자 무시) 정확히 일치하는 값을 찾음

contains/icontains
  - contains: 문자열 내에 특정 값이 포함되어 있는지 (대소문자 구분)
  - icontains: 문자열 포함 여부를 대소문자 구분 없이 확인

비교 연산자(gt, gte, lt, lte)
  - 숫자 또는 날짜 필드에 대해 크거나 작음을 비교

## ORM, QuerySet API를 사용하는 이유

1. 데이터베이스 추상화 
  
  - 개발자는 특정 데이터베이스 시스템에 종속되지 않고 일관된 방식으로 데이터를 다룰 수 있음 

2. 생산성 향상 
  
  - 복잡한 SQL 쿼리를 직접 작성하는 대신 Python 코드로 데이터베이스 작업을 수행할 수 있음

3. 객체 지향적 접근 
  
  - 데이터베이스 테이블을 Python 객체로 다룰 수 있어 객체 지향 프로그래밍의 이점을 활용할 수 있음 
