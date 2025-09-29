# Django 6 _ Django_Form

## Djago Form 

HTML 'form': 지금까지 사용자로부터 데이터를 제출 받기위해 활용한 방법, 그러나 비정상적 혹은 악의적인 요청을 필터링 할 수 없음 

> 유효한 데이터인지에 대한 확인이 필요

**유효성 검사**

- 수집한 데이터가 정확하고 유효한지 확인하는 과정 

> Django Form의 유효성 검사는 사용자가 입력한 데이터가 올바른 형식인지 자동으로 점검하는 기능을 제공

**유효성 검사 구현의 어려움**

- 유효성 검사를 구현하기 위해서는 입력 값, 형식, 중복, 범위, 보안 등 많은 것들을 고려해야 함
- 이런 과정과 기능을 직접 개발하는 것이 아닌 Django가 제공하는 Form을 사용

### Form class 

**Form class 정의**

* `articles/forms.py`

```python
from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=10)
    content = forms.CharField()
```

**view에서 Form 인스턴스 생성**

* `articles/views.py`

```python
from django.shortcuts import render
from .forms import ArticleForm

def new(request):
    form = ArticleForm()
    context = {"form": form}
    return render(request, "articles/new.html", context)
```

**url 연결**

* `articles/urls.py`

```python
from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path("new/", views.new, name="new"),
    path("create/", views.create, name="create"),
]
```

**템플릿에서 출력**

* `templates/articles/new.html`

```html
<h1>NEW</h1>
<form action="{% url 'articles:create' %}" method="POST">
  {% csrf_token %}
  {{ form }}
  <input type="submit" value="제출">
</form>
<hr>
<a href="{% url 'articles:index' %}">[back]</a>
```

**최종 결과 화면 미리보기**

```html
<form action="/articles/create/" method="POST">
  <input type="hidden" name="csrfmiddlewaretoken" value="랜덤토큰">
  <div>
    <label for="id_title">Title:</label>
    <input type="text" name="title" maxlength="10" required id="id_title">
  </div>
  <div>
    <label for="id_content">Content:</label>
    <input type="text" name="content" required id="id_content">
  </div>
  <input type="submit" value="제출">
</form>
```

### Widgets

**Widget 정의**

* 특정 필드의 입력 방식을 커스터마이징하는 도구
* input, textarea, checkbox 등으로 변경 가능

**Widget 적용 코드**

* `articles/forms.py`

```python
from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=10)
    content = forms.CharField(widget=forms.Textarea)
```

**렌더링 결과**

* `content` 필드가 `<input>` → `<textarea>` 로 변경됨

```html
<form action="/articles/create/" method="POST">
  <input type="hidden" name="csrfmiddlewaretoken" value="랜덤토큰">
  <div>
    <label for="id_title">Title:</label>
    <input type="text" name="title" maxlength="10" required id="id_title">
  </div>
  <div>
    <label for="id_content">Content:</label>
    <textarea name="content" cols="40" rows="10" required id="id_content"></textarea>
  </div>
  <input type="submit" value="제출">
</form>
```

---

## Djago ModelForm  

**Form vs ModelForm**

- Form
  사용자 입력 데이터를 DB에 저장하지 않을 때
  (예: 검색, 로그인)

- ModelForm
  사용자 입력 데이터를 DB에 저장해야 할 때
  (예: 게시글 작성, 회원가입)

**ModelForm 기능**

- Model과 연결된 Form을 자동으로 생성
- Form 클래스와 Model 클래스를 결합해, 모델 필드를 기반으로 입력 폼 자동 생성
- 데이터 수집과 저장 과정을 동시에 처리

**기존 Form class → ModelForm으로 변경**

- `articles/forms.py`

```python
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
```

**렌더링 결과 (new.html)**

```html
<div>
  <label for="id_title">Title:</label>
  <input type="text" name="title" maxlength="10" required id="id_title">
</div>
<div>
  <label for="id_content">Content:</label>
  <textarea name="content" cols="40" rows="10" required id="id_content"></textarea>
</div>
```

**ModelForm class가 대체하는 것**

- Form class에서 직접 작성했던 `title`, `content` 필드 정의 불필요
- Model과 연결된 필드 정보를 자동으로 가져와 HTML `<input>` / `<textarea>` 생성

