import java.util.Arrays;
import java.util.Scanner;

/*  John Brent David
    CS 2-1
    Outcomes Evaluation 1
    Sir Isaac Morallo
*/
public class OE1_David{
    public static void main(String[] args){
        
        Scanner in= new Scanner(System.in);
        int ch,size,j=1;
        int my_array[]=new int[size];

        //While to repeat the process
        while(j!=0){
        System.out.println("[1] Create an Array list");
        System.out.println("[2] Insert in Array");
        System.out.println("[3] Search in Array");
        System.out.println("[4] Delete in Array");
        System.out.println("[0] Exit");
        System.out.print("Select an Operation: ");
        ch=in.nextInt();

        switch(ch){
            case 0:{
                System.out.println("You have now exited the program! Thank you User!");
                j--;
                break;
            }
            case 1:{
                System.out.println("\nCreate an Array List");

                //Input for size
                System.out.print("Enter the size of the Array: ");
                size=in.nextInt();
                

                //Input for Elements
                for(int i=0;i<size;i++){
                System.out.print("Enter array element for "+i+"th index : ");
                my_array[i]=in.nextInt();
                }

                System.out.println("My Array List : "+ Arrays.toString(my_array));
                break;
            }
            case 2:{
                System.out.println("\nInsert new element in Array");
                int new_array[]=new int[size+1];

                //Copy the array to expanded array
                for(int i=0;i<size;i++){
                    new_array[i]=my_array[i];
                }

                System.out.print("Enter a new element in the Array : ");
                new_array[size] =in.nextInt();
                System.out.println("This is the Array with newly inserted element : "+ Arrays.toString(new_array));



                

            }
        }//end of switch

        
        
        
        
        
    }//end of while loop
    }//end of main method
}