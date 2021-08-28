#include<iostream>
#include<stdio.h>

using namespace std;

int main(){
    // int a = 10;
    // int *p;

    // p = &a;

    // cout<<a<<endl;
    // cout<<*p<<endl;
    // printf("using pointer %d \n ", p);
    // printf("using pointer %u", *p);
//-----------------------------------------------------------
    // pointer to an array

    // int A[5]={2,4,5,6,7}; //Array in stack memory
    // int *p;
    // p = &A[0];

    // for( int i=0; i<5; i++){
    //     // cout<<A[i]<<endl;
    //     cout<<p[i]<<endl;
    // }
//------------------------------------------------------------
    // int *p;
    // // p = (int *)malloc(5*sizeof(int));
    // p = new int[5];    // dynamically created a memory in the heap

    // p[0]=10; p[1]=15; p[2]=14; p[3]=21; p[4]=31;

    // for (int i=0; i<5; i++){
    //     cout<<p[i]<<endl;
    // }

    // delete [ ] p; // c++ language deallocation of memory in the heap
    // free( p ); // c language (this is for deallocating the memory that is allocated in the heap.)
//-------------------------------------------------------------
    int *p1;
    char *p2;
    float *p3;
    double *p4;
    struct Rectangle *p5;

    cout<<sizeof(p1)<<endl;
    cout<<sizeof(p2)<<endl;
    cout<<sizeof(p3)<<endl;
    cout<<sizeof(p4)<<endl;
    cout<<sizeof(p5)<<endl;
    
    return 0;
}