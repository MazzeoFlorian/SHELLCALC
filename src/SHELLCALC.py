## SHELLCALC 0.2.0
# A cli based calc that does multiplication, dividation, subtraction and addition.abs
# Change log
#
# Version 0.2.0 - Program has end routine, code optimisations, renamed from BASECALC to SHELLCALC.
# Version 0.1.0 - Initial version

x = 1

def calc():
    a = int(input("Please input an integer: "))
    b = int(input("Please input an integer: "))
    c = str(input("Please give an operator (ADD, SUB, MUL, DIV, MOD): "))
    
    if c == "ADD":
        print(a+b)
    elif c == "SUB":
        print(a-b)
    elif c == "MUL":
        print(a*b)
    elif c == "DIV":
        print(a/b)
    elif c == "MOD":
        print(a%b)
    else:
        print("ERROR 1: NOT A VALID OPERATOR.")

while x == 1:
    calc()

    d = str(input("Do you want to continue?[y/n]: "))
    if d == "n":
        break