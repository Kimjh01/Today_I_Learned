# Django 7 _ Authentication_System_01

## Cookie & Session

### HTTP

HyperText Transfer Protocol 문서와 같은 리소스들을 가져올 수 있도록 해주는 규약 (웹에서의 모든 데이터 교환의 기초)

> HTTP는 웹 브라우저와 서버가 서로 대화하기 위해 사용하는 공통 언어 또는 약속, 브라우저가 '이 페이지 보여줘'라고 요청(Request)을 보내면, 서버는 그에 맞는 HTML, 이미지 등을 응답(Response)으로 보내주는 방식으로 동작

**HTTP 특징**

1. 비 연결 지향(connectionless)

- 서버는 요청에 대한 응답을 보낸 후 연결을 끊음 
- 클라이언트는 서버와 서로 연겯되어 있는 상태가 아님

> HTTP가 비 연결 지향으로 설계된 이유? 
- 서버가 문서를 다 읽을 때까지 모든 사용자와의 연결을 계속 유지해야 한다면, 수많은 연결이 서버의 메모리와 자원을 차지하게 됨 
- 자원 낭비를 막기 위해 HTTP는 비 연결방식을 채택함

2. 무상태(stateless)

- 연결을 끊는 순간 클라이언트와 서버 간의 통신이 끝나며 상태 정보가 유지되지 않음
- 무상태의 의미 
  - 장바구니에 담은 상품을 유지할 수 없음
  - 로그인 상태를 유지할 수 없음 

> HTTP가 무상태로 설계된 이유?
- 서버가 모든 클라이언트 상태를 기억한다고 하면 저장하고, 관리해야 하므로 매우 복잡
-  여러 대의 서버를 운영할 때, 클라이언트 상태를 공유하기 위해서 서로 다른 서버가 연결되어야 하는 문제로 인해서 확장성이 저하 
- 무상태는 서버의 부담을 없애고 어떤 서버든 자유롭게 요청을 처리할 수 있게 만들어, 대규모 웹 서비스를 구축하는 데 핵심적인 역할을 함 

### 쿠키

서버가 사용자의 웹 브라우저에 전송하는 작은 데이터 조각

> 웹사이트가 사용자의 브라우저에 남기는 작은 '데이터 조각', 서버는 '나는 이전에 이 사이트에 방문 했었고, 로그인도 했어'와 같이 사용자를 기억하고 식별할 수 있음, 이를 통해 아이디와 비밀번홀ㄹ 다시 입력할 필요 없이 자동 로그인이 유지되거나, 장바구니에 담은 상풍이 저장 

**쿠키 특징**

- 서버가 사용자의 웹 브라우저에 전송하는 작은 데이터 조각 
- 사용자 인증, 추적, 상태 유지 등에 사용되는 데이터 저장 방식
-  Key_value 형식의 데이터 

**쿠키 사용 예시**

- 로그인 유지 (세션 관리) 
- 장바구니 
- 언어, 테마 등 사용자 설정 기억 
 
**쿠키 동작 예시**

1. 브라우저가 웹 서버에 웹 페이지를 요청
2. 웹 서버는 요청된 페이지와 함께 쿠키를 포함한 응답을 브라우저에게 전송
3. 브라우저는 받은 쿠키를 저장소에 저장하고, 쿠키의 속성(만료 시간, 도메인, 주소등)도 함께 저장됨
4. 이후 브라우저가 같은 웹 서버에 웹 페이지를 요청할 때, 저장된 쿠키 중 해당 요청에 적용 가능한 쿠키를 포함하여 함께 전송
5. 웹 서버는 받은 쿠키 정보를 확인하고, 필요에 따라 사용자 식별, 세션 관리 등을 수행
6. 웹 서버는 요청에 대한 응답을 보내며, 필요한 경우 새로운 쿠키를 설정하거나 기존 쿠키를 수정할 수 있음 



```bash
Client (Browser)        ->   HTTP Request   ->        Server (Django)
                           <-  HTTP Response  <-
```

1) 프로젝트 구조

