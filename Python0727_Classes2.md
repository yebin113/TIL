# Classes 상속
- 상속
- 에러와 예외
- EAFP & LBYL

## 상속(inheritance)
- 상위 클래스의 속성과 메서드를 **물려받아** 새로운 하위 클래스를 생성하는 것

### 상속이 필요한 이유

1. 코드 **재사용**
   - 상속을 통해 기존 클래스의 속성과 메서드를 재사용할 수 있음
   - 새로운 클래스를 작성할 때 기존 클래스의 기능을 그대로 활용할 수 있으며, 중복된 코드를 줄일 수 있음

2. 계층 구조
   - 상속을 통해 클래스들 간의 계층 구조를 형성할 수 있음
   - 부모 클래스와 자식 클래스 간의 관계를 표현하고 더 구체적인 클래스를 만들 수 있음


3. **유지 보수**의 용이성
   - 상속을 통해 기존 클래스의 수정이 필요한 경우, 해당 클래스만 수정하면 되므로 유지 보수가 용이해짐
   - 코드의 일관성을 유지하고, **수정이 필요한 범위를 최소화**할 수 있음

### 상속이 없는 경우의 한계
- 학생/교수 정보를 나타내기 어려움

```py
class Person:
    # 사람에 대한 정보를 담은 클래스
    def init__(self, name, age):
        self.name = name
        self.age = age
    def talk(self):
        print(f'반갑습니다. {self.name}입니다.')
# 학생과 교수의 각각의 정보는 한 클래스로 나타내기 힘듬
s1 = person(' 김학생 ', 23)
s1. talk() # 반갑습니다. 김학생입니다.

p1 = Person('박교수' , 59)
p1.talk() # 반갑습니다. 박교수입니다.
```
- 메서드 중복 정의
```py
class Professor:
    # 교수 클래스
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department
    def talk(self): A 중복
        print(f' 반갑습니다. {self. name}입니다.')
class Student:
    # 학생 클래스
    def init(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa
    def talk(self): # 중복
        print(f' 반갑습니다. {self. name}입니다.')
```
### 상속을 사용한 계층구조 변경

```py
class Person:
    def init(self, name, age):
        self.name = name
        self.age = age
    def talk(self): # 상위 클래스의 메서드
        print(f' 반갑습니다. {self. name}입니다.')
class Professor(Person): # 괄호 안에 상속을 받는 부모 클래스의 이름을 넣음
    def __init__(self, name, age, department):
          self.name = name
          self.age = age
          self.department = department
          # 하위 클래스에서 상위 클래스의 메서드 사용 가능
class Student(Person):
    def init(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa

p1 = Professor('박교수', 49, ' 컴퓨터공학과')
s1 = Student('김학생', 20, 3.5)

# 부모 Person 클래스의 talk 메서드를 촬용
p1.talk() # 반갑습니다. 박교수입니다.

#부모 Person 클래스의 talk 메서드들, 활용 
s1.talk() # 반갑습니다. 김학생입니다.
```
### super ()
부모 클래스의 메서드를 호출하기 위해 사용되는 내장 함수
다중상속시 부모 클래스들의 사용순서를 자동으로 맞춰줌

### super() 사용 예시

- 사용전
```py
class Person:
    def init__(self, name, age,number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email

class Student(Person):
    def init(self, name, age, number, email ,student_id):
        self.name = name
        self.age = age
        self.number = number
        self.email = email
        self.student_id = student_id

```



