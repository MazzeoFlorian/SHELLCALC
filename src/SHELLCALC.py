## BASECALC 0.3.0
# A cli based calc that does multiplication, dividation, subtraction and addition.
# Change log
#
# Version 0.3.0 - Code re-write; Added float calculations. Potency added.
# Version 0.2.0 - Program has end routine, code optimisations, modulo added, renamed from BASECALC to SHELLCALC.
# Version 0.1.0 - Initial version.

import time


x = 1 # for the main routine
version = "0.3.2"

def start(): # Starting message
    print("Welcome to SHELLCALC", version, "!")
    time.sleep(1)
    print("Please enter a calculation type or type HLP for a list of commands.")
    time.sleep(1)

def add(): # Adds two integers
    add_a = int(input("Enter a whole number: "))
    add_b = int(input("Enter a whole number: "))
    print(add_a+add_b)

def add_flt(): # Adds two floats
    add_flt_a = float(input("Enter a float number: "))
    add_flt_b = float(input("Enter a float number: "))
    print(add_flt_a+add_flt_b)

def sub(): # Subtracting two integers
    sub_a = int(input("Enter a whole number: "))
    sub_b = int(input("Enter a whole number: "))
    print(sub_a-sub_b)

def sub_flt(): # Subtracting two float numbers
    sub_flt_a = float(input("Enter a float number: "))
    sub_flt_b = float(input("Enter a float number: "))
    print(sub_flt_a-sub_flt_b)

def mul(): # Multiplication function
    mul_a = int(input("Enter a whole number: "))
    mul_b = int(input("Enter a whole number: "))
    print(mul_a*mul_b)

def mul_flt(): # Multiplies two floats
    mul_flt_a = float(input("Enter a float number: "))
    mul_flt_b = float(input("Enter a float number: "))
    print(mul_flt_a*mul_flt_b)

def div(): # Division function
    div_a = int(input("Enter a whole number: "))
    div_b = int(input("Enter a whole number: "))
    print(div_a+div_b)

def div_flt(): # Multiplies two floats
    div_flt_a = float(input("Enter a float number: "))
    div_flt_b = float(input("Enter a float number: "))
    print(div_flt_a/div_flt_b)

def mod(): # Modulo function
    mod_a = int(input("Enter a whole number: "))
    mod_b = int(input("Enter a whole number: "))
    print(mod_a%mod_b)

def pot(): #Potency function
    pot_a = int(input("Enter a whole number: "))
    pot_b = int(input("Enter the potency as a whole number: "))
    print(pot_a**pot_b)

def hlp(): #Help function, prints all commands
    print("List of commands: ")
    print("")
    print("ADD: Addition.")
    print("ADD FLT: Addition (float)")
    print("SUB: Subtraction.")
    print("SUB FLT: Subtraction (float)")
    print("MUL: Multiplication.")
    print("MUL FLT: Multiplication (float)")
    print("DIV: Division.")
    print ("DIV FLT: Division (float)")
    print("MOD: Modulo.")
    print("POT: Exponentional.")
    print("HLP: Help function.")
    print("END: Ends SHELLCALC.")
    print("ABT: About SHELLCALC.")

def abt():
    print("SHELLCALC Version", version)
    time.sleep(1)
    print("by Florian Mazzeo (2025)")
    time.sleep(1)
    print("More information on https://github.com/MazzeoFlorian/SHELLCALC")
    time.sleep(1)

def end(): #End routine
    print("Good bye!")
    time.sleep(1)

#Basically the main funcion loop.
#start() initialzes the starting message and goes to the main calculating function.

start()

#while x is true, accept commands and do the calculations. If not, exit the program.
while x == 1:
    inp = str(input())
    if inp == "ADD":
        add()
    elif inp == "ADD FLT":
        add_flt()
    elif inp == "SUB":
        sub()
    elif inp == "SUB FLT":
        sub_flt()
    elif inp == "MUL":
        mul()
    elif inp == "MUL FLT":
        mul_flt()
    elif inp == "DIV":
        div()
    elif inp == "DIV FLT":
        div_flt()
    elif inp == "MOD":
        mod()
    elif inp == "POT":
        pot()
    elif inp == "HLP":
        hlp()
    elif inp == "ABT":
        abt()
    elif inp == "END":
        end()
        x = 0
    else:
        print("Unkown command. Type HLP for a list of commands.")
        time.sleep(1)
