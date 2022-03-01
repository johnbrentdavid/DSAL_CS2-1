#Implementation of quick sort algo in python
#trinanslate ko lng yung code ni sir from java

def my_partition(arr,start,end):
    pivot = arr[end]
    i = start-1

    for a in range(start,end+1):
        #if current element arr[a] is less than the pivot 
        if(arr[a]<pivot):
            i+=1
            temp =arr[i]
            arr[i] = arr[a]
            arr[a]=temp
    temp= arr[i+1]    
    arr[i+1]=arr[end]
    arr[end] =temp
    return (i+1)

#quicksort function
def my_quicksort(arr,s,e):
    if s<=e:
        p = my_partition(arr,s,e) 
        my_quicksort(arr,s,p-1)
        my_quicksort(arr,p+1,e)

#display function
def displayArr(arr,n):
    for i in range(0,n):
        print(arr[i], end=" ")
    print()

#start of the main
arr = [1,5,2,3,4]
n = len(arr)
print("=====================")
print("Unsorted List: ",end="")
displayArr(arr,n)
print("\n=====================")
my_quicksort(arr,0,n-1)
print("Sorted List: ",end="")
displayArr(arr,n)


