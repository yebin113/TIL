# 0718 Python 기초 2일차

### Data type

- 값의 종류와 그 값에 적용 가능한 연산과 동작을 결정하는 속성
- 값들을 구분하고 어떻게 다뤄야 하는지 알수 있음
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
  - Boolean
  - None
  - functions

---

### int(정수형)

- **정수를 표현**하는 자료형
- 진수표현 가능 - 앞에 붙이면 해당 진수형태로 출력됨
  - 2진수 : `print(0b10)`
  - 8진수 : `print(0o30)`
  - 16진수 : `print(0x10)`
  - ex) 파이썬 내장 함수로도 존재 ()
    - `print(bin(12))` 
    - `print(oct(12)) `
    - `print(hex(12))`

### float(실수형)

- **실수를 표현**하는 자료형
- 실수에 대한 근삿값을 표기 
- 연산 시 주의 사항
  - 컴퓨터는 2진수를 사용, 사람은 10진법을 사용
  - 0.1은 2진수로 표현하면 0.0001100110011001100....같이 무한대로 반복
  - 따라서 0.1은 실제 0.1이 아니라 가장 근삿값으로 저장됨
  - 이런 오차때문에 예상치 못한 결과가 나타나는 것 - **Floating point rounding error**
- 해결책
  1. 임의의 작은 수 활용
     - a와 b의 차이가 0.00000000001보다 작다면 a = b
  2.  math 모듈 사용
     - `math.isclose(a,b)`
- 지수 표현 방식
  - e 또는 E 사용 (`10^ = e`)

---

## Sequence type(나열)

- 여러개의 값들을 **순서대로 나열**하여 저장하는 자료형
- 특징
  - 순서(Sequence)
    - 값들이 **순서대로 저장**(정렬 X)
  - 인덱싱(Indexing)
    - 각 값이 고유한 번호를 가지고 있으며 인덱스 사용하여 특정 위치의 값을 선택하거나 수정가능, **0부터 시작함**
  - 슬라이싱(Slicing)
    - 인덱스 범위를 조절해 부분적인 값을 추출할 수 있음
  - 길이 (Length)
    - `len()` 함수를 사용하여 저장된 값의 개수를 구할 수 있음
  - 반복(Iteration)
    -  반복문을 사용하여 저장된 값들을 반복적으로 처리할 수 있음

#### str

- 문자들의 순서가 있는 변경 불가능한 시퀀스 자료형

  - 불변이기 때문에 변경하고싶을때는 새로운 문자열을 입력하는 방향으로 코딩해야함

- 작은 따옴표(' ') 또는 큰따옴표(" ") 로 감싸서 표현

- 중첩 따옴표

  - 큰 따옴표를 표기하고 싶을때는 밖을 작은 따옴표로
  - 작은 따옴표를 표기하고 싶을때는 밖을 큰 따옴표로
  - 또는  escape sequence

- Escape sequence

  - 역슬래시 뒤에 특정 문자를 넣어 특수 기능을 함

  - | 예약문자 |    기능     |
    | :------: | :---------: |
    |    \n    |   줄바꿈    |
    |    \t    |     탭      |
    |   \\\    |  백슬래시   |
    |   \\'    | 작은 따옴표 |
    |   \\"    |  큰 따옴표  |

- **String Interpolation**

  - 문자열 내에 변수나 표현식을 삽입하는 방법

  - **f - string** (중요!!!)
    - ```name = 'Yun'```
    - `print(f'이름 : {name}')`
    - 변수의 값이 변동되어도 변수의 값 그대로 나옴
    - f - string  Advanced
      - 오른쪽 정렬 `print(f'이름 : {name:>10}')`
      - 가운데 정렬 `print(f'이름 : {name:^10}')`
      - 소수점 조절`print(f'{3.142859:.4f}')`
  - format 함수 - f string 이전 버전
    - `print('이름 : {}',format{name})`
  - 더 옛날 방법(내가 쓰던거...)
    - `print('이름 : %s',%(name))`

