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

int sizeoflist()
{
       node *temp3 = head;
        int n = 1;
        while(temp3->next!=nullptr)
        {
            temp3 = temp3->next;
            n++;
        }

    return n;


}

void inseratmiddle(int value)
{
    int midsizeofl = (sizeoflist())/2;

    node *new_node = new node(value);

    if(head!=nullptr)
    {
        node *temp3 = head;
        for(int i = 1; i<=midsizeofl;i++)
        {
            temp3= temp3->next;
        }
        new_node->next= temp3->next;
        new_node->prev = temp3;
        temp3->next->prev = new_node;
        temp3 = new_node;
    }
    else
    {
        head = new_node;
    }
}


void insertAtend(int value)
{
    node *new_node = new node(value);

    if(head==nullptr)
    {
        head = new_node;

    }
    else
    {
    node *temp3 = head;

    while(temp3->next!=nullptr)
    {
        temp3 = temp3->next;
    }

    temp3->next=new_node;
    new_node-> prev = temp3;

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
    d1.insertAtend(6);
    d1.insertAtend(7);
    d1.insertAtend(8);
    d1.insertAtend(9);
    //d1.inseratmiddle(60);
    cout<<d1.sizeoflist();
    //d1.forwardDisplay();
    d1.backwardDisplay();

    return 0;
}
