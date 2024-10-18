#include<iostream>
#include<string>

using namespace std;

int main(){

 while(1)
    {

    int len, match, *arr;
    char ch;
    int c,d = 0;

    cout<<"Enter the size of range: ";
    // while(1)
    // {
    cin>>len;

    // if(len>0)
    // {
    //     break;
    // }
    // else{
    //     cout<<"Invalid input! Size cannot be zero\n";
    //     cout<<"Enter the size of range again: ";
    // }
    // }
    // Creating arr at run time of len size

    arr = new int[len];

    // Taking element in new array
    for(int i = 0; i<len; i++)
    {
        cout<<"Enter the element "<<i+1<<": ";
        cin>>arr[i];
    }

    // Traversing and displaying all elemement stored

        for(int i = 0; i<len; i++)
    {
        cout<<arr[i]<<" ";

    }


    cout<<"\n";

    cout<<"Enter the number that you want to find: ";
    cin>>match;

    for(int i = 0; i<len; i++)
    {
        d++;
        if(match==arr[i])
        {

            c++;
            break;
        }

    }

    cout<<"n";
    if(c>0)
    {
        cout<<match<<" number found in "<<d<<" tries\n";
    }

    else cout<<match<<" number not found\n";

    delete[] arr;

    cout<<"Do you want try again? Y/N";
    cin>>ch;

    ch = tolower(ch);

    if(ch!='y')
    {
      break;
    }

    cout<<"\n\n";
    }

    return 0;
}
