# 웹사이트의 구성 요소
* HTML : 구조
* CSS :  표현
* Javascript : 동작

# 웹 표준
* 웹에서 표준적으로 사용되는 기술이나 규칙
* 어떤 브라우저든 웹 페이지가 동일하게 보이도록 함(크로스 브라우징)

HTML Living Standard :  
Apple, Google, Microsoft, Mozilla(firefox)  의 기업들이 앞장서서 웹 표준을 만들어나가고 있다.

* 브라우저별 점수 및 호환성 정보를 알 수 있는 사이트
[Can I use... Support tables for HTML5, CSS3, etc](https://caniuse.com/)

# 개발 환경 설정
→ vscode의 open in browser, auto close, auto rename tage, html css support, intellisense for css class names in html, html css support 익스텐션을 설치해준다.(실습시 별도 안내)

# HTML 
* HTML : Hyper Text Markup Language 
* Hyper Text란?
	* 참조(하이퍼링크)를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트 
* Markup Language란?
	* 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어
	* Markup Example?
```HTML
<h1>html</h1>
<p>HTML이란 Hyper Text Markup Language의 약자이다</p>
```

# HTML 기본 구조
* html: 문서의 최상위(root) 요소
* head: 문서 메타데이터 요소
	* 문서 제목, 인코딩, 스타일, 외부 파일 로딩 등
	* 일반적으로 브라우저에 나타나지 않는 내용
	* head 예시
		* title : 브라우저 상단 타이틀
		* meta : 문서레벨 메타 데이터 요소
		* link : 외부 리소스 연결 요소(CSS파일, favicon 등)
		* script : 스크립트 요소 (JavaScript 파일/코드)
		* style : CSS 직접 작성
* body: 문서 본문 요소
	* 실제 화면 구성과 관련된 내용
```HTML
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Document</title>
</head>
<body>

</body>
</html>
```

# Open Graph Protocol
[The Open Graph protocol (ogp.me)](https://ogp.me/)
* 메타 데이터를 표현하는 새로운 규약
	* HTML 문서의 메타 데이터를 통해 문서의 정보를 전달
	* 메타 정보에 해당하는 제목, 설명 등을 쓸 수 있도록 정의


# 요소(element)
* HTML 요소는 시작 태그와 종료 태그 그리고 태그 사이에 위치한 내용으로 구성
	* 요소는 태그로 컨텐츠를 감싸는 것으로 그 정보의 성격과 의미를 정의
	* 내용이 없는 태그들도 존재(닫는 태그가 없음)
		* br(띄어쓰기), hr(수평선), img, input, link, meta

* 요소는 중첩(nested)될 수 있음
	* 요소의 중첩을 통해 하나의 문서를 구조화
	* 여는 태그와 닫는 태그의 쌍을 잘 확인해야함
		* 오류를 반환하는 것이 아닌 그냥 레이아웃이 깨진 상태로 출력됨.

# 속성(attribute)
* <a href(속성명) ="https://google.com"(속성값)></a>
* 속성을 통해 태그의 부가적인 정보 설정
* 요소는 속성을 가질 수 있고 경로나 크기와 같은 추가적인 정보 제공
* 요소의 시작 태그에작성하며 보통 이름과 값이 하나의 쌍으로 존재
* 태그와 상관없이 사용 가능한 속성(HTML Global Attribute)도 있음
	* 모든 HTML 요소가 공통으로 사용할 수 있는 대표적인 속성
		* *id* : 문서 전체에서 유일한 고유 식별자 지정
		* *class* : 공백으로 구분된 해당 요소의 클래스의 목록(CSS,JS에서 요소 선택하거나 접근)
		* *style* : inline 스타일
		* data-\*: 페이지에 개인 사용자 정의 데이터 저장하기 위해 사용
		* title :요소 추가 정보 지정
		* tabindex : 요소의 탭 순서

# 렌더링
* 웹사이트 코드를 사용자가 보게 되는 웹 사이트로 바꾸는 과정
[브라우저는 어떻게 동작하는가? (naver.com)](https://d2.naver.com/helloworld/59361)

# DOM(Documnet Object Model) 트리
* 텍스트 파일인 HTML 문서를 브라우저에서 렌더링 하기 위한 구조
	* HTML 문서에 대한 모델을 구성
	* HTML 문서 내의 각 요소에 접근/수정에 필요한 프로퍼티와 메서드 제공

# 인라인 / 블록 요소
* HTML 요소는 크게 인라인/ 블록 요소로 나눔
* 인라인 요소는 *글자* 취급
* 블록 요소는 *한 줄* 모두 사용

# 텍스트 요소
```html
<img src ="..." alt ="보노보노"> : alt 는 설명해주는 기능
<!--ol-->
<ol>
  <li>순서 있음</li>
</ol>
<!--ul-->
<ul>
  <li>순서 없음</li>
</ul>
<!--pre-->
<pre>
  기본 기본 기본
  우아아아아
</pre>
<!--p태그-->
<p>
  기본 기본 기본 <br>우아아아
</p>
```
# alt는 왜 쓸까?

Alternative Text
```html
<img src="images/dinosaur.jpg"
      alt ="The head and torso of a dinosaur skeleton; it has a large head with long sharp teeth">
```
* alt는 왜 굳이 사용되거나 필요한걸까?
1) 사용자가 시각장애를 가진 경우 screen reader가 그 내용을 읽어 줄 수 있다.
2) 텍스트만 지원되는 브라우저를 사용하는 사용자들이 있기 때문에 alt 정보가 유용할 수 있다.
3) 텍스트를 제공하여 검색엔진이 이를 활용할 수 있다. 
4) 제한된 지역에서 고의적으로 이미지를 꺼놓은 경우 alt 정보가 유용할 수 있다.