```python
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
```

### Mata class

Meta class

- ModelForm의 정보를 작성하는 공간
- 어떤 모델과 연결할지, 어떤 필드를 사용할지 지정
- Form 동작 방식을 제어하는 핵심 역할

**fields와 exclude 속성**

```python
# 특정 필드만 포함
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title',)

# 특정 필드 제외
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ('title',)
```

**주의사항**

- Django에서 ModelForm에 추가 정보/속성을 작성하기 위한 구조일 뿐
- Python의 inner class 개념과 동일하게 보지 말 것

### ModelForm 적용

**ModelForm을 적용한 create 로직**

```python
# `articles/views.py`
from django.shortcuts import render, redirect
from .forms import ArticleForm

def create(request):
    form = ArticleForm(request.POST)
    if form.is_valid():
        article = form.save()
        return redirect('articles:detail', article.pk)
    context = {"form": form}
    return render(request, 'articles/new.html', context)
```

**유효성 검사 결과**

- 제목 입력칸이 비어있을 경우
- `This field is required.` 에러 메시지 자동 출력

**is_valid()**

- 여러 유효성 검사를 실행하고 Boolean 값 반환
- 실패 시 form 객체에 에러 메시지가 포함됨

**공백 데이터가 유효하지 않은 이유와 에러메시지가 출력되는 과정**

모델 필드에는 기본적으로 빈 값 허용하지 않는 제약조건이 설정되어 있음
빈 값은 `is_valid()`에서 False로 평가됨
form 객체에는 해당 에러 메시지가 포함되어 다음 코드 진행

```python
# articles/models.py
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

```python
# articles/views.py
def create(request):
    form = ArticleForm(request.POST)
    if form.is_valid():
        article = form.save()
        return redirect('articles:detail', article.pk)
    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)
```

**ModelForm을 적용 edit 로직**

```python
# articles/views.py
def edit(request, pk):
    article = Article.objects.get(pk=pk)
    form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/edit.html', context)
```

```html
<!-- articles/edit.html -->
<h1>EDIT</h1>
<form action="{% url 'articles:update' article.pk %}" method="POST">
  {% csrf_token %}
  {{ form }}
  <input type="submit">
</form>
```

**ModelForm을 적용한 update 로직**

```python
# articles/views.py
def update(request, pk):
    article = Article.objects.get(pk=pk)
    form = ArticleForm(request.POST, instance=article)
    if form.is_valid():
        form.save()
        return redirect('articles:detail', article.pk)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/edit.html', context)
```

### save 메서드 

**save() 개념**

데이터베이스 객체를 만들고 저장하는 ModelForm의 인스턴스 메서드
유효한 경우 save()를 호출해 모델 인스턴스를 생성 후 DB에 저장
`instance` 인자를 통해 새 객체 생성 / 기존 객체 수정 구분 가능
코드 없이 쉽게 DB 연동 가능

**save() 메서드가 생성과 수정을 구분하는 법**

키워드 인자 `instance` 여부로 판단

```python
# CREATE
form = ArticleForm(request.POST)
form.save()

# UPDATE
form = ArticleForm(request.POST, instance=article)
form.save()
```

**Django Form 정리**

사용자로부터 데이터를 수집하고 처리하기 위한 강력하고 유연한 도구
HTML form 생성, 데이터 유효성 검사 및 처리를 쉽게 할 수 있도록 도움

---

## HTTP 요청 다루기 

### View 함수 구조 변화 

**new & create view 함수간 공통점과 차이점**

공통점: 데이터 생성을 구현하기 위함
차이점: new → GET 요청 처리, create → POST 요청 처리

**view 함수 구조화의 목적**

HTTP request method 차이점을 활용해 동일 목적을 가진 view 함수를 하나로 구조화

**new & create 함수 결합**

```python
def new(request):
    form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)
```

```python
def create(request):
    form = ArticleForm(request.POST)
    if form.is_valid():
        article = form.save()
        return redirect('articles:detail', article.pk)
    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)
