# Django 1 _ Design_Pattern

## Web Application 

- 인터넷을 통해 사용자에게 제공되는 소프트웨어 프로그램을 구축하는 과정
- 다양한 디바이스(모바일, 태블릿, PC등)에서 웹 브라우저를 통해 접근하고 사용할 수 있음

> 네이버를 비롯한 포털, 쿠팡과 같은 인터넷 쇼핑몰부터 Google Docs와 같은 웹 문서 작업 도구등
> 인터넷을 통해 접할 수 있으며 이를 통해 제공되는 서비스르르 통틀어 Web Servise라고 함

### Client and Server

Client - 서비스를 요청하는 주체 
- 사용자의 웹 브라우저, 모바일 앱

Server - 클라이언트의 요청에 응답하는 주체 

> 일반적인 웹 서비스에서는 클라이언트가 페이지를 달라고 "요청"할 경우 서버가 페이지를 "응답"해줌

**우리가 웹 페이지를 보게 되는 과정**

1) 웹 브라우저(클라이언트)에서 'google.com'을 입력 후 Enter

2) 웹 브라우저는 인터넷에 연결된 전세계 어딘 가에 있는 구글 컴퓨터(서버)에게 '메인 홈페이지.html'파일을 달라고 요청

3) 요청을 받은 구글 컴퓨터는 데이터베이스에서 '메인 홈페이지.html'파일을 찾아 응답

4) 웹 브라우저는 전달받은 '메일 홈페이지.html' 파일을 사람이 볼 수 있도록 해석해주고 사용자는 구글의 메인 페이지를 보게 됨

### Frontend & Backend

**웹 개발에서의 Frontend와 Backend**

Frontend
- 사용자 인터페이스 (UI)를 구성하고, 사용자가 애플리케이션과 상호작용을 할 수 있도록 함
> HTML, CSS, JavaScript, 프론트엔드 프레임워크 등

Backend
- 서버 측에서 동작하며, 클라이언트의 요청에 대한 처리와 데이터베이스와의 상호작용 등을 담당
> 서버 언어 (Python, Java 등) 및 백앤드 프레임워크, 데이터베이스, API, 보안 등

**Frontend와 Backend**
Frontend
- HTMl, CSS, JavaScript를 이용해 UI를 구성
> Vue.js: 프론트엔드로 활용되는 대표적인 프레임워크

Backend
- 클라이언트의 요청에 대한 처리와 데이터베이스 상호작용
> Django는 백앤드로 활용되는 대표적인 프레임워크 

---

## Framework 

### Web Framework 

웹 애플리케이션을 빠르게 개발할 수 있도록 도와주는 도구
> 개발에 필요한 기본 구조, 규칙, 라이브러리 등을 제공 (로그인/로그아웃, 회원관리, 데이터베이스, 보안 등)

### Django Framework 

Python 기반의 대표적인 웹 프레임워크
> 클라이언트 - 서버 구조의 서버를 구현하는 것이 Django를 배우는 목적

**왜 Django를 사용하는가?**

다양성
- Python 기반으로 웹, 모바일 앱 백엔드, API 서버 및 빅데이터 관리 등 광범위한 서비스 개발에 적합

확장성 
- 대량의 데이터에 대해 빠르고 유연하게 확장할 수 있는 기능을 제공

보안 
- 취약점으로부터 보호하는 보안 기능이 기존적으로 내장되어 있음

커뮤니티 지원
- 개발자를 위한 지원, 문서 및 업데이트를 제공하는 활성화 된 커뮤니티 

---

## 가상 환경

Virtual Environment 
- 하나의 컴퓨터 안에서 또 다른 '독립된' 파이썬 환경

**가상 환경이 필요한 시나리오 1**
1. 한 개발자가 2개의 프로젝트(A와 B)를 진행해야 하는 상황
2. 프로젝트 A는 requests 패키지 버전 1이 필요
3. 프로젝트 B는 requests 패키지 버전 2이 필요
4. 하지만 파이썬 환경에서 패키지는 1개의 버전만 존재할 수 있음
5. A와 B의 프로젝트의 다른 패키지 버전 사용을 위한 **독립적인 개발 환경**이 필요

