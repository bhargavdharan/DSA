#include<iostream>
#include<stdio.h>

using namespace std;

struct Rectangle
{
    int length;
    int breadth;
};

// void fun(struct Rectangle *pr)
//  {
// //     pr->length = 20;
// //     cout<<"Length==>"<<pr->length<<endl<<"Breadth==>"<<pr->breadth<<endl
 
//  }

struct Rectangle *fun()
{
    struct Rectangle *p;
    p = new Rectangle;
    // p = (struct Rectangle *)malloc(sizeof(struct Rectangle));

    p->length = 15;
    p->breadth = 7;

    return p;
}

int main()
{
    //  struct Rectangle r = {10,5};
    //  fun(&r);

    //  printf(" Length:%d \n Breadth:%d \n",r.length,r.breadth);
    struct Rectangle *ptr = fun();

    cout<<"Length"<<ptr->length<<" ==> "<<endl<<"Breadth"<<ptr->breadth<<endl;
     return 0;
}