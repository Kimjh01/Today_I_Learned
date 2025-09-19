# CSS Box Model 

## CSS Box Model 

### display 속성

박스 타입
- 박스 타입에 따라 페이지에서의 배치 흐름 및 다른 박스와 관련하여 박스가 동작하는 방식이 달라짐

박스 종류
- Block 타입
- Inline 타입

**Block 타입**

- 블록 타입은 하나의 독립된 덩어리처럼 동작하는 요소

> 웹 페이지의 큰 구조와 단락을 만듬

```html

<style>

    .index{
        display: block;
    }

</style>

```

- 항상 새로운 행으로 나뉨(한 줄 전체를 차지, 너비 100%)
- width, height, marginm padding 속성을 모두 사용할 수 있음 
- padding, margin, border로 인해 다른 요소를 상자로부터 밀어냄
- width 속성을 지정하지 않으면 박스는 inline 방향으로 사용 가능한 공간을 모두 차지
    - 상위 컨테이너 너비 100%로 채우는 것
- 대표적인 block 타입 태그 ex. h1 ~ 6, p, div, ul, li

**div**

- 다른 HTML 요소들을 그룹화하여 레이아웃을 구성하거나 스타일링을 적용할 수 있음
- 헤더, 푸터, 사이드바 등 웹 페이지의 다양한 섹션을 구조화하는 데 가장 많이 쓰이는 요소


```html

<div class = "container">
    <h1>제목</h1>
    <p>단락 내용입니다.</p>
</div>
<div>
    <p>콘텐츠</p>
</div>

```

**inline**

- 문장 안의 단어처럼 흐름에 따라 자연스럽게 배치되는 요소

> 줄을 바꾸지 않고, 텍스트의 일부에만 다른 스타일을 적용할 때 사용됨

```html

<style>

    .index{
        display: inline;
    }

</style>

```

- 줄바꿈이 일어나지 않음 (콘텐츠의 크기만큼만 영역을 차지)
- widrh와 height 속성을 사용할 수 없음
- 수직 방향(상하)
    - padding, margin, border가 적용되지만, 다른 요소를 밀어낼 수는 없음
- 수평 방향(좌우)
    - padding, margin, border가 적용되어 다른 요소를 밀어낼 수 있음
- 대표적인 inline 타입 태그 ex. a, img, span, strong

**span**

- 자체적으로 시각적 변화 없음
    - 스타일을 적용하기 전까지는 특별한 변화는 없음
- 텍스트 일부 조작
    - 문장 내 특정 단어나 구문에만 스타일을 적용할 때 유용
- 블록 요소처럼 줄바꿈을 일으키지 않으므로, 문서의 구조에 큰 변화를 주지 않음

```html

<p>이 문장에서 <span style="color: blue;">파란색</span> 단어만 색상이 다릅니다.</p>
<p>이 단어는 <span class="highlight-text">강조되었습니다.</span></p>
<p>이것은<span id="changeText">클릭</span>하면 변경됩니다.</p>

```

## Normal flow

일반적인 흐름 또는 레이아웃을 변경하지 않은 경우 웁 페이지 요소가 배치되는 방식

>ex. 엔터를 눌러 문단을 나누는 것이 block 요소의 배치, 엔터를 누르지 않고 계속 타이핑하는 것이 inline 요소의 배치 방식\

## 기타 display 속성

- inline-block
- none
- flex

**inline-block**

inline과 block의 특징을 모두 가진 특별한 display 속성 값

> 한 줄로 표시하지만 각자 공간을 가지고 있음

```html

<style>

    .index{
        display: inline-block;
    }

</style>

```

**inline-block 타입**
- block과 inline의 특징을 합친 것 (줄바꿈 없이, 크기 지정 가능)
- width 및 height 속성 사용 가능
- padding, margin 및 border로 인해 다른 요소가 상자에서 밀려남

> 주로 가로로 정렬된 내비게이션 메뉴나 여러 개의 버튼, 이미지 갤러리처럼 수평으로 나열하면서, 각 항목의 크기를 직접 제어하고 싶을 때 유용하게 사용

