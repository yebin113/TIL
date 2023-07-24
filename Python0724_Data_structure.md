# 데이터 구조

- 여러 데이터를 효과적으로 사용, 관리하기 위한 구조(str, list, dict 등)



### 자료 구조 

- 컴퓨터 공학에서는 '자료 구조' 라고 함

- 각 데이터의 효율적인 저장, 관리를 위한 구조를 나눠 놓은 것

  

### 데이터 구조 활용 

- 문자열, 리스트, 딕셔너리 등 각 데이터 구조의 **메서드**를 호출하여 **다양한 기능을 활용**하기 



## 메서드

- 객체에 속한 함수 -> 객체의 상태를 조작하거나 동작을 수행
-  익숙한 예시 -> append



#### 메서드 특징 

- 메서드는 클래스(class) 내부에 정의되는 함수
- 변경된 값을 저장하는 함수도 있고, 변경된 값을 반환하고 원본은 그대로인 함수도 있음

- 클래스는 파이썬에서 '**타입을 표현하는 방법**'이며 이미 은연중에 사용해왔음 

- 예를 들어 help 함수를 통해 str을 호출해보면 class 였다는 것을 확인 가능

 ※ 클래스는 후반부 OOP 수업에서 자세히



#### 지금 시점에 알아야 할 것

- 메서드는 어딘가(클래스)에 속해 있는 **함수**이며, 각 데이터 타입별로 다양한 기능을 가진 메서드가 존재

### 메서드 호출 방법

- **데이터타입 객체.메서드()**
- 예시

```py
#문자열 메서드 예시
print('hello'.capitalize())	#Hello

#list 메서드 예시
numbers = [1,2,3]
numbers.append(4)

print(numbers)	#[1,2,3,4]
```



## 시퀀스 데이터 구조



### Sequence type(나열)

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

- 문자열 조회/탐색 및 검증 메서드

| 메서드         | 설명                                                         |
| -------------- | ------------------------------------------------------------ |
| `s.find(x)`    | x의 위치를 반환. 중복 있으면 첫 번째 위치, 없으면 -1을 반환  |
| `s.index(x)`   | x의 첫 번째 위치를 반환. 없으면, 오류 발생                   |
| `s.isalpha(x)` | 문자열이 알파벳으로만 이루어져 있는지 확인 *단순 알파벳이 아닌 유니코드 상 Letter (한국어도 포함) - 출력은 True/ False |
| `s.isupper(x)` | 문자열이 모두 대문자로 이루어져 있는지 확인 - 출력은 True/ False |
| `s.islower(x)` | 문자열이 모두 소문자로 이루어져 있는지 확인 - 출력은 True/ False |
| `s.istitle(x)` | 타이틀 형식 여부 - 출력은 True/ False                        |



- 문자열 조작 메서드

| 메서드                             | 설명                                                         |
| ---------------------------------- | ------------------------------------------------------------ |
| `s. replace(old, new[,count])`     | 바꿀 대상 글자를 새로운 글자로 바꿔서 반환                   |
| `s.strip([chars])`                 | 공백이나 특정 문자를 제거                                    |
| `s. split(sep:=None, maxsplit=-1)` | 공백이나 특정 문자를 기준으로 분리                           |
| `'separator'.join([iterable])`     | 구분자로 iterable을 합침                                     |
| `s.capitalize()`                   | 가장 첫 번째 글자를 대문자로 변경                            |
| `s.title()`                        | 문자열 내 띄어쓰기 기준으로 각 단어의 첫 글자는 대문자로, 나머지는 소문자로 변환  ex) `'Hello world'.title() ` -> `'Hello World'` |
| `s.upper() `                       | 모두 대문자로 변경                                           |
| `s.lower ()`                       | 모두 소문자로 변경                                           |
| `s.swapcase()`                     | 대<->소문자 서로 변경                                        |

#### `s. replace(old, new[,count])`  

- 바꿀 대상 글자를 새로운 글자로 바꿔서 반환

