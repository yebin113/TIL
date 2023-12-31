# GIT

git 이란? "**버전관리 시스템**"

버전 관리의 예시  **Google Docs**

문서의 최종적인 완성을 저장하는 행위와는 개념이 약간 다름

**변경사항을 저장**하여 이전 시점으로 돌아갈 수 있음

최종에최종 찐최종 과 같이 따로 저장할 필요가 없고 **버전이라는 기능**을 사용하면 됨

GIT은 **마지막 파일**과 **변경사항만 기록**함 이전 파일은 저장 x



### 중앙 집중식 VS 분산식

**중앙 집중식** : 중앙 서버에 저장, 파일을 중앙서버에서 가져와 다시 중앙에 업로드

**분산식** : 여러 개의 복제된 저장소에 저장 및 관리, 각자가 관리하기 때문에 협업에 특화

장점

- 중앙서버에 의존하지 않고 동시에 다양한 작업
- 중앙형보다 백업과 복구가 용이



### git의 3가지 영역

- Working Derectory = Working tree
  - 실제 작업중인 파일들이 위치하는 영역(바로 repository에 저장 불가)
- Staging Area
  - 다음 버전에 포함시킬 파일들을 선택적으로 추가하거나 삭제할 수 잇는 중간 준비 영역(대기공간)
-  Repository
  - 버전 이력들과 파일들이 영구적으로 저장되는 영역, 모든 버전과 변경 이력이 기록

**Commit** : 버전, 변경된 파일들을 저장하는 행위, 사진찍듯이 기록하여 snapshot이라고도 함



### 명령어 정리

**`git status` **: 현재 상태를 출력해줌. 현재 파일목록을 찍는 **`ls`**와 같이 많이 사용되는 명령어

`git init` : 로컬 저장소 설정 (초기화) , git의 버전관리를 시작(git 시작할 때마다) 

- local - 온라인 상에 있지 않은 내가 직접 조작하는 환경 vs romote - 원격 환경
- git의 버전관리를 시작할 디렉토리에서 진행
- 명령어 입력하면 오른쪽에 (master) 뜸
- git 로컬 저장소 내에 또다른 git 로컬 저장소를 만들지 말것 - 만들면 지우기

`git add` : **변경사항이 있는** 파일을 staging area에 추가 ( 파일의 생성 자체도 변경사항임)

- `git add 파일이름`
- `git add .` 현재 위치에 있는 파일들을 한번에 올리고 싶으면 .

`git commit` : staging area에 있는 파일들을 저장소에 기록, 버전을 생성하고 변경 이력을 남김

- `git commit -m "message"` : -m은 message의 줄임말, message 에는 변경행위를 적는게 좋음
- 버전을 기록하려면 책임자를 입력해야함(최초 1회)
- `global ` 사용자 등록
  - `git config --global user.email "@gmail.com"`
  - `git config --global user.name "name"`

- `global` 한 컴퓨터 전체의 설정 vs `local`

`git log` : 버전 목록 확인

`git log --oneline` : 한줄로 볼 수 있는 명령어

`git congig --global -l` global 사용자 정보 나오게 하기

**tip** 

- 화면 짤렸을 때 enter 누른다음 q 누르기
- 디렉토리(폴더)는 status에 뜨지 않음
- 자리바꿨을 때 window 자격 증명 git 삭제하기
- visual studio code 실행 자체를 디렉토리 안에서 열어야 터미널 귀찮게 안들어가도됨

