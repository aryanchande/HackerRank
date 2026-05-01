#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#define MAX 100

int main() 
{
    char ch;
    char s[MAX];
    char sen[MAX];
    scanf("%c\n",&ch);
    printf("%c\n",ch);
    scanf("%s\n",s);
    printf("%s\n",s);
    scanf("%[^\n]%*c",sen);
    printf("%s",sen);
    
    

    
    return 0;
}
