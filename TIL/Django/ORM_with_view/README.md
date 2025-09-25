# Django 5 _ ORM_with_wiews

## Read 

**2가지 Read(조회) 진행**

1. 전체 게시글 조회 
2. 단일 게시글 조회 

**단일 게시글 조회**

- 최종 결과화면 미리보기 

```html 

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>1</title>
</head>
<body>
  <h1>DETAIL</h1>
  <h2>1번째 글</h2>
  <hr>
  <p>제목: 첫번째</p>
  <p>내용: 게시글!!</p>
  <p>작성 시각: *****</p>
  <p>수정 시각: *****</p>
  <hr>
  <a herf ="">back<a>
</body>
</html>

```

**단일 게시글 조회 구현**

- `articles/urls.py`

```python
urlpatterns = [
    ...
    path('<int:pk>/', views.detail, name='detail'),
]
```

- `articles/views.py`

```python
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)
```

- `templates/articles/detail.html`

```html
<h2>DETAIL</h2>
<h3>{{ article.pk }} 번째 글</h3>
<hr>
<p>제목: {{ article.title }}</p>
<p>내용: {{ article.content }}</p>
<p>작성일: {{ article.created_at }}</p>
<p>수정일: {{ article.updated_at }}</p>
<hr>
<a href="{% url 'articles:index' %}">[back]</a>
```

**단일 게시글 이동 페이지 링크 작성**

- 최종 결과화면 미리보기 (HTML로 구현)

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>Articles</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 20px;
    }
    h1 {
      margin-bottom: 10px;
    }
    .article {
      border-bottom: 1px solid #ccc;
      padding: 10px 0;
    }
    .article a {
      font-weight: bold;
      color: blue;
      text-decoration: none;
    }
    .article a:hover {
      text-decoration: underline;
    }
    .num {
      margin: 0;
    }
    .content {
      margin: 5px 0 0 0;
    }
  </style>
</head>
<body>
  <h1>Articles</h1>

  <div class="article">
    <p class="num">글 번호: 1</p>
    <a href="/articles/1/"><p>글 제목: 첫번째</p></a>
    <p class="content">글 내용: 게시글!!</p>
  </div>

  <div class="article">
    <p class="num">글 번호: 2</p>
    <a href="/articles/2/"><p>글 제목: first</p></a>
    <p class="content">글 내용: django!</p>
  </div>

  <div class="article">
    <p class="num">글 번호: 3</p>
    <a href="/articles/3/"><p>글 제목: 제목</p></a>
    <p class="content">글 내용: 내용</p>
  </div>
</body>
</html>
```

**단일 게시글 이동 페이지 링크 구현**

- `templates/articles/index.html`

```html
<h1>Articles</h1>
<hr>
{% for article in articles %}
  <p>글 번호: {{ article.pk }}</p>
  <a href="{% url 'articles:detail' article.pk %}">
    <p>글 제목: {{ article.title }}</p>
  </a>
  <p>글 내용: {{ article.content }}</p>
  <hr>
{% endfor %}
```

---

## Create

**Create 로직을 구현하기 위해 필요한 view 함수의 개수는?**

(new) 사용자자 입력 데이터를 받을 페이지를 렌더링 --> (Create) 사용자가 입력한 요청 데이터를 받아 DB에 저장 

> Create 로직 구현에는 두 개의 view 함수가 필요함 

**new - 페이지 렌더링 기능 구현**

- 최종 결과화면 미리보기

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>NEW</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 20px;
    }
    h1 {
      margin-bottom: 15px;
    }
    form div {
      margin-bottom: 10px;
    }
    label {
      display: inline-block;
      width: 60px;
    }
    input[type="text"], textarea {
      width: 300px;
    }
    input[type="submit"] {
      margin-top: 10px;
    }
    a {
      color: blue;
      text-decoration: none;
    }
    a:hover {
      text-decoration: underline;
    }
  </style>
</head>
<body>
  <h1>NEW</h1>
  <form action="#" method="GET">
    <div>
      <label for="title">Title:</label>
      <input type="text" name="title" id="title">
    </div>
    <div>
      <label for="content">Content:</label>
      <textarea name="content" id="content"></textarea>
    </div>
    <input type="submit" value="제출">
  </form>
  <hr>
  <a href="/articles/">[back]</a>
</body>
</html>
```