- 우리랑 배우던 표기법이랑 다름 (파이썬 문법이 아님) (BNF 표기법 차용) 대괄호는 선택인자를 의미함(사용하지 않아도 됨)

```py
text = 'Hello, world'
new_text = text.replace('world', 'Python')
print(new_text)		#Hello, Python!
```



#### `s.strip([chars])`

- 문자열의 **시작과 끝**에 있는 공백 혹은 지정한 문자를 제거

```py
text = '   Hello, world   '
new_text = text.strip()
print(new_text)	 #Hello, world
```



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





```py
text = 'helLo, woRld!' 
new_text1 = text. capitalize() 
new text2 = text. title() 
new_text3 = text. upper() 
new_text4 = text. swapcase() 

print (new_text1) 	# Hello, world! 
print (new_text2) 	# Hello, world! 
print (new_text3)	# HELLO, WORLD!
print (new_text4)	# HELlO, WOrLD!
```



#### 메서드는 이어서 사용 가능



## 리스트

- 리스트 값 추가 및 삭제 메서드

| 메서드          | 설명                                                         |
| --------------- | ------------------------------------------------------------ |
| `L.append(x)`   | 리스트 마지막에 항목 x를 추가                                |
| `L.extend(x)`   | iterable m의 모든 항목들을 리스트 끝에 추가 (+=과 같은 기능) |
| `L.insert(i,x)` | 리스트 인덱스  i에 항목 X를 삽입                             |
| `L.remove(x)`   | 리스트 가장 왼쪽에 있는 항목(첫 번째) x를 제거 항목이 존재하지 않을 경우, ValueError |
| `L.pop()`       | 리스트 가장 오른쪽에 있는 항목(마지막)을 반환 후 제거        |
| `L.pop(i)`      | 리스트의 인덱스 i에 있는 항목을 반환 후 제거                 |
| `L.clear()`     | 리스트의 모든 항목 삭제                                      |



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
numbers2 = [4,5,6]

numbers.extend(numbers2)
print(numbers)		#[1, 2, 3, 4, 5, 6]
```

- insert

```py
numbers = [1,2,3]
numbers.insert(1,5)

print(numbers)      #[1, 5, 2, 3]
```



#### `L.remove(x)`

- 리스트에서 첫번째로 일치하는 항목을 삭제

```py
numbers = [1,2,3]
numbers.remove(2)

print(numbers)      #[1, 3]
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



#### 리스트 탐색 및 정렬 메서드

| 문법                      | 설명                                                         |
| ------------------------- | ------------------------------------------------------------ |
| `L.indext(x, start, end)` | 리스트에 있는 항목 중 가장 왼쪽에 있는 항목 x의 인덱스를 반환 |
| `L.reverse()`             | 리스트를 거꾸로 나열                                         |
| `L.sort()`                | 리스트를 정렬(매개변수 이용가능) - 원본을 바꿔서 반환값x     |
| `L.count()`               | 리스트에서 항목 x의 개수를 반환                              |



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



#### 문자열에 포함된 문자들의 유형을 판별하는 메서드 

- `isdecimal()` 
  - 문자열이 모두 숫자 문자(0~9)로만 이루어져 있어야 True 
- `isdigit() `
  - `isdecimal()`과 비슷하지만, 유니코드 숫자도 인식 (도 숫자로 인식) 
- `isnumeric() `
  - `isdigit()`과 유사하지만, 몇 가지 추가적인 유니코드 문자들을 인식 (분수, 지수, 루트 기호도 숫자로 인식)

![](C:\Users\SSAFY\Downloads\0724_1.PNG)



# 중요한 메서드

- 문자열
  - split
  - join

- list
  - append
  - extend
  - pop

- 리스트 정렬
  - reverse
  - sort

## Quiz(0725 미리보기)

```py
numbers = [1, 2, 3]

# 1. 할당
list1 = numbers

# 2. 슬라이싱
list2 = numbers[:]

numbers[0] = 100

print(list1)        # [100, 2, 3]
print(list2)        # [1, 2, 3]
```

![](C:\Users\SSAFY\Downloads\0724_2.PNG)