사용 후
```py
class Person:
    def __init__(self, name, age,number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email

class Student(Person):
    def __init__(self, name, age, number, email ,student_id):
    # 부모클래스의 init 에서드 호출
        super.__init__(name, age, number, email)
        self.Student.id = Student.id

```
```py

class Person:
    def init(self, name, age):
        self.name = name
        self.age = age
    def talk(self): # 상위 클래스의 메서드
        print(f' 반갑습니다. {self.name}입니다.')
class Professor(Person): # 괄호 안에 상속을 받는 부모 클래스의 이름을 넣음
    def __init__(self, name, age, department):
        
        # 1. 직접 인자 작성
        # self.name = name
        # self.age = age
        # self.department = department

        # 2. Person에 추가
        # Person.__init__(self,name,age)
        # self.department = department
        # 이런 경우에는 상위 클래스 이름이 바뀔때 하나하나 바꿔줘야함

        
        # 3. super()사용
        # self 없어도 됨
        super().__init__(self,name,age)
        self.department = department
        

        # 하위 클래스에서 상위 클래스의 메서드 사용 가능
class Student(Person):
    def __init__(self, name, age, gpa):
        super().__init__(self,name,age)
        self.gpa = gpa

```
### 다중 상속
- 두 개 이상의 클래스를 상속 받는 경우
- 상속받은 모든 클래스의 요소를 활용 가능함
- **중복**된 속성이나 메서드가 있는 경우 **상속 순서에 의해 결정**됨

### 다중 상속 예시
```py
class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return f'안녕, {self.name}'
    

class Mom(Person):
    gene = 'XX'
    def swim(self):
        return '엄마가 수영'
    

class Dad(Person):
    gene = 'XY'
    def walk(self):
        return '아빠가 걷기'


class FirstChild(Dad, Mom):
    # 다중상속(아빠부터 시작)

    def swim(self):
        # 엄마 클래스의 함수 재정의
        return '첫째가 수영'
    
    def cry(self):
        # 부모클래스에 없는 함수
        return '첫째가 응애'

baby1 = FirstChild('아기') 
# 초기 인자 name을 받음

print(baby1.cry()) # 첫째가 응애
print(baby1.swim()) # 첫째가 수영
print (baby1.walk()) # 아빠가 걷기
print(baby1.greeting()) # 안녕, 아기
print(baby1.gene) # XY
```

### 다중상속일때 뒤쪽의 변수를 써야 할 떄
- 따로 변수 지정해주기
  `dad_gene = Dad.gene # 상속 순서를 바꿀수없을때는 따로 변수 지정하기`
### 상속관련함수와 메서드
#### `mro()`
- Method Resolution Order
- 매서드 해결 순서
- 해당 인스턴스의 클래스가 어떤 부모 클래스를 가지는지 확인하는 메서드
- 기존의 인스턴스 -> 클래스 순으로 이름 공간을 탐색하는 과정에서 상속 관계에 있으면 인스턴스 -> 자식 클래스 -> 부모 클래스로 확장

---
## 에러와 예외


### 버그
- 소프트웨어에서 발생하는 오류 또는 결함
- 프로그램의 예상된 동작과 실제 동작 사이의 불일치


### 버그의 기원
- 최초의 버그는 1945년 프로그래밍 언어의 일종인 코볼 발명자 그레이스 호퍼가 발견
- 역사상 최초의 컴퓨터 버그는 Mark II 라는 컴퓨터 회로에 벌레인 나방이 들어가 합선을 일으켜 비정상적으로 동작한 것을 기록한 것
- "버그"라는 용어는 이전부터 사용되어 왔지만 이 사건을 계기로 컴퓨터 시스템에서
발생하는 오류 또는 결함을 지칭하는 용어로 널리 사용되기 시작

### Debugging
- 소프트웨어에서 발생하는 버그를 찾아내고 수정하는 과정
- 프로그램의 오작동 원인을 식별하여 수정하는 작업

#### 디버깅 방법

1. print 함수 활용
   - 특정 함수 결과, 반복/조건 결과 등 나눠서 생각, 코드를 bisection으로 나눠서 생각

2. 개발 환경(text editor, IDE) 등에서 제공하는 기능 활용
   - breakpoint, 변수 조회 등

3. Python tutor 활용 (단순 파이썬 코드인 경우)
4. 뇌 컴파일, 눈 디버깅 등

---
## 에러
- 프로그램 실행 중에 발생하는 예외 상황

- 문법 에러(Syntax Error)
    - 프로그램의 구문이 올바르지 않은 경우 발생 (모타, 괄호 및 콜론 누락 등의 문법적 오류)
