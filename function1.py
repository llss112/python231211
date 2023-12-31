#function1.py
# 기본값을 주는 경우
def times(a=10,b=20):
    return a*b

print(times())
print(times(5))
print(times(5,6))

# 키워드 인자(매개변수명을 자세하게 기술)

def connectURI(server,port):
    strURL="http://"+server+":"+port
    return strURL

# 호출
print(connectURI("multi.com","80"))
print(connectURI(port="8080",server="multi.com"))


# 가변 인자 처리 

def union(*ar):
    # 지역변수
    result=[]
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result

# 호축
print(union("HAM","SPAM"))
print(union("HAM","SPAM","EGG"))