# 전역변수

str = "Not Class Member"
class GString:
    def __init__(self):
        # 인스턴스의 멤버 변수
        self.str = "" 
    def set(self, msg):
        self.str = msg
    def print(self):
        # 버그 수정
        print(self.str)

g = GString()
g.set("First Message")
g.print()


