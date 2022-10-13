#파이썬안에 기본적으로 포함되어 있는 함수들이다
#여태 했던 int, input, print 등을 포함해 엄청 많은 종류가 있다

from random import randint

user_choice = int(input("Choose number"))
pc_choice = randint(1, 50)

if user_choice == pc_choice:
    print ("you win computer chose", pc_choice)

elif user_choice > pc_choice:
    print("losercomputer chose", pc_choice)
elif user_choice < pc_choice:
    print("higher!computer chose", pc_choice)