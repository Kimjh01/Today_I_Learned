# Day 25

## Bootstrap

css  프론트엔드 프레임워크 (Toolkit)

> 미리 만들어진 다양한 디자인 요소들을 제공하여 웹 사이트를 빠르고 쉽게 개발할 수 있도록 함

https://getbootstrap.com 접속 후 Install

```html

<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap demo</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
  </head>
  <body>
    <h1>Hello, world!</h1>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js" integrity="sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI" crossorigin="anonymous"></script>
  </body>
</html>

```

**CDN**

서버와 사용자 사이의 물리적인 거리를 줄여 콘텐츠 로딩에 소요되는 시간을 최소화 
- 웹 페이지 로드 속도를 높임

지리적으로 사용자와 가까운 CDN 서버에 콘텐츠를 저장해서 사용자에게 전달

## Bootstrap 사용 가이드

Bootstrap에는 특정한 규칙이 있는 클래스 이름으로 스타일 및 레이아웃이 미리 작성되어 있음

- Spacing을 표현하는 방법
> property: margin 또는 padding
> sides: 방향(top, left, x, y 등)
> size: Spacing의 상대적 너비

**Bootstrap에서 클래스 이름으로 Spacing을 표현하는 방법**

- Property

|  이름  |    값    |
| ----- | -------- |
|   m   |  margin  |
|   p   |  padding |

- Sides

|  이름  |    값    |
| ----- | -------- |
|   t   |    top   |
|   b   |  bottom  |
|   s   |   left   |
|   e   |   right  |
|   y   | top, bottom |
|   x   | left, right |
| blank |  4 side  |

- Size

|  이름  | 값(상대) | 값(절대) |
| ----- | --------- | ------|
|   0   |   0 rem   |  0px  |
|   1   |  0.25 rem |  4px  |
|   2   |  0.5 rem  |  8px  |
|   3   |   1 rem   | 16px  |
|   4   |  1.5 rem  | 24px  |
|   5   |   3 rem   | 48px  |
|  auto |    auto   | auto  |


## Reset CSS

모든 HTML 요소 스타일을 일관된 기준으로 재설정하는 간결하고 압축된 규칙 시트

> HTML Element, Table, List 등의 요소들에 일관성 있게 스타일을 적용 시키는 기본 단계

**Reset CSS 사용 배경**

- 모든 브라우저는 각자의 'user agent stylesheet'를 가지고 있음
    - 웹사이트를 보다 읽기 편하게 하기 위해

- 문제는 이 설정이 브라우저마다 상이하다는 것
- 모든 브라우저에서 웹사이트를 동일하게 보이게 만들어야 하는 개발자에겐 매우 골치 아픈 일

> 모두 똑같은 스타일 상태로 만들고 스타일 개발을 시작

**User-agent stylesheets**

모든 문서에 기본 스타일을 제공하는 기본 스타일 시트

**Normalize CSS**

- Reset CSS 방법 중 대표적인 방법
- 웹 표준 기준으로 브라우저 중 하나가 불일치 한다면 차이가 있는 브라우저를 수정하는 방법
    - 경우에 따라 IE 또는 EDGE 브라우저는 표준에 따라 수정할 수 없는 경우도 있는데, 이 경우 IE 또는 EDGE의 스타일을 나머지 브라우저에 적용시킴

**Bootstrap에서의 Reset CSS**

- Bootstrap은 bootstrap-reboot.css 라는 파일명으로 normalize.css를 자체적으로 커스텀해서 사용하고 있음

## Bootstrap 활용

### Typography

제목, 본문 텍스트, 목록 등

```html
<div class="display-1">Display 1</div>
<p>You can use the mark tag to
    <mark>highlight</mark>text.
</p>
<ul clsaa="list-unstyled">
    <li>Unstyled list item 1</li>
    <li>Unstyled list item 2</li>
</ul>
```

**Display headings**

