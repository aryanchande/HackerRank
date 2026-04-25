#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n,e,s;
    cin>>n;
    int a[n];
    for(int i=0;i<n;i++){
        cin>>e;
        a[i]=e;
    }
    s=sizeof(a)/sizeof(a[0]);
    for(int i=s-1;i>=0;i--){
        cout<<a[i]<<' ';
    }
return 0;
}
