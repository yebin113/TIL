# Data Structure

## 비시퀀스 데이터 구조

### Set
- 고유한 항목들의 정렬되지 않은 컬렉션
- 세트 메서드
- 중복 원소 x
- 집합 연산 가능

| 메서드               | 설명                                                  |
| -------------------- | ----------------------------------------------------- |
| `s.add(x)`           | 세트 s에 항목 x를 추가. 이미 x가 있다면 변화 없음     |
| `s.clear()`          | 세트 s 의 모든 항목을 제거                            |
| `s.remove(x)`        | 세트 s에 항목 x를 제거. 항목 x 가 없을경우 Key Error  |
| `s.pop()`            | 세트 s에서 랜덤하게(순서가 없기 때문) 항목을 반환하고, 해당 항목을 제거 |
| `s.discard(x)`       | 세트 s에서 항목 x를 제거                              |
| `s.update(iterable)` | 세트 s에 다른 iterable 요소를 추가                    |

####  `s.add(x)` 
- 세트에 x를 추가

```python
my_set = {1,2,3}
my_set.add(4)
print(my_set)   # {1,2,3,4}

my_set.add(4)
print(my_set)   # {1,2,3,4}
```

#### `s.clear()`
- 세트의 모든 항목을 제거


```python
my_set = {1,2,3}
my_set.clear()
print(my_set)   # set()
# 빈 세트는 중괄호로 표기하지 않음
# 빈 중괄호는 딕셔너리로 표기됨
```

####  `s.remove(x)`  
- 세트에서 항목 x를 제거

```python
my_set = {1,2,3}
my_set.remove(2)
print(my_set)   # {1,3}

# 요소가 없을 경우
my_set.remove(10)
print(my_set)   # Key Error
```


####  `s.discard(x)`  
- 세트에서 항목 x를 제거. remove 와 달리 에러 x

```python
my_set = {1,2,3}
my_set.discard(2)
print(my_set)   # {1,3}

my_set.discard(10)
print(my_set.discard(10))    # None
# 아무런 결과x
# 반환값이 0

my_set.discard(1.0)  
# 형변환 됨
print(my_set)   # {3}

my_set.remove(10)       # KeyError: 10

```

####  `s.pop(x)`  
- 세트에서 임의의 요소를 제거 후 반환

```python
my_set = {1,2,3}
element = my_set.pop()

print(element)   # 1
print(my_set)   # {2,3}

```
#### `s.update(iterable)`
- 세트에 다른 iterable 요소를 추가


```python
my_set = {1,2,3}
my_set.update([4,5,1])
print(my_set)   # {1,2,3,4,5}

```

#### 세트의 집합 메서트
| 메서드                    | 설명                                                         | 연산자|
| ----------------- | ------------------------------------------------------------ |------------|
| `set1.difference(set2)`   | set1에는 들어있지만 set2에는 없는 항목으로 세트를 생성 후 반환 |  set1 - set 2
| `set1.intersection(set2)` | set1과 set2 모두 들어있는 항목으로 세트를 생성 후 반환       | set1 & set 2
| `set1.issubset(set2)`     | set1의 항목이 모두 set2에 들어있으면 True를 반환             | set1 <= set 2
| `set1.issuperset(set2)`   | set1가 set2의 항목을 모두 포함하면 True를 반환               | set1 >= set 2
| `set1.union(set2)`        | set1 또는 set2에(혹은 둘 다) 들어있는 항목으로 세트를 생성 후 반환 | set1 (파이프라인) set 2 |

```python
set1 = {0,1,2,3,4}
set2 = {1,3,5,7,9}

print(set1.difference(set2)) # {0, 2, 4} 
print(set1.intersection(set2)) # {1, 3} 
print(set1.issubset(set2)) # False
print(set1.issuperset(set2)) # False
print(set1.union(set2)) # {0, 1, 2, 3, 4, 5, 7, 9}
```

## 딕셔너리
- 고유한 항목들(키 값은 중복될 수 없음)의 정렬되지 않은 컬렉션

