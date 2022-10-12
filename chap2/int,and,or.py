age = int(input("how old are you?")) #input으로 하나의 return값을 입력 할 수 있다 현재 내가 원하는건 숫자이다 
#""안에 있는것은 무엇을 쓰던 문자로 인식하기 때문에 int를 넣었다 만약 20을 입력한다 치면 int("20") 이게 결과값이다 따옴표 안에 문자로 있지만 int로 
# 숫자로 인식하게끔 변경해 주었다

if age < 18: 
    print("you can't drink")

elif age <= 36 and age >= 18: #and는 양쪽 두개가 모두 참이어야 직동된다 해석하면 18보다 같거나 크고, 36보다 작거나 같은 수를 입력해야 실행된다
    print("you drink beer")

elif age == 60 or age == 50: # or은 둘 중 하나만 참이면 실행된다 해석하면 60 또는 50이 입력되면 실행된다
    print("birthday party!!")


else:
    print("go ahead")