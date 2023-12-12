class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber

    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, self.phoneNumber))
# 자식 클래스

# class Student(Person):
#     # 변수가 추가(덮어쓰기)
#     def __init__(self, name, phoneNumber, subject, studentID):
#         self.name = name
#         self.phoneNumber = phoneNumber
#         self.subject = subject
#         self.studentID = studentID

class Student(Person):
    # 변수가 추가(덮어쓰기)
    def __init__(self, name, phoneNumber, subject, studentID):
        Person.__init__(self,name,phoneNumber)
        # 부모쪽에도 어차피 있으니까 부모꺼 초기화를 호출 하는 것
        self.subject = subject
        self.studentID = studentID
    def printInfo(self):
        super().printInfo()
        print("Info(학과:{0}, 학번: {1})".format(self.name, self.phoneNumber))

p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "빅데이터학과", "991122")
print(p.__dict__)
print(s.__dict__)
# 결국 인스턴스가 내부에서는 딕셔너리임

p.printInfo()
s.printInfo()




