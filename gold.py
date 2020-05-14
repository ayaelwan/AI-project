#include <iostream>
using namespace std;
int main()
{
    int year ,month ;
    double oil , gold , dollar, the_gram;

   cout<<"Enter the current  year : ";
   cin>>year;
   if (year==2020)
   {
        cout<<"Enter the current  month : ";
   cin>>month;
    if (month<5)
        cout<<"ERROR   " ;
        else
            if (month>=5&&month<=12 ){
            cout<<"please enter the oil price : ";
cin>>oil;
cout<<"please enter the dollar price : ";
cin>>dollar;
cout<<"enter the gram of the gold that you want to buy is it 18gm ,21gm ,24gm : ";
cin>>the_gram;}
if (the_gram==18){
     gold=((oil*dollar)+10)+24/the_gram;
}else  if (the_gram==21){
    gold=((oil*dollar)+15)+24/the_gram;
}else if (the_gram==24){
 gold=((oil*dollar)+20)+24/the_gram;
}
cout<<"the price one gram of gold is :"<<gold;}

else
    cout<<"ERROR";
 return 0;
}