- 게시글 생성 페이지 구현

```python
# `articles/urls.py`
urlpatterns = [
    ...
    path('new/', views.new, name='new'),
]
```

```python
# `articles/views.py`
def new(request):
    return render(request, 'articles/new.html')
```

```html
<!--`templates/articles/new.html`-->
<h1>NEW</h1>
<form action="#" method="GET">
  <div>
    <label for="title">Title: </label>
    <input type="text" name="title" id="title">
  </div>
  <div>
    <label for="content">Content: </label>
    <textarea name="content" id="content"></textarea>
  </div>
  <input type="submit">
</form>
<hr>
<a href="{% url 'articles:index' %}">[back]</a>
```

- Index 페이지에 new 페이지로 이동할 수 있는 하이퍼링크 작성

```html
<!--`templates/articles/index.html`-->
<h1>Articles</h1>
<a href="{% url 'articles:new' %}">NEW</a>
<hr>
...
```

**create - 데이터 저장 기능 구현**

- 최종 결과화면 미리보기

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>게시글 작성 완료</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 20px;
    }
    h1 {
      color: black;
    }
  </style>
</head>
<body>
  <h1>게시글이 작성 되었습니다.</h1>
</body>
</html>
```

- 데이터 저장 기능 구현

```python
# `articles/urls.py`
urlpatterns = [
    ...
    path('create/', views.create, name='create'),
]
```

```python
# `articles/views.py`
def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')

    # 1. 인스턴스 생성 후 속성 할당 및 저장
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # 2. 인스턴스 생성 시 속성 할당 후 저장
    article = Article(title=title, content=content)
    article.save()

    # 3. create() 메서드를 통한 인스턴스 생성 및 즉시 저장
    # Article.objects.create(title=title, content=content)

    return render(request, 'articles/create.html')
```

```html
<!--`templates/articles/create.html`-->
<h1>게시글이 작성 되었습니다.</h1>
```

```html
<!--`templates/articles/new.html`-->
<h1>NEW</h1>
<form action="{% url 'articles:create' %}" method="GET">
  <div>
    <label for="title">Title: </label>
    <input type="text" name="title" id="title">
  </div>
  <div>
    <label for="content">Content: </label>
    <textarea name="content" id="content"></textarea>
  </div>
  <input type="submit">
