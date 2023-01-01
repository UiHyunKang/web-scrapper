playing = True

while playing:
    first = int(input("choose number"))

    second = int(input("choose another number"))

    op = input("choose an operation \n options are: + , -, * or /. \n write 'exit' to finish.")
    
    if op == '+':
        print(first + second)

    elif op == '-':
        print(first - second)

    elif op == '*':
        print(first * second)

    elif op == '/':
        print(first / second)
    