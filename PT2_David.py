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
def printRods(start_rod,aux_rod,des_rod):
    print("Start Rod :",end=" ")
    for i in range (0,len(start_rod)):
        print(start_rod[i],end=" ")
    print("\nAux Rod : ",end=" ")
    for i in range (0,len(aux_rod)):
        print(aux_rod[i],end=" ")
    print("\nDes Rod : ",end=" ")
    for i in range (0,len(des_rod)):
        print(des_rod[i],end=" ")
    print("\n------------------")
#main function of tof
def towerofHanoi(num,start,aux,des,source,destination,auxiliary):
    if num == 1:
        des.append(start.pop(len(start)-1))
        print ("Move disk 1 from",source,"to",destination)
        return
    towerofHanoi(num-1,start,des,aux,source, auxiliary, destination)
    des.append(start.pop(len(start)-1))#transfer the top most element of start array
    print ("Move disk",num,"from",source,"to",destination)
    towerofHanoi(num-1,aux,start,des,source, auxiliary, destination)   
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
        value=num #value as placeholder to init start array
        start_rod=[]
        aux_rod=[]
        des_rod=[]
        for i in range (0,num):
            if i==num:
                break
            else:
                start_rod.append(value)
                value-=1
        print("------------------\n   START Position\n------------------")
        printRods(start_rod,aux_rod,des_rod)#Prints Before
        towerofHanoi(num,start_rod,aux_rod,des_rod,"Start","Des","Aux")
        print("------------------\n   END Position\n------------------")
        printRods(start_rod,aux_rod,des_rod)#Prints After
    elif app == 0:
        print("You are now exiting the Program!\nThanks for trying it")
        repeat = False
    else:
        print("Wrong Input! Try Again")
    print("\n=============================")