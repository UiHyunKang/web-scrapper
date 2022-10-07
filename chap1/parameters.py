def abcd():
    print("hello how r u? ")

abcd()

#아래는 function에서 사용할 수 있는 variables 를 추가한 내용이다 
#def abcd(여기를 parameters)라고 함

def abc(name):#name 이라는 이름을 추가해 줌 
    print("hello", name, "how r u?") # name이라는 이름(variables)에 데이터를 받겠다


abc("brian") #function을 실행시키고 name 이라는 이름에 brian 이라는 데이터를 넣어줌
abc(123) #name 이라는 이름에 다른 데이터를 넣어도 잘 작동되는 모습
abc("sung")
#하나 더 만들어보자

def a1(abc):
    print("i love you", abc)

a1(any) #괄호안에 ""를 안넣으면 문자로 인식 안함
a1("any")