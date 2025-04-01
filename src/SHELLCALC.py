## BASECALC 0.3.0
# A cli based calc that does multiplication, dividation, subtraction and addition.

import time

version = "0.3.4"

def start(): # Starting message
    print("Welcome to SHELLCALC", version, "!")
    time.sleep(1)
    print("Please enter a command or type HLP or help for a list of commands.")
    time.sleep(1)

def add(): # Adds two integers
    add_a = int(input("Enter whole number: "))
    add_b = int(input("Enter whole number: "))
    print(add_a+add_b)

def add_flt(): # Adds two floats
    add_flt_a = float(input("Enter number with decimals: "))
    add_flt_b = float(input("Enter number with decimals: "))
    print(add_flt_a+add_flt_b)

def sub(): # Subtracting two integers
    sub_a = int(input("Enter whole number: "))
    sub_b = int(input("Enter whole number: "))
    print(sub_a-sub_b)

def sub_flt(): # Subtracting two float numbers
    sub_flt_a = float(input("Enter number with decimals: "))
    sub_flt_b = float(input("Enter number with decimals: "))
    print(sub_flt_a-sub_flt_b)

def mul(): # Multiplication function
    mul_a = int(input("Enter whole number: "))
    mul_b = int(input("Enter whole number: "))
    print(mul_a*mul_b)

def mul_flt(): # Multiplies two floats
    mul_flt_a = float(input("Enter number with decimals: "))
    mul_flt_b = float(input("Enter number with decimals: "))
    print(mul_flt_a*mul_flt_b)

def div(): # Division function
    div_a = int(input("Enter whole number: "))
    div_b = int(input("Enter whole number: "))
    print(div_a+div_b)

def div_flt(): # Multiplies two floats
    div_flt_a = float(input("Enter number with decimals: "))
    div_flt_b = float(input("Enter number with decimals: "))
    print(div_flt_a/div_flt_b)

def mod(): # Modulo function
    mod_a = int(input("Enter whole number: "))
    mod_b = int(input("Enter whole number: "))
    print(mod_a%mod_b)

def pot(): #Potency function
    pot_a = int(input("Enter whole number: "))
    pot_b = int(input("Enter the potency as a integer: "))
    print(pot_a**pot_b)

def hlp(): #Help function, prints all commands
    print("List of commands (non case-sensitive): ")
    print("")
    print("ADD: Addition.")
    print("ADD FLT: Addition (float)")
    print("SUB: Subtraction.")
    print("SUB FLT: Subtraction (float)")
    print("MUL: Multiplication.")
    print("MUL FLT: Multiplication (float)")
    print("DIV: Division.")
    print("DIV FLT: Division (float)")
    print("MOD: Modulo.")
    print("POT: Exponentional.")
    print("HLP/HELP: Help function.")
    print("END/EXIT/QUIT: Ends SHELLCALC.")
    print("ABT/ABOUT: About SHELLCALC.")

def abt():
    print("SHELLCALC Version", version)
    time.sleep(1)
    print("by Florian Mazzeo (2025)")
    time.sleep(1)
    print("More information on https://github.com/MazzeoFlorian/SHELLCALC")
    time.sleep(1)

def end(): #End routine
    print("Ending SHELLCALC.")
    time.sleep(1)

def main(): #Main function loop
    x = 1
    #start() initialzes the starting message and goes to the main calculating function.
    start()
    #while x is true, accept commands and do the calculations. If not, exit the program.
    while x == 1: #while x equals 1; basically while true is true.
        inp = str(input())
        if inp == "ADD" or inp == "add":
            add()
        elif inp == "ADD FLT" or inp == "add flt":
            add_flt()
        elif inp == "SUB" or inp == "sub":
            sub()
        elif inp == "SUB FLT" or inp == "sub flt":
            sub_flt()
        elif inp == "MUL" or inp == "mul":
            mul()
        elif inp == "MUL FLT" or inp == "mul flt":
            mul_flt()
        elif inp == "DIV" or inp == "div":
            div()
        elif inp == "DIV FLT" or inp == "div flt":
            div_flt()
        elif inp == "MOD" or inp == "mod":
            mod()
        elif inp == "POT" or inp == "pot":
            pot()
        elif inp == "HLP" or inp == "hlp" or inp == "help":
            hlp()
        elif inp == "ABT" or inp ==  "abt" or inp ==  "about":
            abt()
        elif inp == "END" or inp ==  "end" or inp ==  "quit" or inp ==  "QUIT" or inp ==  "exit" or inp ==  "EXIT":
            end()
            break
        else:
            print("Unkown command. Type HLP or help for a list of commands.")
            time.sleep(1)

main()