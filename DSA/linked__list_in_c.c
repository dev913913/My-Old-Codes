#include <stdio.h>
#include<ctype.h>
#include<stdlib.h>
// #include<malloc.h>

struct node
{
    int data;
    struct node *next;
};

struct node *head = NULL;

// Old code (incorrect)
// struct node createNode(int a)
// {
//     struct node *newNode = (struct node *)malloc(sizeof(struct node)); // Allocate memory
//     if (newNode == NULL) {
//         printf("Memory allocation failed\n");
//         exit(1); // Exit if memory allocation fails
//     }
//     newNode->data = a;
//     newNode->next = NULL;
//     return *newNode; // WRONG: Returning the structure, not the pointer
// }
// Explanation: Returning the structure `*newNode` copies the content of the node, 
// but the node's memory will not be preserved after the function returns, 
// leading to problems when we later try to manipulate the node in other functions.


// New code (correct): Now returning a pointer to the node instead of the structure itself
struct node *createNode(int a)
{
    struct node *newNode = (struct node *)malloc(sizeof(struct node));  // Allocate memory for the node
    if (newNode == NULL) {
        printf("Memory allocation failed\n");
        exit(1);
    }
    newNode->data = a;
    newNode->next = NULL;
    return newNode;  // CORRECT: Return the pointer to the newly allocated node
}


// Old code (incorrect)
// void insertNode(int b)
// {
//     struct node *s1 = NULL;  // WRONG: s1 is not allocated memory
//     *s1 = createNode(b);  // WRONG: Dereferencing an uninitialized pointer
//     if(head == NULL)
//     {
//         head = s1;
//     }
//     else
//     {
//         s1->next = head;
//         head = s1;
//     }
// }
// Explanation: `s1` is declared as a pointer but memory is not allocated for it. 
// Dereferencing an uninitialized pointer (`*s1 = createNode(b);`) causes a segmentation fault. 
// This is because `s1` doesn't point to any valid memory location.

// New code (correct): Allocate memory for `s1` and use the return value of `createNode`
void insertNode(int b)
{
    struct node *s1;
    s1 = createNode(b);  // CORRECT: Directly assigning the pointer returned by createNode
    
    if (head == NULL) {
        head = s1;  // If the list is empty, set head to the new node
    } else {
        s1->next = head;  // Insert the new node at the beginning
        head = s1;
    }
}

void deleteNode(int key)
{
    struct node *temp = head, *prev;

    // If head node itself holds the key to be deleted
    if (temp!= NULL && temp->data == key)
    {
        head = temp->next;
        free(temp);
        return;
    }

    // Search for the key to be deleted, keep track of the previous node
    while (temp!= NULL && temp->data!= key)
    {
        prev = temp;
        temp = temp->next;
    }

    // If key was not present in linked list
    if (temp == NULL)
        return;

    // Unlink the node from linked list
    prev->next = temp->next;
    free(temp);
}

void searchNode(int key)
{
    struct node *temp = head;
    int found = 0;

    while (temp!= NULL)
    {
        if (temp->data == key)
        {
            found = 1;
            break;
        }
        temp = temp->next;
    }

    if (found)
        printf("Found %d in the list\n", key);
    else
        printf("%d not found in the list\n", key);
}


void displayList()
{
    struct node *temp = head;
    printf("Linked List: ");
    while (temp!= NULL)
    {
        printf("%d -> ", temp->data);
        temp = temp->next;
    }
    printf("NULL\n");
}


int main()
{
    int data,choice;
    char choice2;
    while (1)
    {
        printf("Choose the following");
        printf("\n1. Insertion");
        printf("\n2. Deletion");
        printf("\n3. Search");
        printf("\n4. Display");
        printf("\n5. Exit");

        printf("\nEnter your choice from 1 to 5: ");

        scanf("%d", &choice);

        switch (choice)
        {
        case 1:
            printf("Enter the data to insert: ");
            scanf("%d", &data);
            insertNode(data);
            printf("\nNode inserted successfully.\n");
            break;
        case 2:
           printf("Enter the data to delete: ");
           deleteNode(data);
            break;
        case 3:
           printf("Enter the data to search: ");
           searchNode(data);
            break;
        case 4:
            displayList();
            break;
        case 5:
            // Exit
            printf("\nExiting...\n");
           return 0;
            break;
        default:
            printf("\nInvalid choice. Please try again.");
        }

        printf("Do you want to continue? (Y/N): ");

        scanf(" %c", &choice2);
        choice2 = toupper(choice2);
        // printf("choice 2: %c\n",choice2);
        if (choice2 != 'Y')
        {   
            printf("\nExiting...\n");
            break;
        }
        
    }
    return 0;
}



// void deleteNode(int data)
// {
//     struct node *temp = head, *prev;

//     if (temp != NULL && temp->data == data)
//     {
//         head = temp->next;
//         free(temp);
//         return;
//     }

//     while (temp!=NULL && temp->data!=data)
//     {
//         prev = temp;
//         temp = temp->next;
//     }

//     if (temp == NULL)
//     {
//         printf("\nElement not found in the list.");
//         return;
//     }

//     prev->next = temp->next;
//     free(temp);
//     return;
// }