#include <iostream>
#include <cmath>
using namespace std;
void raise(int x,int y,int& z){
    z=x;
    while(y!=1){
        z*=x;
        y--;
    }
 } 
 int main(){
     int a,b,c=0;
     char d;
        cout<<"Please enter the first number\n";
        cin>>a;
        cout<<"\nPlease enter the second number\n";
        cin>>b;
        for (int i=0;i<1;i++){
            cout<<"\nPlease choose what operation to use: + - x / ^ : ";
            cin>>d;
            if(d=='+')
                c=a+b;
            else if(d=='-')
                c=a-b;
            else if(d=='x')
                c=a*b;
            else if(d=='/')
                c=a/b;
            else if (d=='^')
                raise(a,b,c);
            else{
                cout<<"\nPlease Enter a Valid Operation!\n";
                i--;
            }   
               
        }
        if(d=='+')
            cout<<"The sum of the two inputs is: "<<c;
        else if(d=='-')
            cout<<"The difference of the two inputs is: "<<c;
        else if(d=='x')
            cout<<"The product of the two inputs is: "<<c;
        else if(d=='/')
            cout<<"The quotient of the two inputs is: "<<c;
        else if (d=='^')
            cout<<"The raised value of "<<a<<" is: "<<c;
        
return 0;
 }