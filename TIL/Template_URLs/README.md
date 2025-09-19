# Template & URLs

## Template System

### Django Template system

**파이썬 데이터(context)를 HTML 문서(Template)와 결합**하여, 
**로직과 표현을 분리**한 채 동적인 웹페이지를 생성하는 도구 

> 모든 기사는 헤더, 폰트, 광고 위치 등 동일한 페이지 틀(Template)을 공유, 각 페이지에 들어가는 데이터(context), 즉 기사 제목, 내용, 기자 이름은 모두 다름 

**HTML의 콘텐츠를 변수 값에 따라 변경**

```html
<!--aricles/index.html-->

<body>
  <h1>Hello, Django!</h1>
</body>
```
context['name']이 변경되면 응답 받은 HTML의 모습도 변경되는 걸 확인

```python 

# views.py

def index(request):
  context = {
    'name': 'Jane',
  }
  return render(request, 'aricles/index.html', context)
```

```html
<!--aricles/index.html-->

<body>
  <h1>Hello, {{name}}!</h1>
</body>
```

**Django Template system의 목적**

**'페이지 틀'에 '데이터'를 동적으로 결합**하여 수많은 페이지를 효율적으로 만들어 내기 위함 

### Django Template Language

DTL: Template에서 조건, 반복, 변수 등의 프로그래밍적 기능을 제공하는 시스템

**DTL Syntax**
1. Variable
2. Filters
3. Tags
4. Comments

**1. Variable**

- Django Template에서의 변수
- `render()` 함수의 **세 번째 인자**로 **딕셔너리 타입(context)*- 을 전달
- 딕셔너리의 **key → template에서 사용 가능한 변수명**이 됨
- `.`(dot)을 사용해 **변수의 속성에 접근*- 가능

```django
{{ variable }}
{{ variable.attribute }}
```

```python
context = {
  'variable_1': 'value_1', # {{ variable_1 }}  → value_1
  'variable_2': {
      'attribute': 'value_2' # {{ variable_2.attribute }}  → value_2
  },
}
```

**2. Filters**

- **표시할 변수를 수정할 때 사용**
  - `{{ 변수|필터 }}` 형태
- 여러 필터를 **chained(연결)*- 가능
- 일부 필터는 **인자를 받기도 함**
- 약 60개의 built-in template filters 제공

```django
{{ variable|filter }}
{{ name|truncatewords:30 }}
```

**3. Tags**

- **반복 또는 논리를 수행하여 제어 흐름**을 만듦
- 일부 태그는 **시작/종료 태그**가 필요
- 약 24개의 built-in template tags 제공

```django
{% tag %}
{% if %} ... {% endif %}
```

- if, else, endif 태그

```python
context = {
  'login': False,
}
```

```django
{% if login %}
  <h1>Hello, User!!!</h1>
{% else %}
  <h1>Please, login.</h1>
{% endif %}
```

출력:

```html
<h1>Please, login.</h1>
```

---

- for 태그

```python
context = {
  'nums': [1, 2, 3],
}
```

```django
<ul>
  {% for num in nums %}
    <li>{{ num }}</li>
  {% endfor %}
</ul>
```

출력:

```html
<ul>
  <li>1</li>
  <li>2</li>
  <li>3</li>
</ul>
```

**4. Comments**

- 주석

- **inline**

```django
<h1>Hello, {# name #}</h1>
```

- **multiline**

```django
{% comment %}
여러 줄 주석
{% endcomment %}
```

- 다음과 같은 화면을 DTL을 활용하여 구성해보자

```
국밥 메뉴는 2글자 입니다.

메뉴판
- 국밥
- 국수
- 카레
- 탕수육

아직 메뉴가 남았습니다.
```

-  urls.py

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', views.index),
    path('dinner/', views.dinner),
]
```

- views.py

```python
import random