### 딕셔너리 메서드
| 메서드 | 설명 |
| ------ | ---- |
|    `D.clear()`    |   딕셔너리 D의 모든 키/값 쌍을 제거   |
|    `D.get(k)`    |   키 k에 연결된 값을 반환 키가 없으면 None 반환   |
|    `D.get(k,v)`    |   키 k에 연결된 값을 반환 키가 없으면 기본값으로 v 반환   |
|    `D.keys()`    |   딕셔너리 D의 키를 모은 객체를 반환   |
|    `D.values()`    |    딕셔너리 D의 값을 모은 객체를 반환  |
|    `D.items()`    |   딕셔너리 D의 키/값 쌍을 모은 객체를 반환   |
|    `D.pop(k)`    |   딕셔너리 D에서 키 k를 제거하고 연결됐던 값을 반환(없으면 오류)   |
|    `D.pop(k,v)`    |  딕셔너리 D에서 키 k를 제거하고 연결됐던 값을 반환(없으면 v를 반환)    |
|    `D.setdefault(k)`    |   딕셔너리 D에서 키 k와 연결된 값을 반환   |
|    `D.setdefault(k,v)`    |   딕셔너리 D에서 키 k와 연결된 값을 반환, k가 D의 키가 아니면 값 v와 연결한 키 k를 D에 추가하고 v를 반환   |
|    `D.update(other)`    |   other 내 각 키에 대해 D에 있는 키면 D에 있는 그 키의 값을 other 에 있는 값으로 대체. other에 있는 각 키에 대해 D에 없는 키면 키/값 쌍을 D 에 추가   |

#### `D.clear()`
- 딕셔너리 D의 모든 키/ 값 쌍을 제거
```py

person = {'name':'Alice','age':25}
person.clear()
print(person)   #{}
```

####  `D.get(k[,default])`  
- 키 연결된 값을 반환하거나 키가 없으면 None 혹은 기본 값을 반환

```py
person = {'name':'Alice','age':25}

# 같은결과
print(person['name']) # Alice
print(person.get('name'))   # Alice

# 다른 결과
print(person.get('country'))    # None
print(person['country'])  # KeyError
print(person.get('country','Unknown'))  # Unknown
```

####  `D.keys()` 
- 딕셔너리 키를 모든 객체를 반환
```py
person = {
    'name': 'Alice', 
    'age': 25
    }
print (person.keys()) # dict_keys (['name', 'age']) 
# 리스트 형태로 저장
for k in person. keys():
    print(k)
"""
name
age
"""
```
####  `D.values()` 
- 딕셔너리 값을 모든 객체를 반환
```py
person = {
    'name': 'Alice', 
    'age': 25
    }
print (person.values()) # dict_values(['Alice', 25])
# 리스트 형태로 저장
for k in person.values():
    print(k)

"""
Alice
25
"""
```


####  `D.items()` 
- 딕셔너리 키/값 쌍을 모든 객체를 반환
```py
person = {'name': 'Alice', 'age': 25}
print (person.items()) 
# dict_items ([('name', 'Alice') ('age', 25)]) 
for k, v in person. items():
    print(k, v)
"""
name Alice
age 25
"""
```

#### `pop(key[, default])`
- 키를 제거하고 연결됐던 값을 반환 (없으면 에러나 default 를 반환)

```py
person = {'name': 'Alice', 'age': 25}
print (person.pop('age')) # 25 
print (person) # {'name':'Alice'}
print (person. pop('country', None))
# None
print (person.pop('country')) 
# KeyError
```

#### `D.setdefault(k[,default])`

- 키 k와 연결된 값을 반환(get과 동일), **k가 D의 키가 없다면**  default와 연결한 키 **k를 D에 추가하고 default를 반환** (get과 다름)

```py

person = {'name': 'Alice', 'age': 25}
print (person. setdefault ('country', 'KOREA')) # KOREA 
print (person)

# {'name':'Alice','age': 25, 'country':'KOREA'}
```

#### `D.update(other)`
- other가 제공하는 키/값 쌍으로 딕셔너리 갱신
- **기존키는 덮어씀**

```py

person = {'name': 'Alice', 'age': 25}
other_person = {'name': 'Jane', 'gender': 'Female'}


person.update (other_person)
print(person) # {'name': 'Jane', 'age': 25, 'gender': 'Female'} 

person. update (age=50)
print(person) # {'name': 'Jane', 'age': 50, 'gender': 'Female'} 

person.update(country= 'KOREA') 
print(person)  # {'name': 'Jane', 'age': 50, 'gender': 'Female', 'country' : 'KOREA'} 
```


