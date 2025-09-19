# Bootstrap Grid system

## Bootstrap Grid system

웹 페이지의 레이아웃을 조정하는 데 사용되는 12개의 컬럼으로 구성된 시스템

> 반응형 디자인을 지원해 웹 페이지를 모바일, 태블릿, 데스크탑 등 다양한 기기에서 적절하게 표시할 수 있도록 도와줌

**Responsive Web Design**

디바이스 종류나 화면 크기에 상관없이, 어디서든 일관된 레이아웃 및 사용자 경험을 제공하는 디자인 기술

## Grid system 구조

**Grid system 기본 요소**

Container
    - Column들을 담고 있는 공간 

Column
    - 실제 컨텐츠를 포함하는 부분

Gutter
    - 컬럼과 컬럼 사이의 여백 영역(상하좌우)

1개의 row안에 12개의 column 영역이 구성
    - 각 요소는 12개 중 몇개를 차지할 것인지 지정됨

## Grid system 실습 

- col-*를 사용해서 칸을 지정

```html

<div class="container">
  <div class="row">
    <div class="col-4 box">
      <div>col-4</div>
    </div>

    <div class="col-8 box">
      <div class="row">
        <div class="col-6">
          <div class="box">col-6</div>
        </div>
        <div class="col-6">
          <div class="box">col-6</div>
        </div>
        <div class="col-6">
          <div class="box">col-6</div>
        </div>
        <div class="col-6">
          <div class="box">col-6</div>
        </div>
      </div>
    </div>
    
  </div>
</div>

```

- offset-*을 이용하여 간격을 띄움

```html

<div class="container">
  <div class="row">
    <div class="col-4">
      <div class="box">col-4</div>
    </div>
    <div class="col-4 offset-4">
      <div class="box">col-4 offset-4</div>
    </div>
  </div>

  <div class="row">
    <div class="col-3">
      <div class="box">col-3</div>
    </div>
    <div class="col-3 offset-3">
      <div class="box">col-3 offset-3</div>
    </div>
  </div>

  <div class="row">
    <div class="col-6 offset-3">
      <div class="box">col-6 offset-3</div>
    </div>
  </div>
</div>

```

**Gutters**

Grid system에서 column 사이에 여백 영역
- x축은 padding, y축은 margin으로 여백 생성

> 실제 컬럼 간에 좌우 간격(x축)은 변하지 않으며 padding으로 인해 컬럼 안에 contents의 너비가 변함

Gutter를 이용해 간격을 조정
- gx-0
- col 사이 여백 제거 

```html

<div class="container">
  <div class="row gx-0">
    <div class="col-6">
      <div class="box">col</div>
    </div>
    <div class="col-6">
      <div class="box">col</div>
    </div>
  </div>
</div>

```

- row 사이 여백 증가

```html

<div class="container">
  <div class="row gy-5">
    <div class="col-6">
      <div class="box">col</div>
    </div>
    <div class="col-6">
      <div class="box">col</div>
    </div>
    <div class="col-6">
      <div class="box">col</div>
    </div>
    <div class="col-6">
      <div class="box">col</div>
    </div>
  </div>
</div>

```

## Grid system for responsive web

디바이스 종류나 화면 크기에 상관없이, 어디서든 일관된 레이아웃 및 사용자 경험을 제공하는 디자인 기술

- Bootstrap grid system에서는 12개의 column과 6개의 breakpoints를 사용하여 반응형 웹 디자인을 구현

## Grid system Breakpoints

웹 페이지를 다양한 화면 크기에 적절하게 배치하기 위한 분기점
- 화면 너비에 따라 6개의 분기점 제공(xs, sm, md, lg, xl, xxl)

|        | xs <576px | sm ≥576px | md ≥768px | lg ≥992px | xl ≥1200px | xxl ≥1400px |
|--------|-----------|-----------|-----------|-----------|------------|-------------|
| **Container max-width** | None (auto) | 540px | 720px | 960px | 1140px | 1320px |
| **Class prefix**        | `.col-` | `.col-sm-` | `.col-md-` | `.col-lg-` | `.col-xl-` | `.col-xxl-` |

- 각 breakpoints 마다 설정된 최대 너비 값 "이상으로" 화면이 커지면 grid system 동작이 변경됨

## Breakpoints 실습

- 화면 사이즈에 따라 column의 배치를 바꿈
```html

<div class="container">
  <div class="row">
    <div class="col-12 col-sm-6 col-md-2 col-lg-3 col-xl-4">
      <div class="box">col</div>
    </div>
    <div class="col-12 col-sm-6 col-md-8 col-lg-3 col-xl-4">
      <div class="box">col</div>
    </div>
    <div class="col-12 col-sm-6 col-md-2 col-lg-3 col-xl-4">
      <div class="box">col</div>
    </div>
    <div class="col-12 col-sm-6 col-md-12 col-lg-3 col-xl-12">
      <div class="box">col</div>
    </div>
  </div>
</div>

<style>

.box {
  border: 1px solid black;
  background-color: lightblue;
  text-align: center;
  padding: 10px;     /* 박스 안쪽 여백 */
  margin: 5px 0;     /* 위아래 간격 */
  font-weight: bold; /* 글자 강조 */
}

</style>

```

