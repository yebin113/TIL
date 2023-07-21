# 0721 관통프로젝트 1일차



## 관통 프로젝트란? 

- 강의 시간에 배운 내용을 모두 포함(관통) 
- 추가적인 내용 학습 
- 프로젝트 도전!



### 진행 방식

1. 프로젝트 목표 소개
2. 이론 설명
3. 강사님들과 함께 실습 진행 (라이브는 여기까지)
4. 도전 과제 진행

- 도전 과제는 두 개의 버전이 존재 
- PJT01 --> PJTO2 --> PJTO3 --> PJTO4 --> **PJTO5 -->  ... > PJTO9 -- > PJT10 **(1학기 마지막)
  - 4번째까지는 변경 가능 5번째부터 **변경 불가능**
- 버전 1: **금융 데이터를 활용**한 금융 상품 비교 애플리케이션
  - 사용자의 금융 상품을 비교하고 사용자에게 알맞은 금융 상품을 추천하는 기능
  - 마이뱅크
  - Bankbook
- 버전 2: **Open API와 외부 데이터를 활용**한 영화 추천 서비스 
  - 왓챠
  - 넷플릭스



### 교안 표기

- Youtube에서는 두 가지 프로젝트를 모두 설명드리기에, 다음과 같이 교안에 구분하여 표기합니다

  | 두 서비스 모두를 위한 배경지식 | 금융상품비교 서비스관련 | 영화추천서비스 관련페이지 |
  | ------------------------------ | ----------------------- | ------------------------- |
  | 금융상품비교                   | 금융상품비교            |                           |
  | 영화추천 서비스                |                         | 영화추천 서비스           |

  

### 프로젝트를 위한 배경지식

1. 목표
2. API 이해하기
3. 날씨 데이터 수집

#### 실습(라이브) 목표 

- 파이썬으로, **인터넷에 있는 날씨 정보**를 가져와, 내가 원하는 정보만 출력 

#### 날씨 정보 

- 실습 프로젝트를 진행하기 위해선 날씨 데이터가 있어야 합니다. 

- 그러나... 직접 데이터를 모으기엔 너무 어렵습니다! 

  

- 간단하게, 인터넷에 있는 데이터를 가져오면 됩니다. 

  - 데이터를 가져오는 방법을 이해하기 위해서 반드시 알아야 할 전문용어들이 있습니다.

### 전문용어 이해하기

| 클라이언트                  | 서버                                                  |
| --------------------------- | ----------------------------------------------------- |
| 부탁하는 역할               | 부탁을 받으면 처리해주거나, 원하는 값을 돌려주는 역할 |
| 너가 가진 정보 줘. --> 서버 | 클라이언트<-- 원하는 정보 줄께                        |

![](C:\Users\SSAFY\Downloads\0721_1.PNG)



- 우리가 네이버 홈페이지에 접속하는 건 다음과 같이 표현할 수 있음
  - 네이버 주소를 입력하면 익히 알고 있는 네이버 메인 화면을 달라고 요청
  - 서버는 클라이언트가 요청한 네이버 메인 화면을 돌려줌

![](C:\Users\SSAFY\Downloads\0721_2.PNG)



- 이번 프로젝트에서는 날씨 정보가 필요합니다. 
  - 날씨 정보를 가지고 있는 서버가 있습니다. 
  - 해당 서버에 날씨 정보를 달라고 요청하면 됩니다.

![](C:\Users\SSAFY\Downloads\0721_3.PNG)



#### 1. 클라이언트가 정보를 달라고 요청한다

#### 2. 서버는 클라이언트의 요청에 따라 원하는 정보를 돌려준다



클라이언트는 어떻게 요청을 보낼 수 있을까요? -> **request**



#### 클라이언트가 서버에 요청하는 두 가지 방법

1. 웹 브라우저(크롬)을 켜서 주소창에 주소(URL)를 입력한다.



https://fakestoreapi.com/carts 입력해보기 (개발용)

``````
# 결과
[{"id":1,"userId":1,"date":"2020-03-02T00:00:00.000Z","products":[{"productId":1,"quantity":4},{"productId":2,"quantity":1},{"productId":3,"quantity":6}],"__v":0},{"id":2,"userId":1,"date":"2020-01-02T00:00:00.000Z","products":[{"productId":2,"quantity":4},{"productId":1,"quantity":10},{"productId":5,"quantity":2}],"__v":0},{"id":3,"userId":2,"date":"2020-03-01T00:00:00.000Z","products":[{"productId":1,"quantity":2},{"productId":9,"quantity":1}],"__v":0},{"id":4,"userId":3,"date":"2020-01-01T00:00:00.000Z","products":[{"productId":1,"quantity":4}],"__v":0},{"id":5,"userId":3,"date":"2020-03-01T00:00:00.000Z","products":[{"productId":7,"quantity":1},{"productId":8,"quantity":1}],"__v":0},{"id":6,"userId":4,"date":"2020-03-01T00:00:00.000Z","products":[{"productId":10,"quantity":2},{"productId":12,"quantity":3}],"__v":0},{"id":7,"userId":8,"date":"2020-03-01T00:00:00.000Z","products":[{"productId":18,"quantity":1}],"__v":0}]
``````



