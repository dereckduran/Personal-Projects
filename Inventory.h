#ifndef INVENTORY_H
#define INVENTORY_H

class Inventory{
private:
    int itemNumber; 
    int quantity;
    double cost;
    double totalCost;

public:
    Inventory();
    Inventory(int itemNumber,int quantity,double cost);
    ~Inventory();
    void setItemNumber(int anItemNumber);
    void setQuantity(int aQuantity);
    void setCost(double aCost);
    void setTotalCost();
    int getItemNumber();
    int getQuantity();
    double getCost();
    double getTotalCost();

};
#endif