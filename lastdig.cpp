#include <iostream>
using namespace std;
int power(int x, long long int b)
{
    int m=10, num=1;
    while(b){
        if (b&1) num=num*x%m;
        b >>= 1;
        x = x*x%m;
    }
    return num;
}
int main()
{
   int t, a;long long int b;
   cin>>t;
   for(int i=0; i<t; i++)
   {
       cin>>a>>b;
       cout<<power(a%10, b)<<endl;
   }
   return 0;
}