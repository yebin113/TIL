# Python0720

## 제어문(contral statement)

- 코드의 실행 흐름을 제어하는 데 사용되는 구문 
- **조건**에 따라 코드 블록을 실행하거나 **반복**적으로 코드를 실행



### 조건문

- 주어진 조건식을 **평가**하여 해당 조건이 **참(True)인 경우에만 코드 블록을 실행하거나 건너뜀**



### if / elif / else

- 파이썬 조건문에 사용되는 키워드



### if

- 기본구조

```python
if 표현식:
    코드블록
elif 표현식:
    코드블록
else:
    코드블록
```



조건문 예시

![contralstatement1](C:\Users\SSAFY\Downloads\0720_1.PNG)

1. a가 3보다 큰지를 평가  
2. True 
3. if의 코드블록이 실행되고 else의 코드블럭은 무시됨
4. if문을 끝내고 다음 코드 실행



![control2](C:\Users\SSAFY\Downloads\0720_2.PNG)

1. a가 3보다 큰지를 평가  
2. False
3. if의 코드블록이 무시되고 else의 코드블럭이 실행됨
4. if문을 끝내고 다음 코드 실행



#### 복수 조건문 예시

- 조건식을 동시에 검사하는 것이 아니라 순차적으로 비교
- `elif` 문이 추가됨

```py
dust = 35 
if dust > 150: 
    print('매우 나쁨') 
elif dust > 80: 
    print('나쁨') 
elif dust > 30: 
    print('보통') 
else: print('좋음')
```

1. dust 가 150 보다 큰가요? -> False
2. dust 가 80 보다 큰가요? -> False
3. dust 가 30 보다 큰가요? -> True
4. dust > 30 조건의 코드블럭 실행됨 `print('보통') `
5. else는 무시되고 if문 탈출



#### 중첩 조건문 예시

```py
dust = 480 
if dust > 150: #True
    print('매우 나쁨')	#실행됨 
    if dust > 300: #True
    	print('위험해요 나가지 마세요') #실행됨 
elif dust > 80: #무시
    print('나쁨') 
elif dust > 30: #무시
    print('보통') 
else: print('좋음') #무시
```



- 조건문 예시

  ```py
  num =  int(input("숫자를 입력 : "))
  
  #num 이 홀수라면 ( = 2로 나눈 나머지가 1이라면)
  if num % 2 == 1: # if num % 2: 도 동일하게 실행됨 - 1이 true 이기 때문에
  
      print('홀수입니다.')
  #num이 홀수가 아니라면(짝수면)
  else:   #홀수가 아니라면 짝수이기 때문에 따로 elif 를 적을 필요 없음
      print('짝수입니다')
  ```

  

---

## 반복문

- 주어진 코드 블록을 여러번 반복해서 실행하는 구문
- 특정 작업을 반복적으로 수행(종료조건 x) 또는 주어진 조건이 참인 동안 반복해서 실행(종료조건  o)
- `for / while`



### for

- 임의의 시퀀스의 항목들을 그 시퀀스에 들어있는 순서대로 반복
- **종료조건이 없음**
  - 하지만 시퀀스 자체가 길이가 있기 때문에 종료조건이 포함됨

```py
#기본 구조
for 임시변수 in 반복 가능한 객체:
    코드블록
```

#### 반복 가능한 객체(iterable)

- 반복문에서 순회할 수 있는 객체
- 시퀀스 객체 뿐만 아니라 dict, set 등도 포함됨



#### for 문 원리 

- 리스트 내 첫 항목이 반복 변수에 할당되고 코드블록이 실행 

- 다음으로 반복 변수에 리스트의 2번째 항목이 할당되고 코드블록이 다시 실행 

- ...마지막으로 반복 변수에 리스트의 마지막 요소가 할당되고 코드블록이 실행 

  ```py
  items = ['apple', 'banana','coconut'] 
  
  for item in items: 
      print(item) 
      
  """ 
  apple  
  banana  
  coconut 
  """
  ```



- 문자열 순회도 가능

  ```py
  country = 'Korea'
  
  for char in country:
      print(char)
      
  """
  K
  o
  r
  e
  a
  """
  ```

- range 순회

  ```py
  for i in range(5):
      print(i)
      
  """
  0
  1
  2
  3
  4
  """
  ```

- 인덱스로 리스트 순회

  - 리스트의 요소가 아닌 인덱스로 접근하여 해당 요소들을 변경하기

  ```py
  numbers = [4,6,10,-8,5]
  
  for i in range(len(numbers)): #len(numbers) == 5
      #왜 len 함수를 썼을까?
      #다양한 길이의 리스트가 왔을때 활용하기 위해 길이로 접근함
      numbers[i] = numbers[i]*2
      
  print(numbers)
  #[8,6,20,-16.5]
  ```