def dinner(request):
    foods = ['국밥', '국수', '카레', '탕수육']
    picked = random.choice(foods)
    context = {
        'foods': foods,
        'picked': picked,
    }
    return render(request, 'articles/dinner.html', context)
```

- templates/articles/dinner.html

```django
<p>{{ picked }} 메뉴는 {{ picked|length }}글자 입니다.</p>

<h2>메뉴판</h2>
<ul>
  {% for food in foods %}
    <li>{{ food }}</li>
  {% endfor %}
</ul>

{% if foods|length == 0 %}
  <p>메뉴가 소진 되었습니다.</p>
{% else %}
  <p>아직 메뉴가 남았습니다.</p>
{% endif %}
```

> 예시 코드이며, 다르게 구현할 수도 있습니다.

---

## 탬플릿 상속

**기존 템플릿 구조의 한계**

- 만약 모든 템플릿에 Bootstrap을 적용하려면?

> 모든 템플릿에 Bootstrap CDN을 작성해야 할까? 

**템플릿 상속**

Template inheritance

1. 페이지의 공통요소를 포함
2. 하위 템플릿이 재정의 할 수 있는 공간을 정의

> 여러 템플릿이 **공통요소를 공유할 수 있게*- 해주는 기능

**상속 구조 만들기**

- 상위 템플릿(base.html)

  - skeleton 역할을 하게 되는 상위 템플릿
  - 모든 템플릿이 공유했으면 좋겠는 **공통요소**를 작성
  - 템플릿 별로 재정의할 부분은 **block 태그**를 활용
  - 파일명이 반드시 base일 필요는 없음

```html
<!-- articles/base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  ...
  {% comment %} 생략 {% endcomment %}
</head>
<body>
  {% block content %}
  {% endblock content %}
  {% comment %} 생략 {% endcomment %}
</body>
</html>
```
> <body> 부분은 다른 템플릿에서 재정의 할 수 있는 공간

- 하위 템플릿이 상위 템플릿을 상속받도록 변경

  - **extends*- 태그로 상속받을 템플릿 결정
  - **block*- 태그를 활용해 `base.html`의 같은 이름으로 작성된 block 태그의 내용을 대체

```html
<!-- articles/index.html -->
{% extends 'articles/base.html' %}
{% block content %}
  <h1>Hello, {{ name }}</h1>
{% endblock content %}
```

```html
<!-- articles/dinner.html -->
{% extends 'articles/base.html' %}
{% block content %}
  <p>{{ picked }} 메뉴는 {{ picked|length }}글자 입니다.</p>

  <h2>메뉴판</h2>
  <ul>
    {% for food in foods %}
      <li>{{ food }}</li>
    {% endfor %}
  </ul>

  {% if foods|length == 0 %}
    <p>메뉴가 소진 되었습니다.</p>
  {% else %}
    <p>아직 메뉴가 남았습니다.</p>
  {% endif %}
{% endblock content %}
```

- 상속 구조의 최종 형태

- `articles/base.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>...</head>
<body>
  <!-- 원래 block이 있던 곳 -->
  {% block content %}{% endblock content %}
  <!-- 원래 endblock이 있던 곳 -->
</body>
</html>
```

- `articles/dinner.html`

```html
{% extends 'articles/base.html' %}
{% block content %}
<p>{{ picked }} 메뉴는 {{ picked|length }}글자 입니다.</p>
<h2>메뉴판</h2>
<ul>
  {% for food in foods %}
    <li>{{ food }}</li>
  {% endfor %}
