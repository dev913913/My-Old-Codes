#include <iostream>

using namespace std;

class node
{
public:
    int data;
    node *next;

    // Constructor with a default value
    node(int val = 0) : data(val), next(nullptr) {}
};

int main()
{
    node *head = new node;

    head->data = 5;
    cout<<"Head Data: "<<head->data<<endl;

    node *second = new node(4);
    head->next = second;

    cout<<"Head Data: "<<second->data<<endl;
    
    return 0;
}