#include <iostream>
#include <cstdlib>
#include <stack>
#include <ctime>
#include <queue>
#include <windows.h>

using namespace std;

#define ARRAYLEN(arr) sizeof(arr)/sizeof(arr[0])
//creates the deck organized
void initArray(int cards[]){
    //loop for creating the deck of cards
    for (int i=0;i<52;i++){
        cards[i]=i+1;
    }
}
//shuffles the deck
void mixDeck(stack <int> &newDeck,int cards[]){
    initArray(cards);
    srand(time(0));
    int temp,j;
    //loop for shuffling the array
    for(int i=0;i<52;i++){
        j= (rand()%51)+1;
        
        //Swap the elements of array
        temp = cards[i];
        cards[i]=cards[j];
        cards[j]=temp;
    }
    //push the array value into stack
    for(int i=0;i<52;i++){
        newDeck.push(cards[i]);
    }

}
//distributes the card to the players hand
int giveCard(stack <int> &newDeck,int p1Cards[],int p2Cards[]){
    bool p1Turn=false;
    int i=0,j=0,hide;//i=player 1||j=player 2
    //assign top element to be the monkey
    hide=newDeck.top();
    newDeck.pop();
    //empty out the deck
    while(!newDeck.empty()){
        if (p1Turn){
            p1Cards[i]= newDeck.top();
            newDeck.pop();
            i++;
            p1Turn=false;
        }
        else{
            p2Cards[j]=newDeck.top();
            newDeck.pop();
            j++;
            p1Turn=true;
        }
    }
    return hide;
}
/*converts int value to player recognizable value
    1	2	3	4	5	6	7	8	9	10	11	12	13  Diamonds♦ alt4
    14	15	16	17	18	19	20	21	22	23	24	25	26  Spades♠ alt6
    27	28	29	30	31	32	33	34	35	36	37	38	39  Hearts♥ alt3
    40	41	42	43	44	45	46	47	48	49	50	51	52  Clover♣ alt5
*/
void showCard(int p1Cards[],int p2Cards[]){
    char symbol;
    for(int i=0;i< 25;i++){//displays player1Hand
        if (p1Cards[i]<=13){
            symbol=4;
            switch (p1Cards[i]){
                case 1:cout<<" A"<<symbol;
                break;
                case 11: cout<<" J"<<symbol;
                break;
                case 12: cout<<" Q"<<symbol;
                break;
                case 13: cout<<" K"<<symbol;
                break;
                default: cout<<" "<<p1Cards[i]<<symbol;
            }
        }
        else if (p1Cards[i]<=26 && p1Cards[i]>=14){
            symbol=6;
            switch (p1Cards[i]){
                case 14:cout<<" A"<<symbol;
                break;
                case 24: cout<<" J"<<symbol;
                break;
                case 25: cout<<" Q"<<symbol;
                break;
                case 26: cout<<" K"<<symbol;
                break;
                default: cout<<" "<<p1Cards[i]-13<<symbol;
            }
        }
        else if (p1Cards[i]<=39 && p1Cards[i]>=27){
            symbol=3;
            switch (p1Cards[i]){
                case 27:cout<<" A"<<symbol;
                break;
                case 37: cout<<" J"<<symbol;
                break;
                case 38: cout<<" Q"<<symbol;
                break;
                case 39: cout<<" K"<<symbol;
                break;
                default: cout<<" "<<p1Cards[i]-26<<symbol;
            }
        }
        else if (p1Cards[i]<=52 && p1Cards[i]>=40){
            symbol=5;
            switch (p1Cards[i]){
                case 40:cout<<" A"<<symbol;
                break;
                case 50: cout<<" J"<<symbol;
                break;
                case 51: cout<<" Q"<<symbol;
                break;
                case 52: cout<<" K"<<symbol;
                break;
                default: cout<<" "<<p1Cards[i]-39<<symbol;
            }
        }
    }//end of main for loop
}
//remove the paired cards and put it into a queue
void removeCards(int useDeck[],int p1Cards[],int p2Cards[],bool &turn){

}
int main(){
    stack <int> cardDeck;
    int usedCard[52];
    int cards[52];
    int p1Hand[25];
    int p2Hand[26];
    int monkey;//used for the hidden card
    bool playerTurn=true;

    mixDeck(cardDeck,cards);
    monkey=giveCard(cardDeck,p1Hand,p2Hand);
    usedCard[1]=monkey;//pushes the monkey card at the the start of the array
    showCard(p1Hand,p2Hand);

    removeCards(usedCard,p1Hand,p2Hand,playerTurn);
}