</ul>
{% if foods|length == 0 %}
  <p>메뉴가 소진 되었습니다.</p>
{% else %}
  <p>아직 메뉴가 남았습니다.</p>
{% endif %}
{% endblock content %}
```

### 상속 관련 DTL 태그

- 'extends' tag

```django
{% extends 'articles/base.html' %}
```

- 자식(하위) 템플릿이 부모 템플릿을 확장한다는 것을 알림
- 반드시 자식 템플릿 **최상단에 작성**되어야 함
- `extends` 태그는 2개 이상 사용 불가능

- 'block' tag

```django
{% block 'content' %}{% endblock 'content' %}
```

- 하위 템플릿에서 재정의 할 수 있는 블록을 정의
- 상위 템플릿에서 작성하며 하위 템플릿이 작성할 수 있는 공간을 지정하는 것

**다시 살펴보기**

- 하위 템플릿의 `block`이 상위 템플릿의 `block`의 내용을 대체함

```html
<!-- articles/base.html -->
<body>
  {% block content %}{% endblock content %}
</body>

<!-- articles/index.html -->
{% extends 'articles/base.html' %}
{% block content %}
  <h1>Hello, {{ name }}</h1>
{% endblock content %}
```

---

## 요청과 응답

### HTML form

데이터를 보내고 가져오기 

Sending and Retrieving form data: HTML 'form' element를 통해 사용자와 애플리케이션 간의 상호작용 이해하기

**HTML form**

- HTTP 요청을 서버에 보내는 가장 편리한 방법

```
Client ----HTTP(S)----> Server
        <---Response---
```

- HTTP 요청을 서버에 보내는 가장 편리한 방법

```html
<form action="#" method="GET">
  <div>
    <label for="name">아이디 :</label>
    <input type="text" name="name" id="name">
  </div>
  <div>
    <label for="password">패스워드 :</label>
    <input type="password" name="password" id="password">
  </div>
  <input type="submit" value="로그인">
</form>
```

**form element**

- 사용자로부터 할당된 데이터를 서버로 전송하는 HTML 요소

> 웹에서 사용자 정보를 입력하는 여러 방식 (`text`, `password`, `checkbox` 등)을 제공

**form을 이용해 Naver로 요청 보내기: fake Naver**

- form을 이용해 사용자가 입력한 검색어를 Naver에 전달하여 검색 결과를 확인
- input에 입력한 값은 URL 파라미터로 전달됨 (`?query=검색어`)

**fake Naver 실습**

- form 요소로 검색창 만들기

- urls.py

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', views.index),
    path('dinner/', views.dinner),
    path('search/', views.search),
]
```

- views.py

```python
def search(request):
    return render(request, 'articles/search.html')
```

- articles/search.html

```html
{% extends 'articles/base.html' %}
{% block content %}
<form action="#" method="GET">
  <label for="message">검색어</label>
  <input type="text" name="query" id="message">
  <input type="submit" value="submit">
</form>
{% endblock content %}
```

- input에 hello를 입력하고 제출 버튼을 누른 뒤 브라우저 URL 확인
- `http://127.0.0.1:8000/search?query=hello` 형태로 전달됨
- input의 `name` 속성이 URL 파라미터의 key가 됨

```html
<input type="text" name="query" id="message">
```

- 실제 Naver에서 검색 후 URL 확인
- `query` 파라미터에 입력값이 전달됨

```
https://search.naver.com/search.naver?query=hello
```

- form의 action을 Naver 검색 URL로 변경하여 테스트

- articles/search.html

```html
{% extends 'articles/base.html' %}
{% block content %}
<form action="https://search.naver.com/search.naver" method="GET">
  <label for="message">검색어</label>
  <input type="text" name="query" id="message">
  <input type="submit" value="submit">
</form>
{% endblock content %}
```

### HTML form 핵심 속성

action & method - form의 핵심 속성 2가지

데이터를 어디(action)로 어떤 방식(method)으로 요청할지 

**action & method 예시**

```html
<form action="https://search.naver.com/search.naver" method="GET">
  <label for="message">검색어</label>
  <input type="text" name="query" id="message">
  <input type="submit" value="submit">
</form>
```

- action

  - 입력 데이터가 전송될 URL을 지정 (목적지)
  - 지정하지 않으면 현재 페이지의 URL로 전송됨

- method

  - 데이터를 어떤 방식으로 보낼 것인지 정의
  - HTTP request method 지정 (`GET`, `POST`)

