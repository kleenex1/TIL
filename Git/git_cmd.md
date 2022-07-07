# Git 기본 명령어
- `$ git add [파일 이름]` : 수정사항이 있는 특정 파일을 staging area에 올리기
- `$ git add [디렉토리명]` : 해당 디렉토리 내에서 수정사항이 있는 모든 파일들을 staging area에 올리기 
- `$ git add .` : working directory 내의 수정사항이 있는 모든 파일들을 staging area에 올리기
- `$ git reset [파일 이름]` : staging area에 올렸던 파일 다시 내리기

# Git에서 커밋 다루기
- `$ git log` : 커밋 히스토리 출력
- `$ git log --pretty=oneline` : [pretty 옵션](https://git-scm.com/docs/pretty-formats)
  * git config alias.[별명] [커맨드] : 앞의 --pretty=oneline같이 긴 커맨드를 git [별명]으로 대체하여 쓸 수 있다.
- `$ git show [커밋아이디]` : 특정 커밋에서 어떤 변경사항 있었는지 확인
- `$ git commit --amend` : 최신 커밋을 다시 수정해서 새로운 커밋으로 만듦 
- `$ git diff [커밋A] [커밋B]` : 두 커밋 차이 비교
- `$ git reset [옵션] [커밋 아이디]` : 션에 따라 하는 작업이 달라짐(옵션을 생략하면 --mixed 옵션이 적용됨) 
		(1) HEAD가 특정 커밋을 가리키도록 이동시킴(--soft는 여기까지 수행)
		(2) staging area도 특정 커밋처럼 리셋(--mixed는 여기까지 수행)
		(3) working directory도 특정 커밋처럼 리셋(--hard는 여기까지 수행)
		그리고 이때 커밋 아이디 대신 HEAD의 위치를 기준으로 한 표기법(예 : HEAD^, HEAD~3)을 사용해도 됨
- `$ git tag [태그 이름] [커밋 아이디]` : 특정 커밋에 태그 붙임

# GitHub Push & Pull 
  > 로컬에서 Github라는 원격 저장소에 보내려면 remote 설정을 먼저 해줘야 한다.
  > git remote add origin Github_Repository_Url </br>
    `origin`: 최초로 remote 할때 origin이라는 이름을 쓰는것이 관례
  
  * Git Push : ```$ git push <원격저장소이름> <브랜치이름>```
  * Git Pull : ```$ git pull <원격저장소이름> <브랜치이름>```
  * Git Clone(상대방 원격저장소를 받아보고 싶을때) : ```$ git clone <원격저장소주소>``` </br>
  **git push**와 **git pull**은 그 작업 단위가 브랜치입니다. 예를 들어, master 브랜치에서 git push를 하면 master 브랜치의 내용만 리모트 레포지토리의 master 브랜치로 전송되지, premium 브랜치의 내용이 전송되는 것은 아닙니다.(git push에 --all이라는 옵션을 주면 모든 브랜치의 내용을 전송할 수 있기는 합니다.)</br>

  * Remote </br>
  ```$ git remote -v``` : 현재 연결되어 있는 원격저장소를 확인 </br>
  ```$ git remote remove <name>```: 옵션을 통해서 연결되어 있는 저장소 연결을 끊을 수 있음 </br>
  ```$ git remote add <name> <url>```: 옵션으로 다시 연결가능함 </br>
  * Ignore </br>
    * [Python.gitignore 링크](https://github.com/github/gitignore/blob/main/Python.gitignore)
    * 이미 push된 file에 대해 git ignore 적용하기 
    ```
    $ git rm -r --cached .
    $ git add .
    $ git commit -m "Apply .gitignore"
    $ git push origin master
    ```

# Branch 사용하기
- `$ git branch [새 브랜치 이름]` 
- `$ git checkout -b [새 브랜치 이름]` : 생성하고 해당 브랜치로 이동
- `$ git branch -d [기존 브랜치 이름]` : 브랜치 삭제
- `$ git merge [기존 브랜치 이름]` : 현재 브랜치에 [기존 브랜치] 머지
- `$ git merge --abort` : 머지 하다가 conflict 발생 시, 일단 머지를 취소하고 이전 상태로 돌아감

# Git 심화
- `$ git fetch` : 로컬 레포지토리에서 현재 HEAD가 가리키는 브랜치의 업스트림(upstream) 브랜치로부터 최신 커밋들을 가져옴(가져오기만 한다는 점에서, 가져와서 머지까지 하는 git pull과는 차이가 있음)

- `$ git blame` : 특정 파일의 내용 한줄한줄이 어떤 커밋에 의해 생긴 것인지 출력 

- `$ git revert` : 특정 커밋에서 이루어진 작업을 되돌리는(취소하는) 커밋을 새로 생성



- `$ git reflog` : HEAD가 그동안 가리켜왔던 커밋들의 기록을 출력

- `$ git log --all --graph` : 모든 브랜치의 커밋 히스토리를, 커밋 간의 관계가 잘 드러나도록 그래프 형식으로 출력

- `$ git rebase [브랜치 이름]`: A, B 브랜치가 있는 상태에서 지금 HEAD가 A 브랜치를 가리킬 때, **git rebase B**를 실행하면 A, B 브랜치가 분기하는 시작점이 된 공통 커밋 이후로부터 존재하는 A 브랜치 상의 커밋들이 그대로 B 브랜치의 최신 커밋 이후로 이어붙여짐(git merge와 같은 효과를 가지지만 커밋 히스토리가 한 줄로 깔끔하게 된다는 차이점이 있음)

- `$ git stash` : 현재 작업 내용을 스택 영역에 저장

- `$ git stash apply [커밋 아이디]` : 스택 영역에 저장된 가장 최근의(혹은 특정) 작업 내용을 working directory에 적용

- `$ git stash drop [커밋 아이디]` : 스택 영역에 저장된 가장 최근의(혹은 특정) 작업 내용을 스택에서 삭제

- `$ git stash pop [커밋 아이디]` : 스택 영역에 저장된 가장 최근의(혹은 특정) 작업 내용을 working directory에 적용하면서 스택에서 삭제

- `$ git cherry-pick [커밋 아이디]` : 특정 커밋의 내용을 현재 커밋에 반영