기존 Heading보다 더 눈에 띄는 제목이 필요할 경우
    - 더 크고 약간 다른 스타일

```html
<!-- Display Heading -->
<h1 class="display-1">Display 1</h1>
<h1 class="display-2">Display 2</h1>
<h1 class="display-3">Display 3</h1>
<h1 class="display-4">Display 4</h1>
<h1 class="display-5">Display 5</h1>
<h1 class="display-6">Display 6</h1>
```

**Inline text elements**

HTML inline 요소에 대한 스타일

```html

<!-- Inline text elements -->
<p>You can use the mark tag to <mark>highlight</mark> text.</p>
<p><del>This line of text is meant to be treated as deleted text.</del></p>
<p><s>This line of text is meant to be treated as no longer accurate.</s></p>
<p><ins>This line of text is meant to be treated as an addition to the document.</ins></p>
<p><u>This line of text will render as underlined.</u></p>
<p><small>This line of text is meant to be treated as fine print.</small></p>
<p><strong>This line rendered as bold text.</strong></p>
<p><em>This line rendered as italicized text.</em></p>

```
**List**

HTML list 요소에 대한 스타일

```html

<!-- Lists -->
<ul class="list-unstyled">
  <li>This is a list.</li>
  <li>It appears completely unstyled.</li>
  <li>Structurally, it's still a list.</li>
  <li>However, this style only applies to immediate child elements.</li>
  <li>Nested lists:
    <ul>
      <li>are unaffected by this style</li>
      <li>will still show a bullet</li>
      <li>and have appropriate left margin</li>
    </ul>
  </li>
  <li>This may still come in handy in some situations.</li>
</ul>

```

### Colors

**Bootstrap Color System**

- Bootstrap이 지정하고 제공하는 색상 시스템
- 일관성 있는 의미론적 관점의 색상을 적용할 수 있게 해줌
    - 'blue' 대신 'primary', 'red' 대신 'danger' 등

**Colors**

- Text, Border, Background 및 다양한 요소에 사용하는 Bootstrap의 색상 키워드

**Text colors**

```html

<!-- text colors -->
<p class="text-primary">.text-primary</p>
<p class="text-primary-emphasis">.text-primary-emphasis</p>
<p class="text-secondary">.text-secondary</p>
<p class="text-secondary-emphasis">.text-secondary-emphasis</p>
<p class="text-success">.text-success</p>
<p class="text-success-emphasis">.text-success-emphasis</p>
<p class="text-danger">.text-danger</p>

```

**Baxkground colors**

```html

<!-- background colors -->
<div class="p-3 mb-2 bg-primary text-white">
  .bg-primary
</div>
<div class="p-3 mb-2 bg-primary-subtle text-emphasis-primary">
  .bg-primary-subtle
</div>
<div class="p-3 mb-2 bg-secondary text-white">
  .bg-secondary
</div>
<div class="p-3 mb-2 bg-secondary-subtle text-emphasis-secondary">
  .bg-secondary-subtle
</div>
<div class="p-3 mb-2 bg-success text-white">
  .bg-success
</div>
<div class="p-3 mb-2 bg-success-subtle text-emphasis-success">
  .bg-success-subtle
</div>
<div class="p-3 mb-2 bg-danger text-white">
  .bg-danger
</div>


```

### Component

Bootstrap Component
- Bootstrap에서 제공하는 UI 관련 요소 

> UI 관련 요소란 버튼, 네비게이션 바, 카드, 폼, 드랍다운 등을 의미

**Component 이점**

일관된 디자인을 제공하여 웹 사이트의 구성 요소를 구축하는데 유용하게 활용

**대표 컴포넌트 사용해보기**

- Alerts
- Badges
- Cards
- Navbar

> Component의 동작은 JavaScript를 활용해서 만들어짐
> 만약 동작이 잘 되지 않을 경우, 다음을 확인
> Bootstrap의 `script` 요소가 잘 추가되어 있는지 확인
> "data-*"로 시작하는 속성들이 잘 정의되어 있는지 확인

