# Classes 상속
- 상속
- 에러와 예외
- EAFP & LBYL

## 상속(inheritance)
- 기존 클래스의 속성과 메서드를 물려받아 새로운 하위 클래스를 생성하는 것

### 상속이 필요한 이유

1. 코드 재사용
   - 상속을 통해 기존 클래스의 속성과 메서드를 재사용할 수 있음
   - 새로운 클래스를 작성할 때 기존 클래스의 기능을 그대로 활용할 수 있으며, 중복된 코드를 줄일 수 있음

2. 계층 구조
   - 상속을 통해 클래스들 간의 계층 구조를 형성할 수 있음
   - 부모 클래스와 자식 클래스 간의 관계를 표현하고 더 구체적인 클래스를 만들 수 있음


3. 유지 보수의 용이성
   - 상속을 통해 기존 클래스의 수정이 필요한 경우, 해당 클래스만 수정하면 되므로 유지 보수가 용이해짐
   - 코드의 일관성을 유지하고, 수정이 필요한 범위를 최소화할 수 있음

### 상속 없이 구현 하는 경우
- 학생/교수 정보를 나타내기 어려움

```py
class Person:
    def init__(self, name, age):
        self.name = name
        self.age = age
    def talk(self):
        print(f'반갑습니다. {self.name}입니다.')
s1 = person(' 김학생 ', 23)
s1. talk() # 반갑습니다. 김학생입니다.

p1 = Person('박교수' , 59)
p1.talk() # 반갑습니다. 박교수입니다.
```
- 메서드 중복 정의
```py
class Professor:
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department
    def talk(self): A 중복
        print(f' 반갑습니다. {self. name}입니다.')
class Student:
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
    def talk(self): # 메서드 재사용
        print(f' 반갑습니다. {self. name}입니다.')
class Professor(Person):
    def __init__(self, name, age, department):
          self.name = name
          self.age = age
          self.department = department
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



-----------여기까지함
```py
class Person:
    def init__(self, name, age,number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email

class Student(Person):
    def init(self, name, age, number, email ,student_id):
m 부모클래스의 init 에서드 호출
super..
init_ (name, age, number, email)
self.student id = student id

```
다중 상속
- 두 개 이상의 클래스를 상속 받는 경우
- 상속받은 모든 클래스의 요소를 활용 가능함
- 중복된 속성이나 메서드가 있는 경우 상속 순서에 의해 결정됨

다중 상속 예시
class Person:
def
--init_ _(self, name:
self.name = name
def greeting(self):
return f'9, {self .name}'
class Mom (Person):
gene = 'XX'
def swim(self:
return ' 엄마가 수영
class Dad(Person):
gene = 'xy'
def walk(self):
return '아빠가 걷기'

class FirstChild(Dad, Mom) :
def swim(self):
return ' 첫째가 수영
def cry(self):
return ' 첫째가 응애'

baby1 = FirstChild('0f7|')
print(baby1.cry()

첫째가 응애
print(baby1.swim())

첫째가 수영
print (baby1.walk()
아빠가 걷기
print (babyl. gene)
＃？？

상속관련함수와 메서드
mro()
- Method Resolution Order
- 해당 인스턴스의 클래스가 어떤 부모 클래스를 가지는지 확인하는 메서드
- 기존의 인스턴스 -> 클래스 순으로 이름 공간을 탐색하는 과정에서 상속 관계에 있으면 인스턴스 -> 자식 클래스 -> 부모 클래스로 확장

---
## 에러와 예외
