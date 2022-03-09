#John Brent David
#CS 2-1
#Function for Fibonacci 
from pickle import APPEND
from tracemalloc import start
import random

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
#Recursion calling function
# I have created a simple game in which you will choose which has more in an array Odd or Even?
def is_even(n):
    if n == 0:
        return True
    else:
        return not_even(n-1)

def not_even(n):
    if n == 0:
        return False
    else:
        return is_even(n-1)

#START
repeat = True
while repeat:
    app = int(input("What application would you like to use?\n[1]Fibonacci\t\t[2]Factorial\n[3]Reverse a number\t[4]Reverse a Word\n[5]Tower of Hanoi\t[6]Odd or Even Game\n[0]EXIT\nDecision : "))
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
    elif app== 6:
        numEven =0
        numOdd = 0
        arr=[]
        #this gives the random value to the array
        for i in range (0,49):
            arr.append(random.randint(1,100))
            print(arr[i], end=" ")
            is_it_even=is_even(arr[i])
            #if statement to know if the element at ith index is even or odd then add 1 to the correct category
            if is_it_even:
                numEven +=1
            else:
                numOdd +=1
        choice = int(input("\nWhat do you think has more on the list?\n[1]Odd\t[2]Even\nDecision: "))
        if choice ==1:
            if numEven < numOdd:
                print("Congrats!You guessed it correctly")
            else:
                print("Unfortunately!You guessed it wrong")
        elif choice == 2:
            if numOdd < numEven:
                print("Congrats!You guessed it correctly")
            else:
                print("Unfortunately!You guessed it wrong")
        else:
            print("Wrong input!")
    elif app == 0:
        print("You are now exiting the Program!\nThanks for trying it")
        repeat = False
    else:
        print("Wrong Input! Try Again")
    print("\n=============================")