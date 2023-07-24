# TIL

- 자주 찾아보는 기능들 모아놓기

## VS code 단축키

같은 명령어 또 칠때

- 방향키 위

복사하기

- alt + shift + 아래 화살표

같은 내용 한번에 적기 

- alt + ctrl + 아래 화살표 (멀티 커서) -> 위치가 좀 다를 경우에는 alt 누르고 클릭해서 적기

변수명 한번에 바꿀때

- 원하는 내용이나 변수 클릭해서 블럭으로 잡고 ctrl + d

원하는 곳으로 코드 옮기기

- alt 누른채로 화살표로 이동

### Escape sequence

| 예약문자 |    기능     |
| :------: | :---------: |
|    \n    |   줄바꿈    |
|    \t    |     탭      |
|   \\\    |  백슬래시   |
|   \\'    | 작은 따옴표 |
|   \\"    |  큰 따옴표  |

### f - string

- `print(f'이름 : {name}')`

- **print 함수가 아니여도 사용 가능함!!** 일반 url에 사용 가능

  `f'https://jsonplaceholder.typicode.com/users/{i}'`

- f - string  Advanced
  - 오른쪽 정렬 `print(f'이름 : {name:>10}')`
  - 가운데 정렬 `print(f'이름 : {name:^10}')`
  - 소수점 조절`print(f'{3.142859:.4f}')`

### Dict(딕셔너리)




- **딕셔너리 안의 딕셔너리** 에 접근 하고 싶을때
  
  - `dict_1[n][m]`  - dict_1의 n 번째 요소인 딕셔너리 안의 m번째 요소
  
- 키와 value에 접근하고 싶으면 

  ```py
  for key in dict:
      print(key,key[i])
  ```

- key - value 쌍으로 이루어진 순서와 중복이 없는 변경 가능한 자료형

- key는 변경 불가능한 자료형만 사용가능(str, int, float, tuple, range ...)

- value 는 모든 자료형 사용 가능

- key를 통해 value 에 접근

  ```python
  my_dict = {'apple':12, 'list':[1,2,3]}
  
  print(my_dict['apple']) #12
  print(my_dict['list'])  #[1,2,3]
  
  #값 변경
  my_dict['apple'] = 100
  print(my_dict) 			#{'apple':100, 'list':[1,2,3]}
  ```

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

### 단축평가 (시험문제 스타일)

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


#### 위치인자

- 함수 호출시 인자의 위치에 따라 전달되는 인자

- **위치인자는 함수호출시 반드시 값을 전달해야함**

  ```python
  def greet (name, age):
  	print(f'안녕하세요, {name}님! {age}살이시군요.')
  greet('Alice', 25) # 안녕하세요, Alice님! 25살이시군요.
  ```

  

#### 기본인자

- 함수 정의에서 매개변수에 기본 값을 할당하는 것

- 함수 호출시 인자를 전달하지 않으면, 기본값이 매개변수에 할당됨

  ```py
  def greet (name, age = 30):
  	print(f'안녕하세요, {name}님! {age}살이시군요. ')
  greet('Bob') # 안녕하세요, B0b님! 30살이시군요.
  greet ('Charlie',40) # 안녕하세요, Charlie님! 40살이시군요.
  ```

  

#### 키워드 인자

- 함수 호출시 이름과 함께 값을 전달

- 매개변수와 인자를 일치시키지 않고, 특정 매개변수에 값을 할당할 수 있음

- 인자의 **순서는 중요하지 않으며, 인자의 이름을 명시**하여 전달

- **단, 호출시 키워드 인자는 위치 인자 뒤에 위치해야 함**

  ```py
  def greeting(name,age):
      print(f'안녕,{name}.{age}!!')
  greeting('Alice',25) #안녕, Alice, 25!!
  greeting(25,'Alice') #안녕, 25, Alice!!
  greeting(age=25,name='Alice') #안녕, Alice, 25!!
  greeting(age=25,'Dave') #Error 키워드 인자는 위치 인자 뒤에 위치해야 함
  
  ```

#### Arbitrary Argument Lists(임의의 인자 목록)

- 정해지지 않은 개수의 인자를 처리하는 인자

- 함수 정의 시 매개변수 앞에 '*'를 붙여 사용하며, 여러개의 인자를 **tuple로 처리**

  ```py
  def cal(*args):
      print(args)	
  
  cal(1,2,3,4,5)		#(1,2,3,4,5) 튜플로 출력
  ```

  

#### Arbitrary Ketword Argument Lists(임의의 키워드 인자 목록)

- 정해지지 않은 개수의 키워드 인자를 처리하는 인자
- 함수 정의 시 매개변수 앞에 '*'를 붙여 사용하며, 여러개의 인자를 **dictionary 로 묶어 처리**

```py
def print_info(**kwargs):
    print(kwargs)	

print_info(name='Eve',age=30)	#{'name':'Eve','age':30} 딕셔너리로 출력
```

#### map

- `map(function(함수), iterable(반복이 가능한 객체))`

- 순회 가능한 데이터 구조(문자열, 리스트 등등)의 모든 요소에 function을 적용해줌

- 반복문과 동일