- 화면 사이즈가 변함에 따라 column의 배치를 바뀜
- Offset도 같이 사용 
```html

<div class="container">
  <div class="row g-4">
    <div class="col-12 col-sm-4 col-md-6">
      <div class="box">col</div>
    </div>
    <div class="col-12 col-sm-4 col-md-6">
      <div class="box">col</div>
    </div>
    <div class="col-12 col-sm-4 col-md-6">
      <div class="box">col</div>
    </div>
    <div class="col-12 col-sm-4 col-md-6 offset-sm-4 offset-md-0">
      <div class="box">col</div>
    </div>
  </div>
</div>

<style>

.box {
  border: 1px solid black;
  background-color: lightblue;
  text-align: center;
  padding: 10px;   /* 내부 여백 */
  margin: 5px 0;   /* 위아래 간격 */
}


</style>

```

실제 Bootstap에 작성된 Grid system 코드
- Media Query로 작성됨

```html
<style>
    /* Small devices (landscape phones, 576px and up) */
    @media (min-width: 576px) {
    /* 스타일 작성 */
    }

    /* Medium devices (tablets, 768px and up) */
    @media (min-width: 768px) {
    /* 스타일 작성 */
    }

    /* Large devices (desktops, 992px and up) */
    @media (min-width: 992px) {
    /* 스타일 작성 */
    }

    /* X-Large devices (large desktops, 1200px and up) */
    @media (min-width: 1200px) {
    /* 스타일 작성 */
    }

    /* XX-Large devices (larger desktops, 1400px and up) */
    @media (min-width: 1400px) {
    /* 스타일 작성 */
    }
</style>

```

> 결국 Grid system은 화면 크키에 따라 12개의 칸을 각 요소에 나누어 주는 것임

## CSS Layout 종합 정리

- CSS 레이아웃 기술들은 각각 고유한 특성과 장단점을 가지고 있음
- 이들은 상호 보완적이며, 특정 상황에 따라 적합한 도구가 달라짐
- 최적의 기술을 선택하고 효과적으로 활용하기 위해서는 다양한 실제 개발 경험이 필수적

## UX & UI

**UX**

user Experience
제품이나 서비스를 사용하는 사람들이 느끼는 전체적인 경험과 만족도를 개선하고 최적화하기 위한 디자인과 개발 분야

> 좋은 향수 향기, 러쉬 향기, 원하는 음악을 검색할 때, 검색 기능이 적절하게 작동하고 검색 결과가 정확하게 나오는 것

- 사람들의 마음과 생각을 이해하고 정리해서 제품에 녹여내는 과정
- 유저 리서치, 데이터 설계 및 정제, 유저 시나리오, 프로토타입 설계 

> 프로토타입(Prototype)은 제품 개발 전 실제 작동 방식을 미리 보고 검증하기 위한 초기 모델

**UI**

User Interface
서비스와 사용자 간의 상호작용을 가능하게 하는 디자인 요소들을 개발하고 구현하는 분야

> 리모콘: 사용자가 버튼을 누르면 TV가 켜지고, 채널을 변경하거나 볼륨을 조절
> ATM: 사용자가 터치스크린을 통해 사용자 정보를 입력하고, 원하는 금액을 선택할 수 있음
> 웹 사이트: 사용자가 로그인 버튼을 누르면, 이동하는 화면의 디자인 및 레이아웃

- 예쁜 디자인 보다는 사용자가 더 쉽고 편리하게 사용할 수 있도록 고려
- 이를 위해서는 디자인 시스템, 중간 산출물, 프로토타입 등이 필요

## The Grid system

- CSS가 아닌 편집 디자인에서 나온 개념으로 구성 요소를 잘 배치해서 시각적으로 좋은 결과물을 만들기 위함
- 기본적으로 안쪽에 있는 요소들의 오와 열을 맞추는 것에서 기인
- 정보 구조와 배열을 체계적으로 작성하여 정보의 질서를 부여하는 시스템

## Grid Cards

- row-cols 클래스를 사용하여 행당 표시할 열(카드) 수를 손쉽게 제어할 수 있음

```html

<div class="container">
  <div class="row row-cols-1 row-cols-sm-3 row-cols-md-2 g-4">
    
    <div class="col">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">Card title</h5>
          <p class="card-text">Some quick example text to build on the card title.</p>
        </div>
      </div>
    </div>

    <div class="col">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">Card 2</h5>
          <p class="card-text">Another supporting text inside the card body.</p>
        </div>
      </div>
    </div>

    <div class="col">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">Card 3</h5>
          <p class="card-text">And here is some extra text for the third card.</p>
        </div>
      </div>
    </div>

    <div class="col">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">Card 4</h5>
          <p class="card-text">More text for the fourth card body content.</p>
        </div>
      </div>
    </div>

  </div>
</div>

```

## UI Design Guidelines

https://developer.samsung.com/codelab

https://m3.material.io/

https://developer.apple.com/kr/design/resources/