```
cookie_auth_demo/
├─ manage.py
├─ shop/ (settings/urls)
├─ accounts/ (Custom User + 로그인/회원가입)
├─ cart/ (쿠키 기반 장바구니)
├─ products/ (상품)
└─ templates/
```

2) Settings

```python
# shop/settings.py
INSTALLED_APPS = [
    "accounts",
    "products",
    "cart",
]

AUTH_USER_MODEL = "accounts.User"
LOGIN_URL = "accounts:login"
LOGIN_REDIRECT_URL = "products:list"
LOGOUT_REDIRECT_URL = "products:list"
```

3) Custom User model

```python
 accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    nickname = models.CharField(max_length=30, blank=True)
```
4) Forms & Views

```python
# accounts/forms.py
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email", "nickname")

class LoginForm(AuthenticationForm):
    pass
```

```python
# accounts/views.py
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from .forms import SignupForm, LoginForm

def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("products:list")
    else:
        form = SignupForm()
    return render(request, "accounts/signup.html", {"form": form})

def login_view(request):
    return LoginView.as_view(authentication_form=LoginForm,
                             template_name="accounts/login.html")(request)

def logout_view(request):
    logout(request)
    return redirect("products:list")
```

5) Templates

```html
<!-- templates/base.html -->
<!doctype html>
<html lang="ko">
  <head>
    <meta charset="utf-8">
    <title>{% block title %}Demo{% endblock %}</title>
  </head>
  <body>
    <nav>
      {% if request.user.is_authenticated %}
        {{ request.user.username }} | 
        <a href="{% url 'accounts:logout' %}">로그아웃</a>
      {% else %}
        <a href="{% url 'accounts:login' %}">로그인</a> |
        <a href="{% url 'accounts:signup' %}">회원가입</a>
      {% endif %} |
      <a href="{% url 'products:list' %}">상품</a> |
      <a href="{% url 'cart:view' %}">장바구니</a>
    </nav>
    <hr>
    {% block content %}{% endblock %}
  </body>
</html>
```

6) Products

```python
# products/models.py
from django.db import models

class Product(models.Model):
    name  = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    def __str__(self): return self.name
```

```python
# products/views.py
from django.shortcuts import render
from .models import Product

def product_list(request):
    qs = Product.objects.all().order_by("id")[:20]
    return render(request, "products/list.html", {"products": qs})
```

```html
<!-- templates/products/list.html -->
{% extends "base.html" %}
{% block title %}상품 목록{% endblock %}
{% block content %}
<h1>상품 목록</h1>
<ul>
{% for p in products %}
  <li>
    {{ p.name }} - {{ p.price }}원
    <form action="{% url 'cart:add' p.id %}" method="post">
      {% csrf_token %}
      <input type="number" name="qty" value="1" min="1">
      <button type="submit">담기</button>
    </form>
  </li>
{% endfor %}
</ul>
{% endblock %}
```

7) Cart (쿠키 기반 장바구니)

```python
# cart/cookies.py
import json
CART_COOKIE_NAME = "cart"
CART_COOKIE_MAX_AGE = 60 * 60 * 24 * 30

def read_cart(request):
    raw = request.COOKIES.get(CART_COOKIE_NAME)
    if not raw: return {}
    try:
        return json.loads(raw)
    except: return {}

def write_cart(response, cart, secure=False):
    response.set_cookie(
        key=CART_COOKIE_NAME,
        value=json.dumps(cart, ensure_ascii=False),
        max_age=CART_COOKIE_MAX_AGE,
        httponly=True,
        samesite="Lax",
        secure=secure,
        path="/",
    )
    return response
```