```html
<!--이제 다른 요소를 밀어낼 수 있는 span-->
<p>Lorem ipsum dolor sit amet<span>consectetur</span> adipisicing elit. </p>
<!--list 요소를 가로로 정렬-->
<ul>
    <li><a herf="#">link</a></li>
    <li><a herf="#">link</a></li>
    <li><a herf="#">link</a></li>
</ul>
<!--div 요소를 가로로 정렬-->
<div class="container">
    <div class="box"></div>
    <div class="box"></div>
    <div class="box"></div>
</div>
<style>

    span{
        margin: 20px;
        padding: 20px;
        width: 80px;
        height: 50px;
        background-color: lightblue;
        border: 2px solid blue;
        display: inline-block;

    }
    ul>li{
        background-color: #4CAF50;
        padding: 10px 20px;
        display: inline-block;
    }
    .container{
        text-align: center;
    }
    .box{
        display: inline-block;
        width: 100px;
        height: 100px;
        background-color: #4CAF50;
        margin: 10px

    }

</style>

```

**none**

요소를 화면에 표시하지 않고, 공간조차 부여되지 않음

> 레이아웃에서 아예 빠져 있는 상태가 none 타입

```html

<style>

    .index{
        display: none;
    }

</style>

```

**none 타입**

- 요소를 화면에 표시하지 않고, 공간조차 부여되지 않음

```html
    <div class="box"></div>
    <div class="box none"></div>
    <div class="box"></div>
    <style>
        .box{
            width: 100px;
            height: 100px;
            background-color: red;
            border: 2px solid black;
        }

        .none{
            display: none;
        }
    </style>
```

## CSS Position

**CSS Layout**

- 각 요소의 위치와 크기를 조정하여 웹 페이지의 디자인을 결정하는 것
- 요소들을 상하좌우로 정력하고, 간격을 맞추고, 전체적인 페이지의 뼈대를 구성
- 핵심 속성: display(block, inline, flex, grid,...)

**CSS Position**

- 요소를 Normal Flow에서 제거하여 다른 위치로 배치하는 것
- 다른 요소 위에 올리기, 화면의 특정 위치에 고정시키기 등
- 핵심 속성: position(static, relative, absolute, fixed, sticky,...)

**Position 이동 방향**

- 네 가지 방향 속성(상, 하, 좌, 우)을 이용해 요소의 위치를 조절할 수 있음
- 겹치는 요소의 쌓이는 순서를 조절할 수 있음

**Position 유형**

- static
- relative
- absolute
- fixed
- sticky

**Position: static** 

- 요소를 Normal Flow에 따라 배치
- top, right, bottom, left 속성이 적용되지 않음
- 기본 값

```html
    <style>
        .static{
            position: static;
            background-color: lightcoral;
        }
    </style>
```

```html
<div class="container">
    <div class="box static">static</div>
    <div class="box absolute">absolute</div>
    <div class="box relative">relative</div>
    <div class="box fixed">fixed</div>
</div>
<style>

    *{
        box-sizing: border-box;
    }
    body{
        height: 1500px;
    }
    .container{
        position: relative;
        width: 300px;
        height: 300px;
        border: 1px solid black;
    }
    .box{
        width: 100px;
        height: 100px;
        border: 1px solid black;

    }

</style>
```

**Position: relative** 

- 요소를 Normal Flow에 따라 배치
- 자신의 원래 위치(static)을 기준으로 이동
- top, right, bottom, left 속성으로 위치를 조정
- 다른 요소의 레이아웃에 영향을 주지 않음
    (요소가 차지하는 공간은 static일 때와 같음)

```html
    <style>
        .relative{
            position: relative;
            background-color: lightblue;
            top: 100px;
            left: 100px;
        }
    </style>
```

**Position: absolute** 

- 요소를 Normal Flow에서 제거
- 가장 가까운 relative 부모 요소를 기준으로 이동
    - 만족하는 부모 요소가 없다면 body 태그를 기준으로 함