# CSS 
* CSS : Cascading(위에서 아래로 흐르는/상속,종속) Style Sheets
* 스타일을 지정하기 위한 언어
* 선택하고 스타일을 지정한다. 
* *주로 활용하는 속성 위주로 찾아서 쓰면서 기억하자*
* 
```css
  h1 {
  color: blue;
  font-size: 15px;
  }
```

**1. 인라인 (사용하지 않음, 비효율적)**
```HTML
<body>
  <h1 style ="color: blue; font-size: 100px;">Hello</h1>
</body>
```
**2. 내부참조**
```HTML
<head>
  <title>Document</title>
  <style>
    h1 {
      color: blue;
      font-size: 15px;
    }
  </style>
```
**3. 외부참조(파일을 따로 만듦)**
```CSS
mystyle.css
  h1 {
  color: blue;
  font-size: 15px;
  }
```
```HTML
<head>
  <title>Document</title>
  <link rel="stylesheet" href="mystle.css">
</head>
```
# CSS 기초 선택자
* 요소 선택자
	* HTML 태그를 직접 선택
* 클래스(class)선택자
	* 마침표(.) 문자로 시작하며, 해당 클래스가 적용된 항목을 선택
* 아이디(id)선택자
	* (#) 문자로 시작하며, 해당 아이디가 적용된 항목을 선택
	* 일반적으로 하나의 문서에 1번만 사용
	* 여러번 사용해도 동작하지만 단일 id 사용 권장
* *우선순위 : id > class > 태그*
  * 다만 일반적으로 CSS스타일은 클래스로만 한다.
	* id는 잘 활용하지 않고, JS로 개발할 때 보통 활용
```HTML
<style>
  h1 {
    color : red;
    font-size: 25px
  }
  .title-brown {
    color : brown;
  }
  #title-yellow {
    color: yellow
  }
</style>
<body>
  <!--전부 red로 나옴-->
  <h1>태그선택자1</h1>
  <h1>태그선택자2</h1>
  <!--brown으로 나옴-->
  <h3 class="title-brown">클래스선택자1</h3>
  <!--yellow로 나옴-->
  <h3 id="title-yellow">아이디선택자<h3>
</body>
```
# HTML 코드 확인 할때 유용한 웹사이트
* https://jsfiddle.net
* 실행 한 뒤 Update를 하면 해당 주소가 계속 남아 있음(링크로 활용가능) 

# HTML COLOR CODES
* htmlcolorcodes.com
* 글자색 조정할때 rgb값 & HEX값(16진법) 두가지 방식으로 쓸 수 있음
```html
h1 {
  color: rgb(97, 249, 107)
  color: #61F96B
}
```

# 텍스트 스타일링
```html
p {
  text-decoration: line-through; (overline, underline)
  text-weight: 100,200,300..900;(글꼴에 따라 지원되는 글자 두께가 다름 normal : 400과 똑같고 bold : 700과 같음 *100단위)
}
a {
  text-decoration: none; (링크 밑줄없애는 기능)
}
```
# 웹 폰트 사용하기
* fonts.google.com 
* fonts.google.com/earlyaccess
* 링크를 복사하고 font-family를 사용하면됨.
```html
<link href="https://fonts.google..~" rel="stylesheet">
#text-style {
  font-family: "Times New Roman", Arial, sans-serif; (첫번째 글꼴을 쓰도록 하고 없으면 Arial, 없으면 sans-serif)
}
```
# 폰트 파일 사용하기
```html
@font-face {
  src: url("../fonts/file이름.otf");
  font-family: "이름지어주기";
}
p {
  font-family: "이름지어주기";
}
```

# span 태그
* \<div> 는 새로운 줄에 넣어버림
* \<span> 는 영향이 없음