### 키를 통해 값을 조회하는 세가지 방법
```py
blood_types = ['A','B','A','O','AB','AB','O','A','B','O','B','AB']
# 1. []
new_dict = {}
# blood_type을 순회하면서
for blood_type in blood_types:
    # 기존의 키가 이미 존재한다면
    if blood_type in new_dict:
        # 기존의 키의 값을 1 증가
        new_dict[blood_type] += 1

    # 키가 존재하지 않는다면( 처음 설정된 키)
    else:
        # 1을 할당
        new_dict[blood_type] = 1

print(new_dict)        # {'A': 3, 'B': 3, 'O': 3, 'AB': 3}

# 2. .get()
new_dict_2 = {}
# blood_type을 순회하면서
for blood_type in blood_types:
    # 기존의 키가 이미 존재한다면 blood_type 이 조회되기 때문에 default 작동 x
    # 뒤 쪽에 +1해줘야 함
    new_dict_2[blood_type] = new_dict_2.get(blood_type, 0) +1
print(new_dict_2)   # {'A': 3, 'B': 3, 'O': 3, 'AB': 3}
# 3. .setdefault()

new_dict_3 = {}
# blood_type을 순회하면서
for blood_type in blood_types:
    # 키가 없으면 0으로 설정하고 있으면 그냥 넘어감
    new_dict_3.setdefault(blood_type, 0)
    # 1 증가
    new_dict_3[blood_type] += 1
print(new_dict_3)   # {'A': 3, 'B': 3, 'O': 3, 'AB': 3}
```

## 복사

### 데이터 타입과 복사
- 파이썬에서는 데이터에 분류에 따라 복사가 달라짐
- "변경 가능한 데이터 타입"과 "변경 불가능한 데이터 타입"을 다르게 다룸


### 변경 가능한 데이터 타입의 복사
```py
a = [1,2,3,4]
b = a
b[0] = 100

print(a)  #[100,2,3,4]
print(b)  #[100,2,3,4]
```

### 변경 불가능한 데이터 타입의 복사
```py
a = 20
b = a
b = 10

print(a)  # 20
print(b)  # 10
```

### 복사 유형

1. 할당 (Assignment)
2. 얕은 복사 (Shallow copy)
3. 깊은 복사 (Deep copy)

#### 1. 할당
 - 리스트 복사 예시
```py
original_list = [1, 2, 3]
copy_list = original_list
print (original_list, copy_list) 
# [1, 2, 3] [1, 2, 3]
copy_list[0] = 'hi'
print (original_list, copy_list) 
# ['hi', 2, 3] ['hi', 2, 3]
```

- 할당 연산자(=)를 통한 복사는 해당 객체에 대한 객체 참조를 복사

#### 2. 얕은 복사
- 리스트 얕은 복사 예시 (슬라이싱 이용)

```py
a = [1, 2, 3]

# 슬라이싱
b = a[:]
print (a, b) # [1, 2, 3] [1, 2, 3]
b[0] = 100
print (a, b) # [1, 2, 3] [100, 2, 3]

# copy
c = a.copy()
c[0] = 100
print(a,c)  # [1, 2, 3] [100, 2, 3]
```
- 슬라이싱이나 copy 내장함수를 통해 생성된 객체는 원본 객체와 독립적으로 존재

- 한계 
  -  2차원 리스트와 같이 변경가능한 객체가 있는 경우

```py
a = [1, 2, [1,2]]

a = [1, 2, [1,2]]

# 슬라이싱
b = a[:]
b[2][0] = 999
print (a, b) # [1, 2, [999, 2]] [1, 2, [999, 2]]

# 2차원 리스트와 같이 변경가능한 객체가 있는 경우
# 2차원 요소들은 같이 복사됨

# copy
a = [1, 2, [1,2]]
c = a.copy()
c[2][0] = 999
print(a, c) # [1, 2, [999, 2]] [1, 2, [999, 2]]

```
- 한계 (이어서)
  - a와 b의 주소는 다르지만 **내부 객체의 주소는 같기** 때문에 함께 변경됨

#### 3. 깊은 복사
- 리스트 깊은 복사 예시
- copy 모듈을 import 해서 deepcopy 
```py
import copy

original_list = [1, 2, [1, 2]]
deep_copied_list = copy.deepcopy (original_list)
deep_copied_list[2][0] = 100
print (original_list) # [1, 2, [1, 2]] 
print (deep_copied_list) 
# [1, 2, [100, 2]]
```
- 내부에 중첩된 모든 객체까지 새로운 객체 주소를 참조하도록 함
