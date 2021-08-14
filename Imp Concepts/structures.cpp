#include<iostream>
#include<stdio.h>

using namespace std;

//--Definition of structure
struct Rectangle{
    int length;
    int breadth;
    char x;
};

int main()
{
    //--declaring variable of structure
    struct Rectangle r1,r2,r3;
    r1={10,5};
    // printf("%lu", sizeof(r1));

    r1.length = 15;
    r1.breadth = 20;
    cout<<r1.length<<endl;
    cout<<r1.breadth<<endl;

    return 0;
}