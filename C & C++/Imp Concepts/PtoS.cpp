#include<iostream>
#include<stdio.h>

using namespace std;

struct Rectangle
{
    int length;
    int breadth;
};

int main()
{
    //-----pointer to structure-----
    //  Rectangle r={10,5};

    //  cout<<r.length<<endl;
    //  cout<<r.breadth<<endl;

    //  Rectangle *p = &r;

    //  cout<<p->length<<endl;
    //  cout<<p->breadth<<endl;

    //---dynamically in heap
    Rectangle *p;
    // p = (struct Rectangle*)malloc(sizeof(struct Rectangle));
    p = new Rectangle;

    p->length = 15;
    p->breadth= 7;

    cout<<p->length<<endl;
    cout<<p->breadth<<endl;

    cout<<"Size of the memory in the given structure:"<<sizeof(p)<<endl;

     return 0;
}