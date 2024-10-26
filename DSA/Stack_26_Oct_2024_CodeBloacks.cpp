#include<iostream>
#include<ctype.h>
// #include<string.h>

using namespace std;

// const int capacity = 5;


class Stack
{
    public:
    int *arr;
    int data;
    int rear = -1;
    int Size = 0;

    Stack(int capacity)
    {
        arr = new int [capacity];
        Size = capacity - 1;
    }



    ~Stack()
    {
        delete[] arr;
    }

    bool isEmpty()
    {
    return rear == -1;
    }

    bool isFull()
    {
    return rear == Size;
    }


    void push(int elmt)
    {
         if(!isFull())
         {
            rear++;
           arr[rear] = elmt;
           cout<<"\nElement "<<elmt<<" has been added over stack"<<endl;


         }
         else
        {
            cout<<"\nStack Overflow! No more space to add";
         }
    }

    void pop()
    {
        if(!isEmpty())
        {
            int temp = arr[rear];
            rear--;
            cout<<"\nElement "<<temp<<" has been deleted from stack"<<endl;

        }
        else
        {
            cout<<"\nStack Underflow! Nothing to remove"<<endl;
         }
    }

    void peek()
    {
        if(!isEmpty())
        {
            cout<<"\nTop Element:"<<arr[rear];
        }
        else
        {
            cout<<"\nStack Underflow! Nothing to peek"<<endl;
         }
    }

    void display()
    {
        if(!isEmpty())
        {
            for(int i = 0; i<=rear;i++)
            {
                cout<<"\nElement "<<i+1<<":"<<arr[i]<<endl;
            }
        }
        else
        {
            cout<<"\nStack Underflow! Nothing to Display"<<endl;
         }
    }
};



int main()
{
    char ch1,ch2;
    int elnt,Size;
    cout<<"\nEnter the size of your stack: ";
    cin>>Size;
    Stack st(Size);

    while(1)
    {
    cout<<"\nChoose one of the following options"<<endl;
    cout<<" [1] Push"<<endl;
    cout<<" [2] Pop"<<endl;
    cout<<" [3] Peek"<<endl;
    cout<<" [4] Display the whole stack"<<endl;
    cout<<" [5] Check the max size of stack"<<endl;
    cout<<" [0] Exit"<<endl;




        cout<<"Your choice: ";
        cin>>ch1;

        if(ch1!='0')
        {

            switch(ch1)
            {
                case '1':
                    cout<<"Enter the value that you want to push: ";
                    cin>>elnt;
                    st.push(elnt);
                    break;
                case '2':
                    st.pop();
                    break;
                case '3':
                    st.peek();
                    break;
                case '4':
                    st.display();
                    break;
                case '5':
                    cout<<"The max size of your stack is: "<<Size<<endl;
                    break;
                default:
                    cout<<"Invalid input! Please choose only b/w 0 and 5\n"<<endl;

            }
        }
        else
        {
            cout<<"Exiting..."<<endl;
            exit(0);
        }


    /*cout<<"\nDo you want to continue? (Y/N): ";
    cin>>ch2;

    ch2 = tolower(ch2);

    if(ch2 != 'y')
    {
        cout<<"Exiting..."<<endl;
        break;
    }*/



    }
    return 0;
}