- top, right, bottom, left 속성으로 위치를 조정
- 문서에서 요소가 차지하는 공간이 없어짐

```html
    <style>
        .absolute{
            position: absolute;
            background-color: lightgreen;
            top: 100px;
            left: 100px;
        }
    </style>
```

**Position: fixed** 

- 요소를 Normal Flow에서 제거
- 현재 화면영역(viewport)을 기준으로 이동
- 스크롤해도 항상 같은 위치에 유지됨
- top, right, bottom, left 속성으로 위치를 조정
- 문서에서 요소가 차지하는 공간이 없어짐 

```html
    <style>
        .fixed{
            position: fixed;
            background-color: gray;
            top: 0;
            right: 0;
        }
    </style>
```

**Position: sticky** 

- relative와 fixed의 특성을 결합한 속성
- 스크롤 위치가 임계점에 도달하기 전에는 relative처럼 동작
- 스크롤 위치가 임계점에 도달하면 fixed 처럼 화면에 고정
- 다음 sticky 요소가 나오면 이전 sticky 요소의 자리를 대체
    - 이전 sticky 요소와 다름 sticky 요소의 위치가 겹치게 되기 때문

```html
    <style>
        .sticky{
            position: sticky;
            background-color: lightblue;
            top: 0;
            padding: 20px;
            border: 2px solid black;
        }
    </style>
```

## z-index 

요소의 쌓임 순서를 정의하는 속성

> 요소들의 앞뒤 순서를 정해 입체감을 만듬

```html
    <style>
        .index{
            z-index: 1;
        }
    </style>
```

- 정수 값을 사용해 z축 순서를 지정
- 값이 클수록 요소가 위에 쌓이게 됨
- static이 아닌 요소에만 저굥됨
- 기본값은 auto로 부모 요소의 z-index 값에 영향을 받음
- 부모의 z-index가 낮으면 자식의 z-index가 아무리 높아도위로 올라갈 수 없음

> position 속성이 static(기본값)이 아닌 요소에만 z-index가 적용
> 음수 z-index 값은 요소를 부모 요소의 뒤(배경)으로 보낼 때 사용 가능

```html
<div class="container">
    <div class="box red"></div>
    <div class="box green"></div>
    <div class="box blue"></div>
</div>
<style>

    .container{
        position: relative;
    }
    .box{
        position: absolute;
        width: 100px;
        height: 100px;
    }
    .red{
        background-color: red;
        width: 50px;
        height: 50px;
        z-index: 3;
    }
    .green{
        background-color: green;
        width: 100px;
        height: 100px;
        z-index: 2;
    }
    .blue{
        background-color: blue;
        width: 150px;
        height: 150px;
        z-index: 1;
    }

</style>
```

##  CSS Flexbox

**박스 표시(Display)타입**

1. Outer display 타입
- block 타입
- inline 타입

2. Inner display 타입
- 박스 내부의 요소들이 어떻게 배치될지를 결정
- CSS Flexbox(속성: flex)

> block 타입: 블록 타입은 하나의 독립된 덩어리처럼 동작하는 요소
> inline 타입: 문장 안의 단어처럼 흐름에 따라 자연스럽게 배치되는 요소

**CSS Flexbox**

요소를 행과 열 형태로 배치하는 1차원 레이아웃 방식

```html
    <style>
        .container{
            display: flex;
        }
    </style>
```

##  CSS Flexbox 구성 요소 

- main axis
- cross axis
- flex container
- flex item

**main axis(주축)**
- flex item들이 배치되는 기본축
- main start에서 시작하여 main end 방향으로 배치(기본 값)

**cross axis(교차 축)**
- main axis에 수직인 축
- cross start에서 시작하여 cross end 방향으로 배치(기본 값)

**flex container**
- display: flex; 혹은 display: inline-flex;가 설정된 부모 요소
- 이 컨테이너의 1차 자식 요소들이 Flex item이 됨
- flexbox 속성 값들을 사용하여 자식 요소 Flex item들을 배치하는 주체