**가상 환경이 필요한 시나리오 2**
1. 한 개발자가 2개의 프로젝트(A와 B)를 진행해야 하는 상황
2. 프로젝트 A는 water 패키지가 필요
3. 프로젝트 B는 fire 패키지가 필요
4. 하지만 파이썬 환경에서 water 패키지와 fire 패키지를 함께 사용하면 충돌이 발생하기 때문에 설치할 수 없음
5. A와 B의 프로젝트의 패키지 충돌을 피하기 위한 **독립적인 개발 환경**이 필요

**가상 환경 비유**
- 같은 집(컴퓨터) 안에, 방(가상 환경)을 따로 만들어 두고, 
- 필요한 물건(라이브러리, 패키지 등)을 그 방에만 들여놓는 것과 유사
- 방이 다르면 들여놓은 물건이 달라도 서로 간섭하지 않음

### 가상 환경 생성 및 활성화 

**가상 환경 생성 및 활성화 과정**

1. 가상 환경 생성
2. 가상 환경 활성화
3. 가상 환경 종료

**1. 가상 환경 생성**

```bash
python -m venv venv 
```

- 현재 디렉토리 안에 venv 라는 폴더가 생성됨 
- venv 폴더 안에는 파이썬 실행 파일, 라이브러리 등을 담을 공간이 마련됨
- venv 라는 이름의 가상 환경을 생성한 것

> 임의의 이름으로 생성이 가능하나 관례적으로 venv 이름을 사용

**2. 가상 환경 활성화**

```bash
# window
source venv/Scripts/activate

# Mac / Linux
source venv/bin/activate
```
- 활성화 후 프롬포트 앞에 (venv)와 같이 표시된다면 성공한 것

> 사용하고 있는 컴퓨터의 OS에 따라 만들어진 venv 폴더의 구조가 다름(그래서 경로를 폴더 구조에 맞춰서 명령어 실행)

**3. 가상 환경 종료**

```bash
deactivate
```

- 활성화한 상태에서 `deactivate` 명령을 입력하면, 다시 Python Global 환경으로 돌아옴

### 의존성 패키지 

Dependencies: 하나의 소프트웨어가 동작하기 위해 필요로 하는 다른 소프트웨어나 라이브러리 
> 컴퓨터가 잘 작동하기 위해서는 CPU, GPU, RAM 등이 필요
> 이들은 컴퓨터의 입장에서는 의존성이라 볼 수 있음

**의존성 패키지**

프로젝트가 의존하는 '개별 라이브러리'들을 가리키는 말
> "프로젝트가 실행되기 위해 꼭 필요한 각각의 패키지"
> 컴퓨터의 의존성인 CPU, GPU, RAM 등을 각각 의존성 패키지라고 할 수 있음

**1. 패키지 목록 확인**

```bash
pip list 
```

- 현재 가상 환경에 설치된 라이브러리 목록을 확인
- 각 생성된 가상 환경은 별도의 패키지가 없음
  - 기본 환경 구성을 위한 pip, setuptools 정도만 존재

> pip: 외부 패키지들을 설치하도록 도와주는 파이썬의 패키지 관리 시스템

ex. 
|   Package  |  Version |
| ---------- | -------- |
|    pip     |   24.0   |
| setuptools |  65.5.0  |

**2. 의존성 기록**

```bash
pip freeze > requiremnents.txt
```

- pip freeze 명령어 
  - 가상 환경에 설치된 모든 패키지를 버전과 함께 **특정한 형식**으로 출력
- 아를 requiremnents.txt라는 파일로 저장하면 나중에 동일한 환경을 재현할 때 유용
- 현업 시에도 팀원들이 똑같은 버전의 라이브러리를 설치하도록 공유 가능

> 다른 파일명으로도 가능하나 관례적으로 requiremnents.txt를 사용

