# CLI 명령어 정리

가장 중요한 것은 **현재 위치**

현재디렉토리 ``.``

이전 디렉토리 ``..``

파일 생성 명령어 `touch`

ex) `touch a .txt`
-> a라는 텍스트 파일 생성

폴더 생성 `mkdir`(make directory)

현재 공간에 있는 파일 찾는 명령어 `ls`

폴더내의 파일에 들어가는 명령어
`cd 파일명`

폴더 밖으로 나가기
`cd ..`

폴더나 파일을 열기
`start`

ex) ```start a.txt```

지우기 명령어 `rm`
ex) `rm a.txt`

디렉토리 삭제 `rm -r`
ex) `rm -r sample`

**절대경로** : root 디렉토리부터 목적지저마지 거치는 모든 경로를 전부 작성한 것

`C:\Users\SSAFY\Desktop\새 폴더` 

**상대경로** : 현재 작업하고 있는 디렉토리를 기준으로 계산된 상대적 위치

현재 위치가 `C:\Users`일 때 
`SSAFY\Desktop\새 폴더`

창이 너무 더러울대 때 청소
`clear`

직전 명령어 기억하는거 - 위 방향키

출력 `echo "hello world"`

현재 위치 출력 `pwd`

현재 파일 리스트 출력 `ls`

문서 내용 출력 `cat 파일명`

log  파일의 마지막 5번째 문장을 출력하기

`tail -5 access.log`

`tmp/files` 이라는 이름의 디렉토리 만들기

*Hint: The directory “*`*tmp/*`*" doesn't exist, with one command you need to create both "*`*tmp/*`*" and "*`*tmp/files*`*"*

```
mkdir -p tmp/files
```

`tmp/files` 안에 `take-the-command-challenge` 복사해오기

```
cp take-the-command-challenge tmp/files/take-the-command-challenge
```

`cp` 복사하는 함수

디렉토리 `tmp/files`에  `take-the-command-challenge` 옮기기

```
mv take-the-command-challenge tmp/files/take-the-command-challenge
```

`mv` 이동하는 함수