**flex item**
- Flex Container 내부에 레이아웃 되는 항목
- 이후 배우는 내용을 이용해 자유로운 순서 변경 및 정렬 가능

## Flexbox 속성

**Flexbox 속성 목록**

Flex Container 관련 속성
- display
- flex-direction
- flex-wrap
- justify-content
- align-items
- align-content

Flex items 관련 속성
- align-self
- flex-grow
- flex-basis
- order

**Flex Container 지정**

- display 속성은 flex로 설정하면, Flex Container로 지정됨
- flex item은 기본적으로 행(주 축의 기본값인 가로 방향)으로 나열
- flex item은 주 축의 시작 선에서 시작
- flex item은 교차 축의 크기를 채우기 위해 늘어남

```html
<style>
    .container{
        height: 500px;
        border: 2px solid black;
        display: flex;
    }
</style>
```

**Flex-direction**

- flex item이 나열되는 방향을 지정
- 속성 
    - row(기본값): 아이템을 가로 방향으로, 왼쪽에서 오른쪽으로 배치
    - column: 아이템을 세로 방향으로, 위에서 알로 배치
    - "-reverse"로 지정하면 flex item 배치의 시작 선과 끝 선이 서로 바뀜 

```html
<style>
    .container{
        flex-direction: row;
        flex-direction: column;
        flex-direction: row-reverse;
        flex-direction: column-reverse;
    }
</style>
```

**Flex-wrap**

- flex item 목록이 flex container의 한 행에 들어가지 않을 경우, 다른 행에 배치할지 여부 설정
- 속성
    - nowrap(기본 값): 줄 바꿈을 하지 않음
    - wrap: 여러 줄에 걸쳐 배치될 수 있게 설정

```html
<style>
    .container{
        flex-direction: nowrap;
        flex-direction: wrap;
    }
</style>
```

**justify-content**

- 주 축을 따라 flex item 들을 정렬하고 간격을 조정
- 속성
    - flex-start(기본값): 주 축의 시작점으로 정렬
    - center: 주 축의 중앙으로 정렬
    - flex-end: 주축의 끝점으로 정렬

```html
<style>
    .container{
        justify-content: flex-start;
        justify-content: center;
        justify-content: flex-end;
    }
</style>
```

**align-content**

- 컨테이너에 여러 줄의 flex item이 있을 때, 그 줄들 사이의 공간을 어떻게 분배할지 지정
    - flex-wrap이 wrap 또는 wrap-reverse로 설정된 여러 행에만 적용됨
    - Flex 아이템이 두 줄 이상일 때만 의미가 있음 (flex-wrap이 nowrap으로 설정된 경우)

- 속성
    - stretch(기본값): 여러 줄을 교차 축에 맞게 늘려 빈 공간을 채움
    - center: 여러 줄을 교차 축의 중앙에 맞춰 정렬
    - flex-start: 여러 줄을 교차 축의 시작점(보통 위쪽)에 맞춰 정렬
    - flex-end: 여러 줄을 교차 축의 끝점(보통 아래쪽)에 맞춰 정렬  

```html
<style>
    .container{
        flex-direction: wrap;
        align-content: flex-start;
        align-content: center;
        align-content: flex-end;
    }
</style>
```

**align-items**
- 컨테이너 안에 있는 flex item 들의 교차 축 정렬 방법을 지정
- 속성
    - stretch(기본값): 아이템을 교차 축 높이를 꽉 채우도록 늘어남
    - center: 아이템을 교차 축의 중앙에 맞춰 정렬
    - flex-start: 아이템을 교차 축의 시작점(가로 방향일 경우 위쪽)에 맞춰 정렬
    - flex-end: 아이템을 교차 축의 끝점(가로 방향일 경우 아래쪽)에 맞춰 정렬

```html
<style>
    .container{
        align-items: flex-start;
        align-items: center;
        align-items: flex-end;
        align-items: stretch;
    }
</style>
```