</form>
<hr>
<a href="{% url 'articles:index' %}">[back]</a>
```

---

## HTTP request methods

### HTTP 

네트워크 상에서 **데이터(리소스)**를 주고 받기 위한 약속

**HTTP request methods**

데이터에 대해 수행을 원하는 작업(행동)을 나타내는 것
- 서버에게 원하는 작업의 종류를 알려주는 역할 

대표적인 메서드 
|              GET              |                 POST               |
| ----------------------------- | ---------------------------------- |
|          리소스 조회           |          데이터 생성/전송           |
| URL에 데이터가 노출됨, 캐싱 가능 | 요청 본문에 데이터, 데이터 노출 없음 |

> 캐싱: 자주 사용하는 데이터나 결과를 임시로 저장해두고 재활용하여 처리 속도를 높이는 기술

### GET method 

서버로부터 데이터를 요청받고 받아오는 데(조회) 사용

> GET 메서드는 주로 검색 쿼리 전송, 웹 페이지 요청, 그리고 API에서 데이터를 조회하는 것과 같이 서버로부터 데이터를 요청하고 받아오는 데 사용

**'GET' Method 특징**

1. 데이터 전송
  - URL의 커리 문자열(Query String)을 통해 데이터를 전송
  - http://127.0.0.1:8000/articels/create/?title=제목&content=내용

2. 데이터 제한
  - URL 길이에 제한이 있어 대량의 데이터 전송에는 적합하지 않음

3. 브라우저 히스토리 
  - 요청 URL이 브라우저 히스토리에 남음

4. 캐싱 
  - 브라우저는 GET 요청의 응답을 로컬에 저장할 수 있음
  - 동일한 URL로 다시 요청할 때, 서버에 접속하지 않고 저장된 결과를 사용
  - 페이지 로딩 시간을 크게 단축 

### POST method 

서버에 데이터를 제출하여 리소스를 변경(생성, 수정, 삭제)하는데 사용

> POST 메서드는 주로 **로그인 정보 제출, 파일 업로드, 새 데이터 생성**(예: 새 게시글 작성), 그리고 **API에서 데이터 변경을 요청**하는 것과 같이 클라이언트가 **서버로 데이터를 전송하여 서버의 상태를 변경**할 때 사용 

**'POST' Method 특징**

1. 데이터 전송
  - HTTP Body를 통해 데이터를 전송

2. 데이터 제한
  - GET에 비해 더 많은 양의 데이터를 전송할 수 있음

3. 브라우저 히스토리 
  - POST 요청은 브라우저 히스토리에 남지 않음

4. 캐싱 
  - POST 요청은 기본적으로 캐시 할 수 없음
  - POST 요청이 일반적으로 서버의 상태를 변경하는 작업을 수행하기 때문

**'GET' & 'POST' Method 정리**

- GET과 POST는 각각의 특성에 맞게 적절히 사용해야 함

- GET: 데이터 조회

- POST: 데이터 생성이나 수정에 주로 사용

### Post method 변경 

**Create 로직 수정 - http method POST로 변경**

- `new.html`의 form 요청은 **새로운 article(새로운 데이터)**을 생성하는 요청
- 따라서 `POST method`로 서버에 전달되는 것이 적절함

```html
<!-- `templates/articles/new.html`-->
<form action="{% url 'articles:create' %}" method="POST">
  <div>
    <label for="title">Title: </label>
    <input type="text" name="title" id="title">
  </div>
  <div>
    <label for="content">Content: </label>
    <textarea name="content" id="content"></textarea>
  </div>
  <input type="submit">
</form>
```

```python
# `articles/views.py`
def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
```

**Create 로직 수정 - http method 변경 후 게시글 생성 테스트**

- GET → POST로 바꾼 후, 게시글 작성 시 **403 Forbidden 응답** 발생
- 이는 Django의 **CSRF 보호 정책** 때문


```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>403 Forbidden</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 20px;
      color: #333;
    }
    h1 {
      color: darkred;
    }
    .highlight {
      font-weight: bold;
      color: red;
    }
  </style>
</head>
<body>
  <h1>Forbidden (403)</h1>
  <p>CSRF verification failed. Request aborted.</p>
  <hr>
  <h3>Help</h3>
  <p>Reason given for failure: <span class="highlight">CSRF cookie not set.</span></p>
  <ul>
    <li>브라우저에서 쿠키가 허용되는지 확인해야 합니다.</li>
    <li>템플릿 내 form에 <code>{% csrf_token %}</code> 태그가 포함되어야 합니다.</li>
    <li>POST 요청은 반드시 유효한 CSRF 토큰을 포함해야 합니다.</li>
  </ul>
