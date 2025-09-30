# Django 8 _ Authentication_System_02

## Login 

- 클라이언트와 서버 간의 상태 정보를 유지하기 위해 **쿠키와 세션**을 사용
- 서버는 각기 다른 사용자를 식별해야 하며, 이를 위해 인증 절차가 필요
- 서버에 "내가 누구인지"를 인증하는 과정이 **Login**
- Login 과정 = **인증(id/password) 완료 + Session 생성 + 클라이언트 연결**

> Session: 서버 측에서 생성되어 클라이언트와 서버 간 상태를 유지하는 데이터 저장 방식.

1. 사용자가 로그인 정보(id/password)를 입력
2. 서버에서 인증 처리
3. 인증 성공 시 서버가 세션(Session) 생성
4. 클라이언트에 세션 ID 전달 (쿠키 저장)

**로그인 페이지 작성**

- 로그인 경로 URL 생성

```python
# accounts/urls.py
app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
]
```

- `/accounts/login/` 요청 시 실행할 `login` 함수 작성
- 로그인 인증에 사용하는 built-in form: **AuthenticationForm**

```python
# accounts/views.py
from django.contrib.auth.forms import AuthenticationForm

def login(request):
    if request.method == 'POST':
        pass
    else:
        form = AuthenticationForm()
        context = {
            'form': form,
        }
    return render(request, 'accounts/login.html', context)
```

## AuthenticationForm()

- 로그인 인증에 사용할 데이터를 입력 받는 built-in form
- `ModelForm`이 아닌 일반 `Form`을 상속받음
  → 사용자 생성/수정이 아니라 **인증**역할만 수행

```python
class AuthenticationForm(forms.Form):
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
    )
```

- 로그인 정보를 서버에 안전하게 전달하기 위해 `POST` 방식 사용
- CSRF 공격 방지를 위해 `{% csrf_token %}` 작성
- 서버에서 전달받은 AuthenticationForm을 화면에 출력

```html
<!-- accounts/login.html -->
<h1>로그인</h1>
<form action="{% url 'accounts:login' %}" method="POST">
    {% csrf_token %}
    {{ form }}
    <input type="submit">
</form>
```

- 사용자가 입력한 로그인 정보를 받는 로직은 `POST` 조건문에 작성
- 입력받은 정보를 기반으로 로그인 후 세션을 생성하는 `login` 함수 사용

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

- `AuthenticationForm`을 통해 인증된 사용자를 로그인 처리
- 매개변수

  - `request`: 현재 사용자의 세션 정보 접근
  - `user`: 로그인된 사용자 기록

```python
auth_login(request, form.get_user())
```

**get_user()**

- AuthenticationForm의 인스턴스 메서드
- 유효성 검사를 통과하면 로그인한 사용자 객체를 반환

**세션 데이터 확인하기**

- 로그인 후 발급받은 세션을 확인할 수 있음
- DB의 `django_session` 테이블에서 `session_key`, `session_data`, `expire_date` 확인 가능

- 브라우저 개발자도구 → Application → Cookies에서 확인 가능
- `sessionid`가 클라이언트에 저장됨

**로그인 링크 작성**

- 메인 페이지에서 로그인 페이지로 이동할 수 있는 링크 작성

```html
<!-- articles/index.html -->
<h1>Articles</h1>
<a href="{% url 'accounts:login' %}">Login</a>
<a href="{% url 'articles:create' %}">NEW</a>
```

## Logout 

**logout**
- 로그아웃은 Session을 삭제하는 과정
- 서버 DB에 저장된 세션 데이터를 비우고, 클라이언트 쿠키에서 세션 ID 제거

> Cookie: 서버가 사용자의 웹 브라우저에 전송하는 작은 데이터 조각

**logout(request)**

1. DB에서 현재 요청(Session Data)을 삭제  
2. 클라이언트 쿠키에서도 Session ID 삭제

**로그아웃 로직 작성**

- 로그아웃 경로 URL 생성

```python
# accounts/urls.py
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
```

- `/accounts/logout/` 요청 시 실행할 `logout` 함수 작성
- DB의 세션 데이터 삭제 + 클라이언트 쿠키에서 세션 ID 제거

```python
from django.contrib.auth import logout as auth_logout

def logout(request):
    auth_logout(request)
    return redirect('articles:index')
```

- 로그아웃 요청은 **POST 방식**으로 처리
- CSRF 공격 방지를 위해 `{% csrf_token %}` 작성

```html
<!-- articles/index.html -->
<h1>Articles</h1>
<a href="{% url 'accounts:login' %}">Login</a>
<form action="{% url 'accounts:logout' %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="Logout">
</form>
```

## AbstractUser Class

**Abstract Base Classes (추상 기본 클래스)**

- 여러 모델에 공통 정보를 재사용할 때 사용하는 클래스
- 데이터베이스 테이블을 직접 만들지 않고, 다른 모델의 부모 클래스로 사용됨
- 인증에 필요한 최소한의 기능만 제공

**AbstractUser Class**