- 예외(Exception)
    - 프로그램 **실행 중**에 감지되는 에러

### 문법 에러예시

1.  Invalid syntax (문법 오류)
`while # SyntaxError: invalid syntax`
2.  assign to literal (잘못된 할당)
`5 = 3 # SyntaxError: cannot assign to literal`
3.  EOL (End of Line)
```py
print('hello

# SyntaxError: EOL while scanning string literal
```
4. EOF (End of File)
```py
print(
# SyntaxError: unexpected EOF while parsing
```

## 예외
- 프로그램 실행중에 감지되는 에러

### 내장 예외(Built-in Exceptions)
- 예외 상황을 나타내는 예외 클래스들
- 파이썬에서 이미 정의되어 있으며 특정 예외 상황에 대한 처리를 위해 사용
[파이썬 자습서][httos://docs.python.ora/ko/3/ibrary/exceptions.html#/ValueError]
### 내장예외 예시
- ZeroDivisionError : 나누기 또는 모듈로 연산의 두 번째 인자가 0일 때 발생, 0으로 나누려 할때
```py
10/0 # ZeroDivisionError: division by zero
```
- NameError : 지역 또는 전역 이름을 찾을 수 없을 때 발생

```py
print (name_error)
NameError: name 'name error' is not defined
```
1. **`TypeError`**
  - 타입 불일치
```py
'2'+2 
# TypeError: can only concatenate str (not "int") to str
```
  - 인자 누락
```py
sum() # TypeError: sum() takes at least 1 positional argument (0 given)
```  
  - 인자 초과
```py
sum(1, 2, 3) # TypeError: sum() takes at most 2 arguments (3 given)
```
  - 인자 타입 불일치
    ```py
    import random random. sample(1, 2)
    random.sample(1,2)
    # TypeError: Population must be a sequence. For dicts or sets, use sorted(d)
    ```

2. `ValueError`
- 연산이나 함수에 문제가 없지만 부적절한 값을 가진 인자를 받았고, 상황이 IndexError 처럼 더 구체적인 예외로 설명되지 않는 경우 발생
```py
int('1.5') # Valueerror; invalad literal for intf) with base 10: '3.5'
range(3). index(6) # ValueError: 6 is not in range
```

3. `IndexError` 
   - 시퀀스 인덱스가 범위를 벗어날 때 발생
   - 반복할 때 자주 만남
```py
empty_list = []
empty_list [2]
# IndexError: list index out of range
```

4. `KeyError` 
   - 딕셔너리에 해당 키가 존재하지 않는 경우
   - get 사용하면 None 반환해서 예방 가능

```py
person = {'name': 'Alice'}
person ['age'] # KeyError:'age'
```
5. `ModuleNotFoundError `
   - 모듈을 찾을 수 없을 때 발생
```py
import hahaha
```

6. `ImportError` 
   - 임포트 하려는 이름을 찾을 수 없을 때 발생
```py  
from random import hahaha

# ImportError: cannot import name 'hahaha' from 'random"
```
7. `Keyboardinterrupt `
- 사용자가 Control-C 또는 Delete를 누를 때 발생
- 무한루프 시 강제 종료
```py
while True:
continue
"""
Traceback (most recent call last):
File ...", line 2, in «modules continue
KeyboardInterrupt
"""
```
8. `IndentationError` 
- 잘못된 들여쓰기와 관련된 문법 오류

```py
for i in range(10):
print(i) # IndentationError: expected an indented block
```

### 예외 처리
**try와 except**
- 파이썬에서는 try문과 except 절을 사용하여 예외 처리

#### try - except 구조
- try 블록 안에는 예외가 발생할 수 있는 코드를 작성
- except 블록 안에는 예외가 발생했을 때 처리할 코드를 작성
- **예외가 발생**하면 프로그램 흐름은 try 블록을 빠져나와 해당 예외에 대응하는 **except 블록으로 이동**

```py
try:

예외가 발생할 수 있는 코드
except 예외:

예외 처리 코드
```
예외처리 예시
```py
try:
result = 10 / 0
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')

# 0으로 나눌 수 없습니다.
```
```py
try:
    num = int(input(' 숫자 입력 : 1 '))
except ValueError:
print('숫자가 아닙니다.')

"""
숫자입력 : a
숫자가 아닙니다.
"""
```

### 복수 예외 처리 연습
- 100을 사용자가 입력한 값으로 나누고 출력하는 코드를 작성해보시오.
1. 먼저, 발생 가능한 에러가 무엇인지 예상해보기

```py
num = int(input ( '100으로 나눌 값을 입력하시오 : '))
print (100 / num)
```
``` py
int('a') # 문자열 입력-> ValueError
100 / int('0') # 0 으로 못나눔 -> ZeroDivisionError
```


- 발생가능한 에러를 모두 명시하거나 & 별도로 작성하기
```py
try:
    num = int(input('0으로 나눌 깊을 입력하시오 : '))
    print (100 / num)
except ValueError:
    print('숫자를 넣어주세요.')
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다. ')
except:
    print('에러가 발생하였습니다. ')

"""
# 한번에 사용 가능
try:
    num = int(input('0으로 나눌 값을 입력하시오 : '))
    print (100 / num)
except (ValueError, ZerobivisionError):
    print(' 제대로 입력해주세요.')
except:
    print('에러가 발생하였습니다. ')
    """

```
- 에러들도 클래스이기때문에 상속개념이 있음
- 아래와 같이 예외를 작성하면 코드는 2번째 except 절에 이후로 도달하지 못함
```py
try:
    num = int(input('0으로 나눌 깊을 입력하시오 : '))
    print (100 / num)
except BaseException: # 더 높은 상속 클래스 이기때문에 여기에 다걸림
    print('숫자를 넣어주세요.')
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다. ')
except:
    print('에러가 발생하였습니다. ')

```

### 내장 예외의 상속 계층구조 주의

- 내장 예외 클래스는 상속 계층구조를 가지기 때문에
except 절로 분기 시 반드시 하위 클래스를 먼저 확인 할 수 있도록 작성해야 함
- [파이썬자습서][https://docs.python.org/ko/3.9/library/exceptions.html]

--- 
## 예외처리와 값 검사에 대한 2가지 접근 방식

1. EAFP
2. LBYL

### EAFP
- "Easier to Ask for Forgiveness than Permission"
- 예외처리를 중심으로 코드를 작성하는 접근방식(try - except)


### LBYL
- "Look Before You Leap"
- 값 검사를 중심으로 코드를 작성하는 접근 방식(if-else)

```py
try:
    result = my_dict['key']
    print(result)
except KeyError:
    print(' Key가 존재하지 않습니다. ')
```

```py
if 'key' in my dict:
    result = my_dict['key']
    print (result)
else:
    print('Key가 존재하지 않습니다. ')
```
| EARP | LBYL |
| -------------------------- |--------------------------------|
| 일단 실행하고 예외를 처리 | 실행하기 전에 조건을 검사 |
| 코드를 실행하고 예외가 발생하면 예외처리를 수행 | 코드 실행 전에 조건문 등을 사용하여 예외 상황을 미리 검사하고 예외 상황을 피하는 방식 |
| 코드에서 예외가 발생할 수 있는 부분을 미리 예측하여 대비하는 것이 아니라 예외가 발생한 두에 예외를 처리 | 코드가 좀 더 예측 가능한 동작을 하지만, 코드가 더 깊고 복잡해질 수 있음|
| 예외 상황을 예측하기 어려운 경우에 유용 | 예외 상황을 미리 방지하고 싶을 때 유용 |
---
## 참고
### as 키워드
- as 키워드를 활용하여 **에러 메시지를 except 블록에서 사용**할 수 있음
```py
my_list = []
try:
    number = my_list[1]
except IndexError as error:
    print(f'{error}가 발생했습니다.')
    # list index out of range가 발생했습니다
```