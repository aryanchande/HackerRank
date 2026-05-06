#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
//Complete the following function.


void calculate_the_maximum(int n, int k) {
  int mand=0,mor=0,mxor=0;
  for(int i=1;i<=n;i++){
    for(int j=i+1;j<=n;j++){
        int cand=i&j;
        int cor=i|j;
        int cxor=i^j;
        if(cand<k && cand>mand) mand=cand;
        if (cor<k && cor>mor) mor=cor;
        if(cxor<k && cxor>mxor) mxor=cxor;   }
  }
  printf("%d\n%d\n%d\n",mand,mor,mxor);
}

int main() {
    int n, k;
  
    if (scanf("%d %d", &n, &k)==2){
     calculate_the_maximum(n, k);
    }
    return 0;
}
