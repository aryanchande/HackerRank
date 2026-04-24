#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
int Max(int x,int y,int z,int w){
    return max({x,y,z,w});
}


int main() {
    int a,b,c,d;
    cin>>a>>b>>c>>d;
    cout<<Max(a,b,c,d);
    return 0;
}