```python
# cart/views.py
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from products.models import Product
from .cookies import read_cart, write_cart

def view(request):
    cart = read_cart(request)
    items, total = [], 0
    for pid, info in cart.items():
        qty, price = int(info["qty"]), float(info["price"])
        subtotal = qty * price
        total += subtotal
        items.append({"id": pid, **info, "subtotal": subtotal})
    return render(request, "cart/cart.html", {"items": items, "total": total})

def add(request, pk):
    product = get_object_or_404(Product, pk=pk)
    qty = int(request.POST.get("qty", 1))
    cart = read_cart(request)
    key = str(product.pk)
    current = cart.get(key, {"name": product.name, "price": float(product.price), "qty": 0})
    current["qty"] += qty
    cart[key] = current
    resp = HttpResponseRedirect(reverse("cart:view"))
    return write_cart(resp, cart, secure=request.is_secure())

def clear(request):
    resp = HttpResponseRedirect(reverse("cart:view"))
    resp.delete_cookie("cart", path="/")
    return resp
```

```html
<!-- templates/cart/cart.html -->
{% extends "base.html" %}
{% block title %}장바구니{% endblock %}
{% block content %}
<h1>장바구니</h1>
<table border="1">
<tr><th>ID</th><th>상품</th><th>가격</th><th>수량</th><th>소계</th></tr>
{% for it in items %}
<tr>
  <td>{{ it.id }}</td>
  <td>{{ it.name }}</td>
  <td>{{ it.price }}</td>
  <td>{{ it.qty }}</td>
  <td>{{ it.subtotal }}</td>
</tr>
{% empty %}
<tr><td colspan="5">비어 있음</td></tr>
{% endfor %}
</table>
<p>총액: {{ total }}</p>
<form action="{% url 'cart:clear' %}" method="post">{% csrf_token %}
  <button type="submit">초기화</button>
</form>
{% endblock %}
```

**보안 포인트**

* **HttpOnly** : JS 접근 차단 → XSS 완화
* **Secure** : HTTPS에서만 전송
* **SameSite=Lax** : 기본 추천
* **Max-Age** : 쿠키 수명

**쿠키의 작동 원리와 활용**

1. 쿠키 저장 방식
- 브라우저(클라이언트)는 쿠키를 KEY-VALUE의 데이터 형식으로 저장 
- 쿠키에는 이름, 값 외에도 만료 시간, 도메인, 경로 등의 추가 속성이 포함 됨 

2. 쿠키 전송 과정
- 서버는 HTTP 응답 헤더의 Set-Cookie 필드를 통해 클라이언트에게 쿠키를 전송
- 브라우저는 받은 쿠키를 저장해 두었다가, 동일한 서버에 재요청 시 HTTP 요청 Header의 Cookie 필드에 저장된 쿠키를 함께 전송

3. 쿠키의 주요 용도
- 두 요청이 동일한 브라우저에서 들어왔는지 아닌지를 판단할 때 주로 사용됨
- 이를 이용해 사용자의 로그인 상태를 유지할 수 있음
- 상태가 없는(statelesss) HTTP 프로토콜에서 상태 정보를 기억시켜 주는 역할 

> 서버에게 '나 로그인 된(인증된) 사용자야!' 라는 인증 정보가 담긴 쿠키를 매 요청마다 계속 보내는 것 

**쿠키 사용 목적**

1. 세션 관리(Session management) 
  - 로그인, 아이디 자동완성, 공지 하루 안보기, 팝업 체크, 장바구니 등의 정보 관리 

2. 개인화(Personalization)
  - 사용자 선호 설정(언어 설정, 테마 등)저장

3. 추적, 수집(Tracking)
  - 서용자 행동을 기록 및 분석

> 쿠키는 탈취될 수 있으니, 비밀번호 등 민감한 정보는 절대 직접 저장하면 안됨, 모든 요청에 포함되어 전송되므로, 크기를 최소화해야 사이트 성능에 유리함 

### 세션

- 서버 측에서 생성되어 클라이언트와 서버 간 상태를 유지
- 상태 정보는 서버에 저장, 클라이언트에는 세션 ID만 쿠키로 전달
- 쿠키만 사용하는 것보다 훨씬 보안적

```bash
1. 클라이언트 로그인 성공
2. 서버: 세션 데이터 생성 후 저장
3. 서버: 세션 ID 발급 → Set-Cookie: sessionid=...
4. 브라우저: 쿠키에 sessionid 저장
5. 이후 요청 시 sessionid 포함
6. 서버: 세션 ID 확인, 로그인 상태 유지
7. 서버: 요청 처리 후 응답
```