- 중첩된 반복문

  - 안쪽 반복문이 다 끝나야 바깥쪽의 반복문으로 나감
  - print 가 호출되는 횟수 => len(outers) * len(inners)

  ```py
  outers = ['A','B']
  inners = ['c','d']
  
  for outer in outers:
      for inner in inners:
          print(outer, inner)
          
  """
  A c - outers[0], inners[0]
  A d - outers[0], inners[1]
  B c - outers[1], inners[0]
  B d - outers[1], inners[1]
  """
  ```

- 중첩 리스트 순회

  - 안쪽 리스트 요소에 접근하려면 바깥 리스트를 순회하면서 중첩 반복을 사용해 각 안쪽 반복을 순회

  ```py
  elements = [['A','B'],['c','d']]
  
  for elem in elements:
      print(elem)
  """
  ['A','B']
  ['c','d']
  """
  for elem in elements:	#중첩 리스트에 접근하는 법
      for item in elem:	#중첩 반복
          print(item)
  """
  A
  B
  c
  d
  """
  ```

  

### while

- 주어진 조건식이 참인동안 코드를 반복해서 실행
- 조건식이 거짓이 될 때까지 반복 (조건 만들때 거짓으로 될때까지로 설정하는 것이 편함)

```py
while 조건식:
    코드블록
```

- while 반복문 예시

  ```py
  a = 0
  
  while a<3:
      print(a)
      a+=1
      
  print("끝")
  """
  0
  1
  2
  끝
  """
  ```

- 사용자 입력에 따른 반복 
  - while문을 사용한 특정 입력 값에 대한 종료 조건 활용하기 

```py
number = int(input('양의 정수를 입력해주세요 : '))

while number <= 0: 
    if number < 0: 
        print('음수를 입력했습니다.') 
    else: 
        print('0은 양의 정수가 아닙니다. ') 
    number = int(input('양의 정수를 입력해주세요.: ') 

print(' 잘했습니다!') 
                 
"""
양의 정수를 입력해주세요.: 0 
0은 양의 정수가 아닙니다. 
양의 정수를 입력해주세요.: -1 
음수를 입력했습니다. 
양의 정수를 입력해주세요.: 1 
잘했습니다!
"""
```

#### while문은 반드시 종료조건이 필요



### 적절한 반복문 활용하기 

- **for **
  - **반복 횟수가 명확**하게 정해져 있는 경우에 유용 
  - 예를 들어 리스트, 튜플, 문자열 등과 같은 **시퀀스 형식의 데이터**를 처리할 때 

- **While **
  - 반복 횟수가 불명확하거나 **조건에 따라 반복을 종료**해야 할 때 유용 
  - 예를 들어 사용자의 입력을 받아서 특정 조건이 충족될 때까지 반복하는 경우



## 반복제어

- for문과 while은 매 반복마다 본문 내 모든 코드를 실행하지만 때때로 일부만 실행하는 것이 필요할 때가 있음

- break vs continue

| break            | continue             |
| ---------------- | -------------------- |
| 반복을 즉시 중지 | 다음 반복으로 건너뒴 |

- 

- 

- 프로그램 종료 조건 만들기 

  ```py
  number = int(input('양의 정수를 입력해주세요.: '))
  while number <= 0:
      #이스터에그 같은 존재
  	if number == -9999:	
  		print('프로그램을 종료합니다.')
  		break	
          #종료조건이 아니여도 반복문을 종료
          
  	if number < 0:
          print(' 음수는 입력했습니다.')
  	else:
  		print('0은 양의 점수가 아닙니다.')
  	number = int(input('양의 정수를 입력해주세요.:') )
  print('잘했습니다!')
  """
  양의 정수를 입력해주세요.: -9999
  프로그램을 종료합니다.
  잘했습니다!
  """
  ```

  

- break 예시
  - 짝수를 찾을때까지 반복하는 코드

```py
numbers = [1, 3, 5, 6, 7, 9, 10, 11] 
found_even = False 

for num in numbers: 
    if num % 2 == 0: # 짝수일때 if문 안의 코드 실행
        print(' 첫 번째 짝수를 찾았습니다: ', num)
    	found _even = True
        break	#짝수를 찾는다면 반복문 탈출

if not found_even:	#짝수를 찾지 못했을때, found_even== False --> not False == True
    print('짝수를 찾지 못했습니다')	
```



