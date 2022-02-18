//John Brent David CS 2-1
//OE3
import java.util.*;

public class singlelinkedlist{

    class Node{
        int data;
        Node next;
        //constructor-defined method
        public Node(int data){
            this.data = data;
            this.next = null;
        }
    }

//represents the head and the tail
    public Node head= null;
    public Node tail = null;

//method to add in the linked list
    public void addNode(int data){
        //ability to create node using instance of the Node
        Node newNode = new Node(data);

        //checker - if the list is empty
        if(head == null){
            head = newNode;
            tail = newNode;
        }
        else{ 
            tail.next = newNode;
            tail = newNode;
        }
    }
//method to remove in the linked list
    public void removeNode(int index){
    if(index == 0){
        this.head = head.next;
    }
    Node current = this.head;
    Node previous = this.head;
    while(index+1!=1){
        previous=current;
        current = current.next;
        index--;
    }
    //this is the actual part that removes
    previous.next = current.next;
    current = null;
} 
//method for printing linked list
    public void printNode(){

        Node current = head;

    if(head == null){
            System.out.print("Link list is empty!");
            return;
    }
    System.out.println("Node of the linked list...");
    while(current != null){
        System.out.print("{" +current.data+"}");
        current = current.next;
    }
    System.out.println();
    }

    public static void main(String[] args){
      singlelinkedlist myList = new singlelinkedlist();
      int add,remove;
      boolean repeat=true;
      int action;
      Scanner in = new Scanner(System.in);
      while(repeat){
          System.out.print("What do you want to do?\n[1]Add element\n[2]Remove Element\n[3]Print List\n[4]Exit\nUser Input : ");
          action = in.nextInt();
          switch(action){
            case 1:{
                System.out.print("What value do you want to add : ");
                add = in.nextInt();
                myList.addNode(add);
                System.out.println("Succesfully added\n==========================");
                break;
            }
            case 2:{
                System.out.print("What index do you want to remove : ");
                remove = in.nextInt();
                myList.removeNode(remove);
                System.out.println("Succesfully removed\n==========================");
                break;
            }
            case 3:{
                myList.printNode();
                System.out.println("==========================");
                break;
            }
            case 4:{
                System.out.print("Thanks for trying my code!\n-by John Brent David");
                repeat=false;
                break;
            }
            default:{
                System.out.print("Invalid User Input!");
            }
        }//end of switch statement 
      }//end of main loop

    }//end of main method
}