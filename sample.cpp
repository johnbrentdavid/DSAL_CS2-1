#include <iostream>
#include <cmath>
using namespace std;
//function for asking repeat the program
bool askRepeat(){
    cout<<"What would you like to do next?\n[1] Use another Operation\n[2] No more\n";
    bool wrong=true;
    int a;
    do{
    cout<< "Command : ";
    cin>>a;
    if (a==1)
        return true;
    else if (a==2){
        cout<<"You are now exiting the program.\n Thank you!";
        return false;
        }
    else
        cout<<"Command Invalid!\n";
    }while(wrong);

}
//functions used for Basic Calculator
void raise(float x,float y,float& z){
    z=x;
    while(y!=1){
        z*=x;
        y--;
    }

 } 
int add(float a,float b){
    return a+b;
}
int sub(float a,float b){
    return a-b;
}
int mul(float a,float b){
    return a*b;
}
int div(float a,float b){
    return a/b;
} 
void basicCalculator(){
float a,b,c=0;
     char d;
        cout<<"Please enter the first number\n";
        cin>>a;
        cout<<"\nPlease enter the second number\n";
        cin>>b;
        for (int i=0;i<1;i++){
            cout<<"\nPlease choose what operation to use: + - x / ^ : ";
            cin>>d;
        switch(d){
        case '+':{  
            c=add(a,b);   
            break;
        }
        case '-':{
            c=min(a,b);
            break;
        }  
        case 'x':{
            c=mul(a,b);
            break;
        }
        case '/':{
            div(a,b);
            break;        
        }
        case '^':{
            raise(a,b,c);
            break;
        }
        default:{
            cout<<"\nPlease Enter a Valid Operation!\n";
            i--;
            
        }
               
        }//end of switch
        }//end of loop
        switch(d){
        case '+':{  
            cout<<"The sum of the two inputs is: "<<c<<endl;
            break;
        }
        case '-':{
            cout<<"The difference of the two inputs is: "<<c<<endl;
            break;
        }  
        case 'x':{
            cout<<"The product of the two inputs is: "<<c<<endl;
            break;
        }
        case '/':{
            cout<<"The quotient of the two inputs is: "<<c<<endl;
            break;        
        }
        case '^':{
            cout<<"The raised value of "<<a<<" is: "<<c<<endl;
            break;
        }

        }
}


 int main(){
     int op;
     bool repeat =true;
     do{
     cout<<"\nWhat Operation would you like to use?\n[1] Basic Calculator\n[2] Create Array \n[0] Exit the Program\n\nCommand : ";
     cin>>op;
     switch (op){
         case 0:{
             cout<<"You are now exiting the program.\n Thank you!";
             repeat=false;
             break;
         }
         case 1:{
             cout<<"Greetings! you are now using Basic Calculator\n";
             basicCalculator();
             repeat= askRepeat();
             break;
         }
         case 2:{
             cout<<"Greetings! You are now using Array Creation\n";
             repeat = askRepeat();
             break;
         }
         default:{
             cout<<"Error try again\n";
         }
     }
     }while(repeat);
return 0;
 }