- **관리자 권한 포함**, User 모델의 완전한 기능을 가진 클래스
- `AbstractBaseUser`를 상속하는 추상 클래스
- Django 기본 User 모델의 모든 필드(username, email 등)가 이미 구현되어 있음

**추상 기본 클래스 정리**

| 구분     | AbstractBaseUser                | AbstractUser                          |
| ------ | ------------------------------- | ------------------------------------- |
| 제공 필드  | 최소한의 인증 필드 (비밀번호, last_login 등) | 기본 User 모델의 모든 필드 (username, email 등) |
| 장점     | 최대의 유연성과 자유도                    | 개발 속도가 빠르고 편리함                        |
| 사용 케이스 | 전화번호 기반 등 완전히 새로운 인증 체계         | 기존 인증 유지 + 프로필 사진, 닉네임 같은 필드 추가       |
| 예시     | 기본 피자 도우                        | 토핑이 올라간 피자                            |

## 회원 가입

- User 객체를 **Create**하는 과정
- 사용자가 입력한 ID, 비밀번호 등을 DB에 저장하여 새로운 User 생성

- User 객체를 **Create**하는 과정
- 사용자가 입력한 ID, 비밀번호 등을 DB에 저장하여 새로운 User 생성

### 

**회원가입 페이지 작성**

- 회원가입 경로 URL 생성

```python
# accounts/urls.py
urlpatterns = [
    path('signup/', views.signup, name='signup'),
]
```

- `/accounts/signup/` 요청 시 실행할 `signup` 함수 작성
- 회원가입에는 Django built-in form `UserCreationForm` 사용

```python
# accounts/views.py
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    if request.method == 'POST':
        pass
    else:
        form = UserCreationForm()
        context = {'form': form}
    return render(request, 'accounts/signup.html', context)
```

**UserCreationForm()**

- 회원가입 데이터 입력을 받는 built-in **ModelForm**
- 유효성 검사를 통과한 데이터로 새 User 객체 생성 후 DB에 저장
- 비밀번호는 자동으로 암호화되어 저장됨

```python
class UserCreationForm(BaseUserCreationForm):
    def clean_username(self):
        username = self.cleaned_data.get("username")
        if username and self._meta.model.objects.filter(username__iexact=username).exists():
            self._update_errors(
                ValidationError({"username": self.instance.unique_error_message(self._meta.model, ["username"])})
            )
        return username
```

- 회원가입 데이터 전송은 **POST 방식**으로 처리
- CSRF 공격 방지를 위해 `{% csrf_token %}` 사용
- 서버에서 전달받은 `UserCreationForm`을 화면에 출력

```html
<!-- accounts/signup.html -->
<h1>회원가입</h1>
<form action="{% url 'accounts:signup' %}" method="POST">
    {% csrf_token %}
    {{ form }}
    <input type="submit">
</form>
```

**회원 가입 로직 에러**

- 회원가입 시도 후 에러 발생

  ```
  Manager isn't available; 'auth.User' has been swapped for 'accounts.User'
  ```
- 원인: 기본 `UserCreationForm`이 과거 Django의 기본 `User` 모델을 사용하도록 작성되어 있기 때문

> **TIP**
>
> - 에러 메시지를 직접 확인하고 원인을 분석하는 습관을 길러야 함
> - 에러 자체가 학습 자료가 됨

- `UserCreationForm`은 Meta 클래스에서 기본 User 모델을 참조:

```python
class BaseUserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username",)
```

- 해결 방법: **Custom User Model**을 사용하도록 연결


**커스텀 유저 모델을 사용하기 위해 Form 재작성**

- `get_user_model()`을 활용하여 현재 프로젝트에서 활성화된 User 모델을 가져옴

```python
# accounts/forms.py
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
```

**get_user_model()**

- 현재 프로젝트에서 활성화된 User 모델을 반환하는 함수
- `settings.AUTH_USER_MODEL`에 따라 기본 User 모델 또는 Custom User 모델을 가져옴
- `User`를 직접 참조하는 대신 `get_user_model()`을 사용하는 것이 권장됨

> **장점**
>
> - User 모델이 변경되어도 코드 수정 불필요
> - 재사용성과 유연성 향상

**User 모델을 직접 참조하지 않는 이유**

- `get_user_model()`을 쓰면 Custom User Model 자동 반영
- Django 공식 문서에서도 `User` 직접 참조 대신 `get_user_model()` 사용을 권장

**회원 가입 로직 완성**

- 기존 `UserCreationForm` → `CustomUserCreationForm`으로 교체

```python
# accounts/views.py
from .forms import CustomUserCreationForm

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {'form': form}
    return render(request, 'accounts/signup.html', context)
```

## 회원 탈퇴 

- User 객체를 삭제하는 과정
- `request.user.delete()`를 통해 현재 로그인한 사용자를 삭제

```python
def delete(request):
    request.user.delete()
    return redirect('articles:index')
```

> **TIP**
> 실제 서비스에서는 물리적으로 삭제하기보다는 계정을 **비활성화 처리**하는 경우가 많음

**회원 탈퇴 로직 작성**

- URL 경로 생성

```python
# accounts/urls.py
urlpatterns = [
    path('delete/', views.delete, name='delete'),
]
```

