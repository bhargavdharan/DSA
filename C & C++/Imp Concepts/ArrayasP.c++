#include<iostream>
#include<stdio.h>

using namespace std;

void fun(int A[],int n)
{
    // cout<<sizeof(A)/sizeof(int)<<endl;
    // for( int i = 0; i<7; i++){
    // cout<<A[i]<<endl;
    // }
    A[0] = 15;


}

int main()
{
     int A[] = {2,3,4,5,6,7,8};
     int n = 7;
     fun(A,n);
     cout<<sizeof(A)/sizeof(int)<<endl;
     for( int x:A )
     cout<<x<<" ";

     return 0;
}