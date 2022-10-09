def tax(money=1200000): # tax라는 이름의 function를 만들었고 (money라는 parameter를 만듬) = 1200000으로 값을 입력 안할시 출력이 되게 만들었음
    return money * 0.1 #print 대신 return을 넣음 print(money * 0.1) 에서 return으로 바뀌면서 괄호도 같이 뻄 

def tax2(taxmess):
    print("thank you for paying", taxmess)

to_pay = tax(3700000) #return이 아닌 print 였을시 tax()만 하면 되지만 return으로 함수의 값을 받았음 
#여태 print로 출력을 했으면 return은 그 출력값을 돌려받는 것이다
#to_pay는 tax()의 return 값이 된다
tax2(to_pay)