- .../accounts/delete/url로 요청이 들어왔을 때 실행할 delete 메서드 작성
- 현재 로그인한 사용자 정보를 활용해 삭제 후 메인 페이지로 리다이렉트
- 탈퇴 버튼은 POST 방식으로 작성

```python
# accounts/views.py
def delete(request):
    request.user.delete()
    return redirect('articles:index')
```

```html
<!-- articles/index.html -->
<form action="{% url 'accounts:delete' %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="회원탈퇴">
</form>
```

## 인증된 사용자에 대한 접근 제한

1. is_authenticated 속성
2. login_required 데코레이터 

### is_authenticated 속성

**is_authenticated**

- 사용자가 인증 되었는지 여부를 알 수 있는 User model의 읽기 전용 속성
- 인증 사용자에 대해서는 항상 `True`, 비인증 사용자에 대해서는 항상 `False`
- 사용되는 경우
  - 사용자의 로그인 상태에 따라 다른 메뉴를 보여줄 때
  - view 함수 내에서 특정 기능을 로그인한 사용자에게만 허용하고 싶을 때

**is_authenticated 적용하기**

- 로그인과 비로그인 상태에서 화면에 출력되는 링크를 다르게 설정 

```html
<!--articles/index.html-->
{% if request.user.is_authenticated %}
    <h3>Hello, {{ user.username }}</h3>

    <a href="{% url 'articles:create' %}">NEW</a>

    <form action="{% url 'accounts:logout' %}" method="POST">
        {% csrf_token %}
        <input type="submit" value="Logout">
    </form>

    <form action="{% url 'accounts:delete' %}" method="POST">
        {% csrf_token %}
        <input type="submit" value="회원탈퇴"> </form>

    <a href="{% url 'accounts:update' %}">회원정보 수정</a> {% else %}
    <a href="{% url 'accounts:login' %}">Login</a>
    <a href="{% url 'accounts:signup' %}">Signup</a>
{% endif %}
```

- 인증된 사용자라면 로그인/회원가입 로직을 수행할 수 없도록 하기 

```python 
# accounts/views.py

def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')

def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
```

**login_required**

- 인증된 사용자에 대해서만 view 함수를 실행시키는 데코레이터 
- 비인증 사용자의 경우 /accounts/login/ 주소로 redirect 시킴
- 사용되는 경우 
  - 게시글 작성, 댓글 달기 등 누가 작성했는지 중요한 곳에서 사용

> 데코레이터: 기존 함수를 감싸, 특별한 기능(인증 등)을 추가하는 함수

**login_required 적용하기**

- 인증된 사용자만 게시글을 작성/수정/삭제 할 수 있도록 수정 

```python 
# articles/views.py
from django.contrib.auth.decorators import login_required

@login_required
def create(request):
    pass

@login_required
def delete(request, article_pk):
    pass

@login_required
def update(request, article_pk):
    pass
```

- 인증된 사용자만 로그아웃/탈퇴/수정/비밀번호 변경 할 수 있도록 수정 

```python 
# accounts/views.py
from django.contrib.auth.decorators import login_required

@login_required
def logout(request):
    pass

@login_required
def delete(request):
    pass

@login_required
def update(request):
    pass

@login_required
def change_password(request):
    pass
```

## is_authenticated 코드

- 메서드가 아닌 속성 값임을 주의 

```python 
@property
def is_authenticated(self):
    """
    Always return True. This is a way to tell if the user has been
    authenticated in templates.
    """
    return True
```

## 회원가입 후 자동 로그인 

- 회원가입 성공한 user 객체를 활용해 login 진행 

```python 
# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login 
from .forms import CustomUserCreationForm

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user) 
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)
```

```python 
def save(self, commit=True):
    user = super().save(commit=False)
    user.set_password(self.cleaned_data["password"]) 
    if commit:
        user.save()
    return user
```

## 회원 탈퇴 개선

**탈퇴와 함께 기존 사용자의 Session Data 삭제 방법**

- 사용자 객체 삭제 이후 로그아웃 함수를 호출해야 함
- 단, "탈퇴(1)후 로그아웃(2)"의 순서가 바뀌면 안됨 
  - 먼저 로그아웃이 진행되면 해당 요청 객체 정보가 없어지면서, 탈퇴에 필요한 유저 정보 또한 없어지기 때문

```python 
# accounts/views.py
@login_required
def delete(request):
    request.user.delete() 
    auth_logout(request) 
    return redirect('articles:index')
```

## Auth built-in form 코드 

- UserCreationForm()

* [UserCreationForm](https://github.com/django/django/blob/5.2/django/contrib/auth/forms.py#L271)

```python 
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    def clean_username(self):
        """Reject usernames that differ only in case."""
        username = self.cleaned_data.get("username")
        if (
            username
            and self._meta.model.objects.filter(username__iexact=username).exists()
        ):
            self._update_errors(
                ValidationError(
                    {
                        "username": self.instance.unique_error_message(
                            self._meta.model, ["username"]
                        )
                    }
                )
            )
        else:
            return username
```