## Semantic Web

웹 데이터를 의미론적으로 구조화된 형태로 표현하는 방식

> 요소의 시작적 측면이 아닌 요소의 목적과 역할에 집중하는 방식

## Semantic in HTML

**HTML 요소가 의미를 가진다는 것**

외형 보다는 요소 자체의 의미에 집중하는 것

```html

<!--단순히 제목처럼 보이게 큰 글자로 만드는 것-->
<p style="font-size: 30px;">Heaging</p>

<!--"페이지 내 최상위 제목"이라는 의미를 제공하는 요소 h1 -> 브라우저에 의해 스타일이 지정-->
<h1>Heaging</h1>

```
**HTML Semantic Element**

기본적인 모양과 기능 이외이 의미를 가지는 HTML 요소

> 검색엔진 및 개발자가 웹 페이지의 콘텐츠를 이해하기 쉽게 해줌

**HTML Semantic Element 예시**

header
- 소개 및 탐색에 도움을 주는 콘텐츠

nav
- 현재 페이지 내, 또는 다른 페이지로의 링크를 보여주는 구획

main
- 문서의 주요 콘텐츠

article
- 독립적으로 구분해 배포하거나 될수 있는 구성의 콘텐츠 구획

section
- 문서의 독립적인 구획, 더 적합한 요소가 없을 때 사용

> Semantic 요소가 브라우저에 보여질 때는 div 요소와 똑같이 나오게 됨

aside
- 문서의 주요 내용과 간접적으로만 연관된 부분 

footer
- 가장 가까운 조상 구획(main, article등)의 작성자, 저작권 정보, 관련 문서

```html

<header>
  <h1>Header</h1>
</header>
<nav>
  <ul>
    <li><a href="#">Home</a></li>
  </ul>
</nav>
<main>
  <article>
    <h2>Article Title</h2>
    <p>Article content</p>
  </article>
  <aside>
    <h3>Aside</h3>
    <ol>
      <li><a href="#">Link</a></li>
    </ol>
  </aside>
</main>
<footer>
  <p>&copy; All rights reserved.</p>
</footer>

```

## Semantic in CSS

CSS를 효율적이고 유지 보수가 용이하게 작성하기 위한 일련의 가이드라인

**OOCSS**

Object Oriented CSS
- 객체 지향적 접근법을 적용하여 css를 구성하는 방법론

- 순서
> 구조와 스킨을 분리
> 컨테이너와 콘텐츠를 분리

**구조와 스킨 분리**
하나의 선택자에 구조와 색상(스킨)에 대한 선언이 혼재됨
> 다른 색의 버튼을 추가할 때 구조 코드 반복

```html
<style>
    /* bad */
    .blue-button {
    border: none;
    font-size: 1em;
    padding: 10px 20px;
    background-color: blue;
    color: white;
    }

    .red-button {
    border: none;
    font-size: 1em;
    padding: 10px 20px;
    background-color: red;
    color: white;
    }
</style>
```

구조(.button)와 색상(.button-blue)을 나타내는 선택자가 분리됨
> 다른 색의 버튼을 추가할 때 다른 선언만 추가 

```html
<style>
/* good */
    .button {
    border: none;
    font-size: 1em;
    padding: 10px 20px;
    }

    .button-blue {
    background-color: blue;
    color: white;
    }

    .button-red {
    background-color: red;
    color: white;
    }
</>
```

**컨테이너와 콘텐츠 분리**

객체에 직접 적용하는 대신 객체를 둘어싸는 컨테이너에 스타일 적용
스타일을 정의할 때 위치에 의존적인 스타일을 사용하지 않도록 함
콘텐츠를 다른 컨테이너로 이동시키거나 재배치할 때 스타일이 깨지는 것을 방지