2. 서버에 정보를 요청하는 파이썬 코드를 작성한다. (request)

   1. 터미널 오픈

   2. `pip install requests`

   3. ```py
      import requests
      url = 'https://fakestoreapi.com/carts'
      response = requests.get(url)
      print(response)	#<Response [200]>
      ```

   4. 파일 타입 바꿔주기

      ```py
      import requests
      url = 'https://fakestoreapi.com/carts'
      response = requests.get(url).json()
      print(response)
      ```



#### url

- 요청을 보내는 서버의 주소

#### request.get(url)

- 해당 서버(url)에 데이터를 달라고 요청을 보내는 함수

#### .json()

- 내부의 데이터를  JSON(파이썬의 딕셔너리와 비슷함) 형태로 변환해주는 함수





### 서버는 어떻게 요청을 해석할까 

- 서버는 **어떻게 요청을 이해하고 데이터를 반환**할 수 있을까요?

- 서버에 요청을 보내는 클라이언트는 매우 다양
  - 클라이언트들은 각자 다른 방식으로 요청을 보낼 것
- 서버가 어떻게 모두 해석할 수 있을까? -> API가 해줌



### API

- 클라이언트가 원하는 기능을 수행하기 위해서 서버 측에 만들어 놓은 프로그램
  - 기능 예시: 데이터 저장, 조회, 수정, 삭제 등등
- 클라이언트와 서버 사이의 중간다리 역할을 해줌
- 서버 측에 특정 주소로 요청이 오면 정해진 기능을 수행하는 API 를 미리 만들어 둡니다. 
  - 클라이언트는 서버가 미리 만들어 놓은 주소로 요청을 보냅니다.

![](C:\Users\SSAFY\Downloads\0721_4.PNG)



### 날씨정보를 제공해주는 API

- 날씨 정보를 수집하기 위해서는 두 가지를 찾아야 합니다.
  - 날씨 정보를 가지고 있는 서버 
  - 해당 서버가 제공하는 API



### 오픈 API

- 외부에서 사용할 수 있도록 **무료로 개방된 api **
- 사용법은 공식 문서(Docs) 에 명시되어 있습니다.
- 프로젝트에서 사용되는 API
  - OpenWeatherMap APl : 기상 데이터 및 날씨 정보를 제공하는 오픈 API 
  - 금융상품통합비교공시 API: 금융감독원에서 제공하는 금융 상품 정보를 제공하는 오픈 API



### 오픈 API 특징 및 주의사항 



#### 악성 사용자가 100만 개의 계정을 생성해 API 에 요청을 보내는 상황

- 너무 많은 계정에서 동시에 요청을 보내면 서버가 견디지 못함

- 이러한 문제점을 해결하기 위해 오픈 API 는 **API KEY** 를 활용하여 사용자를 확인

  - 사용자 인증 혹은 회원가입을 하면 서버에서 API KEY 를 발급해 줍니다. 

  - 서버에 요청할 때 마다 해당 API KEY 를 함께 보내 정상적인 사용자인 것을 확인 받습니다.
  - 

#### API KEY 를 가지고 있는 악성 사용자가 1초에 100만 개의 요청을 보내는 상황

- 서버가 견디지 못하여 정상적인 서비스가 불가능합니다. 

- 일부 오픈 AP 는 **사용량이 제한**되어 있습니다
  - 공식 문서의 일일 및 월간 사용량 제한을 반드시 확인하여야 합니다
  - [주의] **사용량이 초과될 경우 요금이 청구**될 수 있습니다





### 프로젝트 미션 정리 

- 파이썬으로 **날씨 정보를 제공해주는 서버의 URL** 을 이용하여 날씨 정보를 가져옵니다



#### 날씨 데이터 수집

#### API가 사용하는 데이터 형식 - JSON

- Javascript Object Notation 의 약자. 직역하면 '자바스크립트 객체 표기법' . 
- 데이터를 저장하거나 전송할 때 많이 사용되는 경량의 텍스트 기반의 **데이터 형식**
- 통신 방법이나 프로그래밍 문법이 아니라 단순히 데이터를 표현하는 표현 방법 중 하나

- 특징
  - 데이터는 중괄호({ }) 로 둘러싸인 키-값 쌍의 집합으로 표현됨 ( 딕셔너리와 유사 ) 
  - 키 = 문자열 / 값 = 다양한 데이터 유형을 가질 수 있다 
  - 값은 쉼표(,)로 구분됨 (여러 데이터가 온다면 리스트 형태로 옴)

