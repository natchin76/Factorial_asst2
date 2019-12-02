#include<stdio.h>
#include"fact.h"
#include<time.h>   /*to calculate time taken to run the function*/
int main(){
int n;
double f;
clock_t t;
float time;
printf("Enter an integer.:");
scanf("%d",&n);
t=clock();     /*initializing t*/
f=fact(n);
t=clock()-t;   /*gives no. of clock cycles*/
time=(float)t/CLOCKS_PER_SEC;    /*t gives no. of clock cycles, thus dividing by clocks per second*/
printf("Factorial of %d is %.10e\n",n,f);
printf("It took %.10e seconds to run the function\n",time);
return(0);
}
