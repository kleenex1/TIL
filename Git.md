# Git이란 ?
  1. 분산 버전 관리시스템
  2. 협업 관리 

# Repository & Commit 
  1. Repository</br>
    - 버전별 프로젝트 모습을 나타낸다.</br>
    - 커밋이 저장되는 곳
  2. Commit</br>
    - 하나의 버젼으로 남기는 동작

# Working directory / Staging area / Repository
  - `Working directory` : 현재 작업(수정)한 파일
  - `Staging area` : git add를 한 파일들이 존재하는 영역(index)
  - `repository` : commit을 하면 저장되는 곳(버전)

---

# 기본 명령어
  1. `$ git add` <file> : Staging area에 올리는 명령어
  2. `$ git commit` -m '<커밋메시지>' : 간단하게 변경사항을 나타낼 수 있도록 명확하게 작성
  3. `$ git status` : staging area에 있는지 유무 및 working dir의 파일 tracking 유무 확인 가능
  4. `$ git log` : 버전 확인 기능 </br>
    - `log --oneline` : log 한줄씩 간단하게 확인 가능 </br>
    - `log --pretty --oneline` : 커밋된 아이디 전체 확인이 가능 & log 한줄씩

# Git 설정 파일(config)
  - 사용자 정보 
    * $ git config --global user.name "*username*"
    * $ git config --global user.email "*user@email.com*"
  - 설정 확인
    * $ git config -list
    * $ git config --global --list
    * $ git config user.name

# Git Push & Pull 
  > 로컬에서 Github라는 원격 저장소에 보내려면 remote 설정을 먼저 해줘야 한다.
  > git remote add origin Github_Repository_Url </br>
    `origin`: 최초로 remote 할때 origin이라는 이름을 쓰는것이 관례
  
<<<<<<< HEAD
  1. Git Push </br>
  ```$ git push <원격저장소이름> <브랜치이름>```
  2. Git Pull </br>
  ```$ git pull <원격저장소이름> <브랜치이름>```
  3. Git Clone(상대방 원격저장소를 받아보고 싶을때) </br>
=======
  * Git Push </br>
  ```$ git push <원격저장소이름> <브랜치이름>```
  * Git Pull </br>
  ```$ git pull <원격저장소이름> <브랜치이름>```
  * Git Clone(상대방 원격저장소를 받아보고 싶을때) </br>
>>>>>>> 5247879fe4bbd8e9db6be82eb187f95b04e8049c
  ```$ git clone <원격저장소주소>```
  * Remote </br>
  ```$ git remote -v``` : 현재 연결되어 있는 원격저장소를 확인 </br>
  ```$ git remote remove <name>```: 옵션을 통해서 연결되어 있는 저장소 연결을 끊을 수 있음 </br>
  ```$ git remote add <name> <url>```: 옵션으로 다시 연결가능함 </br>
  
  
# Git Branch
