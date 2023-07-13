# Remote Repository(원격저장소)

**원격저장소** : 코드와 버전 관리 이력을 **온라인 상의 특정위치에 저장**하여 여러 개발자가 **협업**하고 코드를 공유할 수 있는 저장공간

**git**과 **github**의 직접적인 연관? git을 공유한다는 의미의 이름임

**README** : 디렉터리나 압축 파일에 포함된 기타 파일에 대한 정보를 포함하고 있으며, 일반적으로 컴퓨터 소프트웨어와 함께 배포된다

`git remote add origin 주소(https://github.com/yebin113/gitpractice0713)` : 로컬 저장소에 원격 저장소 주소 추가

`git remote remove origin` : 원격 저장소 주소 지우기

`git push origin master` :  origin이라는 원격 저장소에 master을 push

파일에 변경사항이 발생했을 때 `add` 후 `commit` 한 뒤 다시 `push` 해야 업데이트 됨

자리바꿨을 때 window 자격 증명 git 삭제하기

`git clone 주소(https://github.com/yebin113/gitpractice0713) `  :원격 저장소에서 전체 파일을 복제해오는것

`git remote set-url origin 새 주소` : push 하고 싶은 **새 주소로 변경**하고 싶을 때

`git pull` : 원격저장소에서 변경 사항만 복제해옴 (복제할 변경사항이 있는 파일 해당 폴더로 이동해야함 `cd gitpractice0713`)



### git 에 파일 push하고 싶을때

1. `git init`
2. ``touch 파일명`
3. 파일수정
4. `git add 파일명`
5. `git commit -m "first commit"`
6. `git remote add origin 주소`
7. `get push origin master`

### clone 다운받아서 고치고 싶을때

1. `git clone 주소`

2. `cd 디렉토리`

3. 파일 수정

4. `git add 파일명`

5. `git commit -m "message"`

6. `git push origin master`