#전역변수
str = "Not Class Member"

#파이썬은 명확하게 코딩하는 것이 좋다!
#클래스 정의
class GString:
    #초기화 메서드
    def __init__(self):
        #인스턴스 멤버 변수
        self.str = "" 
    #값 셋팅 메서드(세터)
    def set(self, msg):
        self.str = msg
    #값 리딩 메서드(게터)
    def print(self):
        #버그 발생!
        print(self.str)

g = GString()
g.set("First Message")
g.print()
