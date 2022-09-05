# HTML 문서 구조화
* table의 각 영역을 명시하기 위해 \<thead>, \<tbody>, \<tfoot> 요소를 활용
* 테이블 태그에 3요소가 모두 필요한 것은 아니다. 선택해서 활용하면 된다.
* \<tr>로 가로 줄을 구성하고 내부에는 \<th> 혹은 \<td> 로 셀을 구성
* colspan, rowspan을 통해 셀 병합

```HTML
<body>
  <table>
    <thead>
      <tr>
        <th>ID</th>
        <th>Name</th>
        <th>Major</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>1</td>
        <td>홍길동</td>
        <td>Computer Science</td>
      </tr>
    </tbody>
    <tfoot>
      <tr>
        <td>총계</td>
        <td colspan="2">1명</td>
    </tfoot>
    <caption>학생 명단</caption>
  </table>
</body>
```

# Form 
https://web.dev/learn/forms/
* \<form>은 정보(데이터)를 서버에 제출하기 위해 사용하는 태그
* \<form> 기본 속성
	* action: form을 처리할 서버의 URL(데이터를 보낼 곳)
	* method: form을 제출할 때 사용할 HTTP 메서드 (GET 혹은 POST)
	* enctype: method가 post인 경우 데이터의 유형
		* application/x-www-form-urlencoded: 기본값
		* mulitpart/form-data: 파일 전송시(input type이 file인 경우)
		* text/plain: HTML5 디버깅 용 (잘 사용되지 않음)

```HTML
<form action="/search" method="GET">
</form>
```

# Input
* 다양한 타입을 가지는 입력 데이터 유형과 위젯이 제공됨
* \<input> 대표적인 속성
	* name : form control에 적용되는 이름 (이름/ 값 페어로 전송됨)
	* value : form control에 적용되는 값 (이름/값 페어로 전송됨)
	* required, readonly, autofocus, autocomplete, disabled 등
```HTML
<form action="/search" method="GET">
  username: <input type="text" name="q">
</form>
```
→https:/www.google.com/search?q=HTML

# Input label
* label을 클릭하여 input 자체의 초점을 맞추거나 활성화 시킬 수 있음
	* 사용자는 선택할 수 있는 영역이 늘어나 웹 / 모바일 환경에서 편하게 사용할 수 있음
	* label과 input 입력의 관계가 시각적 뿐만 아니라 화면리더기에서도 label을 읽어 쉽게 내용을 확인 할 수 있도록 함
* \<input>에 id 속성을, \<label>에는 for 속성을 활용하여 상호 연관을 시킴
```HTML
<label for="agreement">개인정보 수집에 동의합니다.</label>
<input type="checkbox" name="agreement" id="agreement">
```
* 예제
```HTML
<body>
  <form action="">
    <label for="username">username</label>
    <input type="email" name="username" id="username">
    <input for="password">password</label>
    <input type="password" name="password" id="password">
    <input type="submit" value="얍!">
  </form>
</bdoy>
```

# Input 유형 - 일반
* 일반적으로 입력을 받기 위하여 제공되며 타입별로 HTML기본 검증 혹은 추가 속성을 활용할 수 있음
	* text : 일반 텍스트 입력
	* password : 입력 시 값이 보이지 않고 문자를 특수기호로 표현
	* email : 이메일 형식이 아닌 경우 form 제출 불가
	* number : min, max, step 속성을 활용하여 숫자 범위 설정 가능
	* file : accept 속성을 활용하여 파일 타입 지정 가능

# Input 유형 - 항목 중 선택
* 일반적으로 label 태그와 함께 사용하여 선택 항목을 작성함
* 동일 항목에 대하여는 name을 지정하고 선택된 항목에 대한 *value를 지정해야함*
	* checkbox : 다중 선택
	* radio : 단일 선택

```HTML
<div>
  <p>checkbox</p>
  <input id="html" type="checkbox" name="language" value="html">
  <label for="html">HTML</label>
  <input id="python" type="checkbox" name="language" value="python">
  <lable for="python">파이썬</label>
  <hr>
  <p>radio</p>
  <input id="html" type="radio" name="language" value="html">
  <label for="html">HTML</label>
  <input id="python" type="radio" name="language" value="python">
  <lable for="python">파이썬</label>
</div>
```
![스크린샷](./%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-09-05%20102939.png)

# Input 유형 - 기타
* 다양한 종류의 input을 위한 picker를 제공
	* color : color picker
	* date : date picker
* hidden input을 활용하여 사용자 입력을 받지 않고 서버에 전송되어야 하는 값을 설정 (django 다룰때 다시함)
	* hidden : 사용자에게 보이지 않는 input

# Bootstrap
* CDN (Content Delivery Network)
	* 컨텐츠(CSS, JS, Image, Text 등)을 효율적으로 전달하기 위해 여러 노드에 가진 네트워크에 데이터를 제공하는 시스템. 개별 end-user의 가까운 서버를 통해 빠르게 전달 가능(지리적 이점) 외부 서버를 활용함으로써 본인 서버의 부하가 적어짐.
* spacing (Margin and padding)
	* **{property}{sides}-{size}**
	* mt - 3
	```html
	<div class="mt-3 ms-5">bootstrap-sapcing</div>
	```
	* **{property}**
		* m - for classes that set *margin*
		* p - for classes that set *padding* 
	* **{sides}**
		* t - for classes that set margin-top or padding-top
		* b - for classes that set margin-bottom or padding-bottom
		* x - for classes that set both \*-left and \*-right
		* y - for classes that set both \*-top and \*-bottom
		* s - (start) for classes that set margin-left or padding-left in LTR(left to right), margin-right or padding-right in TRL
		* e - (end) for classes that set margin-right or padding-right in LTR, margin-left or padding-left in RTL
		* blank - for classes that set a margin or padding on all 4 sides of the element.
	* **{size}**
		* 0 - eliminate margin or padding : 0
		* 1 - set the margin or padding to $spacer \*.25 (4px)
		* 2 - \*0.5
		* 3 - equl to **1rem** (16px)
		* 4 - \*1.5
		* 5 - \*3
		* auto : auto (**블럭 요소 수평 중앙 정렬 가로 가운데 정렬** )<br>
![스크린샷](./%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-09-05%20110441.png)
