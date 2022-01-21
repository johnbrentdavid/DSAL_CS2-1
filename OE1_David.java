import java.util.Arrays;
import java.util.Scanner;


/*  John Brent David
    CS 2-1
    Outcomes Evaluation 1
    Sir Isaac Morallo
*/
public class OE1_David{
    public static void createArray(int[] our_array){
        Scanner in= new Scanner(System.in);
        int size;

        //Initial Create an Array
        System.out.println("\nCreate an Array List");      
         //Input for size
        System.out.print("Enter the size of the Array: ");
        size=in.nextInt();
        int my_array[]=new int[size];

        //Input for Elements
        for(int i=0;i<size;i++){
            System.out.print("Enter array element for "+i+" index : ");
            my_array[i]=in.nextInt();
        }

        System.out.println("My Array List : "+ Arrays.toString(my_array)+"\n\n");
    }
    public static void main(String[] args){
        
        Scanner in= new Scanner(System.in);
        int ch,size,j=1;

        //Initial Create an Array
        System.out.println("\nCreate an Array List");      
         //Input for size
        System.out.print("Enter the size of the Array: ");
        size=in.nextInt();
        int my_array[]=new int[size];

        //Input for Elements
        for(int i=0;i<size;i++){
            System.out.print("Enter array element for "+i+" index : ");
            my_array[i]=in.nextInt();
        }

        System.out.println("My Array List : "+ Arrays.toString(my_array));
        //end of initial creation
        
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
                createArray(my_array);
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
                System.out.println("This is the Array with newly inserted element : "+ Arrays.toString(new_array)+"\n\n");
                break;
            }
            case 3:{
                System.out.print("What number would you like for me to search in the array? ");
                int search;
                search = in.nextInt();
                boolean searched =false;

                //for loop to search for the input
                for(int i=0;i<size;i++){
                    if(search==my_array[i]){
                        System.out.println("Your number "+search+" is founded at index "+i+" of the array.\n\n");
                        searched=true;
                    }
                }
                    if(searched==false)
                        System.out.println("Your number is not founded at index on the array.\n\n");

                break;
            }
            case 4:{
                System.out.print("What number would you like for me to delete in the array "+Arrays.toString(my_array)+" ?");

                int delete_index,delete=in.nextInt();
                int delete_array[]=new int[size-1];
                boolean deleted=false;

                for(int i=0;i<size;i++){
                    if(delete==my_array[i]){
                        delete_index=i;
                        deleted=true;
                        for(int k=0;k<delete_index;k++){
                            delete_array[k]=my_array[k];
                        }
                        for(int k=delete_index;k<size-1;k++){
                            delete_array[k]=my_array[k+1];
                        }
                    }
                }
                if(deleted==false)
                    System.out.println("Your number has not been found on the current array.\n\n");
                else
                    System.out.println("Your new array with deleted element is now  "+Arrays.toString(delete_array)+".\n\n");
                break;
                   
            }
        }//end of switch
    }//end of while loop
    }//end of main method
}