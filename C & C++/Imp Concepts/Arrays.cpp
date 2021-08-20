#include<iostream>
#include<stdio.h>

using namespace std;

int main()
{
    int n;
    cout<<"Enter Size";
    cin>>n;
    // int A[10] = {2,4,6,8,10,12,14};
    int A[n];
    A[0] = 10;

    //for loop
    // for(int i=0;i<10;i++){
    //     cout<<A[i]<<endl;
    // }

    //for-each loop
    for(int x:A)
    {
        cout<<x<<endl;
    }

    // cout<<sizeof(A)<<endl;
    // cout<<A[8]<<endl;
    // printf("%d\n",A[9]);


    return 0;
}