import java.util.*;
public class OE4_David{

public static int my_partition(int arr[],int start,int end){
    int pivot = arr[end];
    int i = start -1;
    for(int j=start;j<=end;j++){
        //if current element arr[a] is less than the pivot 
        if(arr[j]<pivot){
            i+=1;
            int temp =arr[i];
            arr[i] = arr[j];
            arr[j]=temp;
        }
    }
    int temp= arr[i+1];  
    arr[i+1]=arr[end];
    arr[end] =temp;
    return (i+1);
}
public static void my_quicksort(int arr[],int s,int e){
    if (s<=e){
        int p = my_partition(arr,s,e);
        my_quicksort(arr,s,p-1);
        my_quicksort(arr,p+1,e);
    }
}
public static void displayArr(int arr[],int n){
    for(int i=0;i<n;i++){
        System.out.print(arr[i]+" ");
    }
    System.out.println();
}
    public static void main(String[] args){
        Scanner in= new Scanner(System.in);
        //Array Creation
        int size;
        System.out.print("Enter the desired size of the array : ");
        size= in.nextInt();
        int[] my_array = new int[size];
        for(int i=0;i<size;i++){
            System.out.print("Enter array element for "+i+" index : ");
            my_array[i]=in.nextInt();
        }
        //Main Output for Code
        int n = my_array.length;
        System.out.print("=======================\nInput Array :");
        displayArr(my_array,n);

        my_quicksort(my_array,0, n-1);
        System.out.print("Sorted Array :");
        displayArr(my_array,n);
        System.out.println("Minimum Value :"+my_array[0]);
        System.out.print("Maximum Value :"+my_array[my_array.length -1]);



    }
}