</body>
</html>
```

**해결 방법**

1. `new.html`의 form 내부에 `{% csrf_token %}` 추가
2. Django 기본 CSRF 미들웨어 활성화 상태 유지
3. 정상적으로 POST 요청이 전달되면 403 오류 해결

---

## HTTP response status code

서버가 클라이언트의 요청에 대한 처리 결과를 나타내는 3자리 숫자 

> 클라이언트는 이 코드를 통해 요청이 성공했는지, 실패했는지, 아니면 추가적인 조치가 필요한지 즉시 파악할 수 있음, 이를 통해 웹 브라우저는 적절한 메시지를 사용자에게 표시하거나, 개발자는 문제해결을 위한 단서를 얻게 됨

**403 Forbidden 응답의 의미**

서버에 요청이 전달되었지만. 권한 때문에 거절되었다는 것을 의미 

### CSRF 

Cross-Site-Request-Forgery(사이트 간 요청 위조)

- 사용자가 자신의 의지와는 무관하게 공격자가 의도한 행동(글쓰기, 정보 수정, 송금 등)을 특정 웹사이트에 요청하게 만드는 해킹 방식 

**CSRF (위조된 인감도장)**

1. 신뢰할 수 있는 관계 (로그인)
  - 사용자는 은행(bank.com)에 정상적으로 로그인하여, 은행은 사용자를 신뢰하고 있다는 증표(세션 쿠키)를 브라우저에 발급. 이 쿠키가 바로 당신의 '인감도장'  

2. 악성 위임장 (악성 링크)
  - 사기꾼(해커)은 "무료 경품 이벤트!"와 같은 미끼 링크를 사용자에게 보냄. 이 링크의 실제 내용은 "내 돈 100만원을 해커에게 송금해라"는 내용이 담긴, 당신의 인감도장만 찍으면 되는 '위조된 위임장'

3. 나도 모르는 날인 (요청 전송)
  - 사용자가 미끼 링크를 클릭하는 순간, 당신의 브라우저는 자기도 모르게 bank.com에 위조된 위임장(송금 요청)을 보냄. 이때 브라우저는 bank.com에 보낼 때마다 인감도장(세션 쿠키)을 자동으로 찍어서 보냄

4. 은행의 착각 (공격 성공)
  - 은행 입장에서는 정상적인 인감도장이 찍힌 위임장이 도착했으므로, 이 요청이 당신의 진짜 의사라고 믿고 송금을 실행 

**CSRF 공격의 방어**

- Django는 이러한 공격을 막기 위해 CSRF 토큰이라는 안전장치를 사용 
- 이는 위임장에 진짜 서명이 있는지 확인하는 것처럼, 모든 중요한 요청에 대해 "내가 직접 보낸 요청이 맞다"는 일회용 비밀 코드를 함께 보내도록 하여 위조된 요청을 막아줌

**CSRF Token 적용**

- DTL의 `csrf_token` 태그를 사용해 손쉽게 사용자에게 토큰 값을 부여
- 요청 시 토큰 값도 함께 서버로 전송될 수 있도록 하는 것

```html
<!--`templates/articles/new.html`-->
<h1>NEW</h1>
<form action="{% url 'articles:create' %}" method="POST">
  {% csrf_token %}
  <div>
    <label for="title">Title: </label>
    <input type="text" name="title" id="title">
  </div>
  <div>
    <label for="content">Content: </label>
    <textarea name="content" id="content"></textarea>
  </div>
  <input type="submit">
</form>
<hr>
<a href="{% url 'articles:index' %}">[back]</a>
```

```html
<!--실제 렌더링 결과 (개발자 도구 확인)-->
<form action="/articles/create/" method="POST">
  <input type="hidden" name="csrfmiddlewaretoken" value="랜덤한_토큰값">
  <div>
    <label for="title">Title: </label>
    <input type="text" name="title" id="title">
  </div>
  <div>
    <label for="content">Content: </label>
    <textarea name="content" id="content"></textarea>
  </div>
  <input type="submit">
