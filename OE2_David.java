public class OE2_David {
    
    public static void bubbleSort(int[] array1){
        int ctr = array1.length;
        int temp=0;

        for(int i=0;i<ctr;i++){
            for(int j=1;j<ctr-i;j++){
                System.out.println("ELements ["+ array1[j-1]+"] ["+ array1[j]+"]");
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
    int[] my_array = {14,33,27,35,10};
    int[] my_array2 = {14,33,27,10,35,19,42,44};

        System.out.print("Unsorted Array : { ");
        printArray(my_array);

        bubbleSort(my_array);

        System.out.print("Sorted Array : { ");
        printArray(my_array);

        System.out.print("No Insertion Array : { ");
        printArray(my_array2);

        insertionSort(my_array2);

        System.out.print("Inserted Array : { ");
        printArray(my_array2);
    }
}