> ">"는 pip 명령어가 아닌 CLI(shell)의 Redirection operator로, 이전 명령어의 출력을 파일로 redirect, 즉 생성하고 작성
> 같은 명령어를 다시 사용할 경우 이전 파일의 내용을 덮어씀

**의존성 리스트 예시**

- requests 패키지 설치 후 현재 가상 환경의 패키지 목록 변화 
- 1개만 설치되는 것이 아님
  - requests가 필요로 하는 의존성들이 존재하기 때문 

ex. 
|       Package      |  Version |
| ------------------ | -------- |
|          pip       |   24.0   |
|       setuptools   |  65.5.0  |
|        certifi     |2025.06.15|
|         idna       |  65.5.0  |
|       requests     |  2.32.4  |
|       urllib3      |  2.5.0   |
| charset-normalizar |  3.4.2   |

**의존성 리스트 공유 시나리오**

1. 2명 (A와 B)의 개발자가 하나의 프로젝트를 함께 개발한다고 가정

2. 개발자 A가 먼저 가상 환경을 생성 후 프로젝트를 설정하고 관련된 패키지를 설치하고 
   개발하다가 헙업을 위해 GitHub에 프로젝트를 push B

3. 개발자 B는 해당 프로젝트를 clone 받고 실행해보려 하지만 실행되지 않음

4. 개발자 A가 이 프로젝트를 위해 어떤 패키지를 설치했고, 어떤 버전을 설치했는지 A의 가상 환경 상황을 알 수 없음

5. 가상 환경에 대한 정보 즉 **패키지 목록**이 공유되어야 함

**의존성 패키지 관리가 필요한 이유**

패키지마자 버전이 다름
- 버전이 다른 경우 함수명이나 동작이 달라질 수 있음

프로젝트가 커질수록 사용하는 패키지의 개수도 늘어나게 됨
- 어떤 버전을 쓰고 있는지 기록 및 공유가 필수적 

다른 PC나 팀원들이 같은 환경을 구성할 때 **의존성 리스트**가 반드시 필요

### 의존성 패키지 가반 설치

```bash
python -m venv venv 

# window
source venv/Scripts/activate

pip install -r requirements.txt
```

1. 가상 환경 준비 
  - 새로운 가상 환경을 생성 및 활성화 

2.  requirements.txt로 부터 패키지 설치 
  -  requirements.txt에 기록된 패키지 버전을 읽어와 같은 환경으로 설치

### 가상 환경 주의사항

**가상 환경 주의사항 및 권장사항**

1. 가상 환경 "들어가고 나오는" 것이 아니라 사용할 Python 환경을 "On/Off"로 전환하는 개념
- 가상 환경 활성화는 **현재 터미널 환경**에만 영향을 끼침
- 새 터미널 창을 열면 **다시 활성화**해야함 

2. 프로젝트마다 **별도의 가상 환경**을 사용 

3. 일반적으로 가상 환경 폴더 venv는 **관련된 프로젝트와 동일한 경로에 위치**시킴

4. 폴더 venv는 .gitignore파일에 작성되어 **원격 저장소에 공유하지 않음**
  - 저장소 크기를 줄여 효율적인 협업과 배포를 가능하게 하고 
  - OS 별 차이점으로 인한 문제를 방지하기 위함 
  - 대신 requirements.txt를 공유하여 각자의 가상 환경을 구성 

**가상 환경이 필요한 이유**

1. 프로젝트마다 다른 버전의 라이브러리 사용
  - 한 프로젝트에서는 Django 4.2를 다른 프로젝트에서는 Django 5.2를 사용해야 할 수도 있음 
  - 가상 환경을 사용하면 서로 다른 버전을 동시에 설치해도 충돌 없이 각각의 프로젝트를 유지할 수 있음

2. 의존성 충돌 방지
  - 프로젝트별로 라이브러리를 독립적으로 관리하게 해줌
  - 여러 프로젝트가 동시에 같은 라이브러리를 쓰더라도 버전 충돌 문제를 예방

3. 팀원 간 협업
  - 누구든지 동일한 방식으로 가상 환경을 만들어서, 똑같은 버전의 라이브러리를 설치하면 에러 가능성을 줄일 수 있음

