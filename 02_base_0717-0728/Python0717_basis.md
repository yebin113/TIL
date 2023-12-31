# 0717 Python 기초 1일차

### 프로그래밍이란? 

프로그램 - 명령어들의 집합

ex) 프로그램 작성 - 친구에게 집으로 오는 길을 적어주는 것

프로그램 실행 - 적어준 길을 순서대로 따라가는 것

**핵심** - **문제를 해결**하기 위해 사용함



### **python**을 사용하는 이유

- 간결하고 읽기 쉬운 문법
- 다양한 응용분야 (데이터 분석, 인공지능, 웹개발, 자동화)

프로그래밍 언어 : 사람이 기계어를 직접 작성할 수 x. 사람이 쓰는 말로 이루어진 규칙과 문법이 있는 언어

인터프리터 (컴파일러): 프로그래밍 언어를 운영체제가 이해하는 언어로 바꿔주는 과정(번역기의 역할)



### python  실행 방법

- **shell** 이라는 프로그램으로 한번에 한줄씩 입력해서 실행
  - 잘 사용 되지 않음
  - 나가고 싶을때  `exit()` 사용
- 확장자가 .py인 파일에 작성된 파이썬 프로그램을 실행 (주로 사용됨)

---

### 표현식과 값

**표현식(expression)**  

- 값 변수 연산자 등을 조합하여 계산되고 결과를 내는 코드 구조

**평가** 

- 표현식이나 문장을 실행하여 그 결과를 계산하고 값을 결정하는 과정 (표현식이나 문장을 **순차적으로 평가**하여 프로그램의 동작을 결정)

**문장 **

- 실행이 가능한 동작을 기술하는 코드(조건문, 반복문,함수 정의 등)

- 표현식이 문장을 포함함(보통 여러개의 표현식이 문장이라 불림)

### 타입과 연산자

- 값이 어떤 종류의 데이터인지, 어떻게 해석되고 처리되어야 하는지를 정의
- 2가지 요소로 이루어짐 (**값**, 값에 적용할 수 있는 **연산**)
- **Numeric Type**
  - int(정수)
  - float(실수)
  - complex(복소수)
- **Sequence type(순서가 존재)**
  - list
  - tuple
  - range
- Text Sequence Type
  - str(문자열)
- Set Type
  - set
- Mapping Type
  - dict
- 기타

**연산자**

- 음수부호,뺄셈 (-) , 덧셈 (+), 곱셉(*), 나눗셈(/), 정수나눗셈(몫)(//), 나머지(%), 지수 (**)

**연산자 우선순위**

- ** 지수
- 음수 부호
- 곱셈, 나눗셈, 정수 나눗셈, 나머지
- 덧셈, 뺄셈

**괄호를 잘 쓰는 것이 중요함**

---

### 변수,값 그리고 메모리

- 거리에 집 주소가 있듯, 메모리의 모든 위치에는 그 위치를 고유하게 식별하는 메모리 주소가 존재
- https://pythontutor.com/render.html#mode=display (파이썬 시각화 site)

**변수(식별자)**

- 값을 참조하는 이름
- 값을 담는 도구
- 메모리 주소의 닉네임 같은 의미

**객체**

- 타입을 갖는 메모리 주소 내 할당된 값
- "값이 들어있는 상자"

**변수명 규칙**

- 영문 알파벳, 언더스코어(_), 숫자로 구성
- 숫자로 시작할 수 없음
- 대소문자 구분함
- 언더스코어로 시작할 수 없음
- 내장함수와 같은 이름 사용 불가(`for`, `and`, `sum`, `list`)

**할당문**

1. 할당 연산자 오른쪽에 있는 표현식을 평가해서 값(메모리 주소)을 생성
2. 값의 메모리 주소를 '=' 왼쪽에 있는 변수에 저장
   - 존재하지 않는 변수라면 -> 새 변수를 생성
   - 기존에 존재했던 변수라면 -> 기존 변수를 재사용해서 변수에 들어있는 메모리 주소를 변경

---

### 읽기 좋은 코드

**Style Guide**

- 코드의 일관성과 가독성을 향상시키기 위한 규칙과 권장 사항들의 모음

#### Python Style Guide

- 변수명은 무엇을 위한 변수인지 **직관적인 이름**을 가져야 함

  - ex) 온도와 관련된 변수 - `temperature`
  - `list` 타입이면 `변수명_list` 또는 복수형 변수 이름 사용하는 센스

  - `is`로 시작하는 변수면 값이 `True` 아니면 `False` 로 리턴되는 경우많음
  - 변수가 대문자로 되어있음  -> 상수값으로 사용됨 ex) `SECONDS_PER_MINUTE = 60`

- 공백 4칸을 사용하여 코드블록 **들여쓰기** (중괄호 사용 x 들여쓰기로 문법 조정함)

- 한줄의 길이는 79자로 제한하며, **길어질 경우 줄바꿈**을 사용(역슬래시 \ 사용하여 줄바꿈)

- 문자와 밑줄(_)을 사용하여 함수, 변수, 속성의 이름을 작성

- 함수 정의나 클래스 정의 등의 블록 사이에는 빈 줄을 추가

- 연산자와 할당문 양쪽에 **공백 추가**하면 가독성 좋음

**주석**

- 코드 설명
- 또는 임시로 코드 비활성화 할때
- 코드 문서화
- **한 줄 주석 #**
- **여러 줄 주석 - 드래그해서 ctrl \ **
- 설명할때 사용하는 여러줄 주석 `"""   """`

### 파이썬 visual studio code 실행방법

terminal 키고 `python 파일명.py`