**세션 동작 원리**

1. 클라이언트 로그인 요청 → 서버가 인증 성공 시 세션 데이터 생성 후 저장
2. 세션 데이터 인증용 세션 ID 발급
3. 세션 ID를 클라이언트에게 응답 (데이터는 서버에 저장, 클라이언트엔 열쇠만 전달)
4. 클라이언트는 세션 ID를 쿠키에 저장
5. 클라이언트가 동일 서버에 재접속 시 쿠키(session id)와 함께 요청 전송
6. 서버는 session id를 확인하여 로그인 상태 확인
7. 서버는 요청 처리 후 응답

```bash
Client --(1. 로그인 성공)--> Server
Client (2. 세션 데이터 생성/저장)--> Server
Client <--(3. 세션 ID 응답) Server
Client <--(4. 세션 ID 쿠키 저장) Server
Client --(5. 쿠키 전송)--> Server
Client <--(6. 세션 id 확인)-- Server
Client <--(7. 응답)-- Server
```

**세션 특징**

- 서버 측에서 생성되어 상태를 유지
    - 서버의 메모리나 데이터베이스에 저장되므로, 서버 리소스를 사용(효율적 관리 필요)
- 상태 정보를 저장하는 방식
- 쿠키에 세션 ID 저장, 매 요청마다 전달
- 영구적 유지되지 않음

> 중요한 데이터 저장 → 보안 주의 필요, 세션 ID 탈취 시 공격자가 사용자 행세 가능

**세션 정리**

1. 서버는 세션 데이터 생성 후 저장 → 세션 ID 생성
2. 클라이언트는 세션 ID를 쿠키에 저장
3. 이후 모든 요청에 쿠키 포함 → 서버가 인증

**쿠키와 세션의 목적**

- 클라이언트와 서버 간 **상태 정보 유지하고 사용자 식별**하기 위함

## Django Authentication System 

**인증(Authentication)의 필요성**

- 클라이언트/서버 간 상태 정보를 유지해야 함
- 서로 다른 사용자를 식별해야 함
- 로그인 = 나임을 증명하는 절차
- 다양한 인증이 존재
    - 아이디/비밀번호
    - 소셜 로그인 (OAuth)
    - 생체인증

> Django에서는 사용자 인증과 관련된 가장 중요하고 기본적인 뼈대를 제공 Django Authentication System

**Django Authentication System**

- Django가 제공하는 사용자 인증 시스템
- 기본 제공 기능:

  - **User Model**: 사용자 관리
  - **Session 관리**: 로그인 상태 유지
  - **기본 인증**: ID/Password

> 활용 예시: 로그인, 로그아웃, 회원가입, 정보 수정

**기본 User Model의 한계**

- 인증 후 사용된 User Model은 별도의 User 클래스 정의 없이 내장된 auth 앱에 작성된 Uset 클래스를 사용
- Django 기본 `User` 모델은 `username`, `password` 등 제한적 필드만 제공
- 추가 정보(생년월일, 주소 등) 확장이 어려움

**내장된 auth 앱**

- `username`, `password`, `email` 등의 필드를 가진 User 모델을 제공
- `django.contrib.auth` 에 기본 User Model 포함
- 단순히 로그인 여부만 확인하는 것을 넘어, 사용자별 또는 그룹별로 특정 행동에 대한 권한 부여가 가능
- `settings.py`에서 INSTALLED_APPS에 포함되어 있음

**User Model 대체 필요성**

- 프로젝트 요구에 맞춰 사용자 모델 확장 가능
- 예: 이메일을 username으로 사용, 필요 없는 필드 제거, 데이터베이스 모델을 더 간결하게 관리할 수 있음

> Django에서 제공하는 기본 유저 모델이 아닌 우리가 직접 커스텀한 유저 모델을 사용해보자

## Custom User model 

**사전 준비**

- 두 번째 app `accounts` 생성 및 등록
- `auth`와 관련한 경로나 키워드들은 Django 내부적으로 `accounts`라는 이름을 사용하므로 동일하게 지정 권장

