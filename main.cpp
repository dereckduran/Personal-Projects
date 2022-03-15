#include <iostream>
#include "Inventory.h"
using namespace std;

int main(){
    Inventory inventory;
    int aQuantity = 0;
    int anItemNumber = 0;
    double aCost = 0;

    cout<< "This program calculates the \ntotal cost of an item in your inventory. \n\n";
    
    cout<<"Please enter the identification number of the item."<<endl;
    cin>> anItemNumber;
    while(anItemNumber < 0){
        cout<< "Invalid item number, please enter a positive number."<< endl;
        cin>>anItemNumber;
    }
    inventory.setItemNumber(anItemNumber);

    cout<<"Please enter the quantity of the item #" << inventory.getItemNumber() <<endl;
    cin>>aQuantity;
    while(aQuantity < 0){
        cout<< "Invalid quantity, please enter a positive number."<< endl;
        cin>>aQuantity;
    }
    inventory.setQuantity(aQuantity);

    cout<<"Now finally, please enter the cost per unit of item #"<< inventory.getItemNumber() << endl;
    cin>> aCost;
    while(aCost < 0.01){
        cout<< "Invalid cost, please enter a positive number."<< endl;
        cin>>aCost;
    }
    inventory.setCost(aCost);

    inventory.setTotalCost();

    cout<<"___________________________"<<endl;
    cout<< "Calculating the total cost of item #"<< inventory.getItemNumber()<< endl;
    cout<< "The total cost of item #"<< inventory.getItemNumber() << " with "<< inventory.getQuantity() << " units at the unit price of " << inventory.getCost()<<endl;
    cout<< "is " << inventory.getTotalCost()<< endl;


}