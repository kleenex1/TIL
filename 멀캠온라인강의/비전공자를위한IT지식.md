# 개발자의 암호문 - API
API는 클라이언트 프로그램과 서버 프로그램이 중간에 있는 체계
API는 클라이언트와 서버를 이어주는 개념

 - 클라이언트 관점
 * CREATE __컴퓨터주소/timelinecreate__ `POST 메서드` 
 * READ __컴퓨터주소/timelineread__     `GET 메서드`
 * UPDATE __컴퓨터주소/timelineupdate__ `PUT 메서드`(전체) / `PATCH 메서드`(일부)
 * DELETE __컴퓨터주소/timelinedelete__ `DELETE 메서드`
  → __/이런식__ 으로 이름을 정해놓으면 개발자마다 다른 네이밍으로 인한 문제가 생길 수 있다.
   체계적으로 이름을 정해야겠다 → `Restful한 API`
   

- 서버의 관점
* READ `잘됐어` (200) `잘 안됐어` (클라이언트쪽에서 잘못 : 400, 서버에서 잘못 : 500)

# 요청과 응답을 주고 받을 때의 형식 - JSON(요즘 많이 씀) / XML(과거에 많이 쓰던 것)
* JSON 형식
```
{
  키1(Key): 값1(Value),
  키2(Key): 값2(Value),
}
```
* 로그인 요청 예시
```
{
  "id": "wychoi",
  "pw": "a12345"
}
```

