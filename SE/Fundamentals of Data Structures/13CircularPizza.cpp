#include<iostream>
#include<stdlib.h>
using namespace std;
class pizza
{
int front,rear,q[5];
public:
    pizza()
    {
    front=-1;   //indicates empty queue
    rear=-1;
    }

    int isfull()
    {
        if((front==0&&rear==4)||front==rear+1)      //CHECK WHETHER THE FRONT POSITION BEHIND THE REAR OR NOT
        {
        return 1;       //THE QUEUE IS FULL
        }
        else
        {
        return 0;       //THE QUEUE IS NOT FULL
        }
    }

    int isempty()
    {
        if(front==-1&&rear==-1)         //CHECKS whether THE QUEUE IS EMPTY?
        {
        return 1;       //YES EMPTY
        }
        else
        {
        return 0;       //NOT EMPTY
        }
    }

    void add()
    {
        if(isfull()==0)
        {
            cout<<"\n Enter the Pizza ID: ";
                if(front==-1&&rear==-1)
                {
                front=0;
                rear=0;
                cin>>q[rear];
                }
                else
                {
                rear=(rear+1)%5;    //new rear position.. jo filled rear position hai already, the empty position next to it.
                cin>>q[rear];           //maintain the circular behaviour of the queue
                }
            char c;
            cout<<" Do you want to place another order ? ";
            cin>>c;
            if(c=='y'||c=='Y')
            add();      //recursively call of add() func
        }
        else
        {
            cout<<"\n Orders are full ";
        }
    }

    void serve()   //deletion of queue from front
    {
        if(isempty()==0)
        {
            if(front==rear)
            {
            cout<<"\n Order served is : "<<q[front];
            front=-1;
            rear=-1;
            }
            else
            {
            cout<<"\n Order served is : "<<q[front];
            front=(front+1)%5;
            }
        }
        else
        {
            cout<<"\n Orders are empty ";
        }
    }

    void display()
    {
        if(isempty()==0)
        {
            for(int i=front;i!=rear;i=(i+1)%5)          //when i will reach 4 index then i+1=5 & 5%5=0.. Hence now i will become i=0
            {
                cout<<q[i]<<"<- ";
            }
            cout<<q[rear];
        }
        else
        {
            cout<<"\n Orders are empty";
        }
    }

    void check()                // selection counter
    {
        int ch;
        cout<<"\n\n * * * * PIZZA PARLOUR * * * * \n\n";
        cout<<"1. Place Order for a Pizza \n";
        cout<<"2. Display the Orders \n";
        cout<<"3. Serve a Pizza \n";
        cout<<"4. Exit \n Enter your choice : ";
        cin>>ch;
        switch(ch)
        {
            case 1: add(); break;
            case 2: display(); break;
            case 3: serve(); break;
            case 4: exit(0);
            default:
            cout<<"Invalid choice ";
            check();
        }
        char ch1;
        cout<<"\n Do you want to continue? ";
        cin>>ch1;
        if(ch1=='y'||ch1=='Y')
        check();        //recursively call check() func
    }
};

int main()
{
    pizza p1;
    p1.check();
    return 0;
}