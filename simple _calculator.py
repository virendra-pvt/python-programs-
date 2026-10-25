a=int(input("Enter a number: "))
op=input("Enter an operator (+, -, *, /): ")
b=int(input("Enter another number: "))
if op == '+':
    print(a+b)
if op == '-':
    print(a-b)
if op == '*':
    print(a*b)
if op == '/':
    if b != 0:
        print(a/b)
    else:
        print("Error: Division by zero is not allowed.")
        