> Bootstrap의 미디어 객체(Utilities > Flex > Media object)는 컨테이너와 콘텐츠 분리 원칙을 잘 보여주는 예시 

**OOCSS 적용 예시**

변경 전
- .header와 .footer 클래스가 폰트 크기와 색 둘 다 영향을 주고 있음

```html

<style>
    /* bad */
    .header h2 {
    font-size: 24px;
    color: white;
    }

    .footer h2 {
    font-size: 24px;
    color: black;
    }
</style>

```

변경 후 
- .container .tittle은 폰트 크기 담당(콘텐츠 스타일)
- .header와 .footer는 폰트 색 담당(컨테이너 스타일)

```html

<style>
    /* good */
    .container .title {
    font-size: 24px;
    }

    .header {
    color: white;
    }

    .footer {
    color: black;
    }
</style>

```

```html
<div class="card">
  <h2 class="card-title">Card Title</h2>
  <p class="card-description">This is a card description.</p>
  <button class="btn btn-blue">Learn More</button>
  <button class="btn btn-red">Learn More</button>
</div>

<style>
    /* 기본 Card 구조 */
    .card {
    border: 1px solid #ccc;
    border-radius: 4px;
    padding: 16px;
    width: 50%;
    }

    /* Card 제목 */
    .card-title {
    font-size: 20px;
    font-weight: bold;
    margin-bottom: 8px;
    }

    /* Card 설명 */
    .card-description {
    font-size: 16px;
    margin-bottom: 16px;
    }

    /* 기본 버튼 구조 */
    .btn {
    display: inline-block;
    border-radius: 4px;
    padding: 8px 16px;
    font-size: 1rem;
    font-weight: 400;
    color: #212529;
    text-align: center;
    text-decoration: none;
    cursor: pointer;
    }

    /* 파란 배경 버튼 */
    .btn-blue {
    background-color: #007bff;
    color: #fff;
    }

    /* 빨간 배경 버튼 */
    .btn-red {
    background-color: #cb2323;
    color: #fff;
}

</style>

```

## Bootstrap을 사용하는 이유

- 가장 많이 사용되는 CSS 프레임워크
- 사전에 디자인된 다양한 컴포넌트 및 기능
    - 빠른 개발과 유지보수
- 손쉬운 반응형 웹 디자인 구현
- 커스터마이징(customizing)이 용이
- 크로스 브라우징(Cross browsing) 지원
    - 모든 주요 브라우저에서 작동하도록 설계되어 있음

## CDN 없이 사용하기

**Bootstrap 코드 파일을 다운받아 활용**

Bootstrap 코드 파일 다운로드
- https://getbootstrap.com/docs/5.3/getting-started/download/

bootstrap.css 와 bootstrap.bundle.js 만 선택
CSS 파일은 HTML head 태그에 가져와서 사용
JS 파일은 HTML body 태그에 가져와서 사용

> 파일 별 포함된 기능이 다르므로 공식문서를 통해 확인
- https://getbootstrap.com/docs/5.3/getting-started/contents/

- 파일 배치 및 불러오기 코드 예시

```html

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="css/bootstrap.css">
  <title>Document</title>
</head>
<body>
  <script src="js/bootstrap.bundle.js"></script>
</body>
</html>


```

## 의미론적 마크업

**의미론적인 마크업이 필요한 이유**

검색엔진 최적화(SEO)
- 검색 엔진이 해당 웹 사이트를 분석하기 쉽게 만들어 검색 순위에 영향을 줌

웹 접근성 (Web Accessibility)
- 웹 사이트, 도구, 기술이 고령자나 장애를 가진 사용할 수 있도록 설계 및 개발하는 것
ex. 스크린 리더를 통해 전맹 시각장애 사용자에게 웹의 글씨를 읽어줌

**책임과 역할**
HTML: 콘텐츠의 구조와 의미
CSS: 레이아웃과 디자인