</form>
```

**요청 시 CSRF Token을 함께 보내야 하는 이유**

- Django 서버는 해당 요청이 DB에 데이터를 하나 생성하는(DB에 영향을 주는) 요청에 대해 "Django가 직접 제공한 페이지에서 데이터를 작성하고 있는 것인지"에 대한 확인 수단이 필요한 것

- 겉모습이 똑같은 위조 사이트나 정상적이지 않는 요청에 대한 방어 수단 

- 기존 요청 향태
  - 요청 데이터 -> 게시글 작성

- 변경 요청 형태
  - 요청 데이터 + 인증 토큰 -> 게시글 작성 

**그런데 왜 POST일 때만 Token을 확인할까?**

- POST는 단순 조회(GET)와 달리 리소스의 변경(생성, 수정, 삭제)을 요청하는 의미와 기술적 특성을 지님
- DB에 조작을 가하는 요청은 반드시 인증 수단이 필요

>  데이터베이스에 대한 변경사항을 만드는 요청이기 때문에 토큰을 사용해 최소한의 신원 확인을 하는 것 

**게시글 작성 결과**

- 더 이상 URL Query String 형태로 보냈던 데이터가 표시되지 않음(기존 GET method 방식)

     ```
     http://127.0.0.1:8000/articels/create/?title=제목&content=내용%21
     ```

- POST 방식에서는 URL에 데이터가 노출되지 않음

- 게시글 생성 후 개발자 도구를 사용해 Form Data가 전송되는 것 확인 

   - `Network` 탭에서 요청을 확인하면, `Payload` 부분에 `Form Data`로 값이 전달됨
   - 즉, 사용자가 입력한 `title`, `content` 값이 안전하게 **Request Body**에 담겨 전송됨

---

## Redirect

**현재 문제 상황: 게시글 작성 후 응답 방식**

- 현재 서비스는 게시글 작성(POST 요청) 이후, 완료 메시지 페이지를 **직접 반환**
- **게시글 저장 후 페이지를 응답하는 것은 POST 요청에 대한 적절한 응답이 아님**
- 이후 새로고침/뒤로가기 등에서 원치 않는 동작 유발 가능

```bash
┌──────────────────────────────────────────────┐
│  게시글이 작성 되었습니다.                     │
└──────────────────────────────────────────────┘
```

**“완료 페이지 응답” 방식의 문제점**

- HTTP 표준 관점

  - POST는 **데이터 생성/변경**에 사용되며 **동일 요청 반복 금지**
  - 완료 페이지에서 새로고침 시 **중복 생성 위험**

```bash
# 새로고침에 따른 중복 생성 개념도
[REFRESH]  ──>  [SERVER]  ──>  [DUPLICATE DATA]
```

- 사용자 경험(UX) 관점

  - 완료 페이지를 직접 응답하는 방식은 **직관적이지 않음**
  - 브라우저 기록/상태 관리와 흐름이 어긋나 **혼란** 유발

```bash
[게시글 작성] -> [완료 페이지] -X- 새로고침 -> [또 완료 페이지]
                           (사용자 혼란/중복 위험)
```

**게시글 작성 성공 후 적절한 응답 방법**

- **서버는 데이터 저장 후 페이지를 직접 응답하지 말고, 사용자가 적절한 기존 페이지로 가도록 해야 함**
- 문장 변환: “사용자를 보낸다.” ⇒ “사용자가 **GET 요청을 한 번 더 보내도록** 해야 한다.”
- 즉, 서버가 클라이언트를 끌고 가는 게 아니라, **클라이언트가 새 GET 요청을 보내도록 유도**하는 응답을 사용

**게시글이 작성 성공 후 적절한 응답 방법**

`redirect()`

**클라이언트가 인자에 작성된 주소로 다시 요청**을 보내도록 하는 함수

**redirect() 함수 적용**

- create view 함수 변경

```python
# articles/views.py
from django.shortcuts import render, redirect

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    article = Article(title=title, content=content)
    article.save()
    return redirect('articles:detail', article.pk)
```

**redirect 동작 원리**

1. 클라이언트는 `redirect` 응답을 받으면 **detail URL로 다시 요청**을 보냄

2. 그 결과 `detail` view가 호출되어 해당 게시글의 detail 페이지가 응답됨

> 사용자는 “작성 완료 후 작성된 게시글 상세로 이동”한 것으로 자연스럽게 느낌

```python
from django.shortcuts import render, redirect

def create(request):
    return redirect('articles:detail', article.pk)
```

- 시퀀스 다이어그램

```bash
Client                          Django (Server)
  |                                      |
1 | POST /articles/create/ (title,content,csrf)  ---->
  |                                      |  2) create view 호출
  |                                      |    - DB에 Article 저장
  |                                      |    - redirect 응답(다음 URL 지시)
3 | <---- 302 Redirect: /articles/<pk>/  |
  |                                      |