**align-self**

- 컨테ㅣ너 안에 있는 flex item들을 교차 축을 따라 개별적으로 정렬
- 속성
    - auto(기본값): 부모 컨테이너의 align-items 속성 값을 상속
    - stretch: 해당 아이템만 교차 축 방향으로 늘어나 컨테이너를 꽉 채우도록 정렬
    - center: 해당 아이템만 교차 축의 중앙에 정렬
    - flex-start: 해당 아이템만 교차 축의 시작점(가로 방향일 경우 위쪽)에 맞춰 정렬
    - flex-end: 해당 아이템만 교차 축의 끝점(가로 방향일 경우 아래쪽)에 맞춰 정렬

```html
<style>
    .item1{
        align-self: center;
    }
    .item2{
        align-self: flex-end;
    }
</style>
```

**목적에 따른 속성 분류**
- 배치 (flex-direction, flex-wrap)
- 공간 분배(justify-content, align-content)
- 정렬(align-items, align-self)

**속성 쉽게 이해하는 방법**
- justify: 주축
- align: 교차 축

> justify-items 및 justify-self 속성이 없는 이유는 무엇인가?
> 애초에 필요가 없기 때문, 간단하게 margin auto를 통해 정렬 및 배치가 가능

**flex-grow**
- 남는 행 여백을 비율에 따라 flex item에 분배
- flex item이 컨테이너 내에서 확장하는 비율을 지정

> flx-shrink
> flex-grow와 반대되는 개념, 컨테이너의 공간이 부족할 때, flex item이 줄어드는 비율을 지정하는 속성

```html
<div class="container">
    <div class="item item-1">1</div>
    <div class="item item-2">2</div>
    <div class="item item-3">3</div>
</div>
<style>

    .container{
        display: flex;
        width: 100%;
    }
    .item{
        font-size: 3rem;
        color: white;
        height: 100px;
    }
    .item-1{
        background-color: red;
        flex-grow: 1;
    }
    .item-2{
        background-color: green;
        flex-grow: 2;
    }
    .item-3{
        background-color: blue;
        flex-grow: 3;
    }

</style>
```

**flex-basis**
- flex item의 초기 크기 값을 지정
- flex basis와 width 값을 동시에 적용한 경우 flex-basis가 우선

```html
<div class="container">
    <div class="item item-1">1</div>
    <div class="item item-2">2</div>
    <div class="item item-3">3</div>
</div>
<style>

    .container{
        display: flex;
        width: 100%;
    }
    .item{
        font-size: 3rem;
        color: white;
        height: 100px;
    }
    .item-1{
        background-color: red;
        flex-basis: 300px;
    }
    .item-2{
        background-color: green;
        flex-basis: 600px;
    }
    .item-3{
        background-color: blue;
        flex-basis: 300px;
    }

</style>
```

## flex-wrap 응용

**반응형 레이아웃 작성**

- 다양한 디바이스와 화면 크기에 자동으로 적응하여 콘텐츠를 최적으로 표시하는 웹 레이아웃 방식
- flex-wrap을 사용해 반응형 레이아웃 작성 (flex-grow & flex-basis 활용)
- .card 요소를 flex 컨테이너로 설정
- 컨테이너의 공간이 부족할 경우, 여러 줄로 나뉘어 배치되도록 허용
- 각 flex item의 기본 너비를 설정
- 컨테이너에 여유 공간이 있을 때 공간을 차지하며 늘어날 수 있도록 함(두 flex item 모두 값이 1이므로 절반씩 나눠가짐)

```html
<div class="card">
    <img class="thumbnail" src="#" alt="#">
    <div class="content">
      <h2>Heading</h2>
      <p>...</p>
  </div>
</div>
<style>

    .card{
        border: 1px solid black;
        flex-wrap: wrap;
        display: flex;
        width: 80%;
    }
    .img{
        width: 100%;
    }
    .thumbnail{
        flex-basis: 700px;
        flex-grow: 1;
    }
    .content{
        flex-basis: 350px;
        flex-grow: 1;
    }

</style>
```

