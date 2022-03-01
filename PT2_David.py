#John Brent David
#CS 2-1
#Function for Fibonacci 
from tracemalloc import start


next_num =1
prev_num =0
total_num =0
def Fibonacci(num1):
    global next_num #use global variable to overwrite a global variable inside a function
    global prev_num #only works when using python
    global total_num
    if(num1 >0):
        total_num = (prev_num + next_num)
        prev_num = next_num
        next_num = total_num
        print(total_num," ",end="")
        Fibonacci(num1-1)
#function for factorial
def getFactorial(num1):
    if num1 ==1:
        return 1
    else:
        num2 = num1 -1 
        return(num1 *getFactorial(num2))
#function to reverse the number
def reverseNum(num):
    if num<10:
        print(num)
        return
    else:
        print(num%10,end="") #use end = "" when printing to prevent newline when printing
        reverseNum(int(num/10))
#function to reverse a word
def reverseWord(word):
    if len(word)==0:
        return word
    else:
        return reverseWord(word[1:])+word[0]
#function for tower of hanoi
start_rod = []
mid_rod = []
end_rod = []
def initRod(num):#WE USE STACK here the method APPEND is == to push in other languages
    global start_rod
    if num<1:
        return
    else:
        print(num)
        start_rod.append(num)
        print(start_rod.top())
        initRod(num-1)

def towerofHanoi():
    global start_rod
    global mid_rod
    global end_rod

#START
repeat = True
while repeat:
    app = int(input("What application would you like to use?\n[1]Fibonacci\t\t[2]Factorial\n[3]Reverse a number\t[4]Reverse a Word\n[5]Tower of Hanoi\n[0]EXIT\nDecision : "))
    if app == 1:
        num1 = int(input("How many # to display on fibonacci series: "))
        Fibonacci(num1)
    elif app == 2:
        num1 = int(input("Enter a base value to factorial: "))
        print("The factorial of",num1,"is",getFactorial(num1)) 
    elif app == 3:
        num1 = int(input("Enter a value to be reversed: "))
        reverseNum(num1)   
    elif app == 4:
        word = str(input("Enter a value to be reversed: "))
        print("The reverse of the word is :",reverseWord(word))
    elif app == 5:
        num = int(input("Enter the number of rings: "))
        initRod(num)

    elif app == 0:
        print("You are now exiting the Program!\nThanks for trying it")
        repeat = False
    else:
        print("Wrong Input! Try Again")
    print("\n=============================")