**input element**

- 사용자의 데이터를 입력 받을 수 있는 HTML 요소
- `type` 속성 값에 따라 다양한 유형의 입력 데이터 수신

> 핵심 속성: `name`

**name attribute**

```html
<input type="text" name="query" id="message">
```

- `input` 요소의 핵심 속성
- 사용자가 입력한 데이터에 붙이는 이름(key)
- 데이터를 제출했을 때 서버는 `name` 속성 값으로만 접근할 수 있음

**Query String Parameters**

- 사용자의 입력 데이터를 URL 주소에 파라미터로 통해 서버로 보내는 방법
- `?` 뒤에 `key=value` 쌍으로 붙이며 `&`로 구분

- 예시

  ```
  http://host:port/path?key=value&key=value
  ```

### HTML form 활용

**사용자 입력 데이터를 받아 그대로 출력하는 서버 만들기**

**1. throw 로직**

- fake Naver 실습을 참고해 throw 페이지 만들기

- urls.py

```python
urlpatterns = [
    path('throw/', views.throw),
]
```

- views.py

```python
def throw(request):
    return render(request, 'articles/throw.html')
```

- articles/throw.html

```html
{% extends 'articles/base.html' %}
{% block content %}
<h1>Throw</h1>
<form action="/catch/" method="GET">
  <input type="text" id="message" name="message">
  <input type="submit">
</form>
{% endblock content %}
```

**2. catch 로직**

- throw 페이지에서 요청한 사용자의 입력 데이터를 GET으로 받아오기

- urls.py

```python
urlpatterns = [
    path('catch/', views.catch),
]
```

- views.py

```python
def catch(request):
    context = {
        'msg': request.GET.get('message')
    }
    return render(request, 'articles/catch.html', context)
```

- articles/catch.html

```html
{% extends 'articles/base.html' %}
{% block content %}
<h1>Catch</h1>
<h3>{{ msg }}를 받았습니다!</h3>
{% endblock content %}
```

**request**

- `form`으로 전송한 데이터뿐만 아니라 Django로 들어오는 **모든 요청 관련 데이터**가 담겨 있음
- view 함수가 호출될 때 **첫 번째 인자로 전달**

**request 객체 살펴보기**

```python
def catch(request):
    print(request)
    print(type(request))
    print(dir(request))
    print(request.GET)
    print(request.GET.get('message'))
    return render(request, 'articles/catch.html')
```

출력 예시:

```bash
<WSGIRequest: GET '/catch/?message=안녕!'>
<class 'django.core.handlers.wsgi.WSGIRequest'>
['COOKIES', 'FILES', 'GET', ...]
<QueryDict: {'message': ['안녕!']}>
안녕!
```

**request 객체에서 form 데이터 추출**

```python
request.GET.get('message')
```

- `request.GET`에 작성한 `message`가 담겨 있음
- `QueryDict` 자료형으로 반환되며, 딕셔너리의 `get()` 메서드를 사용해 값 조회 가능

**catch 로직 마무리**

- views.py

```python
def catch(request):
    message = request.GET.get('message')
    context = {
        'message': message,
    }
    return render(request, 'articles/catch.html', context)
```

- articles/catch.html

```html
{% extends 'articles/base.html' %}
{% block content %}
<h1>Catch</h1>
<h3>{{ message }}를 받았습니다!</h3>
{% endblock content %}
```

**throw - catch 간 요청과 응답 정리**

- 브라우저에서 `/throw/` 입력 시 동작 흐름

1. 브라우저에서 `http://127.0.0.1:8000/throw/` 요청
2. `urls.py`에서 `'throw/'` path 매칭
3. `views.throw()` 함수 호출
4. `throw.html`을 렌더링하여 응답 객체 반환
5. Django가 응답 객체를 브라우저에 전달
6. 브라우저가 응답 객체를 해석하여 화면에 출력

**throw 페이지에서 form 전송 시 흐름**

