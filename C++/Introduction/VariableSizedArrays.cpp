#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n,q;
    cin>>n>>q;
    vector<vector<int>>a(n);
    
    for(int i=0;i<n;i++){
        int s;
        cin>>s;
        a[i].resize(s);
        for(int j=0;j<s;j++){
            cin>>a[i][j];
        }}
    for(int k=0;k<q;k++){
        int f,s;
        cin>>f>>s;
        cout<<a[f][s]<<endl;
    }
    return 0;
}
