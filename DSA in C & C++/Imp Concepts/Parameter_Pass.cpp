//-------------call by value--------------
#include<iostream>
#include<stdio.h>

using namespace std;

int add(int a, int b)//formal parameters as arguments
{
    // a++;
    // cout<<a;
    // return 0;  //Here a value changes
    int c;
    c = a + b;

    return c;

}

int main()
{
     int num1,num2,sum;
     num1 = 10;
     num2 = 20;
     sum = add(num1,num2);//actual parameters as argument

     cout<< endl <<num1; // Here num1 value does not change
     cout<<endl<<"Sum is "<<sum;

     return 0;
}

/*
* Here formal parameters will change and actual parameters will not be changed
*
*
*
*
*
*/