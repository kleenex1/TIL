# 형 변환

* String, Number, Boolean
Number('10') --> 숫자
String(10) --> 문자열


console.log('4'+3) = 43

--------------------------------------------------------------------------------------------------------------------
* falsy값 : '', 0, Nan 

# 형 변환(Type Conversion)
- 산술연산자(*,%,-,+), 비교연산자(<,>,<=,>=), (==, !=)
- console.log('4'-true); (true가 형변환이 자동적으로 되어 1로 계산됨.) 
- console.log(1 == '1'); true
- console.log(1 == true); true

* 더하기 연산은 피연산자가 한쪽이라도 문자열이 있을 경우 양쪽 모두 문자열로 형변환
* 더하기 기호를 제외한 일반 산술연산자들은 모두 숫자형으로 변환한 다음 연산


- 단, 일치 비교 연산(===,!==)는 형변환이 일어나지 않음.
console.log(1 === '1'); false
console.log(1 === true); false

# 템플릿 문자열
템플릿 문자열을 쓰면 변수와 문자열을 + 기호로 잇지 않아도 한번에 쓸 수 있다.
console.log(`문자열문자열 ${변수}문자열`)
console.log(`문자열문자열 ${함수(변수)}문자열`)

# JS의 자료형
String, Number, Boolean 이외에도
Null과 Undefined라는 것이 있다.
Null - 의도적으로 없음을 표현할 때 사용하는 값
Undefined - 값이 없다는 것을 확인하는 값

```javascript
let x;
console.log(x); undefined
let y = x;
x = null;
console.log(y); undefined
console.log(x); null
x = y;
console.log(x); undefined
```