# ! 후 탭을 누르면 
* emmet 기능을 통해 코드 짜는 생산성을 증대할 수 있다.
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
</body>
</html>
```
* emmet 기능
[Cheat Sheet (emmet.io)](https://docs.emmet.io/cheat-sheet/)

# 크기 단위
* px(픽셀)
	* 모니터 해상도의 한 화소 '픽셀' 기준
	* 픽셀의 크기는 변하지 않기 때문에 고정적인 단위
* %
	* 백분율 단위
	* 가변적인 레이아웃에서 자주 사용

* em
	* (바로 위, 부모 요소에 대한) 상속의 영향을 받음
	* 배수 단위, 요소에 지정된 사이즈에 상대적인 사이즈를 가짐
* rem
	* (바로 위, 부모 요소에 대한) 상속의 영향을 받지 않음
	* 최상위 요소(html)의 사이즈를 기준으로 배수 단위를 가짐
```html
<style>
  .em {
   font-size: 2em;
  }
  .rem {
    font-size: 2rem;
  }
</style>
<h2 class="em">32픽셀</h2>
<ul class="em">
  <li class="em">64픽셀</li>
</ul>
<h2 class="rem">32픽셀</h2>
<ul class="rem">
  <li class="rem">32픽셀</li>
</ul>
```
* *html 기본 font-size는 16px 이다.*

* 크기 단위 viewport
	* 디바이스의 viewport 기준으로 상대적인 사이즈가 결정
	* 예) vw, vh, vmin, vmax
	* [CSS 값 과 단위 - Web 개발 학습하기 | MDN (mozilla.org)](https://developer.mozilla.org/ko/docs/Learn/CSS/Building_blocks/values_and_units)
# 색상 단위
* 색상 키워드
* RGB 색상
	* '#' +HEX값
	* RGB()
* HSL 색상
	* 색상, 채도, 명도
* a는 투명도(alpha)
```html
p { color: black;}
p { color: #000; }
p { color: #00000; }
p { color: rgt(0, 0, 0,); }
p { color: hsl(120, 100%, 0); }

p { color: rgba(0, 0, 0, 0.5); }
p { color: hsla(120, 100% 0.5);}
```

# CSS문서 표현
* 텍스트
	* 서체(font-family),서체 스타일() font-style, font-weight)
	* 자간(letter-spacing), 단어 간격(word-spacing), 행간(line-height)
* 컬러(color), 배경(background-image, background-color)
* 기타 HTML 태그별 스타일링 
	* li, table 등

# CSS 적용 우선순위
1. 중요도(Importance)
	* !important
2. 우선 순위(Specificity)
	* 인라인 > id > class, 속성, pseudo-class >요소, pseudo-element
3. CSS 파일 로딩 순서

# CSS 상속
* CSS는 상속을 통해 부모 요소의 속성을 자식에게 상속한다.
	* 속성 중에는 상속이 되는 것과 되지 않는 것들이 있다
	* 되는것
		* TEXT 관련 요소(font,color,text-align), opacity, visibilty
	* 안되는 것
		* Box model 관련 요소(width,height,margin,padding,border,box-sizing,dsplay)
		* Position 관련 요소(position, top,right,bottom,left,z-index)

# Box model
* 모든 요소는 네모(박스모델)이고 
* 위에서부터 아래로, 왼쪽에서 오른쪽으로 쌓인다.(좌측상단배치)
	* CSS 원칙 1 : inline Direction(한줄배치) & Block Direction (Normal Flow)
	* CSS 원칙 2: display에 따라 크기와 배치가 달라진다.

* Margin : 테두리 바깥의 외부 여백 (배경색 지정 못함)
* Border : 테두리 영역
* Padding : 테두리 안쪽의 내부 여백, 요소에 적용된 배경색, 이미지는 padding까지 적용
* Content : 글이나 이미지 등 요소의 실제 내용

__*Tip : MDN 문서를 참조하면 더 많은 내용이 있다.*__
```HTML
.margin3 {
  margin: 10px 20px 30px; 상 좌우 하
}
.margin4 {
  margin: 10px 20px 30px 40px; 상 하 좌 우
}
.border {
  border-width: 2px;
  border-style: dashed;
  border-color: black;
}
```
# Box-sizing
* 기본적으로 모든 요소의 box-sizing은 context-box
	* Padding을 제외한 순수 contents 영역만을 box로 지정
* 다만 우리가 일반적으로 영역을 볼 때는 border까지의 너비를 100px 보는 것을 원함? --> 그 경우 box-sizing을 border-box로 설정

# 대표적으로 활용되는 Display
* display : block
	* 줄 바꿈이 일어나는 요소
	* 화면 크기 전체의 가로 폭을 차지한다
	* 블록 레벨 요소 안에 인라인 레벨 요소가 들어갈 수 있음
* display : inline
	* 줄 바꿈이 일어나지 않는 행의 일부 요소
	* content 너비만큼 가로 폭을 차지한다
	* width, height, margin-top, margin-bottom을 지정할 수 없다
	* 상하 여백은 line-height로 지정한다
* display : inline-block
	* block과 inline레벨 요소의 특징을 모두 가짐
	* inline처럼 한 줄에 표시할 수 있고, block처럼 width, height, margin 속성을 모두 지정할 수 있음
* display : none
	* 해당 요소를 화면에 표시하지 않고, 공간조차 부여되지 않음
	* 이와 비슷한 visibility : hidden은 해당 요소가 공간은 차지하나 화면에 표시만 하지 않는다.
* 참고
	* [display - CSS: Cascading Style Sheets | MDN (mozilla.org)](https://developer.mozilla.org/ko/docs/Web/CSS/display)

# 블록 레벨 요소와 인라인 레벨 요소
* 블록 레벨 요소와 인라인 레벨 요소 구분(HTML 4.1까지)
* 대표적인 블록 레벨 요소 : div / ul,ol.li/p/hr/form 등
* 대표적인 인라인 레벨 요소 : span / a / img /input, label/b , em, i, strong 등

( *실습에서 다시 다룰 예정*)
```html
<style>
  .card {
    border: 1px solid black;
    width: 30rem;
    height: 40rem;
    text-align: center;
  }
  .card-image {
    width: 90%;
    border-radius: 1rem;
  }
  .profile-image {
    width: 2rem;
    height: 2rem;
  }
  .profile {
    text-align : left;  
}
  .profile-name {
    line-height: 2rem;
  }
</style>
<body>
  <div class="card">
    <img class="card-image" src=".." alt="설명">
    <h3>문구 삽입</h3>
      <div class="profile">
        <img src=".." alt="설명">
        <span>문구 삽입</span>
    </div>
  </div>
</body>
```
 
