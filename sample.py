from xmlrpc.client import boolean
#function for Basic Calc
#recursion for getting the factorial
def getFactorial(num1):
    if num1 ==1:
        return 1
    else:
        num2 = num1 -1 
        return(num1 *getFactorial(num2))
def Basic_Calc():
    op = input("What do you want to do?\n[1]ADD\t\t[2]SUBTRACT\n[3]TIMES\t[4]DIV\n[5]REMAINDER\t[6]FACTORIAL\nDecision : ")
    if op == '1':
        num1 = input("Enter your 1st number: ")
        num2 = input("Enter your 2nd number: ")
        print(int(num1)+int(num2))
    elif op =='2':
        num1 = input("Enter your 1st number: ")
        num2 = input("Enter your 2nd number: ")
        print(int(num1)-int(num2))
    elif op =='3':
        num1 = input("Enter your 1st number: ")
        num2 = input("Enter your 2nd number: ")
        print(int(num1)*int(num2))
    elif op =='4':
        num1 = input("Enter your 1st number: ")
        num2 = input("Enter your 2nd number: ")
        print(int(num1)/int(num2))
    elif op == '5':
        num1 = input("Enter your 1st number: ")
        num2 = input("Enter your 2nd number: ")
        print(int(num1)%int(num2))
    elif op == '6':
        num1 = int(input("Enter a base value to factorial: "))
        print("The factorial of",num1,"is",getFactorial(num1))
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
    print("=============================")