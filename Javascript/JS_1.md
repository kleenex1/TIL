# 브라우저에서 할 수 있는 일
* DOM 조작
  * 문서(HTML) 조작
* BOM 조작
  * navigator, screen, location, frames, history, XHR
* JavaScript Core (ECMAScript)
  * Data Structure(Object, Array), Conditional Expression, Iteration
  * DOM / BOM 조작을 위해 ECMAScript가 필요하다.

# DCM이란?
* HTML, XML과 같은 문서를 다루기 위한 문서 프로그래밍 인터페이스
* 문서를 구조화하고 구조화된 구성 요소를 하나의 객체로 취급하여 다루는 논리적 트리 모델
* 문서가 구조화되어 있으며 각 요소는 객체로 취급
* 단순한 속성 접근, 메서드 활용뿐만 아니라 프로그래밍 언어적 특성을 활용한 조작 가능
* 주요 객체
  * window: DOM을 표현하는 창, 가장 최상위 객체(작성 시 생략 가능)
  * document: 페이지 컨텐츠의 Entry Point 역할을 하며 <body> 등과 같은 수많은 다른 요소들을 포함
  * navigator, location, history, screen
  ![s](./screenshot/800px-DOM-model.svg.png)

# DOM - 해석
* 파싱 (Parsing)
  * 구문 분석, 해석
  * 브라우저가 문자열을 해석하여 DOM Tree로 만드는 과정

# BOM이란?
* Browser Object Model
* 자바스크립트가 브라우저와 소통하기 위한 모델
* 브라우저의 창이나 프레임을 추상화해서 프로그래밍적으로 제어할 수 있도록 제공하는 수단
  * 버튼, URL입력창, 타이틀 바 등 브라우저 윈도우 및 웹 페이지 일부분을 제어 가능
* window 객체는 모든 브라우저로부터 지원받으며 브라우저의 창을 지칭

# JavaScript Core
* 프로그래밍 언어
* BOM&DOM 을 조작하기 위한 프로그래밍 언어

# let과 const의 차이점?
`immutable`의 여부

변수 선언에는 기본적으로 const를 사용하고, 재할당이 필요한 경우에 한정해 let 을 사용하는 것이 좋다.

→ 재할당이 필요한 경우에 한정해 let 을 사용한다. 이때, 변수의 스코프는 최대한 좁게 만든다.

→ 재할당이 필요 없는 상수와 객체에는 const 를 사용한다.
(객체를 재할당하는 경우는 생각보다 흔하지 않다. 
const 를 사용하면 의도치 않은 재할당을 방지해 주기 때문에 보다 안전하다.)

**let**은 변수에 재할당이 가능하다.
```javascript
    let name = 'python'
    console.log(name) // python

    let name = 'javascript'
    console.log(name) 
    // Uncaught SyntaxError: Identifier 'name' has already been declared

    name = 'react'
    console.log(name) //react
```

**const**는 변수 재선언, 변수 재할당 모두 불가능하다.
```javascript
const name = 'python'
    console.log(name) // python

    const name = 'javascript'
    console.log(name) 
    // Uncaught SyntaxError: Identifier 'name' has already been declared

    name = 'react'
    console.log(name) 
    //Uncaught TypeError: Assignment to constant variable.
```

# 선택자 활용
* 하나를 선택한다 : querySelector
* 모든 결과를 선택한다 : querySelectorAll

# JS
```javascript
/*a tag 조작*/
const a = document.createElement('a')
a.innerText = '실라버스'
const body = document.querySelector('body')
body.appendChild(a)
a.setAttribut('href','https://syllaverse.com')
console.log(a.getAttribute('href'))
```
