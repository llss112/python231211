#DemoSetDict

print("---tuple---")
tp=(10,20,30)
print(len(tp))

# 함수정의 
def calc(a,b):
    return a+b,a*b
# 출력이 여러개면 튜플로 묶인다.

# 함수 호출

result=calc(3,4)
print(result)

print("id:%s,name:%s"%("kim","김유신"))

print("---set---")
a={1,2,3,3}
b={3,4,4,5}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

print("---형식---")
a=list((1,2,3))
a.append(4)
print(a)



print("---dict---")
device={"아이폰":5,"아이패드":10,"윈도우타블렛":50}
print(device)
print(device["아이폰"])
device["맥북"]=15
device["아이폰"]=6
print(device)
del device["아이폰"]
print(device)


phone={"kim":"111","lee":"222","park":"333"}
print("kim" in phone)
print("kang" not in phone)
p=phone
print(phone)
print(p)
print(id(phone),id(p))
# ID는 주소 값이 나온다. 동일한 주소를 보고 있으면 같은 주고값이 출력된다.(진짜 주소는 아니고 주소 비스무리한거)

p["kang"]="123"

print(phone)
print(p)
print(id(phone),id(p))