---

## Django 프로젝트

### Django 프로젝트 생성 및 서버 실행

**Django 프로젝트 생성 및 서버 실행 과정**
1. Django 설치
2. 프로젝트 생성
3. 서버 실행 

**1. Django 설치**

```bash
pip install django
```

- 현재 환경에 Django 패키지를 설치 
> Django 버전을 명시하지 않을 경우 python 3.11 기준 최신 버전인 5.2.x 버전이 설치 됨

**2. 프로젝트 생성**

```bash
django-admin startproject firstpjt .
```

- "firstpjt" 라는 이름의 django 프로젝트를 생성 

**3. 서버 실행**

```bash
python manage.py runserver 
```

- "manage.py"와 동일한 위치에서 명령어 진행 

---

## Django Design Pattern 

### Design Pattern

소프트웨어 설계에서 반복적으로 발생하는 문제에 대한, 검증되고 재사용 가능한 일반적인 해결책

> "애플리케이션의 구조는 이럭헤 구성하자"라는 모범 답안 또는 관행 대표적인 디자인 패턴: MVC

**MVC 디자인 패턴**

하나의 애플리케이션을 구조화하는 대표적인 구조적 디자인 패턴

Model 
- 데이터 및 비즈니스 로직을 처리

View
- 사용자에게 보이는 화면을 담당

Controller
- 사용자의 입력을 받아 Model과 View를 제어

> 시각적 요소와 뒤에서 실행되는 로직을 서로 영향 없이, 독립적이고 쉽게 유지 보수할 수 있는 애플리케이션을 만들기 위함

**MTV 디자인 패턴**

Django에서 애플리케이션을 구조화하는 디자인 패턴

- View -> Template
- Controller -> View

> 기존 MVC 패턴과 동일하나 단순히 명칭을 다르게 정의한 것

### 프로젝트와 앱

**Django project**
- 애플리케이션의 집합
  - DB 설정, URL 연결, 전체 앱 설정 등을 처리 

**Django application**
- 독립적으로 작동하는 기능 단위 모듈
  - 각자 특정한 기능을 담당
  - 다른 앱들과 함께 하나의 프로젝트를 구성 

**만약 온라인 커뮤니티 카페를 만든다면?**

|     프로젝트     |             앱           |
| --------------- | ------------------------ |
|       카페      | 게시글, 댓글, 회원 관리 등 |
| (전체 설정 담당) |     (DB, 인증, 화면)     |

**다양한 서비스에 대입해보면**

카페 프로젝트
  - 게시글, 댓글, 회원 관리 앱

쇼핑몰 프로젝트 
  - 상품 조회, 배송 조회, 결제 앱

교육 관리 프로젝트 
  - 학생 관리, 문제 관리, 점수 관리 앱

**1. 앱 생성**

```bash
python manage.py startapp articles
```

- 'articles'라는 폴더와 내부에 여러 파일이 새로 생성됨
> 앱의 이름은 '복수형'으로 지정하는 것을 권장

**2. 앱 등록**

- 반드시 앱을 생성(1)한 후에 등록(2)해야 함 
> 등록 후 생성은 불가 

```python 

# settings.py

INSTALLED_APPS = [
    'articles',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

```

> 등록을 먼저 할 경우, 생성을 위한 명령어 실행 중 아직 존재하지 않은 aricles 앱을 찾으려다 실패하기 때문 

### 프로젝트 및 앱 구조 

**프로젝트 구조**

settings.py
- 프로젝트의 모든 설정을 관리 

urls.py
- 요청 들어오는 URL에 따라 이에 해당하는 적절한 views를 연결

__init__.py
- 해당 폴더를 패키지로 인식하도록 설정하는 파일 

asgi.py
- 비동기식 웹 서버와의 연결 관리 설정

wsgi.py
- 웹 서버와의 연결 관련 설정

manage.py
- Django 프로젝트와 다양한 방법으로 상호작용하는 커맨드라인 유틸리티 

