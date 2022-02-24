from xmlrpc.client import boolean
#function for Basic Calc
def Basic_Calc():
    num1 = input("Enter your 1st number: ")
    num2 = input("Enter your 2nd number: ")
    op = input("What do you want to do?\n[1]ADD\n[2]SUBTRACT\n[3]TIMES\n[4]DIV\n[5]REMAINDER\nDecision : ")
    if op == '1':
        print(int(num1)+int(num2))
    elif op =='2':
        print(int(num1)-int(num2))
    elif op =='3':
        print(int(num1)*int(num2))
    elif op =='4':
        print(int(num1)/int(num2))
    elif op == '5':
        print(int(num1)%int(num2))
    else:
        print("Invalid input")
#function for MAD LIB
def Mad_Lib():
    color = input("Enter a color:")
    pnoun = input("Enter a plural noun:")
    celeb = input("Enter a celebrity: ")
    print ("Roses are",color.lower())
    print(pnoun.lower().title(),"are blue\nI love ", celeb.lower().title())

#START
repeat = True
while repeat:
    app = int(input("What application would you like to use?\n[1]Basic Calculator\n[2]Mad Libs\n[3]EXIT\nDecision : "))
    if app == 1:
        Basic_Calc()
    elif app == 2:
        Mad_Lib()
    elif app == 3:
        print("You are now exiting the Program!\nThanks for trying it")
        repeat = False
    else:
        print("Wrong Input! Try Again")