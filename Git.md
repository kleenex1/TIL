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
  
  * Git Push </br>
  ```$ git push <원격저장소이름> <브랜치이름>```
  * Git Pull </br>
  ```$ git pull <원격저장소이름> <브랜치이름>```
  * Git Clone(상대방 원격저장소를 받아보고 싶을때) </br>
  ```$ git clone <원격저장소주소>```
  * Remote </br>
  ```$ git remote -v``` : 현재 연결되어 있는 원격저장소를 확인 </br>
  ```$ git remote remove <name>```: 옵션을 통해서 연결되어 있는 저장소 연결을 끊을 수 있음 </br>
  ```$ git remote add <name> <url>```: 옵션으로 다시 연결가능함 </br>
  * Ignore </br>
    [Python.gitignore 링크](https://github.com/github/gitignore/blob/main/Python.gitignore)
    * 이미 push된 file에 대해 git ignore 적용하기 
    ```
    $ git rm -r --cached .
    $ git add .
    $ git commit -m "Apply .gitignore"
    $ git push origin master
    ```
---

# 명령어 정리

- **git init** : 현재 디렉토리를 Git이 관리하는 프로젝트 디렉토리(=working directory)로 설정하고 그 안에 레포지토리(.git 디렉토리) 생성

- **git config** **user.name 'codeit'** : 현재 사용자의 아이디를 'codeit'으로 설정(커밋할 때 필요한 정보)

- **git config user.email 'teacher@codeit.kr'** : 현재 사용자의 이메일 주소를 'teacher@codeit.kr'로 설정(커밋할 때 필요한 정보)

- **git add [파일 이름]** : 수정사항이 있는 특정 파일을 staging area에 올리기

- **git add [디렉토리명]** : 해당 디렉토리 내에서 수정사항이 있는 모든 파일들을 staging area에 올리기 

- **git add .** : working directory 내의 수정사항이 있는 모든 파일들을 staging area에 올리기

- **git reset [파일 이름]** : staging area에 올렸던 파일 다시 내리기

- **git status** : Git이 현재 인식하고 있는 프로젝트 관련 내용들 출력(문제 상황이 발생했을 때 현재 상태를 파악하기 위해 활용하면 좋음) 

- **git commit -m "커밋 메시지"** : 현재 staging area에 있는 것들 커밋으로 남기기

- **git help [커맨드 이름]** : 사용법이 궁금한 Git 커맨드의 공식 메뉴얼 내용 출력



- **git push -u(또는 --set-upstream) origin master** : 로컬 레포지토리의 내용을 처음으로 리모트 레포지토리에 올릴 때 사용합니다.

- **git push** : 위의 커맨드를 한번 실행하고 난 후에는 git push라고만 쳐도 로컬 레포지토리의 내용을 리모트 레포지토리에 올릴 수 있습니다.

- **git pull** : 바로 위의 위에 있는 커맨드를 한번 실행하고 난 후에는 git pull이라고만 쳐도 리모트 레포지토리의 내용을 로컬 레포지토리로 가져옵니다.

- **git clone [프로젝트의 GitHub 상 주소]** : GitHub에 있는 프로젝트를 내 컴퓨터로 가져오기

 

- **git log** : 커밋 히스토리를 출력

- **git log --pretty=oneline** : --pretty 옵션을 사용하면 커밋 히스토리를 다양한 방식으로 출력할 수 있습니다. --pretty 옵션에 oneline이라는 값을 주면 커밋 하나당 한 줄씩 출력해줍니다. --pretty 옵션에 대해 더 자세히 알고싶으면 [이 링크](https://git-scm.com/docs/pretty-formats)를 참고하세요. 

- **git show [커밋 아이디]** : 특정 커밋에서 어떤 변경사항이 있었는지 확인

- **git commit --amend** : 최신 커밋을 다시 수정해서 새로운 커밋으로 만듦

- **git config alias.[별명] [커맨드]** : 길이가 긴 커맨드에 별명을 붙여서 이후로는 별명으로도 해당 커맨드를 실행할 수 있게 설정

- **git diff [커밋 A의 아이디] [커밋 B의 아이디]** : 두 커밋 간의 차이 비교

- **git reset [옵션] [커밋 아이디]** : 옵션에 따라 하는 작업이 달라짐(옵션을 생략하면 --mixed 옵션이 적용됨) 

​		(1) HEAD가 특정 커밋을 가리키도록 이동시킴(--soft는 여기까지 수행)

​		(2) staging area도 특정 커밋처럼 리셋(--mixed는 여기까지 수행)

​		(3) working directory도 특정 커밋처럼 리셋(--hard는 여기까지 수행)

​		그리고 이때 커밋 아이디 대신 HEAD의 위치를 기준으로 한 표기법(예 : HEAD^, HEAD~3)을 사용해도 됨

- **git tag [태그 이름] [커밋 아이디]** : 특정 커밋에 태그를 붙임

 

- **git branch [새 브랜치 이름]** : 새로운 브랜치를 생성

- **git checkout -b [새 브랜치 이름]** : 새로운 브랜치를 생성하고 그 브랜치로 바로 이동

- **git branch -d [기존 브랜치 이름]** : 브랜치 삭제

- **git checkout [기존 브랜치 이름]** : 그 브랜치로 이동

- **git merge [기존 브랜치 이름]** : 현재 브랜치에 다른 브랜치를 머지

- **git merge --abort** : 머지를 하다가 conflict가 발생했을 때, 일단은 머지 작업을 취소하고 이전 상태로 돌아감



- **git fetch** : 로컬 레포지토리에서 현재 HEAD가 가리키는 브랜치의 업스트림(upstream) 브랜치로부터 최신 커밋들을 가져옴(가져오기만 한다는 점에서, 가져와서 머지까지 하는 git pull과는 차이가 있음)

- **git blame** : 특정 파일의 내용 한줄한줄이 어떤 커밋에 의해 생긴 것인지 출력 

- **git revert** : 특정 커밋에서 이루어진 작업을 되돌리는(취소하는) 커밋을 새로 생성



- **git reflog** : HEAD가 그동안 가리켜왔던 커밋들의 기록을 출력

- **git log --all --graph** : 모든 브랜치의 커밋 히스토리를, 커밋 간의 관계가 잘 드러나도록 그래프 형식으로 출력

- g**it rebase [브랜치 이름]** : A, B 브랜치가 있는 상태에서 지금 HEAD가 A 브랜치를 가리킬 때, **git rebase B**를 실행하면 A, B 브랜치가 분기하는 시작점이 된 공통 커밋 이후로부터 존재하는 A 브랜치 상의 커밋들이 그대로 B 브랜치의 최신 커밋 이후로 이어붙여짐(git merge와 같은 효과를 가지지만 커밋 히스토리가 한 줄로 깔끔하게 된다는 차이점이 있음)

- **git stash** : 현재 작업 내용을 스택 영역에 저장

- **git stash apply [커밋 아이디]** : 스택 영역에 저장된 가장 최근의(혹은 특정) 작업 내용을 working directory에 적용

- **git stash drop [커밋 아이디]** : 스택 영역에 저장된 가장 최근의(혹은 특정) 작업 내용을 스택에서 삭제

- **git stash pop [커밋 아이디]** : 스택 영역에 저장된 가장 최근의(혹은 특정) 작업 내용을 working directory에 적용하면서 스택에서 삭제

- **git cherry-pick [커밋 아이디]** : 특정 커밋의 내용을 현재 커밋에 반영
