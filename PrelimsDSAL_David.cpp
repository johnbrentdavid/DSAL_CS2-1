#include <iostream>

using namespace std;

// John Brent David CS 2-1
// Prelims for DSAL
void initArray(int arr[],int size){
    cout<<"Enter elements of array \n";
    for(int i=0;i<size;i++){
         cout<<i+1<<" element : ";
         cin>>arr[i];
    }
}

void Insert(int arr[],int size){
    int toinsert,newsize=size+1;
    cout<<"Enter the element to insert : ";
    cin>>toinsert;
    int newArr[newsize];
    
    for(int i=0;i<size;i++){//loop for duplicating array
        newArr[i]=arr[i];
    }
    newArr[size]=toinsert;
    cout<<"Array with inserted element : ";
    for(int i=0;i<newsize;i++){//loop for printing inserted array
        cout<<newArr[i]<<" ";
    }
    cout<<"\n================================"<<endl;
}
void Delete(int arr[],int size){
    bool correct=false;
    int del;
    while(!correct){
        for(int i=0;arr[i]!=0;i++){//loop for printing current array
            cout<<arr[i]<<" ";
        }
        cout<<"--> Choose what element to delete : ";
        cin>>del;
        for(int i=0;i<size;i++){//loop for deletion
            if(del==arr[i]){
                correct=true;
                for(int j=i;j<size;j++)
                    arr[j]=arr[j+1];
                cout<<"Successfully deleted!\n";
                break;
            }
        } 
        if(!correct){
            cout<<"Choose an element that exist!\n";
        }
    }//end of while loop

    for(int i=0;i<arr[i]!=0;i++){//loop for printing deleted array
            cout<<arr[i]<<" ";
    }
    cout<<"\n================================"<<endl;
}
int Search(int arr[],int size){
    int find;//number to look for in the array
    cout<<"Enter the element to be searched : ";
    cin>>find;

    for(int i=0;i<size;i++){
         if(arr[i]==find){
             cout<<"Search is Successful!\nPosition of the item searched: "<<i+1;
             cout<<"\n================================"<<endl;
            return 0;
         }
     }
    cout<<"Search is Unsuccessful";
    cout<<"\n================================"<<endl;
    return 0;
}

void Action(int arr[],bool &repeat,int size){
    int action;
    cout<<"What do you want to do next? \n[1] Insertion\n[2] Deletion \n[3] Searching\n[0] Exit\nAction : ";
    cin>>action;
    switch(action){
        case 3:{
            Search(arr,size);
            break;
        }
        case 1:{
            Insert(arr,size);
            break;
        }
        case 2:{
            Delete(arr,size);
            break;
        }
        case 0:{
            repeat=false;
            cout<<"You are now exiting the program! Thank you!";
            break;
        }
        default:{
            cout<<"Wrong Input";
        }

    }
}

int main(){
    int size;
    cout<<"John Brent David\t CS 2-1\nPrelims Code Submission\n\n";
    cout<<"How many elements : ";
    cin>>size;
    int myarray[size];//creation of array
    
    initArray(myarray,size);//creates the array
    bool repeat=true;
    while(repeat){
        Action(myarray,repeat,size);
    }
    
}