//-------call by Address---------
#include<iostream>
#include<stdio.h>

using namespace std;

int add(int *a, int *b)
{
    //--for understanding im using swap concept here-
    int c;
    c = *a;
    *a = *b;
    *b = c;
    c = *a + *b;

    return c;
}

int main()
{
     int num1, num2, sum,c;
     num1 = 10;
     num2 = 20;
     sum = add(&num1,&num2);

     cout<<"First Number "<<num1<<endl;
     cout<<"Second Number "<<num2<<endl;
     cout<<"Anonymous:"<< c <<endl; // stores some garbage value

     cout<<"The sum is: "<<sum;

     return 0;
}