1. throw 페이지에서 form 데이터 작성 후 제출 (form의 action 값으로 요청)
2. `/catch/` URL로 요청 (사용자 입력 데이터와 함께 전송)
3. `urls.py`에서 `'catch/'` path 매칭
4. `views.catch()` 함수 호출
5. `request.GET`에서 사용자가 보낸 form 데이터 추출
6. catch view가 응답 객체를 반환
7. Django가 브라우저로 전달 → 브라우저가 화면 출력

---

## Django URLs

**Django URLs의 역할**

- 클라이언트의 요청 URL에 따라 실행될 **view 함수가 달라짐**
- Django 프로젝트에서 `urls.py`가 **요청을 적절한 view로 연결**해주는 역할 수행

**URL dispatcher**

- URL 패턴을 정의하고
  해당 패턴이 일치하는 요청을 처리할 **view 함수에 연결(매핑)**
- 일종의 **운항 관리자, 분배기*- 역할

### Variable Routing

**현재 URL 관리의 문제점**

- 템플릿의 많은 부분이 중복되고, URL의 일부만 변경되는 상황에서는 비효율적
- 예: 아래처럼 유사한 URL을 계속 작성해야 함

```python
urlpatterns = [
    path('articles/1/', ...),
    path('articles/2/', ...),
    path('articles/3/', ...),
    ...
]
```

**Variable Routing**

- **URL 일부에 변수를 포함**시키는 것
- 포함된 변수는 **view 함수의 인자로 전달**됨

```python
urlpatterns = [
    path('articles/<int:num>/', ...),
]
```

- `<path_converter:variable_name>` 형태 사용
- `int`, `str`, `slug`, `uuid`, `path` 총 5가지 타입 지원

```python
path('articles/<int:num>/', views.detail)
path('hello/<str:name>/', views.greeting)
```

- 요청 URL의 <int: num>, <str: name>의 위치에 들어있는 값이 변수처럼 취급됨
  - 정수 num 변수가 views.detail에, 문자열 name 변수가 views.greeting에 키워드 인자로 전달됨
  - 예시:요청 URL이 `/articles/10/` → `views.detail(request, num=10)`, `/hello/John/` → `views.greeting(request, name="John")`

- Path Converter
  - URL 변수의 타입을 지정
  - str, int 등 5가지 타입 지원

**Variable Routing 실습**

- urls.py

```python
urlpatterns = [
    path('articles/<int:num>/', views.detail),
]
```

- views.py

```python
def detail(request, num):
    context = {'num': num}
    return render(request, 'articles/detail.html', context)
```

- detail.html

```html
{% extends 'articles/base.html' %}
{% block content %}
<h1>Detail</h1>
<h3>{{ num }}번 글입니다.</h3>
{% endblock content %}
```
> Path Converter의 변수명과 View 함수의 파라미터 이름은 같아야 함

- URL 변화에 따라 템플릿에서 출력되는 `num` 값이 달라짐
- 예: `/articles/1/` → `1번 글입니다.`
  `/articles/486/` → `486번 글입니다.`

- urls.py

```python
urlpatterns = [
    path('hello/<str:name>/', views.greeting),
]
```

- views.py

```python
def greeting(request, name):
    context = {'name': name}
    return render(request, 'articles/greeting.html', context)
```

- greeting.html

```html
{% extends 'articles/base.html' %}
{% block content %}
<h1>Greeting</h1>
<h3>{{ name }}님 안녕하세요 !</h3>
{% endblock content %}
```

- URL 변화에 따라 템플릿에서 출력되는 `name` 값이 달라짐
- 예: `/hello/John/` → `John님 안녕하세요 !`
  `/hello/Jane/` → `Jane님 안녕하세요 !`


### App URL 정의

**App URL mapping**

- 각 앱에 `urls.py`를 정의하여 관리하는 방식
- 프로젝트와 앱의 URL을 나누어 관리 → **URL 충돌 방지 및 유지보수성 향상**
- 앱이 여러 개 생겨도 서로의 URL이 섞이지 않도록 관리 가능

