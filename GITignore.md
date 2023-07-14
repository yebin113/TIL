# GIT ignore

git에 올리면 안되는 파일들

git 에서 특정 파일이나 디렉토리를 추적하지 않도록 설정하는데 사용되는 텍스트 파일

대표적인것 

- API 키

예시

1. `.gitignore` 파일 생성(파일명 앞에 '.' 입력, 확장자 없음
2.  a,b 텍스트파일 생성
3. `.gitignore` 파일 안에 `a.txt` 작성
4. `git init`
5. `git status`

홈페이지 : **`gitignore.io`** -> gitignore 파일 자동분류해줌



작업 시작 전에  **`gitignore.io`**  검색해서 내 해당 상태를 추가하여 파일 목록 복붙해서 저장해두고 작업시작하는 게 편함

**`README`**와 같이 최상단에 두면 됨(파일속에 위치 x)

`.gitignore` 자체도 `push`대상