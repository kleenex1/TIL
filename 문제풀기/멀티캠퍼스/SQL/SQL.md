# Database

- 데이터베이스는 체계화된 데이터의 모임
- 여러 사람이 공유하고 사용할 목적으로 통합 관리되는 정보의 집합
- 논리적으로 연관된 자료의 모음, 내용을 구조화 하여 검색과 갱신의 효율화를 꾀함
- 몇 개의 자료 파일을 조직적으로 통합하여 자료 항목의 중복을 없애고 자료를 구조화

* 데이터베이스로 얻는 장점들
  - 데이터 중복 최소화
  - 데이터 무결성 (정확한 정보를 보장)
  - 데이터 일관성
  - 데이터 독립성 (물리적 / 논리적)
  - 데이터 표준화
  - 데이터 보안 유지

# RDB(Relational Database) - 관계형 데이터베이스

  - 서로 관련된 데이터를 저장하고 접근할 수 있는 데이터베이스 유형
  - 키와 값들의 간단한 관꼐를 표 형태로 정리한 데이터 베이스
  **스키마**
  - 데이터베이스에서 자료의 구조, 표현방법, 관계등 전반적으로 명세를 기술한 것
  ```sql
  .schema healthcare # 입력하면 아래처럼 조회 혹은 생성하면서 설정
  CREATE TABLE healthcare (
  id PRIMARY KEY,        
  sido INTEGER NOT NULL, 
  gender INTEGER NOT NULL,
  age INTEGER NOT NULL,  
  height INTEGER NOT NULL,
  weight INTEGER NOT NULL,
  waist REAL NOT NULL,   
  va_left REAL NOT NULL, 
  va_right REAL NOT NULL,
  blood_pressure INTEGER 
  NOT NULL,
  smoking INTEGER NOT NULL,
  is_drinking BOOLEAN NOT NULL
  );
  ```

  **기본키(Primary Key)** 
  - 각 행(레코드)의 고유 값
  - 반드시 설정해야 하며, 데이터베이스 관리 및 관계 설정 시 주요하게 활용됨

# RDBMS 관계형 데이터베이스 관리 시스템
- SQLite 
  - 서버 형태가 아닌 파일 형식으로 응용 프로그램에 넣어서 사용하는 비교적 가벼운 데이터베이스
  - 구글 안드로이드 운영체제에 기본적으로 탑재된 데이터베이스이며, 임베디드 소프트웨어에도 많이 활용
  - 로컬에서 간단한 DB 구성을 할 수 있으며, 오픈소스 프로젝트이기 때문에 자유롭게 사용가능

- SQlite Data Type
  1. Null
  2. INTEGER
    - 크기에 따라 0,1,2,3,4,6 또는 8바이트에 저장된 부호 있는 정수
  3. REAL
    - 8바이트 부동 소수점 숫자로 저장된 부동 소수점 값
  4. TEXT
  5. BLOB
    - 입력된 그대로 정확히 저장된 데이터 (별다른 타입없이 그대로 저장)


# SQL (Structured Query Language)
  - 관계형 데이터베이스 관리시스템의 데이터 관리를 위해 설계된 특수 목적 프로그래밍 언어
  - 데이터베이스 스키마 생성 및 수정
  - 자료의 검색 및 관리
  - 데이터베이스 객체 접근 조정관리
  
  DDL(Data Definition Language)	: 관계형 데이터베이스 구조를 정의하기 위한 명령어	
    - CREATE, DROP, ALTER
  DML(Data Manipulation Language) : 데이터를 저장, 조회, 수정, 삭제 등을 하기 위한 명령어
    - INSERT, SELECT, UPDATE, DELETE
  DCL(Data Control Language) : 데이터베이스 사용자의 권한 제어를 위해 사용하는 명령어	
    - GRANT, REVOKE, COMMIT, ROLLBACK

# 데이터베이스 생성하기
```sql
$ sqlite3 ___.sqlite3
sqlite> .database
```

# csv 파일을 table로 만들기
```sql
>.mode csv
>.import ____.csv table이름
>.tables
table이름
```

# 기본 명령어
```sql
1. 테이블 생성
CREATE TABLE 테이블명 (
  id INTEGER PRIMARY KEY,
  name TXT
);

2. 스키마 조회
.schema 테이블명

3. 테이블 삭제
DROP TABLE 테이블명

# 필드 제약 조건
NOT NULL : NULL 값 입력 금지
UNIQUE : 중복 값 입력 금지 (NULL 값은 중복 가능)
PRIMARY KEY : 테이블에서 반드시 하나 NOT NULL + UNIQUE
FOREIGN KEY : 외래키, 다른 테이블의 KEY
CHECK : 조건으로 설정된 값만 이볅 허용
DEFAULT : 기본 설정 값

예시)
CREATE TABLE students(
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  age INTEGER DEFAULT 1 CHECK (0 < age)
);
```

# CRUD
- INSERT
  - 테이블에 단일 행 삽입
  - INSERT INTO 테이블_이름 (컬럼1, 컬럼2) VALUES (값1, 값2);
  - 정의된 모든 컬럼에 맞춰 순서대로 입력
  - INSERT INTO 테이블_이름 VALUES (값1, 값2, 값3);

- READ
  - SELECT
  - ORDER BY, DISTINCT, WHERE, LIMIT, GROUP BY .. 등과 같은 다양한 절과 함께 사용

- LIMIT
  - 쿼리에서 반횐되는 행 수를 제한
  - 특정 행부터 시작해서 조회하기 위해 OFFSET 키워드와 함께 사용하기도 함
  ```sql
  SELECT * FROM MY_TABLE LIMIT 10 OFFSET 5
  ```
  - 6번째 행부터 10개 행을 조회 (6번째 행부터 10개를 출력)

- WHERE
  - 쿼리에서 반한된 행에 대한 특정 검색 조건을 지정

- SELECT DISTINCT
  - 조회 결과에서 중복 행을 제거
  - DISTINCT 절은 SELECT 키워드 바로 뒤에 작성해야 함

- UPDATE
  ```sql
  UPDATE classmates SET address='서울' WHERE rowid=5;
  ```

- DELETE
  ```sql
  DELETE FROM classmates WHERE rowid=5;
  ```