```python
# accounts/urls.py
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = []
```

```python
# crud/urls.py
urlpatterns = [
    ...,
    path('accounts/', include('accounts.urls')),
]
```

**Custom User Model로 대체하기**

- `AbstractUser` 클래스를 상속받아 커스텀 User 클래스 작성
- 기존 User 클래스도 `AbstractUser`를 상속받으므로 구조 동일

```python
# accounts/models.py
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
```

- Django 기본 User 모델을 우리가 작성한 User로 교체
- `AUTH_USER_MODEL` 값을 변경해야 함

```python
# accounts/models.py
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
```

```python
# settings.py
AUTH_USER_MODEL = 'accounts.User'
```

- admin site에 새 User 모델 등록
- 기본 User 모델이 아니므로 직접 등록 필요

```python
# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)
```

**AUTH_USER_MODEL**

- Django 프로젝트의 User를 나타내는 데 사용되는 모델을 지정하는 속성

**주의**

- 프로젝트 중간에 `AUTH_USER_MODEL` 변경은 권장하지 않음
- 이미 프로젝트가 진행 중이라면 DB 초기화 후 진행 필요

**사용하는 User 테이블의 변화**

* 기존 `auth_user` 테이블이 `accounts_user` 테이블로 대체됨

```bash
Before: auth_user
After:  accounts_user
```

**프로젝트 시작 시 주의사항**

* 새 프로젝트라면 반드시 User 모델을 대체해야 함
* 기본 User 모델과 동일하게 작동하면서, 나중에 맞춤 설정 가능

> 지금 당장 필요 없어도 만들어 두는 것을 권장, 나중에 닉네임, 프로필 등의 필드를 쉽게 확장 가능, 모델 생성 후 `settings.py`에 `AUTH_USER_MODEL` 설정 필요

## Login

**Login**

- 클라이언트와 서버 간 상태 정보를 유지하기 위해 쿠키와 세션을 사용
- 서버는 요청을 보낸 사용자가 누구인지 식별해야 함
- 인증(id/password)을 통해 사용자가 "나"임을 증명하는 과정이 바로 Login

> Login은 인증 완료 후, 세션을 만들고 클라이언트와 연결하는 단계

1. 로그인 (id/password)
2. 로그인 인증
3. 세션 생성 후 서버 저장
4. 클라이언트에 쿠키 전달

> Session: 서버 측에서 생성되어 클라이언트와 서버 간 상태 정보를 유지하는 데이터 저장 방식

**로그인 페이지 작성**

```python
# accounts/urls.py
app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
]
```

- .../accounts/login/url로 요청이 들어왔을 때 실행할 login 함수 작성
- 로그인 인증에 사용할 데이터를 입력 받는 built-in form(AuthenticationForm) 사용

```python
# accounts/views.py
from django.contrib.auth.forms import AuthenticationForm

def login(request):
    if request.method == 'POST':
        pass
    else:
        form = AuthenticationForm()
        context = {'form': form}
    return render(request, 'accounts/login.html', context)
```

**AuthenticationForm()**

- 로그인 인증에 사용할 데이터를 입력 받는 built-in form 
- User 모델과 직접 연결된 "ModelForm"이 아닌, 일반 "Form"을 상속 받음
  - 일반 "Form"이기 때문에 사용자를 생성하거나 수정하는 용도가 아닌 "인증"하는 역할만 수행  

```python
class AuthenticationForm(forms.Form):
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True}))
    password = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
    )
```

> User 모델과 직접 연결된 ModelForm이 아닌 일반 Form을 상속받음 → **“인증” 전용**

- 로그인 정보를 서버에 안전하게 전송하기 위해 "POST 방식"을 사용
- CSRF 공격을 방지하기 위해 csrf_token 작성
- 서버로부터 전달받은 AuthenticationForm을 화면에 출력  

```html
<!-- accounts/login.html -->
<h1>로그인</h1>
<form action="{% url 'accounts:login' %}" method="POST">
  {% csrf_token %}
  {{ form }}
  <input type="submit">
</form>
```

