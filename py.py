# Person 정의
class Person:
    # 클래스 속성(클래스 변수)
    name = 'unknown'

    # 인스턴스 메서드
    def talk(self):
        print (self.name)

p1 = Person()
p1.talk() # unknown
# P1은 인스턴스 변수가 정의되어 있지 않아
# 클래스 변수(unknown)가 출력됨

# p2 인스턴스 변수 설정 전/후
p2 = Person()
p2.talk() # unknown
p2.name = 'Kim' # 인스턴스 변수 설정하면
p2.talk() # Kim 본인의 인스턴스 변수 나옴
# p2는 인스턴스 변수가 정의되어 인스턴스 변수(Kim)가 출력됨

p3 = Person('Yun')
p3.talk()
print(Person.name) # unknown
print (p1.name) # unknown
print (p2.name) # Kim
# Person 클래스의 값이 Kim으로 변경된 것이 아닌 p2 인스턴스의 이름 공간에 nameo Kim으로 저장됨