4 | GET /articles/<pk>/  ---------------->
  |                                      |  5) detail view 호출
6 | <---- 200 OK (detail page HTML)      |
  |                                      |
# 결과: POST 이후 새로고침해도 중복 생성되지 않음 (PRG 패턴)
```

---

## Delete

**Delete 기능 구현**

- 최종 결과 화면 미리보기
```html
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8" />
<title>DETAIL – Redirect 결과</title>
</head>
<div class="wrap">
  <div class="browser">
    <div class="page">
      <h1>DETAIL</h1>
      <h3>8 번째 글</h3>
      <hr>
      <p>제목: 제목!</p>
      <p>내용: 내용!</p>
      <p class="muted">작성 시각: 2025-09-25 09:00</p>
      <p class="muted">수정 시각: 2025-09-25 09:10</p>
      <hr>
      <button>DELETE</button>
      <br>
      <a href="/articles/">[back]</a>
    </div>
  </div>
</div>
</body>
</html>
```

### 1-2. URL 설정 (`articles/urls.py`)

```python
# `articles/urls.py`
from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    # ...
    path("<int:pk>/delete/", views.delete, name="delete"),
]
```
```python
# `articles/views.py`
from django.shortcuts import get_object_or_404, redirect
from .models import Article

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect("articles:index")
```

```html
<!-- templates/articles/detail.html -->
<h2>DETAIL</h2>
<hr>

<p>{{ article.pk }}번째 글</p>

<p>제목: {{ article.title }}</p>
<p>내용: {{ article.content }}</p>
<p>작성 시각: {{ article.created_at }}</p>
<p>수정 시각: {{ article.updated_at }}</p>

<form action="{% url 'articles:delete' article.pk %}" method="POST">
  {% csrf_token %}
  <input type="submit" value="DELETE">
</form>

<a href="{% url 'articles:index' %}">[back]</a>
```

> 핵심: **삭제는 POST 요청으로만** 처리하고, CSRF 토큰을 반드시 포함

---

## Update

**Update 로직 — 필요한 view 함수의 개수는?**

```bash
사용자 입력 데이터를 받을 페이지를 렌더링 ─────────▶ 사용자가 입력한 요청 데이터를 받아 DB에 저장
edit(폼 렌더)                                          update(실제 수정 반영)
```

> **Update 로직 구현에는 두 개의 view 함수가 필요**

**edit — 페이지 렌더링 기능 구현**

- 최종 결과 화면 미리보기

```bash
# 왼쪽: DETAIL / 오른쪽: EDIT

DETAIL                                  EDIT
┌───────────────────────────────┐       ┌───────────────────────────────┐
│ 8번째 글                       │       │ EDIT                          │
│ 제목: 제목!                   │       │ Title: [제목!]                │
│ 내용: 내용!                   │       │ Content: [내용!]              │
│ 작성 시각: 20XX-XX-XX ...     │       │ [제출]                        │
│ 수정 시각: 20XX-XX-XX ...     │       │ [back]                        │
│ [EDIT] [DELETE] [back]        │       └───────────────────────────────┘
└───────────────────────────────┘
```

- 기능 구현

```python
# `articles/urls.py`
from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    # ...
    path("<int:pk>/edit/", views.edit, name="edit"),
    path("<int:pk>/update/", views.update, name="update"),
]
```

```python
# `articles/views.py`
from django.shortcuts import render, get_object_or_404, redirect
from .models import Article

def edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    context = {"article": article}
    return render(request, "articles/edit.html", context)
```

- 기능구현: 수정 시 이전 데이터가 출력 될 수 있도록 작성

```html
<!-- templates/articles/edit.html -->
<h1>EDIT</h1>

<form action="{% url 'articles:update' article.pk %}" method="POST">
  {% csrf_token %}
  <div>
    <label for="title">Title: </label>
    <!-- input 요소: 기존 값은 value 속성으로 미리 채움 -->
    <input type="text" name="title" id="title" value="{{ article.title }}">
  </div>

  <div>
    <label for="content">Content: </label>
    <!-- textarea 요소: value 속성이 없고 태그 사이에 기존 값을 넣음 -->
    <textarea name="content" id="content">{{ article.content }}</textarea>
  </div>

  <input type="submit" value="제출">
