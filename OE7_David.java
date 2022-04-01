import java.util.Scanner;
import java.util.Hashtable;

public class OE7_David {
    public static void main(String[] args) {
        Scanner in= new Scanner(System.in);
        Hashtable<String, String> ht = new Hashtable<>();
        
        
        //For asking user how many values will they enter
        System.out.print("Hello User how many values would you like to add in the hashtable: ");
        int size = in.nextInt();
        
        //loop to initialize the hashtable with values
        String student_no="", student_name=""; 
        for(int i=0;i<size;i++){
            System.out.print("Student Number: ");
            student_no = in.next();
            System.out.print("Student Lastname: ");
            student_name = in.next();
            ht.put(student_no,student_name);
        }
        System.out.println(ht);

        //main while loop
        boolean repeat=true;
        int app;
        while(repeat){//ADDITIONAL DELETE OPERATION TO ALSO IMPLEMENT DELETION
                System.out.print("What do you want to do next?\n[1]Insert\t\t[3]Delete\n[2]Search\t\t[4]Print\n[0]Exit\nDecision: ");
                app = in.nextInt();
                switch (app){
                    case 1://INSERT
                        System.out.print("Student Number: ");
                        student_no = in.next();
                        System.out.print("Student Lastame: ");
                        student_name = in.next();
                        ht.put(student_no,student_name);
                        System.out.println("Successfully Added");
                        break;
                    case 2://SEARCH
                    /*I have gone a little bit overboard on the search since the user can search:
                    the student number or the student lastname this is possible because of the function
                    .containsKey()for student_num and .containsValue() for student_lname
                    */ 
                        System.out.print("What do you want to search\n[1]Student Number\n[2]Student Lastname\nDecision: ");
                        int decide = in.nextInt();
                        String searching;
                        switch(decide){
                            case 1://Student Number
                                System.out.print("Student Number to search: ");
                                searching = in.next();
                                if(ht.containsKey(searching)){//Student number is considered as the key
                                    System.out.println("Yes the Student Number is in the HASHTABLE");
                                }
                                else{
                                    System.out.println("No the Student Number is not in the HASHTABLE");
                                }
                                break;
                            case 2://Student Name
                            System.out.print("Student Lastname to search: ");
                                searching = in.next();
                                if(ht.containsValue(searching)){//checks the hashtable for student name
                                    System.out.println("Yes the Student Lastname is in the HASHTABLE");
                                }
                                else{
                                    System.out.println("No the Student Lastname is not in the HASHTABLE");
                                }
                                break;
                            default:
                                System.out.println("Wrong Input!");
                        }
                        break;
                    case 3://DELETE
                        System.out.println("Before: " + ht);
                        System.out.print("Student Number to Delete:");
                        String del = in.next();
                        ht.remove(del);
                        System.out.println("After: "+ht);
                        break;
                    case 4://PRINT
                        System.out.println(ht);
                        break;
                    case 0:
                        repeat = false;
                        break;
                    default:
                        System.out.println("Wrong Input! Try Again! ");
                }


        }


    }//end of main 
}//end of class