**앱 구조**

admin.py 
- 관리자용 페이지 설정

models.py
- DB와 관련된 Model을 정의
- MTV 패턴의 M

views.py
- HTTP 요청을 처리하고 해당 요청에 대한 응답을 반환
  - url, model, template과 연동
- MTV 패턴의 V

apps.py
- 앱의 정보가 작성된 곳

tests.py
- 프로젝트 테스트 코드를 작성하는 곳

---

## 요청과 응답

**Django와 요청 & 응답**

* 사용자가 서버에 접속하는 과정

**요청 흐름**

1. 사용자가 URL을 입력 → 요청(Request) 발생
2. Django 프로젝트의 `urls.py`가 요청을 받음
3. `views.py`로 전달되어 로직 실행 (필요하면 `models.py`에서 데이터 읽고 `templates`로 화면 구성)
4. views가 만든 응답(Response)을 브라우저에 반환

> urls.py는 요청을 받고, views.py는 응답을 만듬

* 사용자가 `http://127.0.0.1:8000/articles/` 로 요청을 보낸 경우

**동작 흐름**

* 브라우저 → urls.py → views.py → templates → HTML 응답 → 브라우저

> URL 주소의 `articles/`가 어떤 view함수를 실행할지 urls.py가 결정

**1. URLs**
* `http://127.0.0.1:8000/articles/`로 요청이 왔을 때
> request 객체를 `views` 모듈의 `index` view 함수에 전달하며 호출

```python
# urls.py
from django.contrib import admin
from django.urls import path
# `from articles import views` → articles 패키지에서 views 모듈을 가져오는 것
from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # url 경로는 반드시 ‘/’(slash)로 끝나야 함
    path('articles/', views.index),
]
```

**2. View**

* view 함수가 정의되는 곳
* 특정 경로에 있는 template과 request 객체를 결합해 응답 객체를 반환

```python
# views.py
from django.shortcuts import render

def index(request):
    return render(request, 'articles/index.html')
```

> 모든 view 함수는 첫번째 인자로 request 객체를 필수적으로 받음
> 매개변수 이름은 꼭 `request`일 필요는 없지만 관례적으로 `request`로 작성함

**3. Template**

1. articles 앱 폴더 안에 `templates` 폴더 생성
2. `templates` 폴더 안에 `articles` 폴더 생성
3. `articles` 폴더 안에 템플릿 파일 생성

> templates 폴더명은 반드시 `templates`여야 하며 개발자가 직접 생성해야 함

```html
<!-- articles/templates/articles/index.html -->
<!DOCTYPE html>
<html>
  <head>
    <title>Document</title>
  </head>
  <body>
    <h1>Hello, Django!</h1>
  </body>
</html>
```
---

**Django에서 template을 인식하는 경로 규칙**

* Django는 `app폴더/templates/`까지를 기본 경로로 인식
→ `'articles/index.html'` 처럼 templates 이후의 경로만 작성
```python
# views.py
from django.shortcuts import render
return render(request, 'articles/index.html')
```

**요청 후 응답 페이지 확인**

* 브라우저로 요청 보내보기
* 주소창에 `http://127.0.0.1:8000/articles/` 입력

**결과**
→ "Hello, Django" 화면 출력

**요청과 응답 과정 정리**

1. 브라우저가 `http://127.0.0.1:8000/articles/`로 요청
2. urls.py가 `articles/` 경로에 맞는 view함수 호출
3. index views.py가 응답 객체 생성 및 반환
4. 브라우저는 index view 함수가 반환한 응답 객체를 해석해 페이지 렌더링

**데이터 흐름에 따른 코드 작성하기**

* 사용자의 요청에서부터 데이터의 흐름은 **URLs → View → Template**
* 코드의 작성도 마찬가지로 데이터의 흐름을 따라 작성할 것 

```python
# URLs
path('articles/', views.index),

# View
def index(request):
    return render(request, 'articles/index.html')

# Template
articles/templates/articles/index.html
```

---

## render 함수