## 마진 상쇄

- 두 block 타입 요소의 martin top과 bottom이 만나 더 큰 margin으로 결합되는 현상

**Margin collapsing 예시**

- 두 요소 모두 margin 20px이지만 실제 두 요소의 상/하 공간은 40이 아닌 20으로 상쇄

Margin collapsing(마진 상쇄) 이유
> 복잡한 레이아웃에서 요소 간 간격을 일관 되게 유지할 수 있음(일관성)
> 요소 간의 간격을 더 예측 가능하고 관리하기 쉽게 만들 수 있음(단순성)

## 박스 타입 별 수평 정령

**Block 요소의 수평 정렬**
- margin: auto 사용
- 블록의 너비를 지정하고 좌우 마진을 auto로 설정

```html
<div class="box margin-auto">
  </div>

<style>

    .box{
        border: 1px solid black;
        background-color: crimson;
        height: 100px;
        width: 100px;
    }

    .margin-auto{
        margin: 0 auto;
    }

</style>
```

**Inline 요소의 수평 정렬**
- text-align 사용 
- 부모 요소에 적용

```html
<div class="text-center">
    <span> inline 요소</span>
  </div>

<style>

    .text-center{
        text-align: center;
    }

</style>
```

**Inline-block 요소의 수평 정렬**
- text-align 사용 
- 부모 요소에 적용

```html
<div class="text-center">
    <div class="box inline-block"></div>
  </div>

<style>

    .text-center{
        text-align: center;
    }

    .inline-block{
        display: inline-block;
    }

</style>
```

## 실제 Position 활용 예시

1) absolute
    - 특정 요소 위에 다른 요소를 겹쳐서 배치할 때 유용하게 사용 됨
2) fixed
    - 페이지를 스크롤해도 항상 같은 자리에 표시되는 요소를 만들 때 사용
3) sticky
    - 일반적인 문서 흐름에 따라 배치되다가, 스크롤이 특정 위치에 도달하면 고정되는 속성

## Flexbox Shorthand 속성

Shorthand: "Flex-flow"
- flex-direction과 flex-wrap 속성을 한 번에 지정할 수 있는 단축 속성 

```html
<style>

    /*기본 속성 사용 시*/
    .container{
        flex-flow: flex-direction flex-wrap;
    }

    /*단축 속성 사용 시*/
    .container{
        flex-direction: row;
        flex-wrap: wrap;
    }

</style>
```

Shorthand: "flex"
- flex-grow, flex-shrink, flex-basis 속성을 한 번에 지정할 수 있는 단축 속성(기본값으로는 1, 1, 0%)

- 기본 속성 
```html
<style>

    .set{

        /*1. One values unitless number: flex-grow*/
        flex-grow: 2;
        flex-shrink: 1;
        flex-basis: 0%;

        /*2. One values length or percentage: flex-basis*/
        flex-grow: 1;
        flex-shrink: 1;
        flex-basis: 10rem;

        /*3. Two values flex-grow, flex-shrink*/
        flex-grow: 1;
        flex-shrink: 1;
        flex-basis: 30px;

        /*4. Two values flex-grow, flex-shrink*/
        flex-grow: 2;
        flex-shrink: 2;
        flex-basis: 0%;

        /*5. Tree values flex-grow, flex-shrink, flex-basis */
        flex-grow: 2;
        flex-shrink: 2;
        flex-basis: 10%;

    }

</style>
```

- 단축 속성
```html
<style>
    .set{

        /*1. One values unitless number: flex-grow*/
        flex: 2;

        /*2. One values length or percentage: flex-basis*/
        flex: 10rem;
        flex: 30px;

        /*3. Two values flex-grow, flex-shrink*/
        flex: 1 30px;

        /*4. Two values flex-grow, flex-shrink*/
        flex: 2 2;

        /*5. Tree values flex-grow, flex-shrink, flex-basis */
        flex: 2 2 10%;

    }

</style>
```