import java.util.*;
public class OE2_David {
    
    
    public static void bubbleSort(int[] array1){
        int ctr = array1.length;
        int temp=0;

        for(int i=0;i<ctr;i++){
            for(int j=1;j<ctr-i;j++){
                if(array1[j-1]>array1[j]){
                    //swapping code
                    temp=array1[j-1];
                    array1[j-1]=array1[j];
                    array1[j]=temp;
                }
            }
        }//end of main for loop
    }
    public static void printArray(int[] array1){
        for(int i=0;i<array1.length;i++){
            System.out.print( array1[i]+ "  ");
        }
        System.out.println("}");
    }
    public static void insertionSort(int array2[]){
        int ctr=array2.length;
        for(int i=1;i<ctr;i++){
            int to_insert = array2[i];//to insert
            int j=i-1;//hole position

            while(j>-1 && array2[j]>to_insert){
                array2[j+1] = array2[j];
                j--;
            }
            array2[j+1]=to_insert;
        }
    }
    public static void main(String[] args) {
    //Code for user input
        Scanner in= new Scanner(System.in);
        int size;
        System.out.print("Enter the desired size of the array : ");
        size= in.nextInt();
        int[] my_array = new int[size];
        for(int i=0;i<size;i++){
            System.out.print("Enter array element for "+i+" index : ");
            my_array[i]=in.nextInt();
        }
        System.out.println("My Array List : "+ Arrays.toString(my_array)+"\n\n");
    //Command to Sort
        boolean wrong=false;
        do{
        System.out.print("What type of sorting would you like to do?\n[1] Insertion\n[2] Bubble Sort\n[3] Exit\nSelect Operation : ");
        int op=in.nextInt();
        
        switch(op){
            case 1:{
                System.out.print("Unsorted Array : { ");
                printArray(my_array);
        
                bubbleSort(my_array);
        
                System.out.print("Sorted Array : { ");
                printArray(my_array);
                wrong=false;
                break;
            }
            case 2:{
                System.out.print("No Insertion Array : { ");
                printArray(my_array);

                insertionSort(my_array);

                System.out.print("Inserted Array : { ");
                printArray(my_array);
                wrong=false;
                break;
            }
            case 3:{
                System.out.print("Thanks for using my Array Sorting Code!");
                wrong=false;
                break;
            }
            default:{
                System.out.println("\nPlease enter a valid number!\n");
                wrong=true;
            }
        }
        }while(wrong); 
    }//end of main line
}//end of code
