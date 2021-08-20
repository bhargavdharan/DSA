//------------call by reference---------

#include<iostream>
#include<stdio.h>

using namespace std;

void swap(int &x, int &y)
{
    int temp;
    temp = x;
    x = y;
    y = temp;
}

int main()
{
     int num1,num2;
     num1 = 10;
     num2 = 15;
     cout<< "Before swapping...! " << endl;
     cout<< " First Number" << num1 << endl;
     cout<< " Second Number" << num2 << endl;


     swap(num1,num2);

     cout<< "After swapping...! " << endl;
     cout<< " First Number" << num1 << endl;
     cout<< " Second Number" << num2 << endl;
     return 0;
}

// Here Reference are nicknames not a pointers