**기존 URL 구조**

- 모든 URL이 **프로젝트 루트의 `urls.py`**에 몰려 있음
- 앱이 많아질수록 URL 관리가 복잡해지고, 충돌 위험 존재

```bash
firstpjt/urls.py
└── path('articles/', views.index)
└── path('pages/', views.index)
```
**2번째 앱 pages 생성 후 발생할 수 있는 문제**

- 서로 다른 앱에 **같은 이름의 view 함수**가 있을 경우 충돌
- 예: `articles/views.py` 와 `pages/views.py`에 둘 다 `index()` 존재

```python
# 비권장: views에 별칭 부여
from articles import views as article_views
from pages import views as page_views

urlpatterns = [
    path('pages/', page_views.index),
]
```

**변경된 URL 구조**

- 각 앱마다 `urls.py`를 만들어 **자기 앱의 URL을 직접 관리**
- 프로젝트의 `urls.py`는 각 앱의 `urls.py`를 **include()로 불러오기만 함**

```bash
Django 프로젝트
├── firstpjt/urls.py        ← include로 각 앱 URL 연결
├── articles/urls.py         ← articles 앱 전용 URL
└── pages/urls.py             ← pages 앱 전용 URL
```

**include() 함수**

- `include('app.urls')` 로 각 앱의 URL을 참조할 수 있게 매핑
- URL의 일치하는 부분까지만 잘라내고, **나머지 경로는 각 앱의 urls.py로 전달**

```python
# firstpjt/urls.py
from django.urls import path, include

urlpatterns = [
    path('articles/', include('articles.urls')),
    path('pages/', include('pages.urls')),
]
```

```python
# articles/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('dinner/', views.dinner),
    path('search/', views.search),
    path('throw/', views.throw),
    path('catch/', views.catch),
    path('<int:num>/', views.detail),
    path('hello/<str:name>/', views.greeting),
]
```

```python
# pages/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
]
```

**include 동작 방식 예시**

- 요청: `http://127.0.0.1:8000/articles/index/`
- `firstpjt/urls.py` 에서 `articles/` 까지 매칭
- 나머지 `index/`는 `articles/urls.py`로 전달되어 `views.index` 실행

**URL 구조 변화 요약**

- **기존:*- 모든 URL → `firstpjt/urls.py`
- **변경 후:*- 각 앱의 URL은 각 앱의 `urls.py`에서 관리, 프로젝트에서는 include로 연결

---

## URL 이름 지정

### Naming URL patterns

**URL 구조 변경에 따른 문제점**

- 기존 'articles/' 주소가 'articles/index/'로 변경됨에 따라 해당 URL을 사용하는 모든 위치를 찾아가 변경해야 함

```python
# firstpjt/urls.py
from django.urls import path, include

urlpatterns = [
    path('articles/', include('articles.urls'))
]
```

```python
# articles/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
]
```

> "URL에 이름을 지어주면 이름만 기억하면 되지 않을까?"

**Naming URL patterns**

- URL에 이름을 지정하는 것
- path 함수에 name 인자를 키워드 인자로 정의해서 사용

```python
# articles/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('dinner/', views.dinner, name='dinner'),
    path('search/', views.search, name='search'),
    path('throw/', views.throw, name='throw'),
    ...
]
```

```python
# pages/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
]
```

**URL 표기 변화**

- 해당 url을 사용했던 곳의 링크 변경
- 새로운 articles/urls.py

```python
# articles/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('dinner/', views.dinner, name='dinner'),
    path('search/', views.search, name='search'),
    path('throw/', views.throw, name='throw'),
    ...
]
```

```html
<!-- articles/index.html -->
{% extends 'articles/base.html' %}

{% block content %}
<h1>Hello, {{ name }}</h1>
<a href="/dinner/">dinner</a>
<a href="/search/">search</a>
<a href="/throw/">throw</a>
{% endblock content %}
```

