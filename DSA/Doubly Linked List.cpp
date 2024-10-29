#include<iostream>


using namespace std;


class Dlinked_list
{
private:
class node
{
    public:
    int data;
    node *next;
    node *prev;

    node(int value)
    : data(value), next(nullptr), prev(nullptr)
    {}

};

node *head; // Declare head without initialization

public:
    Dlinked_list() : head(nullptr) {}
void insertAtBeginning(int value)
{
    node *new_node = new node(value);

    if(head==nullptr)
    {
        head = new_node;

    }
    else
    {
        new_node->next = head;
        head->prev = new_node;
        head = new_node;

    }
}
void forwardDisplay()
{
    node *temp = head;

    while(temp!=nullptr)
    {
        cout<<temp->data<<"->";
        temp = temp->next;
    }

    cout<<"nullptr"<<endl;
}
/*
void forwardDisplay()
{
    node *temp = head;

    while(temp!=nullptr)
    {
        cout<<temp->data<<"->";
        temp = temp->next;
    }
}*/

void backwardDisplay()
{
    node *temp2 = head;

    while(temp2->next!=nullptr)
    {
        temp2 = temp2->next;
    }

    while(temp2!=nullptr)
    {

        cout<<temp2->data<<"->";
        temp2 = temp2->prev;
    }

    cout<<"nullptr"<<endl;
}


};
int main()
{
    Dlinked_list d1;
    d1.insertAtBeginning(5);
    d1.insertAtBeginning(6);
    d1.insertAtBeginning(7);
    d1.forwardDisplay();
    d1.backwardDisplay();
    return 0;
}
