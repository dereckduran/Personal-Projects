#include <iostream>
#include "Inventory.h"
using namespace std;

Inventory::Inventory(){

    int itemNumber = 0;
    int quantity = 0;
    double cost = 0.0; 
    double totoalCost = 0.0;
}
Inventory::Inventory(int itemNumber,int quantity, double cost)
{
    
}
Inventory::~Inventory(){
    cout<<"________________________________"<<endl;
    cout<<"Destroying object..."<<endl;
    cout<<"Object Destroyed."<<endl;
    system("pause");
}

void Inventory::setItemNumber(int anItemNumber)
{
    itemNumber = anItemNumber;
}

void Inventory::setQuantity(int aQuantity)
{
    quantity = aQuantity;
}

void Inventory::setCost(double aCost)
{
    cost = aCost;
}

void Inventory::setTotalCost()
{
    totalCost = getQuantity() * getCost();
}

int Inventory::getItemNumber()
{
    return itemNumber;
}

int Inventory::getQuantity()
{
    return quantity;
}

double Inventory::getCost()
{
    return cost;
}
double Inventory::getTotalCost()
{
    return totalCost;
}