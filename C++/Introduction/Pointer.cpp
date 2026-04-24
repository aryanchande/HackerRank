#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
void update(int*a,int*b){
    *a+=*b;
    *b=abs(*a-2*(*b));
}


int main() {
    int g,h;
    int*c=&g;
    int*d=&h;
    cin>>g>>h;
    update(c,d);
    cout<<g<<endl;
    cout<<h<<endl;
    return 0;
}