```

```python
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)
```

### new & create 함수 결합

**새로운 create view 함수**

```python
# articles/views.py
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)
```

- 두 함수의 유일한 차이점이었던 request method 에 따른 분기

```python
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)
```

- POST일 때는 과거 create 함수 구조였던 객체 생성 및 저장 로직 처리

```python
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)
```

- POST가 아닐 때는 과거 new 함수에서 진행했던 form 인스턴스 생성

```python
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)
```

- context에 담기는 form은

  1. is_valid()를 통과하지 못해 에러메시지를 담은 form
  2. else 문을 통한 form 인스턴스

```python
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)
```

**기존 new 관련 코드 수정**

- 사용하지 않게 된 new url 제거

```python
# articles/urls.py
app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/update/', views.update, name='update'),
]
```

- new 관련 키워드를 create로 변경

```html
<!-- articles/index.html -->
<a href="{% url 'articles:create' %}">CREATE</a>

<!-- articles/create.html -->
<h1>CREATE</h1>
<form action="{% url 'articles:create' %}" method="POST">
  {% csrf_token %}
  {{ form }}
  <input type="submit">
</form>
```

- new 관련 키워드를 create로 변경

```python
# articles/views.py
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)
```

**request method에 따른 요청의 변화**

```
(GET)  articles/create/   → 게시글 생성 페이지를 줘!
(POST) articles/create/   → 게시글을 생성해줘!
```

### edit & update 함수 결합 

**새로운 update view 함수**

- 기존 edit과 update view 함수 결합

```python
# articles/views.py
def update(request, pk):
    article = Article.objects.get(pk=pk)

    # update
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
      # edit
        form = ArticleForm(instance=article) 
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)
```

**기존 edit 관련 코드 수정**

- 사용하지 않는 edit url 제거

```python
# articles/urls.py
app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/update/', views.update, name='update'),
]
```

- edit → update 변경

```html
<!-- articles/detail.html -->
<h2>DETAIL</h2>
<h3>{{ article.pk }} 번째 글</h3>
<hr>
<p>제목 : {{ article.title }}</p>
<p>내용 : {{ article.content }}</p>
<p>작성 시각 : {{ article.created_at }}</p>
<p>수정 시각 : {{ article.updated_at }}</p>
<hr>
<a href="{% url 'articles:update' article.pk %}">UPDATE</a><br>
<form action="{% url 'articles:delete' article.pk %}" method="POST">
  {% csrf_token %}
  <input type="submit" value="DELETE">
</form>
```

```html
<!-- articles/update.html -->
<h1>UPDATE</h1>
<form action="{% url 'articles:update' article.pk %}" method="POST">
  {% csrf_token %}
  {{ form }}
  <input type="submit">
</form>
```

---

## ModelForm의 키워드 인자 구성

**ModelForm 키워드 인자 data와 instance**

```python
# ModelForm의 상위 클래스인 BaseModelForm의 생성자 함수 모습
class BaseModelForm(BaseForm):
    def __init__(self, data=None, files=None, auto_id='id_%s', prefix=None,
                 initial=None, error_class=ErrorList, label_suffix=None,
                 empty_permitted=False, instance=None, use_required_attribute=None,
                 renderer=None):
        ...
```

```python
# articles/views.py
form = ArticleForm(request.POST, instance=article)
```

---

## Widgets 응용

**Widgets 응용**

```python
 articles/forms.py
class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title',
                'placeholder': 'Enter the title',
            }
        ),
    )

    class Meta:
        model = Article
        fields = '__all__'
```

```python
class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title',
                'placeholder': 'Enter the title',
                'maxlength': 10,
            }
        ),
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content',
                'placeholder': 'Enter the content',
                'rows': 5,
                'cols': 50,
            }
        ),
        error_messages={'required': '내용을 입력해주세요.'},
    )
```

---

## 필드를 수동으로 렌더링

**필드를 수동으로 렌더링 하기**

```html
{{ form.non_field_errors }}
<form action="..." method="POST">
  {% csrf_token %}
  <div>
    {{ form.title.errors }}
    <label for="{{ form.title.id_for_label }}">Title:</label>
    {{ form.title }}
  </div>
  <div>
    {{ form.content.errors }}
    <label for="{{ form.content.id_for_label }}">Content:</label>
    {{ form.content }}
  </div>
  <input type="submit">
</form>
```
