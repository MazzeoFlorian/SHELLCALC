## BASECALC 0.3.5
# A cli based calc that does multiplication, dividation, subtraction and addition.

import time
import cmds
import calcfunc
import os
import style

def start(): # Starting message
    os.system('clear')
    print("Welcome to SHELLCALC", calcfunc.version, "!")
    time.sleep(1)
    print("Please enter a command or type help for a list of commands.")
    time.sleep(1)

def end(): #End routine
    os.system('clear')
    print("Exiting SHELLCALC.")
    time.sleep(1)
    os.system('clear')

def main(): #Main function loop
    x = 1
    #start() initialzes the starting message and goes to the main calculating function.
    start()
    #while x is true, accept commands and do the calculations. If not, exit the program.
    while x == 1: #while x equals 1; basically while true is true.
        inp = str(input())
        if inp == cmds.inputCommand[0]: #addition
            calcfunc.add()
        elif inp == cmds.inputCommand[1]: #subtraction
            calcfunc.sub()
        elif inp == cmds.inputCommand[2]: #multiplication
            calcfunc.mul()
        elif inp == cmds.inputCommand[3]: #division
            calcfunc.div()
        elif inp == cmds.inputCommand[4]: #modulo calc
            calcfunc.mod()
        elif inp == cmds.inputCommand[5]: #exponential calculation
            calcfunc.pot()
        elif inp == cmds.inputCommand[6]: #help
            calcfunc.hlp()
        elif inp ==  cmds.inputCommand[7]: #about
            calcfunc.abt()
        elif inp ==  cmds.inputCommand[8]: #exit
            end()
            break
        elif inp == cmds.inputCommand[9]: #clear screen
            calcfunc.cls()
        else: #if unknown command
            print(f"{style.bcolors.warning}Unknown command. Type help for a list of commands.{style.bcolors.endc}")
            time.sleep(1)

main()