* 주어진 템플릿을 주어진 컨텍스트 데이터와 결합하고 렌더링 된 텍스트와 함께 HttpResponse 응답 객체를 반환하는 함수

```python
render(request, template_name, context)
```
request

   * 응답을 생성하는 데 사용되는 요청 객체

template_name

   * 템플릿 이름의 경로

context

   * 템플릿에서 사용할 데이터 (생략 가능)
   * 딕셔너리 타입으로 작성

**MTV 디자인 패턴 정리** 

Model

  * 데이터와 관련된 로직을 관리
  * 응용프로그램의 데이터 구조를 정의하고 데이터베이스의 기록을 관리

Template

  * 레이아웃과 화면을 처리
  * 화면상의 사용자 인터페이스 구조와 레이아웃을 정의

> HTTP Request가 들어오면 urls.py → views.py → models.py (데이터) → templates (화면) → HTML 응답 흐름

View

  * Model & Template과 관련한 로직을 처리해서 응답을 반환
  * 클라이언트의 요청에 대해 처리를 분기하는 역할

View 예시

  * 데이터가 필요하면 Model에 접근해 데이터를 가져오고,
  * 가져온 데이터를 Template으로 보내 화면을 구성하고,
  * 구성된 화면을 응답으로 만들어 클라이언트에게 반환

> 그림 설명 :
> View가 중심이 되어 models에서 데이터 가져오고, templates로 화면 만들어 응답함

* Django가 담당하는 부분 : **URLs, Views, Templates**
* Model은 데이터베이스 관리 도구가 담당
> Django는 URLs → Views → Templates까지 담당하고
> Model은 별도로 DB 연결/조작 담당

---

## Trailing Comma

* “후행 쉼표”
* 리스트, 딕셔너리, 튜플 등의 자료구조에서 마지막 요소 뒤에 쉼표를 추가하는 것
* 문법적으로 아무런 영향 없음
* 일반적으로 선택사항

  * 단일 요소 튜플을 만들 때는 예외

**Trailing Comma 사용 이유**

* 새로운 요소를 추가하거나 순서를 변경할 때 편리
* 값의 목록, 인자, 또는 import 항목들이 시간이 지남에 따라 확장될 것으로 예상되는 경우에 주로 사용
* 여러 줄에 걸쳐 작성된 데이터 구조에서 유용하며, 코드의 가독성과 유지보수성을 향상시키는 데 도움

* 일반적인 패턴

  * 각 값(등)을 별도의 줄에 배치하고,
  * 항상 후행 쉼표를 추가한 뒤,
  * 닫는 괄호 / 대괄호 / 중괄호를 다음 줄에 배치하는 것

* 단는 구분 기호와 같은 줄에 후행 쉼표를 두는 것은 권장하지 않음

**예시**

```python
# Correct
FILES = [
    'setup.cfg',
    'tox.ini',
]
initialize(
    FILES,
    error=True,
)

# Wrong
FILES = ['setup.cfg', 'tox.ini',]
initialize(FILES, error=True,)
```

---

## 프레임워크의 규칙 및 설계 철학

**지금까지 등장한 Django의 규칙**

1. urls.py에서 각 url 문자열 경로는 반드시 ‘/’로 끝남
2. views.py에서 모든 view 함수는 **첫번째 인자로 요청 객체**를 받음

   * 매개변수 이름은 반드시 `request`로 지정하기
3. Django는 **특정 경로**에 있는 template 파일만 읽어올 수 있음

   * 특정 경로: `app 폴더/templates`

**프레임워크의 규칙**

* 프레임워크를 사용할 때는 일정한 규칙을 따라야 하며
  이는 저마다의 설계 철학이나 목표를 반영하고 있음

  * 일관성 유지, 보안 강화, 유지보수성 향상, 최적화 등

* 프레임워크는 개발자에게 도움을 주는 **도구와 환경을 제공하기 위해 규칙을 정해 놓은 것**
  * 우리는 이를 잘 활용하여 특정 기능을 구현하는 방법을 표준화하고
  * 개발 프로세스를 단순화할 수 있도록 해야 함



