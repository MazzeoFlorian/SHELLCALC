## BASECALC 0.1.0
# A cli based calc that does multiplication, dividation, subtraction and addition.abs
# Version 0.1.0 can only do integers and two numbers

a = input("Please input the first integer: ")
y = str(input("Input one of the following operators: +, -, *, /: "))
b = input("Input the second integer: ")
if y == "+":
    print(a+b)
elif y == "-":
    print(a-b)
elif y == "*":
    print(a*b)
elif y == "/":
    print(a/b)
else:
    print("ERROR 1: NOT A VALID OPERATOR.")