- 사용자가 입력한 로그인 정보를 입력받는 로직 "POST" 조건문에 작성
- 입력 받은 정보를 기반으로 로그인하여 세션을 만드는 "login" 함수를 활용

```python
# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'accounts/login.html', context)
```

**login(request, user)**

```python
auth_login(request, form.get_user())
```
- `AuthenticationForm`을 통해 인증된 사용자를 로그인 하는 함수
- `request`: 세션 정보 접근하기 위해 사용
- `user`: 로그인된 사용자 객체 기록하기 위해 사용

**get_user()**

- `AuthenticationForm`의 인스턴스 메서드 

> 유효성 검사를 통과했을 경우, 로그인 한 사용자 객체를 반환

**로그인 링크 작성**

```html
<!-- articles/index.html -->
<h1>Articles</h1>
<a href="{% url 'accounts:login' %}">Login</a>
<a href="{% url 'articles:create' %}">NEW</a>
<hr>
```

## Template with Authentication data

**Template with Authentication data**

- 템플릿에서 인증 관련 데이터를 출력하는 방법

**현재 로그인 되어있는 유저 정보 출력하기**

- user라는 context 데이터를 사용할 수 있는 이유?

> django가 미리 준비한 context 데이터가 존재하기 때문(context processors)

```html
<!-- articles/index.html -->
<h3>Hello, {{ user.username }}</h3>
```

> `user`는 Django의 context processor(`django.contrib.auth.context_processors.auth`) 덕분에 자동 제공됨


**context processors**

- 템플릿이 렌더링 될 때 호출 가능한 컨텍스트 데이터 목록
- 작성된 컨텍스트 데이터는 기본적으로 템플릿에서 사용 가능한 변수로 포함
- django에서 자주 사용하는 데이터 목록을 미리 템플릿에 로드 해 둔 것 

```python
# settings.py
TEMPLATES = [
    {
        ...
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
```

## 쿠키의 수명

**쿠키 종류별 Lifetime**

1. **Session cookie** 
- 현재 세션(current session)이 종료되면 삭제됨
- 브라우저 종료 시 삭제

2. **Persistent cookies** 
- Expires 속성에 지정된 날짜 혹은 Max-Age 속성에 지정된 기간이 지나면 삭제됨

## 쿠키와 보안

1. 제한된 정보만 저장
- 쿠키에는 보통 중요하지 않은 정보만 저장 (사용자 ID나 세션 번호 같은 것)

2. 암호화
- 중요한 정보는 서버에서 암호화해서 쿠키에 저장

3. 만료 시간 설정
- 쿠키에는 만료 시간을 설정, 시간이 지나면 자동으로 삭제

4. 도메인 제한
- 쿠키는 특정 웹사이트에서만 사용할 수 있도록 설정할 수 있음 

**쿠키와 개인정보 보호**

* 쿠키 사용 동의 필요 (법적 규제)
* 사이트는 쿠키 정책 고지 + 사용자 동의 획득

## Django에서의 세션 관리 

**세션 in Django**

- DB 기반(`database-backed sessions`) 저장 방식을 기본 값으로 사용
- session 정보는 DB의 django_session 테이블에 저장
- Django는 요청안에 특정 session id를 포함하는 쿠키를 사용해서 각각의 브라우저와 사이트가 연결된 session 데이터를 알아냄
> Django는 우리가 session 메커니즘(복잡한 동작원리)에 대부분을 생각하지 않게끔 많은 도움을 줌

## AuthenticationForm 내부 코드 

**Django GitHub 코드 참고**

* [AuthenticationForm() 코드](https://github.com/django/django/blob/main/django/contrib/auth/forms.py#L302)
* [AuthenticationForm.get_user()](https://github.com/django/django/blob/main/django/contrib/auth/forms.py#L373)

## User 모델 대체하기 Tip 

User 모델을 대체하는 순서를 숙지하기 어려울 경우 `AUTH_USER_MODEL` 교체 시 공식 문서 순서대로 진행하는 것 권장