```html
<!-- articles/index.html -->
{% extends 'articles/base.html' %}

{% block content %}
<h1>Hello, {{ name }}</h1>
<a href="{% url 'dinner' %}">dinner</a>
<a href="{% url 'search' %}">search</a>
<a href="{% url 'throw' %}">throw</a>
{% endblock content %}
```

> a 태그의 href 속성 값 뿐만 아니라 form의 action 속성 등도 변경

- 브라우저 상의 실제 링크 확인

```html
<!-- articles/index.html -->
{% extends 'articles/base.html' %}

{% block content %}
<h1>Hello, {{ name }}</h1>
<a href="{% url 'dinner' %}">dinner</a>
<a href="{% url 'search' %}">search</a>
<a href="{% url 'throw' %}">throw</a>
{% endblock content %}
```

브라우저 Elements 예시:

```
<a href="/articles/dinner/">dinner</a>
<a href="/articles/search/">search</a>
<a href="/articles/throw/">throw</a>
```

### DTL URL tag

**DTL URL tag**

```django
{% url 'url_name' arg1 arg2 %}
```

- 주어진 URL 패턴의 이름과 일치하는 절대 경로 주소를 반환

> URL에 이름을 붙였을 경우 url 태그와 이름을 이용해 템플릿 상에서 이름으로 실제 주소를 작성할 수 있게 해줌

**'url' tag**

- 주어진 URL 패턴의 이름과 일치하는 절대 경로 주소를 반환

```html
<!-- articles/index.html -->
{% extends 'articles/base.html' %}

{% block content %}
<h1>Hello, {{ name }}</h1>
<a href="{% url 'dinner' %}">dinner</a>
<a href="{% url 'search' %}">search</a>
<a href="{% url 'throw' %}">throw</a>
{% endblock content %}
```

브라우저 Elements 예시:

```
<a href="/articles/dinner/">dinner</a>
<a href="/articles/search/">search</a>
<a href="/articles/throw/">throw</a>
```

> 태그 이름, URL 이름, 인자 등은 콤마(,)로 구분되지 않음

- URL 패턴에 변수가 포함되어 있으면, 'url_name' 이후 추가

```html
<!-- articles/index.html -->
{% extends 'articles/base.html' %}

{% block content %}
<h1>Articles</h1>
<a href="{% url 'detail' 1 %}">Article 1</a>
<a href="{% url 'detail' 2 %}">Article 2</a>
<a href="{% url 'detail' 3 %}">Article 3</a>
{% endblock content %}
```

```python
path('<int:num>/', views.detail),
```

브라우저 Elements 예시:

```
<a href="/articles/1/">Article 1</a>
<a href="/articles/2/">Article 2</a>
<a href="/articles/3/">Article 3</a>
```

- DTL의 for 태그에서 사용한 변수 이름 사용 가능

```python
# articles/views.py
def index(request):
    context = {
        'nums': [1, 2, 3],
    }
    return render(request, 'articles/index.html', context)
```

```html
<!-- articles/index.html -->
{% for num in nums %}
<a href="{% url 'detail' num %}">Article {{ num }}</a>
{% endfor %}
```

> 실행 결과는 이전과 동일

--- 

## URL 이름 공간

### app_name 속성

**URL 이름 지정 후 남은 문제**

- articles 앱의 url 이름과 pages 앱의 url 이름이 같은 상황
- 단순히 이름만으로는 완벽하게 분리할 수 없음
    • articles와 pages 모두 index가 있다.

```python
# articles/urls.py
urlpatterns = [
    path('index/', views.index, name='index'),
]
```

```python
# pages/urls.py
urlpatterns = [
    path('index/', views.index, name='index'),
]
```

> "이름에 성(key)을 붙이자"

**'app_name' 속성 지정**

- urls.py에 app_name 변수 설정