```py
# 예시
{
    "name". "김싸피",
    "age": 28 ,
    "city": "서울 캠퍼스",
    "hobbies" : [
        "공부하기",
    	"복습하기"
    ],
    "isStudent":true
}
```





#### JSON - python 예제 

- 파이썬은 JSON 을 활용하는 기능을 가지고 있습니다. 
- 참고
  - 파싱(Parsing): 데이터를 의미 있는 구조로 분석하고 해석하는 과정 
  - json.loads(): JSON 형식의 문자열을 파싱하여 python Dictionary 로 변환

#### Openweathermap API

- 기상 데이터 및 날씨 정보를 제공하는 오픈 API 
- 전세계 날씨 데이터를 가져와 날씨, 일일 및 시간 별 예보 등 다양한 정보를 얻을 수 있습니다. 
- API 사용량 제한 
  - 60 calls/minute (1초에 두번이상 하지 마)
  - 1,000,000 calls/month

#### 1. API KEY 발급

- [Openweathermap API][https://openweathermap.org/current]

  ```py
  API_KEY = 'dd8eae0d0fbcf9e4e14e58c924202f6e'
  ```



#### 2. 서울의 날씨 데이터 받아오기

```py
import requests

API_KEY = 'dd8eae0d0fbcf9e4e14e58c924202f6e'
lat = 37.56
lon = 126.97

url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}'

reponse = requests.get(url).json()
print(reponse)
"""
{'coord': {'lon': 126.97, 'lat': 37.56},
 'weather': [{'id': 721,
   'main': 'Haze',
   'description': 'haze',
   'icon': '50d'}],
 'base': 'stations',
 'main': {'temp': 303.49,
  'feels_like': 308.02,
  'temp_min': 302.93,
  'temp_max': 304.03,
  'pressure': 1012,
  'humidity': 66},
 'visibility': 6000,
 'wind': {'speed': 1.54, 'deg': 170},
 'clouds': {'all': 20},
 'dt': 1689903662,
 'sys': {'type': 1,
  'id': 8105,
  'country': 'KR',
  'sunrise': 1689884785,
  'sunset': 1689936611},
 'timezone': 32400,
 'id': 1835848,
 'name': 'Seoul',
 'cod': 200}
 """
```

```py
# 또는
import requests

API_KEY = 'dd8eae0d0fbcf9e4e14e58c924202f6e'
city_name = 'Seoul'

url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}'

reponse = requests.get(url).json()
print(reponse)
```



#### 2. 서울의 현재 날씨 중 온도만 출력하기 

- 기본적으로 캘빈(K) 온도를 반환합니다. 

- 섭씨 온도 = (캘빈 온도 - 273.15) 로 계산할 수 있습니다. 

  ```py
  import requests
  
  API_KEY = 'dd8eae0d0fbcf9e4e14e58c924202f6e'
  city_name = 'Seoul'
  
  url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}'
  
  reponse = requests.get(url).json()
  temp = reponse['main']['temp']	
  # 딕셔너리의 'main' 키 속의 딕셔너리 중 'temp' value 값을 출력
  temp -= 273.15
  # 섭씨 온도 = (캘빈 온도 - 273.15) 로 계산
  print(temp)
  # 30.340000000000032
  ```

  

#### 2. 서울의 현재 날씨에 대한 설명(description) 데이터만 출력하기 

- 출력 결과 '날씨 설명: clear sky 

- Json 형태의 데이터를 분석하여 원하는 부분만 가져오도록 구성합니다

  ```py
  import requests
  
  API_KEY = 'dd8eae0d0fbcf9e4e14e58c924202f6e'
  city_name = 'Seoul'
  
  url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}'
  
  reponse = requests.get(url).json()
  description = reponse['weather'][0]['description']	
  # 딕셔너리의 'weather' 키 속의 딕셔너리 중 'description' value 값을 출력
  print(description)
  # 'haze'
  ```

  



#### 관통 버전 1 

API_KEY = '**811c53c596a315d34cc689103d22db9d**'

- 프로젝트명: 파이썬을 활용한 API 데이터 수집 
- 목표
  - 파이썬으로 정기 예금 데이터 수집 및 미션 수행 
- 특징
  - 외부 서버를 활용한 데이터 수집
  - 요구사항에 맞게 JSON 형태 데이터 가공

#### 관통 버전2

- 프로젝트명 : 파이썬을 활용한 데이터 수집 1
- 목표
  - 파이썬으로 도서 및 아티스트 데이터 가공 및 미션 수행 
- 특징
  - 샘플 데이터 제공
  - 요구사항에 맞게 JSON 형태 데이터 가공



## [Jupiter 노트북][https://married-spot-253.notion.site/Jupyter-Notebook-63999a09c2874ce096e2e125e2b77c84#1abdc01d43834fd1a44b291773532229]

shut down - ctrl c 연타