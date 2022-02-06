#include <iostream>
#include <cstdlib>
#include <stack>
#include <ctime>
#include <queue>
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
void giveCard(stack <int> &newDeck,int p1Cards[],int p2Cards[],int hide){
    bool p1Turn=false;
    int i=0,j=0;//i=player 1||j=player 2
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
}
/*converts int value to player recognizable value
    1	2	3	4	5	6	7	8	9	10	11	12	13  Diamonds
    14	15	16	17	18	19	20	21	22	23	24	25	26  Spades
    27	28	29	30	31	32	33	34	35	36	37	38	39  Hearts
    40	41	42	43	44	45	46	47	48	49	50	51	52  Clubs
*/
void showCard(int p1Cards[],int p2Cards[]){
    for(int i=0;i< 25;i++)
        switch (p1Cards[i]){
            
        }
    for(int i=0;i< 26 ;i++)
        cout<<p2Cards[i]<<" ";
}
int main(){
    stack <int> cardDeck;
    queue <int> usedCard;
    int cards[52];
    int p1Hand[25];
    int p2Hand[26];
    int monkey;//used for the hidden card

    mixDeck(cardDeck,cards);
    giveCard(cardDeck,p1Hand,p2Hand,monkey);
    usedCard.push(monkey);//pushes the monkey card at the queue
    showCard(p1Hand,p2Hand);

}