```python
# articles/urls.py
app_name = 'articles'
urlpatterns = [
    path('index/', views.index, name='index'),
]
```

```python
# pages/urls.py
app_name = 'pages'
urlpatterns = [
    path('index/', views.index, name='index'),
]
```

- urls.py에 app_name 변수 설정

```python
# articles/urls.py
app_name = 'articles'
urlpatterns = [
    path('index/', views.index, name='index'),
]
```

```python
# pages/urls.py
app_name = 'pages'
urlpatterns = [
    path('index/', views.index, name='index'),
]
```

- app_name 이 추가 또는 수정되면 url 태그에도 해당 내용이 반영되어야 함

```django
{% url 'url_name' arg1 arg2 %}
```

```django
{% url 'app_name:path_name' arg1 arg2 %}
```

- HTML 반영 후 확인

```html
<!-- articles/index.html -->

{% extends 'articles/base.html' %}

{% block content %}
<h1>Hello, {{ name }}</h1>
<a href="{% url 'articles:dinner' %}">dinner</a>
<a href="{% url 'articles:search' %}">search</a>
<a href="{% url 'articles:throw' %}">throw</a>
{% endblock content %}
```

- 최종 링크는 변하지 않음

```html
/articles/dinner/
/articles/search/
/articles/throw/
```

---

## 추가 템플릿 경로

**추가 템플릿 경로 지정**

- 앱 폴더 내부 templates 폴더(기본 경로) 외에 템플릿을 위치하고 싶을 때

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

- 새로운 템플릿 경로

```bash 
.  # BASE_DIR 경로 위치
├── articles/
├── firstpjt/
├── templates/
│   └── base.html
├── db.sqlite3
├── manage.py
└── requirements.txt

```

- 하위 템플릿에서 extends의 경로 수정 필요

```django
{% extends 'base.html' %}
```

**BASE_DIR**

- settings.py에서 경로지정을 편하게 하기 위해 최상단 지점을 지정해 둔 변수

```python
# settings.py
BASE_DIR = Path(__file__).resolve().parent.parent
```

**BASE\_DIR 경로 위치**

```bash
03_DJANGO_TEMPLATE/  # BASE_DIR 경로 위치
├── articles/
├── firstpjt/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── templates/
│   └── base.html
├── db.sqlite3
├── manage.py
└── requirements.txt
```

> Python의 객체 지향 파일 시스템 경로에 대해서 알고 싶다면 다음 링크로
  [https://docs.python.org/ko/3.9/library/pathlib.html#module-pathlib](https://docs.python.org/ko/3.9/library/pathlib.html#module-pathlib)

---

## DTL 주의사항 

**DTL 주의사항**

- Python 처럼 일부 프로그래밍 구조(if, for 등)를 사용할 수 있지만 명칭을 그렇게 설계 했을 뿐
- Python 코드로 실행되는 것이 아니며 Python과는 관련 없음
- 프로그래밍적 로직이 아니라 표현을 위한 것임을 명심하기
- **프로그래밍적 로직은 되도록 view 함수에서 작성 및 처리할 것**
- 공식 문서를 참고해 다양한 태그와 필터 사용해보기
  [https://docs.djangoproject.com/en/5.2/ref/templates/builtins/](https://docs.djangoproject.com/en/5.2/ref/templates/builtins/)

---

## Trailing Slashes 

**URL의 Trailing Slashes**

- Django는 URL 끝에 '/'가 없다면 자동으로 붙임
- "기술적인 측면에서, foo.com/bar 와 foo.com/bar/ 는 서로 다른 URL"
    • 검색 엔진 로봇이나 웹 트래픽 분석 도구에서는 이 두 주소를 서로 다른 페이지로 보기 때문
- 그래서 Django는 검색 엔진이 혼동하지 않게 하기 위해 무조건 붙이는 것을 선택한 것
- 그러나 모든 프레임워크가 이렇게 동작하는 것은 아니니 주의