- 가장 많이 쓰는 코드 `map(int,input().split())`

  ```py
  numbers = [1,2,3]
  result = map(str,numbers) #모든 numbers를 문자열로 바꿔줌
  
  print(result)		#<map object at 0x00001~~~
  print(list(result))	#['1','2','3']
  ```

- 장점 : 함수를 인자로 받을 수 있음(내가 쓴 함수도 가능)

- 여러개의 리스트를 받아서 딕셔너리화 하고 또 각각의 인자를 받아 리스트로 만들기

  `list(map(함수,list1,list2,list3))`

  **조건 : 만든 함수의 매개변수와 인자가 갯수가 동일해야 함**

### zip

- zip(*iterables)

- 같은 인덱스의 iterable을 묶어서 출력

- 임의의 iterable을 모아 튜플을 원소로 하는 zip object를 반환

  ```py
  girls = ['jane','ashley']
  boys = ['peter','jay']
  pair zip(girls,boys)
  
  print(pair)		#<zip object at 0x ~~~
  print(list(pair)) #[('jane','peter'),('ashley','jay')]
  ```

- 두개의 리스트를 딕셔너리로 변환할 수 도 있음

  ```python
  key = ['a','b','c']
  values = [1,2,3]
  my_dict = dict(zip(keys,values))
  print(my_dict) # {'a':1,'b':2,'c':2}
  ```



#### lambda

- map + lambda 일때 응용

```py
numbers=[1,2,3,4,5]
result = map(lambda x:x*2,numbers)
print(result) #[2,4,6,8,10]
```



## Swea 팁

```python
# tip 입력 받아오는 함수
import sys
sys.stdin = open('input.txt')
```



## pip request

```py
import requests

API_URL = f'https://jsonplaceholder.typicode.com/users/{i}'
# API 요청
response = requests.get(API_URL)
# JSON -> dict 데이터 변환
parsed_data = response.json()
```

### 자주 쓰이는 메서드
| 메서드                         | 설명                                       |
| ------------------------------ | ------------------------------------------ |
| `s. split(sep:=None, maxsplit=-1)` | 공백이나 특정 문자를 기준으로 분리 |
`'separator'.join([iterable])`|구분자로 iterable을 합침|
`L.append(x)`|리스트 마지막에 항목 x를 추가|
`L.pop(i)`|리스트의 지정한 인덱스의 항목을 제거하고 반환, 작성하지 않을 경우 마지막 항목 제거|
| `L.reverse()` | 리스트를 거꾸로 나열                                     |
| `L.sort()`    | 리스트를 정렬(매개변수 이용가능) - 원본을 바꿔서 반환값x |


#### `s. split(sep:=None, maxsplit=-1)`

- 지정한 문자를 구분자로 문자열을 분리하여 문자열의 리스트로 반환

```py
text = 'Hello, world'
words = text.split(',')
print(words)	#['Hello', ' world']
```



#### `'separator'.join([iterable])`

- iterable 요소들을 원래의 문자열을 구분자로 이용하여 하나의 문자열로 연결
- split의 반대 함수라고 볼 수 있음

```py
words = ['Hello', ' world']
text = '-'.join(words)
print(text)		#Hello- world
```


#### `L.append(x)` vs `L.extend(x)` vs`L.insert(i,x)`

- append

```py
numbers = [1,2,3]
numbers2 = [4,5,6]

numbers.append(numbers2)
print(numbers)		#[1, 2, 3, [4, 5, 6]]
```

- extend

```py
numbers = [1,2,3]
numbers2 = 4

numbers.extend([numbers2])
print(numbers)		#[1, 2, 3, 4]

# 그냥 요소 한개만 넣으면 extend 에서 에러.. type error iterable 하지 않음
# 따라서 리스트로 타입 변환 해주기!

```

- insert

```py
numbers = [1,2,3]
numbers.insert(1,5)

print(numbers)      #[1, 5, 2, 3]
```

#### `L.pop(i)` - 중요 (append의 반대)

- 리스트의 지정한 인덱스의 항목을 제거하고 반환, 작성하지 않을 경우 마지막 항목 제거

```py
numbers = [1,2,3]
item = numbers.pop()
item1 = numbers.pop(0)

print(item)      # 3
print(item1)    # 1
print(numbers)  # [2]
```



#### `L.sort()` vs`L.reverse()`

```py
numbers = [3,2,1]
numbers.sort()
print(numbers)      #[1, 2, 3]

numbers.sort(reverse=True)
print(numbers)      #[3, 2, 1]
# reverse는 정렬이 아니라 순서를 거꾸로 변경하는 것일 뿐
```

```py
numbers = [3,2,1]

# sort 메서드
print(numbers.sort())      # None - 반환값이 없음
# sorted 함수
print(sorted(numbers))     # [1, 2, 3] - 반환값이 있다(원본이 안바뀜)
```

#### sort()와 같이 반환값이 없는 함수는 바로 출력하면 None 출력

- return이나 print에 메서드 바로 쓰지 말고 함수 사용 후 변수이름만 적을 것

예시

```py
numbers = [3,2,1]

print(numbers.sort())      # None - 반환값이 없음

numbers.sort() 
print(numbers)		#[1,2,3]
```



