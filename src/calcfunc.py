#Calculation functions

import time
import style
import os

version = "0.4" #semantic version numbering


def add(): #Adds two numbers
    add2_a = input("Enter number: ")
    add2_b = input("Enter number: ")
    try:
        num1 = float(add2_a)
        num2 = float(add2_b)
        if num1.is_integer() and num2.is_integer():
            num1 = int(add2_a)
            num2 = int(add2_b)
            num3 = num1+num2
            print(f"{num3:,}")
        else:
            num3 = num1+num2
            float(num3)
            print(f"{num3:,}")
    except ValueError:
        print(f"{style.bcolors.warning}Input wasn't a number.{style.bcolors.endc}")

def sub(): #Subtracts two numbers
    sub1 = input("Enter number: ")
    sub2 = input("Enter number: ")
    try:
        num1 = float(sub1)
        num2 = float(sub2)
        if num1.is_integer() and num2.is_integer():
            num1 = int(sub1)
            num2 = int(sub2)
            num3 = num1-num2
            print(f"{num3:,}")
        else:
            num3 = num1-num2
            float(num3)
            print(f"{num3:,}")
    except ValueError:
        print(f"{style.bcolors.warning}Input wasn't a number.{style.bcolors.endc}")

def mul(): #Multiplies two numbers
    mul1 = input("Enter number: ")
    mul2 = input("Enter number: ")
    try:
        num1 = float(mul1)
        num2 = float(mul2)
        if num1.is_integer() and num2.is_integer():
            num1 = int(mul1)
            num2 = int(mul2)
            num3 = num1*num2
            print(f"{num3:,}")
        else:
            num3 = num1*num2
            float(num3)
            print(f"{num3:,}")
    except ValueError:
        print(f"{style.bcolors.warning}Input wasn't a number.{style.bcolors.endc}")

def div(): #Divides two numbers
    div1 = input("Enter number: ")
    div2 = input("Enter number: ")
    try:
        num1 = float(div1)
        num2 = float(div2)
        if num1.is_integer() and num2.is_integer():
            num1 = int(div1)
            num2 = int(div2)
            num3 = num1/num2
            print(f"{num3:,}")
        else:
            num3 = num1/num2
            float(num3)
            print(f"{num3:,}")
    except ValueError:
        print(f"{style.bcolors.warning}Input wasn't a number.{style.bcolors.endc}")

def mod(): #Divides two numbers
    mod1 = input("Enter number: ")
    mod2 = input("Enter number: ")
    try:
        num1 = float(mod1)
        num2 = float(mod2)
        if num1.is_integer() and num2.is_integer():
            num1 = int(mod1)
            num2 = int(mod2)
            num3 = num1%num2
            print(f"{num3:,}")
        else:
            num3 = num1%num2
            float(num3)
            print(f"{num3:,}")
    except ValueError:
        print(f"{style.bcolors.warning}Input wasn't a number.{style.bcolors.endc}")

def pot(): #Divides two numbers
    pot1 = input("Enter number: ")
    pot2 = input("Enter potency: ")
    try:
        num1 = float(pot1)
        num2 = float(pot2)
        if num1.is_integer() and num2.is_integer():
            num1 = int(pot1)
            num2 = int(pot2)
            num3 = num1**num2
            print(f"{num3:,}")
        else:
            num3 = num1**num2
            float(num3)
            print(f"{num3:,}")
    except ValueError:
        print(f"{style.bcolors.warning}Input wasn't a number.{style.bcolors.endc}")

def hlp(): #Help function, prints all commands
    print("List of commands: ")
    print("")
    print("add: Addition.")
    print("sub: Subtraction.")
    print("mul: Multiplication.")
    print("div: Division.")
    print("mod: Modulo.")
    print("pot: Exponentional.")
    print("help: Help function.")
    print("exit: Exits SHELLCALC.")
    print("about: About SHELLCALC.")

def abt():
    print("SHELLCALC Version", version)
    time.sleep(1)
    print("by Florian Mazzeo (2025)")
    time.sleep(1)
    print("More information on" + f"{style.bcolors.bold}https://github.com/MazzeoFlorian/SHELLCALC{style.bcolors.endc}")
    time.sleep(1)

def cls():
    os.system('clear')
    print("Please enter a command or type help for a list of commands.")