</form>

<hr>
<a href="{% url 'articles:index' %}">[back]</a>
```

- 기능구현: 수정 시 이전 데이터가 출력 될 수 있도록 작성하기 

input 요소:
  - 한 줄 텍스트(예: 제목) value 속성으로 기존 데이터 

  ```html
  <input type="text" name="title" id="title" value="기존데이터">
  ```

textarea 요소:
  - 여러 줄 텍스트(예: 본문)  value 속성이 없고, 태그 여닫는 사이에 값을 넣음

  ```html
  <textarea name="content" id="content">기존 데이터</textarea>
  ```

> input과 textarea 모두 기존 데이터를 화면에 미리 출력해 사용자가 편리하게 수정할 수 있도록 함


- 기능구현: edit 페이지로 이동하기 위한 하이퍼링크 작성 

```html
<!-- detail.html 일부 -->
<a href="{% url 'articles:edit' article.pk %}">[EDIT]</a><br>
<form action="{% url 'articles:delete' article.pk %}" method="POST" style="display:inline;">
  {% csrf_token %}
  <input type="submit" value="DELETE">
</form>
<a href="{% url 'articles:index' %}">[back]</a>
```

**update: 기능 구현**

```python
# `articles/urls.py`
urlpatterns = [
    # ...
    path("<int:pk>/update/", views.update, name="update"),
]
```

```python
# `articles/views.py`
def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:detail', article.pk)
```

- 작성 후 게시글 수정 테스트

```html
<!--`articles/edit.html`-->
<h1>EDIT</h1>
<form action="{% url 'articles:update' article.pk %}" method="POST">
  {% csrf_token %}
  <div>
    <label for="title">Title: </label>
    <input type="text" name="title" id="title" value="{{ article.title }}">
  </div>
  <div>
    <label for="content">Content: </label>
    <textarea name="content" id="content">{{ article.content }}</textarea>
  </div>
  <input type="submit">
</form>
<hr>
<a href="{% url 'articles:index' %}">[back]</a>
```

---

## GER & POST 비교

**GET & POST 비교**

| 구분           | GET                           | POST             |
|----------------|-------------------------------|------------------|
| 데이터 전송 방식 | URL의 Query string parameter   | HTTP body        |
| 데이터 크기 제한 | 브라우저 제공 URL 최대 길이     | 제한 없음        |
| 사용 목적       | 데이터 검색 및 조회            | 데이터 제출 및 변경 |

**GET 요청이 필요한 경우**

- 캐싱 및 성능
  - GET 요청은 캐시(Cache)될 수 있고, 이전 요청 결과를 다시 사용 가능
  - 동일한 검색 결과를 반복 요청할 때 빠른 응답 제공

- 가시성 및 공유
  - GET 요청은 URL에 데이터가 노출되어 북마크 및 공유가 가능

- RESTful API 설계
  - HTTP 메서드 의미에 따라 동작하도록 설계 → 일관성 유지

**HTTP request methods를 활용한 효율적 URL 구성**

- 동일한 URL이라도 method에 따라 동작이 다름  
- HTTP Methods를 통해 클라이언트가 서버에 "무엇을 할지" 명확히 전달
- URL이 같아도 사용되는 메서드(GET, POST등)에 따라 서버의 동작이 달라짐

```bash
(GET)  articles/1/   → 1번 게시글 조회 요청
(POST) articles/1/   → 1번 게시글 조작 요청
```

---

## Cache 

**캐시(Cache) 기본 개념**

데이터나 정보를 임시로 저장하여 다시 요청할 때 빠르게 제공하는 저장 공간

> 캐시의 장점
  - 빠른 응답 시간 → 이미 저장된 데이터를 즉시 제공
  - 서버 부하 감소 → 반복적인 데이터 요청을 줄여 서버 자원 절약
