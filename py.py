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


class FirstChild(Mom,Dad):
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