- continue 예시
  - 현재 반복문의 남은 코드를 건너뛰고 다음 반복으로 넘어감

```py
numbers = [1,2,3,4,5,6,7,8,9,10]

for num in numbers:
    if num % 2 ==0:	# num이 짝수라면
        continue	# 남은코드(print(num))을 실행하지 않고 다음 반복으로 돌아감
    print(num)
    
"""
1
3
5
7
9
"""
```



#### break와 continue 주의사항 

- break와 continue를 남용하는 것은 **코드의 가독성을 저하**시킬 수 있음 
- **특정한 종료 조건**을 만들어 break을 대신하거나, if 문을 사용해 continue 처럼 코드를 건너 뛸 수도 있음 
- 약간의 시간이 들더라도 가능한 코드의 **가독성을 유지**하고 코드의 의도를 명확하게 작성하도록 노력하는 것이 중요



---

## List Comprehension

- **간결하고 효율적**인 **리스트 생성** 방법
- 가독성이 좋지 않음 남용 x

현재 우리가 사용하는 리스트 생성 방법

1. []
2. map + list

- List Comprehension 구조

```py
[expression for 변수 in iterable]

list(expression for 변수 in iterable)
```

- 예시

```PY
 # 0~9 까지 요소를 가지는 리스트 만들기

#1. 일반적인 방법
new_list = []
for i in range(10):
    new_list.append(i)
    #append - list에 값을 넣는 함수
print(new_list) #[0,1,2,3,4,5,6,7,8,9]

# 2. List Comprehension
new_list_2 = [i for i in range(10)] 
print(new_list_2)
```

- if가 들어간 List comprehension

```py
 # 0~9 까지 홀수 요소를 가지는 리스트 만들기

#1. 일반적인 방법
new_list = []
for i in range(10):
    if i % 2 == 1:
        new_list.append(i)
    
    #append - list에 값을 넣는 함수
print(new_list) #[1,3,5,7,9]

# 2. List Comprehension
new_list_2 = [i for i in range(10) if i % 2 == 1] 
print(new_list_2) #[1,3,5,7,9]
```

- if - else 

```py
# 2. List Comprehension
new_list_2 = [i for i in range(10) if i % 2 == 1] 

# 3. if - else list comprehension
new_list_3 = [i if i % 2 == 1 else str(i) for i in range(10) ] 
print(new_list_2) #[1,3,5,7,9]
print(new_list_3) #['0', 1, '2', 3, '4', 5, '6', 7, '8', 9]
```

- elif 는 안됨
- 중첩 if는 가능



### 리스트를 만드는 3가지 방법 비교

```py
# 리스트를 생성하는 3가지 방법 비교
# 어떤게 가장 빠를까?	 - 외부요인에 따라 달라서 단정지을 수 x
# 정수 1,2,3을 가지는 새로운 리스트 만들기

numbers = ['1','2','3']
# 1. for 반복문
new_numbers = []
for number in numbers:
    new_numbers.append(int(number))
print(new_numbers)  

# 2. map
new_numbers_2 = list(map(int, numbers))
print(new_numbers_2) 

# 3. list comprehension
new_numbers_3 = [int(number) for number in numbers ]
print(new_numbers_3)
```



---

### pass

- 아무런 동작도 수행하지 않고 넘어가는 역할

  - 문법적으로 문장이 필요하지만 프로그램 실행에는 영향을 주지 않아야 할 때 사용
  - 온라인 실습실에서 자주 등장

  

1. 코드 작성 중 미완성 부분

   - 구현해야 할 부분이 나중에 추가될 수 있고, 코드를 컴파일하는 동안 오류가 발생하지 않음

   ```py
   def my_function():
       pass
   ```

2. 조건문에서 아무런 동작을 수행하지 않아야 할 때

   ```py
   if condition:
       pass	#아무런 동작도 수행하지 않음
   else:
       #다른동작 수행
   ```

3. 무한 루프에서 조건이 충족되지 않을 때 pass를 사용하여 루프를 계속 진행하는 방법

   ```py
   while True:
       if condition:
           break
       elif condition:
           pass
       else:
           print('..')
   ```

---

### enumerate

- iterable 객체의 각 요소에 대해 인덱스와 함께 반환하는 내장함수

  ```py
  result = ['a','b','c']
  
  print(enumerate(result))        # <enumerate object at 0x00000228721B2040>
  print(list(enumerate(result)))  # [(0, 'a'), (1, 'b'), (2, 'c')]
  
  for index, elem in enumerate(result):
      print(f'인덱스{index}: {elem}')
  
  """
  인덱스0: a
  인덱스1: b
  인덱스2: c
  """
  ```

  