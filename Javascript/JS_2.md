# 호이스팅
* 변수를 선언 이전에 참조할수 있는 현상
* 변수 선언 이전의 위치에서 접근 시 undefined를 반환
* 자바스크립트는 모든 선언을 호이스팅한다.
* var, let, const 모두 호이스팅이 발생하지만, var는 선언과 초기화가 동시에 발생하여 일시적 사각지대가 존재하지 않는다.

# 데이터 타입
* 자바스크립트의 모든 값은 특정한 데이터 타입을 가짐
* 원시타입(Primitive type)과 참조타입(Reference type)으로 분류됨
* 원시타입 : Number, String, Boolean, Undefined, Null, Symbol
* 참조타입 : Objects - Array, Function, ...

# 조건문 종류와 특징
* if statement
  ```javascript
  const nation = 'Korea'
  if (nation === 'Korea') {
    console.log('안녕하세요')
  } else if (nation ==='Frnace') {
    console.log('Bonjour')
  } else {
    console.log('Hello')
  }
  ```
* switch statement
  * 조건 표현식의 결과값이 어느 값(case)에 해당하는지 판별
  * 주로 특정 변수의 값에 따라 조건을 분기할 때 활용
    * 조건이 많아질 경우 if문보다 가독성이 나을 수 있음
  * 표현식의 결과값을 이용한 조건문
  * 표현식의 결과값과 case문의 오른쪽 값을 비교
  * break 및 default문은 선택적으로 사용 가능
  * break문을 만나거나 default 문을 실행할 때까지 다음 조건문 실행
  ```javascript
  /* 이 경우에는 모두 출력*/
  const nation = 'Korea'
  switch(nation) {
    case 'Korea' : {
      console.log('안녕하세요')
    }
    case 'France': {
      console.log('Bonjour')
    }
    default: {
      console.log('Hello')
    }
  }
  ```
* if, else if, else
  * 조건은 소괄호
  * 실행할 코드는 중괄호
  * 블록 스코프 생성

# 반복문의 종류와 특징
* while
```javascript
let i = 0
while (i<6>) {
  console.log(i)
  i += 1
}
```
* for
  * initialization : 최초 반복문 진입 시 1회만 실행되는 부분
  * condition : 매 반복 시행 전 평가되는 부분
  * expression : 매 반복 시행 이후 평가되는 부분
  * 블록 스코프 생성
```javascript
for (initialization; condition; expression) {

}

for (let i = 0; i < 6; i++) {
  console.log(i)
}
```
* for...in
  * 객체(object)의 속성(key)들을 순회할 때 사용
  * 배열도 순회 가능하지만 권장하지 않음
  * 실행할 코드는 중괄호 안에 작성
  * 블록스코프 생성
```javascript
const capitals = {
  korea: 'seoul',
  france: 'paris',
  usa: 'washington D.c'
}

for (let capital in cappitals) {
  console.log(capital)
}
```

* for...of
  * 반복 가능한(iterable) 객체를 순회하며 값을 꺼낼 때 사용
  * 실행할 코드는 중괄호 안에 작성
  * 블록 스코프 생성
```javascript
const fruits = ['딸기', '바나나', '메론']

for (let fruit of fruits) {
  fruit = fruit + '!'
  console.log(fruit)
}
```
# 함수
* 참조 타입 중 하나로써 function 타입에 속함
* Javascript에서 함수를 정의하는 방법은 주로 2가지로 구분
  * 함수 선언식(function declaration)
  * 함수 표현식(function expression)
* JavaScript의 함수는 일급객체(First-class citizen)에 해당
  * 일급 객체: 다음의 조건들을 만족하는 객체를 의미
    * 변수에 할당 가능
    * 함수의 매개변수로 전달 가능
    * 함수의 반환 값으로 사용 가능

# 함수의 정의
* 함수의 이름과 함께 정의하는 방식
* 3가지 부분으로 구성
  * 함수의 이름 (name)
  * 매개변수 (args)
  * 함수 body (중괄호 내부)
  ```javascript
  function add(num1, num2) {
    return num1 + num2
  }
  ```
# 함수 표현식(function expression)
* 함수를 표현식 내에서 정의하는 방식 
  * 표현식: 어떤 하나의 값으로 결정되는 코드의 단위
* 함수 이름을 생략하고 익명 함수로 정의 가능
* 3가지 부분으로 구성
  * 함수의 이름 (생략가능)
  * 매개 변수(args)
  * body (중괄호 내부)
  ```javascript
  const add = function (num1, num2) {
    return num1 + num2
  }
  ```

* 기본인자(default argument)설정 가능
* 매개변수와 인자의 개수 불일치 허용
* Rest Parameter (python의 *args와 유사, 매개변수를 배열로 받음 인자가 넘어오지 않을 경우 빈 배열로 처리)
* Spread operator
```javascript
const spreadOpr = function (arg1, arg2, arg3) {
  return arg1 + arg2 + arg3
}
const numbers = [1,2,3]
spreadOpr(...numbers) // 6
```

# 함수 선언식과 표현식 비교 정리
* 공통점 : 데이터 타입, 함수 구성요소
* 차이점 
  * 함수선언식: 익명 함수 불가능, 호이스팅 O
  * 함수표현식: 익명 함수 가능, 호이스팅 X


# Arrow Function
```javascript
const arrow1 = function (name) {
  return `heelo, ${name}`
}

// 1.function 키워드 삭제
const arrrow2 = (name) => { return `hello, ${name}`}
// 2. 매개변수가 1개일 경우에만 () 생략 가능
const arrrow2 = name => { return `hello, ${name}`}
// 3. 함수 바디가 return을 포함한 표현식 1개일 경우에 {}&return 삭제 가능
const arrrow2 = name => `hello, ${name}`
```

# 배열
* 키와 속성들을 담고 있는 참조 타입의 객체
* 순서를 보장하는 특징이 있음
* 주로 대괄호를 이용하여 생성하고 0을 포함한 양의 정수 인덱스로 특정 값에 접근 가능
* 배열의 길이는 array.length형태로 접근 가능

# 배열 관련 주요 메서드
* forEach
  * array.forEach(callback(element[,index[,array]]))
  * 배열의 각 요소에 대해 콜백 함수를 한번씩 실행
  * 콜백 함수는 3가지 매개변수로 구성
    * element: 배열의 요소
    * index: 배열 요소의 인덱스
    * array: 배열 자체
  * 반환 값이 없는 메서드
  ```javascript
  const fruits = ['딸기','수박','사과','체리']
  fruits.forEach((fruit, index)) => {
    console.log(fruit, index)
    // 딸기 0
    // 수박 1
    // 사과 2
    // 체리 3
  }
  ```

  
  # 객체
  * 객체는 속성의 집합이며, 중괄호 내부에 key와 value의 쌍으로 표현
  * key는 문자열 타입만 가능
    * key이름에 띄어쓰기 등의 구분자가 있으면 따옴표로 묶어서 표현
  * value는 모든 타입(함수포함) 가능
  * 객체 요소 접근은 점 또는 대괄호로 가능
    * key이름에 띄어쓰기 같은 구분자가 있으면 대괄호 접근만 가능

  * 메서드는 객체의 속성이 참조하는 함수
  * 객체.메서드명()으로 호출 가능
  * 메서드 내부에서는 this 키워드가 객체를 의미함
  ```javascript
  const me = {
    firstName: 'John',
    lastName: 'Doe',
    getFullName: function () {
      return this.firstName + this.lastName
    }
  }
  ```