- 문자열 시퀀스 특징

  - `my_str = 'hello'`

  - |             |  h   |  e   |  l   |  l   |  o   |
    | :---------: | :--: | :--: | :--: | :--: | :--: |
    |    index    |  0   |  1   |  2   |  3   |  4   |
    | index(역순) |  -5  |  -4  |  -3  |  -2  |  -1  |

  - 인덱싱

    - `print(my_str[1])  # e`

  - 슬라이싱 ([a:b+1:step] #결과 = a~b(step))

    ```python
    print(my_str[2:4])  # ll
    print(my_str[:3])  # hel
    print(my_str[3:])  # lo
    print(my_str[0:5:2])  # hlo - step 기능
    print(my_str[::-1])  # olleh - step 음수 기능으로 문자열 뒤집기
    ```

  - 길이

    - `print(len(my_str)  # 5`

---

### List

- 여러 개의 값을 순서대로 저장하는 **변경 가능한** 시퀀스 자료형

- 0개 이상의 객체를 포함하며 데이터 목록을 저장

- 대괄호 `[]`로 표기

- 데이터는 어떤 자료형도 저장할 수 있음

  - `my_list_1=[]`
  - `my_list_2=[1,'a',2,'3']`
  - `my_list_3=[1,2,3,'Python',['hello','world','!!!','3']]`

- 중첩된 리스트 접근

  ```python
  my_list_3=[1,2,3,'Python',['hello','world','!!!','3']]
  print(len(my_list_3))  		#5
  print(my_list_3[4][1])  	#world
  print(my_list_3[4][1][3])   #l
  ```

- 리스트에 리스트 할당할 때 주의사항

  - 가변 데이터들은 복사할때 변경사항도 포함됨

```python
list_1 = [1,2,3]
list_2 = list_1

list_1[0] = 100
print(list_2)	#[100,2,3]
```



### Tuple (불변형 리스트)

- 여러 개의 값을 순서대로 저장하는 **변경 불가능한** 시퀀스 자료형
- 0개 이상의 객체를 포함하며 데이터 목록을 저장
- 소괄호 `()`로 표기
- 데이터는 어떤 자료형도 저장할 수 있음
  - `my_tuple_1=()`
  - `my_tuple_2=(1,'a',2,'3')`
  - `my_tuple_3=(1,)` 요소가 1개일 경우 쉼표를 붙여줘야 튜플로 인식, 안붙이면 연산이 됨
- 개발자가 직접 사용하기보다 파이썬 내부 동작에서 주로 사용됨

---

### Range

- `range(n)`

  - 0부터 n-1까지의 숫자의 시퀀스

- `range(n,m)`

  - n부터 m-1까지의 숫자 시퀀스

- 리스트로 형 변환시 데이터 확인가능

  ```python
  my_range_1 = range(5)
  my_range_1 = range(1,10)
  
  print(my_range_1)			#range(0,5)
  print(my_range_2)			#range(1,10)
  
  print(list(my_range_1))		#[0,1,2,3,4]
  print(list(my_range_2))		#[1,2,3,4,5,6,7,8,9]
  ```

---

## Non - sequence Types

- 순서가 없는 변경 가능한 데이터 타입

### Dict(딕셔너리)

- key - value 쌍으로 이루어진 순서와 중복이 없는 변경 가능한 자료형

- key는 변경 불가능한 자료형만 사용가능(str, int, float, tuple, range ...)

- value 는 모든 자료형 사용 가능

- 중괄호 `{}` 로 표기

- key를 통해 value 에 접근

  ```python
  my_dict = {'apple':12, 'list':[1,2,3]}
  
  print(my_dict['apple']) #12
  print(my_dict['list'])  #[1,2,3]
  
  #값 변경
  my_dict['apple'] = 100
  print(my_dict) 			#{'apple':100, 'list':[1,2,3]}
  ```

### Set

- 순서와 중복이 없는 변경 가능한 자료형

  ```python
  my_set_1 = {1,1,1}
  print(my_set_1)		#{1} 중복 x
  ```

- 수학에서의 집합과 동일한 연산처리 가능

  ```python
  my_set_1 = {1,2,3}
  my_set_2 = {3,6,9}
  #합집합
  print(my_set_1 | my_set_2)	#{1,2,3,6,9}
  #차집합
  print(my_set_1 - my_set_2)	#{1,2}
  #교집합
  print(my_set_1 & my_set_2)	#{3}
  ```

- 중괄호 `{}` 로 표기 

  - `my_set = set()`  빈 세트는 set 내장함수 필요함, 딕셔너리와 겹침

---

### None

- 값이 없음을 표현하는 자료형

### Boolean

- True와 False를 표현하는 자료형
- 주로 조건 / 반복문과 함께 사용
- 비교 / 논리 연산의 평가 결과로 사용됨



---

##  Collection

| 컬렉션 | 변경가능 여부 | 나열 여부(순서) |
| :----: | :-----------: | :-------------: |
|  str   |       X       |        O        |
|  list  |       O       |        O        |
| tuple  |       X       |        O        |
|  set   |       O       |        X        |
|  dict  |       O       |        X        |



---

## 형변환



#### 암시적 형변환

- 파이썬이 자동으로 변형하는 것(Boolean 과 Numeric Type 에서만 가능)

  ```python
  print(3 + 5.0)	# 8.0
  print(True + 3)	# 4 // True = 1
  print(True + False) # 1 // False = 0
  ```

  

#### 명시적 형변환

- 개발자가 직접 형변환을 하는 것

- str -> integer : 형식에 맞는 숫자만 가능

- interger -> str : 모두 가능

  ```python
  print(int('1'))			#1
  print(str(1)+'등')	   #1등
  print(float('3.5'))		#3.5
  print(int(3.5))			#3
  print(int('3.5'))		#Error
  ```

  

#### 컬렉션간 형변환

|       | str  |   list   |  tuple   | range |   set    | dict |
| :---: | :--: | :------: | :------: | :---: | :------: | :--: |
|  str  |      |    o     |    o     |   x   |    o     |  x   |
| list  |  o   |          |    o     |   x   |    o     |  x   |
| tuple |  o   |    o     |          |   x   |    o     |  x   |
| range |  o   |    o     |    o     |       |    o     |  x   |
|  set  |  o   |    o     |    o     |   x   |          |  x   |
| dict  |  o   | o(key만) | o(key만) |   x   | o(key만) |      |



---

## 연산자

#### 산술 연산자

| 기호 | 연산자         |
| ---- | -------------- |
| -    | 음수 부호      |
| +    | 덧셈           |
| -    | 뺄셈           |
| *    | 곱셈           |
| /    | 나눗셈         |
| //   | 정수나눗셈     |
| %    | 나머지         |
| **   | 지수(거듭제곱) |



#### 복합 연산자

| 기호 |         |            |
| :--: | :-----: | :--------: |
|  +=  | a += b  | a = a + b  |
|  -=  | a -= b  | a = a - b  |
|  *=  | a *= b  | a = a * b  |
|  /=  | a /= b  | a = a / b  |
| //=  | a //= b | a = a // b |
|  %=  | a %= b  | a = a % b  |
| **=  | a **= b | a = a ** b |

​	

#### 비교 연산자

|   기호   |      내용       |
| :------: | :-------------: |
|    <     |      미만       |
|    <=    |      이하       |
|    >     |      초과       |
|    >=    |      이상       |
|    ==    |    같음(값)     |
|    !=    |  같지 않음(값)  |
|   `is`   |   같음 (주소)   |
| `is not` | 같지 않음(주소) |



#### 논리 연산자

| 기호 |  연산자  | 내용                                                      |
| :--: | :------: | --------------------------------------------------------- |
| and  |  논리곱  | 두개가 모두  True 인 경우에만 전체 표현식을 True 로 평가  |
|  or  |  논리합  | 두개중 하나라도 True 인 경우에 전체 표현식을 True 로 평가 |
| not  | 논리부정 | 단일 피연산자를 부정                                      |

```python
print(True and False)	#False
print(True and False)	#True
print(not True)			#False
print(not 0)			#True
```

- 단축평가

  - 논리 연산에서 두번째 피연산자를 평가하지 않고 결과를 결정하는 동작

    ```python
    vowels = 'aeiou'
    
    print(('a' and 'b') in vowels)
    print(('b' and 'a') in vowels)
    
    print(3 and 5)	#5 3이 0이 아니기 때문에 끝까지 봐야함
    print(3 and 0)	#0 
    print(0 and 3)	#0
    print(0 and 0)	#0
    
    print(5 or 3)	#5 5가 이미 0이 아니기 때문에 결과 나옴
    print(3 or 0)	#3 3이 이미 0이 아니기 때문에 3이 결과
    print(0 or 3)	#3 0이 앞에 나와서 끝까지 봐야함
    print(0 or 0)	#0
    
    ```

    

#### 멤버쉽 연산자

|  기호  | 내용                                                         |
| :----: | ------------------------------------------------------------ |
|   in   | 왼쪽의 피연산자가 오른쪽 피연산자의 시퀀스에 속하는지를 확인 |
| not in | 왼쪽 피연산자가 오른족 피연산자의 시퀀스에 속하지 않는지를 확인 |

```python
word = 'hello'
numbers = [1,2,3,4,5]

print('h' in word)	#True
print('z' in word)	#False

print(4 not in numbers)	#False
print(6 not in numbers)	#True
```



#### 시퀀스형 연산자

| 연산자 | 내용        |
| ------ | ----------- |
| +      | 결합 연산자 |
| *      | 반복 연산자 |

```python
print('A'+'B')	#AB
print('a' * 5)	#aaaaa
print([1,2]+['a','b'])	#[1,2,'a','b']
print([1,2]*2)	#[1,2,1,2]
```



#### 연산자 우선순위

| 우선순위 |        연산자         |         내용          |
| :------: | :-------------------: | :-------------------: |
|   높음   |         `()`          |    소괄호 grouping    |
|          |         `[]`          |   인덱싱, 슬라이싱    |
|          |          **           |       거듭제곱        |
|          |         +, -          | 단향 연산자 양수/음수 |
|          |      `*,/,//,%`       |      산술 연산자      |
|          |         +, -          |      산술 연산자      |
|          | < , <=, >, >=, ==, != |      비교 연산자      |
|          |     `is, is not`      |       객체 비교       |
|          |     `in, not in`      |     멤버십 연산자     |
|          |         `not`         |       논리 부정       |
|          |         `and`         |       논리 AND        |
|   낮음   |         `or`          |        논리 OR        |

