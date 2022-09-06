# Components

* 부트스트랩에 id가 있는 경우 무조건 id를 일치시켜서 유지해야함
* 대부분 자바스크립트를 활용하고 있고 타겟으로 활용되는 경우가 있다
![스크린샷](./%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-09-06%20102530.png)

* Accordian
  * 내부적으로 collapse를 사용하여 접기가 가능하다.
  ```HTML
<div class="accordion" id="accordionExample">
  <div class="accordion-item">
    <h2 class="accordion-header" id="headingOne">
      <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
        Accordion Item #1
      </button>
    </h2>
    <div id="collapseOne" class="accordion-collapse collapse show" aria-labelledby="headingOne" data-bs-parent="#accordionExample">
      <div class="accordion-body">
        Accordian Body
      </div>
    </div>
  </div>
</div>
  ```

* Alert
  ```HTML
<div class="alert alert-primary" role="alert">
  A simple primary alert—check it out!
</div>
  ```
* Badge
```HTML
<h1>Example heading <span class="badge bg-secondary">New</span></h1>
```
  * 링크나 버튼의 모서리에 배치하기.
```HTML
<button type="button" class="btn btn-primary position-relative">
  Inbox
  <span class="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-danger">
    99+
    <span class="visually-hidden">unread messages</span>
  </span>
</button>
```
* Breadcrumb
```HTML
<nav aria-label="breadcrumb">
  <ol class="breadcrumb">
    <li class="breadcrumb-item active" aria-current="page">Home</li>
  </ol>
</nav>

<nav aria-label="breadcrumb">
  <ol class="breadcrumb">
    <li class="breadcrumb-item"><a href="#">Home</a></li>
    <li class="breadcrumb-item active" aria-current="page">Library</li>
  </ol>
</nav>

<nav aria-label="breadcrumb">
  <ol class="breadcrumb">
    <li class="breadcrumb-item"><a href="#">Home</a></li>
    <li class="breadcrumb-item"><a href="#">Library</a></li>
    <li class="breadcrumb-item active" aria-current="page">Data</li>
  </ol>
</nav>
```
* Button 
```HTML
<button type="button" class="btn btn-primary">Primary</button>
<button type="button" class="btn btn-secondary">Secondary</button>
<button type="button" class="btn btn-success">Success</button>
<button type="button" class="btn btn-danger">Danger</button>
<button type="button" class="btn btn-warning">Warning</button>
<button type="button" class="btn btn-info">Info</button>
<button type="button" class="btn btn-light">Light</button>
<button type="button" class="btn btn-dark">Dark</button>

<button type="button" class="btn btn-link">Link</button>
```

* Card
* 이미지 크기 (inline style을 확인하기!)
![스크린샷](./%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-09-06%20104919.png)

* Carousel
```HTML
<div id="carouselExampleSlidesOnly" class="carousel slide" data-bs-ride="carousel">
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img src="..." class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src="..." class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src="..." class="d-block w-100" alt="...">
    </div>
  </div>
</div>
```

* Collapse
  * JavaScript 플러그인으로 콘텐츠의 표시와 숨김에 사용됨.
  * 일반적으로 우리는 버튼을 data-bs-target 속성과 함께 사용 권장합니다. 권장하지 않지만 href 속성을 갖는 링크(및 role="button")를 사용할 수도 있다. 양쪽 모두 data-bs-toggle="collapse"가 필요
  ```html
<p>
  <a class="btn btn-primary" data-bs-toggle="collapse" href="#collapseExample" role="button" aria-expanded="false" aria-controls="collapseExample">
    Link with href
  </a>
  <button class="btn btn-primary" type="button" data-bs-toggle="collapse" data-bs-target="#collapseExample" aria-expanded="false" aria-controls="collapseExample">
    Button with data-bs-target
  </button>
</p>
<div class="collapse" id="collapseExample">
  <div class="card card-body">
    Some placeholder content for the collapse component. This panel is hidden by default but revealed when the user activates the relevant trigger.
  </div>
</div>
  ```

* dropdwon 
  ```HTML
  <div class="dropdown">
  <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false">
    Dropdown button
  </button>
  <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
    <li><a class="dropdown-item" href="#">Action</a></li>
    <li><a class="dropdown-item" href="#">Another action</a></li>
    <li><a class="dropdown-item" href="#">Something else here</a></li>
  </ul>
</div>
  ```

* Modal
```HTML
<div class="modal" tabindex="-1">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title">Modal title</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <p>Modal body text goes here.</p>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div>
```
* 내비게이션
  * 내비게이션 바는 .navbar를 .navbar-expand{-sm|-md|-lg|-xl|-xxl}로 감싸야 하며, color scheme클래스가 필요.
  * .navbar-brand으로 회사명이나 제품명, 프로젝틈명 등.
  .navbar-nav으로 full-height와 보다 가벼운 네비게이션(드롭다운을 위한 지원 포함)을 실현.
  .navbar-toggler은 콜랩스 플러그인과 다른 navigation toggling행동에 사용.
  모든 폼 컨트롤과 액션을 위한 flex와 spacing 유틸리티.
  수직 방향으로 센터링된 문자열을 추가하기 위한 .navbar-text.
  .collapse.navbar-collapse으로 부모 중단점에 따라 내비게이션 바의 콘텐츠를 그룹화하거나 감출수 있음.
  옵션으로 .navbar-scroll를 추가해 max-height와 scroll expanded navbar content이 가능.

